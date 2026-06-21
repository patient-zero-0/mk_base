# STATUS.md · 项目当前状态

> 本文件记录项目实时进度，每次里程碑推进或状态变化时同步更新。
> commit message 前缀：`status:` （如 `status: M0 完成，进入 M1`）

---

## 当前阶段

```
M0 准备阶段  ████████████████████  ✅ 完成（2026-05-03）
M1 数学分析  ████████████████████  ✅ 全面闭环（2026-05-07）
                                    47 条 stable · 依赖图 52 节点 / 201 边
                                    Analytics 上线（mk-base.pages.dev 已注入 beacon）
M2 数学分析  ████████████████████  ✅ 全面闭环（2026-06-21）
                                    Ch3 微分 25 ✅ · Ch4 积分 29 ✅ · Ch5 级数 27 ✅（共 81 条 stable）
                                    依赖图 133 节点 / 565 边 · DoD 6/6 达标
```

**当前版本：** PRD v1.5 · 架构 v1.5
**当前分支：** main（CI/CD 链路已闭合）
**线上站点：** <https://mk-base.pages.dev>
**最后更新：** 2026-06-21

---

## 里程碑总览

| 阶段 | 名称 | 时间 | 目标 | 状态 |
|---|---|---|---|---|
| M0 | 准备 · 基础设施 | 第 1–2 周 | 仓库 + 模板 + CI 全部就绪 | ✅ 完成 2026-05-03 |
| M1 | 数学分析 Ch1–Ch2 | 第 3–5 周 | ≥ 40 条 stable，依赖图首版 | ✅ 完成 2026-05-07（47 条 stable + 依赖图 + Analytics） |
| M2 | 数学分析 Ch3–Ch5 | 第 6–9 周 | ≥ 80 条 stable，例题配套完成 | ✅ 完成 2026-06-21：Ch3（25）+ Ch4（29）+ Ch5（27）= 81 条 stable，DoD 6/6 达标 |
| M3 | 高等代数 Ch1–Ch5 | 第 10–16 周 | ≥ 120 条 stable | ⏳ 已起 4 条占位 |
| M4 | 整合与验收 | 第 17–18 周 | ≥ 300 条，所有验收指标达标 | ⏳ 未开始 |

---

## M0 详细待办

### 📁 仓库与目录结构

- [x] 在 GitHub 创建公开仓库 `MK_Base` <https://github.com/patient-Zero-0/MK_Base>
- [x] 初始化目录结构（已建立 analysis/、algebra/、_cross/、_meta/、_templates/、scripts/、refs/、.github/workflows/）
- [x] 提交 `.gitattributes`（`*.md text eol=lf`）
- [x] 提交 `.gitignore`（排除 `.obsidian/` 等本地配置）
- [x] 配置 main 分支保护规则（Ruleset + bypass for repo admin）

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
- [x] 提交 `.github/workflows/deploy.yml`（含 submodule checkout + Node 22 + deployments 权限）
- [x] 编写 `scripts/check_frontmatter.py`（已修复"depends 允许为空列表"的实现 bug）
- [x] 编写 `scripts/check_dangling_refs.py`
- [x] 编写 `scripts/check_katex.js`
- [x] 提交 `package.json`（katex / glob / markdownlint-cli 锁定版本）
- [x] 提交 `quartz.config.ts`（学院深蓝 + 烫金主题，Noto 衬线汉字）
- [x] 添加 `.quartz-runtime` 作为 jackyzha0/quartz 的 git submodule
- [x] 配置 GitHub Secrets：`CF_API_TOKEN`、`CF_ACCOUNT_ID`
- [x] 连接 Cloudflare Pages 项目 `mk-base`
- [ ] 配置 `CLOUDFLARE_ANALYTICS_TOKEN`（最后一项）
- [ ] 邮件告警 secrets（可选，未配则跳过此步）

### 🧪 验证（M0 完成标准）

- [x] 用 5 条真实条目 + 9 条前置条目端到端验证（含定义 / 定理 / 例题 / 习题 / 跨课）
- [x] 本地 `make check` 等价 4 项检查全部绿色（30 条目，1151 公式）
- [x] PR 触发 check.yml 全部绿色（PR #1，13 秒跑完）
- [x] merge 后 deploy.yml 成功构建（PR #2 → #5，Node 22 + submodule + permissions 接入完成）
- [x] Cloudflare Pages 可正常访问 <https://mk-base.pages.dev>，公式渲染正确
- [ ] 统计 beacon 正常上报（最后一项，等 `CLOUDFLARE_ANALYTICS_TOKEN` 配置）

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

## M2 进度（数学分析 Ch3–Ch5）

> 详细拆解见 `_meta/m2-plan.md`。所有批次均已走 PR 流程合并到 main（CI 4/4 全绿）。

### Ch3 微分 · 25 条 ✅（已合并）

