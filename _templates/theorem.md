---
title: "<在此处填写定理标题，例如：单调有界定理>"
type: theorem
id: ANL-THM-XXX
subject: analysis
chapter: 01-limits
tags:
  - 极限
  - 完备性
depends: []                # 前置定义/定理 ID 列表
uses: []                   # 依赖的公理 ID（如 ANL-AX-001 确界原理）
status: draft
source: "华东师范大学《数学分析》第5版 §X.Y"
difficulty: 3
related: []
corollaries: []            # 由本定理推出的推论 ID（可选）
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

陈述定理成立所需的所有前提。例：

> 设 $\{a_n\}$ 是单调递增的实数列，且存在 $M \in \mathbb{R}$ 使得
> $a_n \leq M$ 对所有 $n \in \mathbb{N}$ 成立。

## 结论

> 则 $\{a_n\}$ 收敛，且 $\displaystyle \lim_{n \to \infty} a_n = \sup_n a_n$。

## 几何/直觉理解

> 必填板块。用比喻、图像或类比说明这个定理在描述什么。
> 写作要点参考 `refs/style-guide.md`。

## 证明

> 完整证明，每一步都给出依据。引用其它条目时使用 `[[ID]]` 格式。

**证明：** 由 [[ANL-AX-001]] 确界原理，……

故 $\displaystyle \lim_{n \to \infty} a_n = L$。$\blacksquare$

## 常见错误

> 难度 ≥ 3 的定理必填。每条须给出反例或反驳，参考 `refs/style-guide.md`。

- ✗ ……（反例：……）
- ✗ ……（容易犯的原因：……）

## 推论与应用

- 推论：[[ANL-THM-XXX]]
- 在例题中应用：[[ANL-EX-XXX]]

<!-- applications 字段非空时，本节才必须出现 -->
## 跨专业应用

- **领域 A**：……
