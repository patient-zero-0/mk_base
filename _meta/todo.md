# 悬空引用待办清单

> 本文件由 `scripts/check_dangling_refs.py --report` 在 PR CI 中自动同步。

---

## 当前状态

**全库悬空 ID 数：0**（最近一次扫描：2026-05-03）

M0 阶段已完成全部 🔴 最高 / 🟠 高 / 🟡 中 优先级前置条目的 draft 编写。

---

## 远期已知"未来悬空"（M2 / M3 待建）

以下 ID 在当前条目正文（**非 frontmatter 引用字段**）以"待建"形式提到，
不会被 CI 标记为悬空，仅作 M2 / M3 排期参考：

| 计划 ID | 类型 | 标题 | 出现位置 | 计划阶段 |
|---|---|---|---|---|
| 待定 | theorem | Cantor 定理（闭区间连续 ⇒ 一致连续） | ANL-DEF-024、ANL-PROB-031 | M2 |
| `ALG-THM-XXX` | theorem | 谱半径定理（$\rho(A) < 1 \Rightarrow A^n \to 0$） | CROSS-001 | M3 |
| `ALG-THM-XXX` | theorem | Jordan 标准形存在性 | CROSS-001 | M3 |
| 待定 | definition | 自然常数 e（极限定义） | ANL-THM-006 推论提及 | M1 后段 |

---

## 优先级图例

- 🔴 最高：阻断 M1 多个条目，必须最先建立
- 🟠 高：阻断 M1 单个条目
- 🟡 中：被引用于「相关」字段，可延后
- 🟢 低：仅出现在「跨课」或「应用」描述中
