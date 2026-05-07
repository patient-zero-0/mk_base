# 悬空引用待办清单

> 本文件由 `scripts/check_dangling_refs.py --report` 在 PR CI 中自动同步。

---

## 当前状态

**全库悬空 ID 数：0**（最近一次扫描：2026-05-05）

M0 / M1 阶段已完成全部 🔴 最高 / 🟠 高 / 🟡 中 优先级前置条目的 stable 升级，
共 47 条 analysis stable 条目。M2 计划见 [`m2-plan.md`](./m2-plan.md)。

---

## 远期已知"未来悬空"（M2 / M3 待建）

以下 ID 在当前条目正文（**非 frontmatter 引用字段**）以"待建"形式提到，
不会被 CI 标记为悬空，仅作 M2 / M3 排期参考：

| 计划 ID | 类型 | 标题 | 出现位置 | 计划阶段 |
|---|---|---|---|---|
| `ALG-THM-XXX` | theorem | 谱半径定理（$\rho(A) < 1 \Rightarrow A^n \to 0$） | CROSS-001 | M3 |
| `ALG-THM-XXX` | theorem | Jordan 标准形存在性 | CROSS-001 | M3 |
| 待定 | theorem | 函数极限四则运算的"$\infty$ 型"扩展 | ANL-THM-004 推广提及 | M2 Ch3 |
| 待定 | theorem | 函数极限的夹逼定理 | ANL-THM-005 推广提及 | M2 Ch3 |

> ✅ 已落地（M1）：
>
> - Cantor 一致连续定理 → [[ANL-THM-015]]（M1 Batch 2）
> - 自然常数 e 的极限定义 → [[ANL-DEF-009]]（M1 Batch 4）
> - 函数极限的四则运算 → [[ANL-THM-009]]（M1 Batch 4）

---

## 优先级图例

- 🔴 最高：阻断 M1 多个条目，必须最先建立
- 🟠 高：阻断 M1 单个条目
- 🟡 中：被引用于「相关」字段，可延后
- 🟢 低：仅出现在「跨课」或「应用」描述中
