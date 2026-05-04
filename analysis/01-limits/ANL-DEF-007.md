---
title: "数列发散到无穷"
type: definition
id: ANL-DEF-007
subject: analysis
chapter: 01-limits
tags:
  - 极限
  - 发散
  - 无穷大
depends:
  - ANL-DEF-001
  - ANL-DEF-004
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §2.1"
difficulty: 2
related:
  - ANL-DEF-005
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设 $\{a_n\}$ 是数列。

**$\{a_n\}$ 发散到 $+\infty$**（记作 $\lim_{n \to \infty} a_n = +\infty$），若：
$$
\forall M > 0, \quad \exists N \in \mathbb{N}^*, \quad \forall n > N : \quad a_n > M.
$$

**$\{a_n\}$ 发散到 $-\infty$**：把上式改为 $a_n < -M$。

**$\{a_n\}$ 发散到 $\infty$**（**不分正负**）：把上式改为 $|a_n| > M$。

> 警告：$\lim a_n = +\infty$ 是**记号**，**不是**说极限存在等于某个数。
> 严格意义上 $\{a_n\}$ 仍是**发散**数列，只是发散方式特殊（"有规律地变大"）。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 收敛 [[ANL-DEF-004]] | 项靠近一个有限的 $L \in \mathbb{R}$ |
| 发散到 $+\infty$ | 项越过任何固定上界 $M$ |
| 一般发散 | 既不收敛也不发散到无穷（如 $(-1)^n$） |
| 无界 [[ANL-DEF-005]] | 存在子列趋于无穷，但**整数列未必都"持续变大"** |

注意第 4 行：**无界 ≠ 发散到 $\infty$**。
反例：$\{n, 1, n+1, 1, n+2, 1, \ldots\}$（在 $n$ 与 $1$ 间交替）无界，但因为有 $a_{n_k} = 1$ 的子列，**不**满足"$|a_n| > M$ 对充分大 $n$ 全部成立"。

## 直觉理解

把"发散到 $+\infty$"想成"逐渐爬升、最终越过任何天花板"：

> 任你画出一条多高的水平线 $y = M$，
> 数列项 $a_n$ 都会**最终穿越并保持在这条线之上**。

形式上与收敛的 ε-N 定义对偶——把"$|a_n - L| < \varepsilon$"换成"$a_n > M$"，
把"任意小的 $\varepsilon$"换成"任意大的 $M$"，量词 $\forall M > 0$ 表达的是
"**无论目标多高**"。

## 常见错误

- ✗ 把 $\lim a_n = +\infty$ 当成"极限存在"。
  扩展实数 $\bar{\mathbb{R}} = \mathbb{R} \cup \{\pm \infty\}$ 中可以认为它收敛于 $+\infty$，
  但在标准 $\mathbb{R}$ 框架下它**不收敛**——四则运算定理不能直接套用。
  反例：$a_n = n, b_n = -n$ 都"$\to \infty$"，但 $a_n + b_n = 0$ 收敛于 $0$，
  与"无穷 + 无穷 = 无穷"的直觉违背。
- ✗ 认为"无界 ⇒ 发散到 $\infty$"。错。无界只要求存在子列趋无穷，
  反例如上文 $\{n, 1, n+1, 1, \ldots\}$。

## 运算约定（扩展实数）

虽不严格收敛，下列规则在物理 / 工程语境常用：

| 运算 | 是 / 否定型 |
|---|---|
| $\infty + \infty = \infty$ | ✅ |
| $\infty - \infty$ | ❌ 不定型 |
| $\infty \cdot 0$ | ❌ 不定型 |
| $\infty / \infty$ | ❌ 不定型 |
| $a / 0$（$a \neq 0$） | ❌ 在 $\mathbb{R}$ 中无定义；含极限时视为 $\pm\infty$ 类型 |

不定型必须**化简后**再判断，常用工具：L'Hôpital、夹逼、变量代换。

## 链接

- 前置：[[ANL-DEF-001]]、[[ANL-DEF-004]]
- 相关：[[ANL-DEF-005]] 有界数列（"未发散到 $\infty$"是有界的必要条件之一）
