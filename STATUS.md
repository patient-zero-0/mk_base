# STATUS.md · 项目当前状态

> 本文件记录项目实时进度，每次里程碑推进或状态变化时同步更新。
> commit message 前缀：`status:` （如 `status: M0 完成，进入 M1`）

---

## 当前阶段

```
M0 准备阶段  ██████████████████░░  接近完成（仅余 GitHub/Cloudflare 接入）
M1 数学分析  █████████████░░░░░░░  26 / 40 条 draft（65%）
```

**当前版本：** PRD v1.5 · 架构 v1.5
**当前分支：** main（本地骨架已就绪）
**最后更新：** 2026-05-03

---

## 里程碑总览

| 阶段 | 名称 | 时间 | 目标 | 状态 |
|---|---|---|---|---|
| M0 | 准备 · 基础设施 | 第 1–2 周 | 仓库 + 模板 + CI 全部就绪 | 🔄 进行中 |
| M1 | 数学分析 Ch1–Ch2 | 第 3–5 周 | ≥ 40 条 stable，依赖图首版 | ⏳ 未开始 |
| M2 | 数学分析 Ch3–Ch5 | 第 6–9 周 | ≥ 80 条 stable，例题配套完成 | ⏳ 未开始 |
| M3 | 高等代数 Ch1–Ch5 | 第 10–16 周 | ≥ 120 条 stable | ⏳ 未开始 |
| M4 | 整合与验收 | 第 17–18 周 | ≥ 300 条，所有验收指标达标 | ⏳ 未开始 |

---

## M0 详细待办

### 📁 仓库与目录结构

- [ ] 在 GitHub 创建公开仓库 `MK_Base`
- [x] 初始化目录结构（已建立 analysis/、algebra/、_cross/、_meta/、_templates/、scripts/、refs/、.github/workflows/）
- [x] 提交 `.gitattributes`（`*.md text eol=lf`）
- [x] 提交 `.gitignore`（排除 `.obsidian/` 等本地配置）
- [ ] 配置 main 分支保护规则（GitHub 后台操作）

### 📋 模板与规范

- [x] 提交 `PROJECT.md`
- [x] 提交 `ARCHITECTURE.md`
- [x] 提交 `STATUS.md`
- [x] 提交 `CONTRIBUTING.md`
- [x] 提交 `README.md`
- [x] 提交 `_templates/definition.md`
- [x] 提交 `_templates/theorem.md`
- [x] 提交 `_templates/example.md`
- [x] 提交 `_templates/problem.md`
- [x] 提交 `refs/` 参考资料夹

### ⚙️ CI/CD

- [x] 提交 `.github/workflows/check.yml`
- [x] 提交 `.github/workflows/deploy.yml`
- [x] 编写 `scripts/check_frontmatter.py`（已修复"depends 允许为空列表"的实现 bug）
- [x] 编写 `scripts/check_dangling_refs.py`
- [x] 编写 `scripts/check_katex.js`
- [x] 提交 `package.json`（katex / glob / markdownlint-cli 锁定版本）
- [x] 提交 `quartz.config.ts`（站点配置骨架）
- [ ] 配置 GitHub Secrets：`CF_API_TOKEN`、`CF_ACCOUNT_ID`、`CLOUDFLARE_ANALYTICS_TOKEN`、邮件告警
- [ ] 连接 Cloudflare Pages（关联 GitHub 仓库，设 build command = `npx quartz build`）
- [ ] 接入 Cloudflare Web Analytics（获取 beacon token，注入 quartz.config.ts）

### 🧪 验证（M0 完成标准）

- [x] 用 5 条真实条目 + 9 条前置条目端到端验证（含定义 / 定理 / 例题 / 习题 / 跨课）
- [x] 本地 `make check` 等价 4 项检查全部绿色（14 条目，403 公式）
- [ ] PR 触发 check.yml 全部绿色（需 GitHub 仓库就绪）
- [ ] merge 后 deploy.yml 成功构建（需 Cloudflare Pages + Quartz 运行时就绪）
- [ ] Cloudflare Pages 可正常访问，公式渲染正确
- [ ] 统计 beacon 正常上报

---

## 当前 `_meta/todo.md` 悬空引用列表

