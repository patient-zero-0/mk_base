---
title: "函数极限的四则运算"
type: theorem
id: ANL-THM-009
subject: analysis
chapter: 02-continuity
tags:
  - 函数极限
  - 四则运算
  - 基础定理
depends:
  - ANL-DEF-008
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §3.2"
difficulty: 3
related:
  - ANL-THM-004
  - ANL-THM-010
  - ANL-THM-011
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $f, g$ 在 $x_0$ 的某去心邻域内有定义，
$\lim_{x \to x_0} f(x) = A$，$\lim_{x \to x_0} g(x) = B$（按 [[ANL-DEF-008]]）。

## 结论

下列四则运算极限均成立：

1. **加法**：$\displaystyle \lim_{x \to x_0} \big(f(x) + g(x)\big) = A + B$。
2. **减法**：$\displaystyle \lim_{x \to x_0} \big(f(x) - g(x)\big) = A - B$。
3. **乘法**：$\displaystyle \lim_{x \to x_0} \big(f(x) \cdot g(x)\big) = A \cdot B$。
4. **除法**：若 $B \neq 0$，则**在 $x_0$ 的某去心邻域内 $g(x) \neq 0$**，且
   $$
   \lim_{x \to x_0} \frac{f(x)}{g(x)} = \frac{A}{B}.
   $$

特别地，对常数 $c$：$\lim_{x \to x_0} c \cdot f(x) = c \cdot A$。

## 直觉理解

数列极限四则定理（[[ANL-THM-004]]）的"连续版本"——
把"$n$ 充分大"换成"$x$ 充分接近 $x_0$"，论证结构完全平行。

关键差别只在**域**：

| 维度 | 数列 [[ANL-THM-004]] | 函数 [[ANL-THM-009]] |
|---|---|---|
| 自变量 | 离散 $n \in \mathbb{N}^*$ | 连续 $x \in \mathbb{R}$ |
| "靠近"工具 | $\forall n > N$ | $\forall x : 0 < \|x - x_0\| < \delta$ |
| "有界"来源 | 收敛 ⇒ 有界（[[ANL-THM-002]]） | 极限存在 ⇒ 局部有界 |
| 除法分母 | 从某项起 $b_n \neq 0$ | 在某去心邻域内 $g(x) \neq 0$ |

核心思路同样三件事：

1. **加减**：用三角不等式直接控制；
2. **乘法**：拆分 $fg - AB = f(g - B) + B(f - A)$，靠**局部有界**抑制 $f$；
3. **除法**：先证 $1/g(x) \to 1/B$，关键是**$|g(x)| \geq |B|/2$ 在某去心邻域**（保号性 [[ANL-THM-010]] 的应用）。

## 证明（以乘法为例）

**证明（乘法）**：要证 $|f(x) g(x) - AB| \to 0$ 当 $x \to x_0$。

**关键拆分**：
$$
f(x) g(x) - AB = f(x) (g(x) - B) + B (f(x) - A).
$$

**局部有界化**：取 $\varepsilon = 1$ 在 $f$ 的极限定义中，存在 $\delta_0 > 0$ 使
$\forall x : 0 < |x - x_0| < \delta_0 \implies |f(x) - A| < 1$，
故 $|f(x)| < |A| + 1 =: M$。

任给 $\varepsilon > 0$：

- 由 $f \to A$，$\exists \delta_1 > 0, \forall x : 0 < |x - x_0| < \delta_1 \implies |f(x) - A| < \tfrac{\varepsilon}{2(|B| + 1)}$
- 由 $g \to B$，$\exists \delta_2 > 0, \forall x : 0 < |x - x_0| < \delta_2 \implies |g(x) - B| < \tfrac{\varepsilon}{2M}$

取 $\delta = \min\{\delta_0, \delta_1, \delta_2\}$，对任意 $0 < |x - x_0| < \delta$：
$$
|f(x) g(x) - AB| \leq M \cdot \tfrac{\varepsilon}{2M} + |B| \cdot \tfrac{\varepsilon}{2(|B| + 1)} < \varepsilon.
$$
$\blacksquare$

加减证明从略；除法 = 乘法 × 倒数，关键是 $1/g \to 1/B$，
该步骤需要 $|g(x)| \geq |B|/2$（由保号性 [[ANL-THM-010]] 应用于 $|g|$ 给出）。

## 常见错误

- ✗ **滥用四则运算到极限不存在的情形**。
  反例：$f(x) = \sin(1/x), g(x) = -\sin(1/x)$ 当 $x \to 0$ 时极限均不存在，
  但 $f(x) + g(x) = 0 \to 0$ 收敛于 $0$。定理**要求两个极限都先存在**，否则不能直接套用。
- ✗ **0/0、∞/∞ 直接套除法**。
  这些是**不定型**——必须先化简（如 L'Hôpital、变量代换、夹逼）再判断。
  反例：$\lim_{x \to 0} \tfrac{\sin x}{x} = 1$（不是 $0/0$），$\lim_{x \to 0} \tfrac{x}{x^2} = \infty$（同样 $0/0$ 但结果不同）。
- ✗ **忽视"分母非零"的局部性条件**。
  当 $B \neq 0$ 时分母从某去心邻域起 $g(x) \neq 0$ 是结论的一部分；
  $B = 0$ 则分式定义都成问题，本定理不覆盖。

## 推论

- **多项式极限**：若 $f \to A$，则 $P(f) \to P(A)$ 对任何多项式 $P$。
- **有理函数极限**：若 $f \to A$ 且 $Q(A) \neq 0$，则 $P(f)/Q(f) \to P(A)/Q(A)$。

## 链接

- 前置：[[ANL-DEF-008]]
- 数列版本：[[ANL-THM-004]]
- 关联：[[ANL-THM-010]] 函数极限的保号性（除法证明的关键）、[[ANL-THM-011]] 复合函数极限