| Batch | 分支 | PR | 内容 | 状态 |
|---|---|---|---|---|
| Batch 1 | `m2/ch3-batch1-derivative-basics` | #19 | 导数 / 微分基础 8 条 | ✅ merged |
| Batch 2 | `m2/ch3-batch2-mean-value-and-taylor` | #20 | 中值定理与 Taylor 7 条 | ✅ merged |
| Batch 3 | `m2/ch3-batch3-applications` | #21 | 应用扩展 5 条 | ✅ merged |
| Batch 4 | `m2/ch3-batch4-problems` | #22 | 习题收尾 5 条 | ✅ merged |

### Ch4 积分 · 29 条 ✅（已合并）

| Batch | 分支 | PR | 内容 | 状态 |
|---|---|---|---|---|
| Batch 5 | `m2/ch4-batch5-riemann-foundations` | #23 | 积分定义层 5 条 | ✅ merged |
| Batch 6 | `m2/ch4-batch6-core-theorems` | #24 | 核心定理 8 条 | ✅ merged |
| Batch 7 | `m2/ch4-batch7-substitution-and-parts` | #25 | 计算工具与例题 5 条 | ✅ merged |
| Batch 8 | `m2/ch4-batch8-improper-integrals` | #26 | 反常积分主线 6 条 | ✅ merged |
| Batch 9 | `m2/ch4-batch9-integral-problems` | #27 | 反常积分 / 积分习题收尾 5 条 | ✅ merged |

### Ch5 级数 · 27 条 ✅（已合并）

| Batch | 分支 | PR | 内容 | 状态 |
|---|---|---|---|---|
| Batch 10 | `m2/ch5-batch10-series-foundations` | #29 | 数项级数定义与必要条件 6 条 | ✅ merged |
| Batch 11 | `m2/ch5-batch11-convergence-tests` | #30 | 判别法核心 8 条 | ✅ merged |
| Batch 12 | `m2/ch5-batch12-uniform-convergence` | #31 | 函数项级数与一致收敛 6 条 | ✅ merged |
| Batch 13 | `m2/ch5-batch13-power-series` | #32 | 幂级数与 Taylor 级数 7 条 | ✅ merged |

### Ch3–Ch5 draft → stable 评审（已合并）

| 章节 | 分支 | PR | 评审要点 | 状态 |
|---|---|---|---|---|
| Ch3 微分 25 条 | `m2/ch3-stable-promotion` | #34 | 中值定理 / L'Hospital / Taylor 双余项核验；修正 6 处过期交叉引用 | ✅ merged |
| Ch4 积分 29 条 | `m2/ch4-stable-promotion` | #35 | Darboux / N-L / 反常积分判别核验；修正 2 处自相矛盾「常见错误」+ 17 处过期标注 | ✅ merged |
| Ch5 级数 27 条 | `m2/ch5-stable-promotion` | #36 | 比值/根值/积分/Abel-Dirichlet/一致收敛/Cauchy–Hadamard 逐条手验；无内容错误 | ✅ merged |

### M2 DoD 校验（`_meta/m2-plan.md` §7）· 6/6 达标 ✅

- [x] 80 条新增 stable（数学分析累计 ≥ 127）→ **81 新增，analysis 累计 128**
- [x] CI 4/4 全绿，悬空引用 = 0 → **7951 公式全过 · 悬空 0**
- [x] `_meta/dependency-graph.json` 节点数 ≥ 132 → **133 节点 / 565 边**
- [x] 每章 ≥ 5 条带 applications 字段 → **Ch3=11 · Ch4=5 · Ch5=6**
- [x] STATUS.md 更新为 M2 完成 → 本次更新
- [x] 所有 Batch 通过 PR 流程合并到 main → **PR #19–#36 全部 merged，无遗留开放 PR**

---

## 非功能指标基准

| 指标 | 目标 | 当前 |
|---|---|---|
| KaTeX 渲染时间 | < 200ms | 待测量 |
| 首屏加载时间（TTI） | < 2s | 待测量 |
| 条目录入时间 | ≤ 30 min/条 | 待测量 |
| CI 检查通过率 | 100% | 4/4（GitHub Actions 已激活，PR #19–#36 全绿） |
| 悬空引用数 | 0（main 分支） | 0（全库 133 条目） |
| KaTeX 公式总量 | — | 7951 条，全部通过校验 |
| 依赖图规模 | 节点 ≥ 132（M2 DoD） | 133 节点 / 565 边 ✅ |
| 条目状态分布 | review ≥ 80% 时启动 stable 评审 | stable = 128 / draft = 5（analysis 全 stable；余 algebra 4 占位 + cross 1） |

---

*M0 / M1 / M2 已全面闭环。M2 完成：Ch3（25）+ Ch4（29）+ Ch5（27）= 81 条 stable（PR #19–#36），DoD 6/6 达标，数学分析 Ch1–Ch5 全部 stable（128 条）。*
*下一步：进入 M3 高等代数 Ch1–Ch5（≥ 120 条 stable），当前已起 4 条占位。*