> 全部 🔴 最高 / 🟠 高 / 🟡 中 优先级 ID 已在 M0 阶段完成 draft。
> 当前全库悬空引用为 **0**（详见 `make check-refs`）。
>
> 仅剩跨课条目 `CROSS-001` 中提及但暂未引用的"待建" ID（公开记录于
> `_meta/todo.md`），属 M3 阶段：
>
> - 高等代数 `ALG-THM-XXX` 谱半径定理 / Jordan 标准形（M3）
> - Cantor 定理（闭区间连续 ⇒ 一致连续）— M2 阶段

---

## 已完成条目（用于 M0 验证）

### M0 验证条目（5 条）

| ID | 标题 | 类型 | 状态 |
|---|---|---|---|
| `ANL-THM-006` | 单调有界定理 | theorem | draft |
| `ANL-THM-007` | Cauchy 收敛准则 | theorem | draft |
| `ANL-DEF-024` | 一致连续 | definition | draft |
| `ANL-EX-007` | 用 ε-δ 证明 lim x²=4 | example | draft |
| `ANL-PROB-031` | sin(x²) 非一致连续 | problem | draft |

### 同期完成的前置条目（9 条，用于消除悬空）

| ID | 标题 | 类型 | 状态 |
|---|---|---|---|
| `ANL-AX-001` | 确界原理 | definition (公理) | draft |
| `ANL-DEF-001` | 数列 | definition | draft |
| `ANL-DEF-002` | Cauchy 列（基本列） | definition | draft |
| `ANL-DEF-003` | 单调数列 | definition | draft |
| `ANL-DEF-004` | 数列收敛（ε-N 定义） | definition | draft |
| `ANL-DEF-005` | 有界数列 | definition | draft |
| `ANL-DEF-008` | 函数极限的 ε-δ 定义 | definition | draft |
| `ANL-DEF-012` | 函数连续 | definition | draft |
| `CROSS-001` | 数列收敛与线性递推（跨课） | definition | draft |

### M1 Batch 1（6 条）

| ID | 标题 | 类型 | 状态 |
|---|---|---|---|
| `ANL-DEF-006` | 子列 | definition | draft |
| `ANL-THM-001` | 数列极限的唯一性 | theorem | draft |
| `ANL-THM-002` | 收敛数列必有界 | theorem | draft |
| `ANL-THM-005` | 数列夹逼定理 | theorem | draft |
| `ANL-THM-008` | Bolzano–Weierstrass 定理 | theorem | draft |
| `ANL-EX-001` | 用夹逼定理求两个经典极限 | example | draft |

### M1 Batch 2（6 条）

| ID | 标题 | 类型 | 状态 |
|---|---|---|---|
| `ANL-THM-003` | 数列极限的保号性 | theorem | draft |
| `ANL-THM-004` | 数列极限的四则运算 | theorem | draft |
| `ANL-THM-013` | 介值定理（IVT） | theorem | draft |
| `ANL-THM-014` | 最值定理 | theorem | draft |
| `ANL-THM-015` | Cantor 一致连续定理 | theorem | draft |
| `ANL-EX-002` | 用极限四则运算求多项式 / 有理式极限 | example | draft |

> 全部 26 条均处于 `draft` 状态，待 GitHub PR + Cloudflare 就绪后统一走流程升为 `stable`。
> 当前 CI 本地验证：4/4 全绿，961 个 KaTeX 公式全部通过。

---

## 非功能指标基准

| 指标 | 目标 | 当前 |
|---|---|---|
| KaTeX 渲染时间 | < 200ms | 待测量 |
| 首屏加载时间（TTI） | < 2s | 待测量 |
| 条目录入时间 | ≤ 30 min/条 | 待测量 |
| CI 检查通过率 | 100% | 4/4 本地通过（GitHub Actions 待激活） |
| 悬空引用数 | 0（main 分支） | 0（全库 30 条目，1151 公式） |
| 条目状态分布 | review ≥ 80% 时启动 stable 评审 | review = 25 / draft = 5（review 占比 83%） |

---

*下一个 action：在 GitHub 创建 `MK_Base` 公开仓库、推送本地骨架、配置 main 分支保护规则、关联 Cloudflare Pages。*
*M1 启动条件：上述 GitHub / Cloudflare 接入完成 + 5 条 M0 验证条目走完一次完整 PR 流程。*
