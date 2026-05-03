# 部署接入清单 · GitHub + Cloudflare（已落地存档）

> ✅ **2026-05-03 已完成**：M0 部署链路闭合，<https://mk-base.pages.dev> 已上线。
> 仅余 Web Analytics token 配置（最后 5 分钟收尾，见 § C）。
>
> 本文件保留作为运维参考——下次需要从零搭建同类项目，可按本清单复刻。
> 实际接入过程中遇到的真实问题（Node 版本、Quartz import、deployments 权限）见
> 文末 § F 故障排查日志。

---

## A. GitHub 仓库保护规则

**前提**：仓库已创建且已 push（仓库地址：<https://github.com/patient-Zero-0/MK_Base>）。

### A.1 启用 main 分支保护

操作路径：仓库 → **Settings** → **Branches** → **Add branch protection rule**

| 字段 | 值 |
|---|---|
| Branch name pattern | `main` |
| ✅ Require a pull request before merging | 勾选 |
| ↳ Require approvals | `1`（单人项目可设 0，但 CI 仍强制） |
| ✅ Require status checks to pass before merging | 勾选 |
| ↳ Require branches to be up to date before merging | 勾选 |
| ↳ Status checks that are required | 等首次 PR 后选 `Quality Check / 内容质量检查` |
| ✅ Do not allow bypassing the above settings | 勾选（仓库主也受约束） |
| ❌ Allow force pushes | 禁用 |
| ❌ Allow deletions | 禁用 |

> **注意**：状态检查必须在 GitHub Actions 至少运行过 1 次后才能在下拉中选择。
> 建议先发起一个空 PR（修一个 typo）触发 `check.yml`，再回来勾选必需检查。

### A.2 GitHub Secrets 配置

操作路径：仓库 → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

| Secret 名称 | 来源 | 用途 |
|---|---|---|
| `CF_API_TOKEN` | Cloudflare → My Profile → API Tokens → "Edit Cloudflare Pages" 模板 | `deploy.yml` 推送至 CF Pages |
| `CF_ACCOUNT_ID` | Cloudflare 控制台右侧 Account ID | 同上 |
| `MAIL_USERNAME` | 你的 Gmail 邮箱 | 构建失败告警 |
| `MAIL_PASSWORD` | Gmail 应用专用密码（不是登录密码） | 同上 |
| `MAIL_TO` | 接收告警的邮箱 | 同上 |

> Gmail 应用密码：登录 myaccount.google.com → Security → 2-Step Verification → App passwords。

---

## B. Cloudflare Pages 项目接入

### B.1 创建 Pages 项目

操作路径：Cloudflare 控制台 → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**

| 字段 | 值 |
|---|---|
| Production branch | `main` |
| Project name | `mk-base`（与 deploy.yml 中 `projectName` 一致） |
| Framework preset | None |
| Build command | `npx quartz build` |
| Build output directory | `public` |
| Root directory | `/`（默认） |

> **注意**：Quartz 不在 npm 上，`npx quartz build` 在 CF Pages 默认环境会报错。
> 解决方案见下方 § B.3。

### B.2 环境变量

在 Pages 项目 → **Settings** → **Environment variables**：

| 变量 | 值 |
|---|---|
| `NODE_VERSION` | `20` |
| `CLOUDFLARE_ANALYTICS_TOKEN` | 见下方 § C 获取 |

### B.3 Quartz 构建链路修复（重要）

当前 `deploy.yml` 假设根目录就是 Quartz 项目，但实际 Quartz 需 `git clone` 上游仓库。
**有两种推荐方案**：

#### 方案 1（推荐）：把 Quartz 作为 git submodule

```bash
git submodule add https://github.com/jackyzha0/quartz .quartz-runtime
git add .gitmodules .quartz-runtime
git commit -m "chore: add quartz as submodule"
```

然后修改 `.github/workflows/deploy.yml`：

```yaml
- name: Checkout（含 submodule）
  uses: actions/checkout@v4
  with:
    submodules: recursive

- name: 准备 Quartz 内容目录
  run: |
    cp -r analysis algebra _cross _meta refs .quartz-runtime/content/
    cp _meta/index.md .quartz-runtime/content/index.md
    cp quartz.config.ts .quartz-runtime/quartz.config.ts

- name: Install Quartz dependencies
  run: cd .quartz-runtime && npm ci

- name: Build
  run: cd .quartz-runtime && npx quartz build
  env:
    NODE_ENV: production
    CLOUDFLARE_ANALYTICS_TOKEN: ${{ secrets.CLOUDFLARE_ANALYTICS_TOKEN }}

- name: Deploy to Cloudflare Pages
  uses: cloudflare/pages-action@v1
  with:
    apiToken: ${{ secrets.CF_API_TOKEN }}
    accountId: ${{ secrets.CF_ACCOUNT_ID }}
    projectName: mk-base
    directory: .quartz-runtime/public
    gitHubToken: ${{ secrets.GITHUB_TOKEN }}
```

