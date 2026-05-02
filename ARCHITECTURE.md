# ARCHITECTURE.md · 架构快照

> **活文档声明**：本文件描述的是**当前版本**的架构状态，不是永久约定。
> 每次架构变更须同步更新本文件，并在 PRD 第 4.6 节追加迭代日志记录。
> 变更对应的 commit message 必须以 `arch:` 为前缀。

---

## 当前版本

**架构版本：v1.5**
**最后更新：2025-01-15**
**对应 PRD：v1.5 § 4.1–4.6**

---

## 技术栈总览

| 层次 | 当前选型 | 备注 |
|---|---|---|
| 内容存储 | Git + GitHub（public 仓库） | 版本控制，纯文本，可迁移 |
| 本地编辑 | Obsidian + LaTeX Suite 插件 | 实时 KaTeX 预览，双向链接 |
| 公式格式 | LaTeX 源码 | 唯一存储格式，渲染层可替换 |
| 公式渲染 | KaTeX（Quartz 内置） | 渲染速度 < 200ms |
| 静态站点 | Quartz v4 | 原生支持双向链接 + KaTeX |
| 全文检索 | Quartz 内置 Flexsearch | MVP 阶段，500 条后重新评估 |
| 部署平台 | Cloudflare Pages | 免费，全球 CDN，自动触发 |
| 访问统计 | Cloudflare Web Analytics | 无 Cookie，无用户标识，仅 PV |
| CI/CD | GitHub Actions（2 个 workflow） | PR 检查 + 发布分离 |

---

## 三条核心链路

### 写入链路（作者侧）

```
Obsidian 本地编辑
    ↓ git push
draft/* 分支
    ↓ 发起 Pull Request
check.yml 自动检查（4 项）
    ↓ 全部通过
Code Review（人工）
    ↓ merge
main 分支
    ↓ 触发
deploy.yml
    ↓ Quartz 构建
Cloudflare Pages 全球分发
```

### 读取链路（用户侧）

```
用户访问域名
    ↓
Cloudflare CDN 边缘节点（最近节点响应）
    ↓
静态 HTML（KaTeX 已在构建期渲染）
    ↓
浏览器展示（零服务端计算）
```

### 统计链路（匿名聚合）

```
页面访问事件
    ↓
Cloudflare Web Analytics（边缘层，无 Cookie）
    ↓ 聚合计数（仅条目 ID + PV，无用户标识）
Cloudflare 后台
    ↓ 每日同步
_meta/analytics.json（公开）
    ↓
知识库「热度排行」页展示
```

---

## CI/CD 配置

### `check.yml` — PR 质量闸门

**触发：** 每次 PR 开启 / 更新时
**必须全部通过，否则阻断合并**

| 步骤 | 工具 | 检查内容 |
|---|---|---|
| ① frontmatter 完整性 | 自定义 Python 脚本 | 所有必填字段存在且非空 |
| ② 悬空引用扫描 | 自定义 Python 脚本 | depends/uses 引用的 ID 均已存在 |
| ③ LaTeX 语法验证 | node-katex | 所有公式可渲染，无报错 |
| ④ Markdown 格式规范 | markdownlint | 符合 `.markdownlint.json` 配置 |

### `deploy.yml` — 自动发布

**触发：** merge 到 `main` 后
**失败时发邮件告警，不阻断 main 分支访问**

| 步骤 | 说明 |
|---|---|
| ① Quartz 构建 | `npx quartz build` |
| ② 推送至 Cloudflare Pages | 使用 `CF_API_TOKEN`（存于 GitHub Secrets） |

---

## 分支策略

```
main          ← 保护分支，只接受 PR 合并，禁止直接 push
draft/*       ← 新条目起草，命名如 draft/analysis-limits
fix/*         ← 错误修正，命名如 fix/anl-thm-006-proof
arch/*        ← 架构变更，命名如 arch/migrate-search-engine
```

**main 分支保护规则：**
- Require pull request before merging
- Require status checks to pass（check.yml 所有步骤）
- Do not allow bypassing the above settings

---

## 迭代触发条件

下列情形**必须**启动架构评审，结论记入 PRD § 4.6：

- 知识条目 > 500 条 → 评估 Flexsearch 中文搜索质量
- 月 PV > 10 万 → 评估 Cloudflare Pages 免费套餐限制
- 内容建设者 > 5 人 → 评估 PR 分配机制
- Quartz / KaTeX 发布 breaking change 大版本
- 面向地区出现新数据隐私法规
- 任何当前免费工具宣布收费（30 天内完成评估）

---

## 架构迭代日志（摘要）

> 完整日志见 PRD § 4.6，本处仅保留最近 3 条。

| 版本 | 日期 | 变更范围 | 变更原因摘要 |
|---|---|---|---|
| v1.0 | 2025-01-15 | 全栈初始化 | 项目立项，MVP 阶段零成本选型 |
| v1.4 | 2025-01-15 | 部署 / 统计 / CI | Cloudflare Pages 优于 GitHub Pages；隐私承诺要求无 Cookie 统计；CI 职责分离 |
| v1.5 | 2025-01-15 | 架构活文档化 | 架构草案改为持续迭代模式，建立迭代日志机制 |
