---
title: "多项式带余除法"
type: theorem
id: ALG-THM-001
subject: algebra
chapter: 01-polynomials
tags:
  - 多项式
  - 整除
  - 基础定理
depends:
  - ALG-DEF-001
  - ALG-DEF-002
uses: []
status: draft
source: "丘维声《高等代数》第3版 §1.2"
difficulty: 3
related:
  - ALG-THM-002
applications:
  - "符号计算系统：多项式约简的核心算法"
  - "编码理论：CRC 校验码的多项式除法实现"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $f(x), g(x) \in K[x]$，且 $g(x) \neq 0$。

## 结论

> 存在**唯一**一对多项式 $q(x), r(x) \in K[x]$ 使
> $$
> f(x) = g(x) \cdot q(x) + r(x), \quad \text{其中 } r(x) = 0 \text{ 或 } \deg r < \deg g.
> $$

称 $q(x)$ 为**商**，$r(x)$ 为**余式**。

## 几何/直觉理解

多项式带余除法是整数带余除法的"次数镜像"：

- 整数：$a = b q + r, \quad 0 \leq r < |b|$（用绝对值衡量"小"）
- 多项式：$f = g q + r, \quad \deg r < \deg g$（用次数衡量"小"）

每次"除"的过程是"减掉 $g$ 的最高次倍式以降低 $f$ 的次数"，
直到次数低于 $g$ 为止——这就是手工长除法的精确表述。

唯一性来自次数的良序性：每一步降次都是确定的。

## 证明

**存在性**（构造）：对 $\deg f$ 用强归纳。

- 若 $\deg f < \deg g$：取 $q = 0, r = f$ 即可。
- 若 $\deg f = n \geq m = \deg g$：设 $f$ 的首项系数为 $a_n$，$g$ 的首项系数为 $b_m$。
  令 $f_1(x) = f(x) - \tfrac{a_n}{b_m} x^{n - m} g(x)$。
  关键观察：$f_1$ 的 $x^n$ 项被消去，故 $\deg f_1 < n$。
  由归纳假设，存在 $q_1, r$ 使 $f_1 = g q_1 + r$，且 $r = 0$ 或 $\deg r < m$。
  代回：
  $$
  f = \frac{a_n}{b_m} x^{n - m} g + g q_1 + r = g \left( \frac{a_n}{b_m} x^{n - m} + q_1 \right) + r.
  $$
  取 $q = \tfrac{a_n}{b_m} x^{n - m} + q_1$ 即得。

**唯一性**：设 $f = g q_1 + r_1 = g q_2 + r_2$，两式相减：
$$
g (q_1 - q_2) = r_2 - r_1.
$$
若 $q_1 \neq q_2$，则左侧 $\deg g(q_1 - q_2) \geq \deg g = m$；
但右侧 $\deg(r_2 - r_1) < m$（两者次数都 $< m$），矛盾。
故 $q_1 = q_2$，从而 $r_1 = r_2$。$\blacksquare$

## 常见错误

- ✗ 漏检条件 $g \neq 0$。零多项式无次数，定理不适用——除以 0 在多项式环里同样无意义。
- ✗ 忽视余式的次数约束 $\deg r < \deg g$，写成"任何分解 $f = gq + r$ 都对"。
  反例：$x^2 + 1 = x \cdot x + 1$（合法，$\deg 1 = 0 < \deg x = 1$），
  但 $x^2 + 1 = (x + 1)(x - 1) + 2$ 中 $r = 2$ 也合法——**两种写法对应不同的 $g$**。
  唯一性说的是"对**给定** $g$，$(q, r)$ 唯一"，不是"$f$ 只有一种分解"。
- ✗ 把"$K[x]$ 上的带余除法"误用到"$\mathbb{Z}[x]$ 上"。
  $K$ 必须是**域**（每个非零系数可逆），否则首项系数 $b_m$ 不一定可除。
  反例：在 $\mathbb{Z}[x]$ 中 $f = x, g = 2x$，求商需要 $1/2 \notin \mathbb{Z}$。

## 推论与应用

- **余数定理**：$f(c) = $ $f(x)$ 除以 $(x - c)$ 的余数。
- **因式定理**：$(x - c) \mid f(x) \iff f(c) = 0$。
- 用于辗转相除法（Euclid 算法）求最大公因式（[[ALG-THM-003]]）。
- 用于 [[ALG-THM-002]] 唯一分解定理证明。

## 链接

- 前置：[[ALG-DEF-001]]、[[ALG-DEF-002]]
- 用于定理：[[ALG-THM-003]] 辗转相除法与 Bézout 等式、[[ALG-THM-002]] 唯一分解定理
- 推广：欧氏环（Euclidean Domain）的一般理论

## 跨专业应用

- **符号计算**：Mathematica / SymPy 等系统的核心化简算法 `PolynomialReduce`、`PolynomialQuotient`、`PolynomialRemainder` 均以本定理为底层
- **编码理论**：CRC（循环冗余校验）算法本质是 $\mathbb{F}_2[x]$ 中的多项式带余除法——发送端发送 $f \cdot x^k - r$，接收端用 $g$ 整除验错
- **密码学**：椭圆曲线运算、AES 密钥扩展中均需有限域上多项式除法