#### 方案 2：fork Quartz，把内容直接放到 fork 的 `content/`

更彻底，但需要在两个仓库间同步。仅当方案 1 不便维护时考虑。

---

## C. Cloudflare Web Analytics 接入

### C.1 创建 Analytics 站点

操作路径：Cloudflare 控制台 → **Analytics & Logs** → **Web Analytics** → **Add a site**

| 字段 | 值 |
|---|---|
| Site name | `MK_Base` |
| Hostname | 部署后 CF 给的 `mk-base.pages.dev`（或自定义域名） |
| Automatic Setup | 关闭（手动注入 token） |

复制生成的 **Site Token**（形如 `abc123...`，约 32 位）。

### C.2 注入到 Quartz 配置

把 token 加到 GitHub Secrets `CLOUDFLARE_ANALYTICS_TOKEN`，
`quartz.config.ts` 已通过 `process.env.CLOUDFLARE_ANALYTICS_TOKEN` 读取。

或者直接在 `quartz.config.ts` 里写死（不推荐，会泄露 token 到公开仓库）：

```typescript
analytics: {
  provider: "cloudflare",
  token: "abc123def456...",
}
```

> Web Analytics 是**无 Cookie**的统计，符合 PROJECT.md 中的隐私承诺。

---

## D. 验证清单（按顺序勾选）

- [ ] 仓库已 public：<https://github.com/patient-Zero-0/MK_Base>
- [ ] main 分支保护规则启用，禁止直接 push
- [ ] 5 个 Secrets 已配置（`CF_API_TOKEN`, `CF_ACCOUNT_ID`, `MAIL_*`, `CLOUDFLARE_ANALYTICS_TOKEN`）
- [ ] 至少一次空 PR 触发 `check.yml`，4 项检查全绿
- [ ] 必需状态检查 `Quality Check / 内容质量检查` 已在分支保护中勾选
- [ ] CF Pages 项目 `mk-base` 创建并关联 GitHub 仓库
- [ ] CF Pages 部署成功，访问 `https://mk-base.pages.dev/` 看到首页
- [ ] 首页能渲染条目列表（如 `/analysis/01-limits/ANL-THM-006`）
- [ ] 公式正确显示（KaTeX）
- [ ] CF Web Analytics 在仪表盘看到 PV 上报
- [ ] 故意提交一个有 LaTeX 错误的 PR，验证 `check.yml` 阻断合并

---

## E. 故障排查

| 现象 | 排查方向 |
|---|---|
| `check.yml` 报"npm ci 失败" | 检查 `package.json` 版本是否被锁死，或 Node 版本是否一致 |
| `deploy.yml` 报 KaTeX 错误 | 检查 `.quartz-runtime/quartz.config.ts` 是否含 `Plugin.Latex` |
| CF Pages 显示 404 | Build output directory 是否填了 `.quartz-runtime/public`（方案 1）或 `public`（方案 2） |
| Analytics 仪表盘无数据 | 浏览器 NoScript / uBlock 拦截了 beacon；或 token 注入失败（查页面 HTML 是否含 `static.cloudflareinsights.com`） |
| 邮件告警没收到 | 检查 Gmail 应用密码是否过期；查 GitHub Actions 日志中 `action-send-mail` 步骤 |

---

## F. 实际接入中遇到的问题（2026-05-03 实施日志）

按时间顺序，实际部署链路调通过程中踩过的坑：

| # | 现象 | 根因 | 修复 |
|---|---|---|---|
| 1 | `npm ci` 报 `EBADENGINE` | Quartz 4.5+ 要求 Node ≥ 22 | deploy.yml & check.yml 升级到 `node-version: "22"` |
| 2 | Build 报 `ERR_MODULE_NOT_FOUND: @jackyzha0/quartz` | Quartz 不在 npm，根目录 quartz.config.ts 用了包名 import | 改为相对路径 `./quartz/cfg`、`./quartz/plugins` |
| 3 | `Plugin.RemoveDrafts()` 过滤掉 `status: draft` 条目 | 项目用 status 表达成熟度，不是私密草稿 | 移除该 filter |
| 4 | Deploy 报 403 `Resource not accessible by integration` | `cloudflare/pages-action@v1` 需要 GitHub Deployments API 权限 | 给 deploy job 加 `permissions: { contents: read, deployments: write }` |
| 5 | git submodule add 拒绝 `.quartz-runtime` | `.gitignore` 仍含此路径 | 从 .gitignore 移除整体排除，仅排除其内部生成物 |
| 6 | dev server 持有 sharp DLL 阻止 `rm -rf` | Node 进程未退出 | `Stop-Process node` 后再清理 |

总耗时：约 90 分钟（含浏览器端配置 + 5 次 PR 修复迭代）。
最终 deploy.yml 见 `.github/workflows/deploy.yml`，是经过这 6 次迭代后的稳定版。

---

*创建日期：2026-05-03 · 已落地存档，作为运维参考保留。*
