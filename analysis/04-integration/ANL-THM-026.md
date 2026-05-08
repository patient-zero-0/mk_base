---
title: "Riemann 可积充要条件（Darboux 准则）"
type: theorem
id: ANL-THM-026
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - Darboux 准则
  - 充要条件
depends:
  - ANL-DEF-026
  - ANL-DEF-025
  - ANL-DEF-027
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §9.2"
difficulty: 4
related:
  - ANL-THM-027
  - ANL-THM-028
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $f : [a, b] \to \mathbb{R}$ **有界**。

## 结论

> 下列三个条件**等价**：
>
> 1. $f$ 在 $[a, b]$ 上 Riemann 可积（[[ANL-DEF-026]]）；
> 2. $\displaystyle \overline{\int_a^b} f = \underline{\int_a^b} f$（[[ANL-DEF-025]] 上下积分相等）；
> 3. **Darboux 准则**：对任意 $\varepsilon > 0$，存在 $[a, b]$ 的分割 $P$ 使
>     $$ U(f, P) - L(f, P) = \sum_{i=1}^n \omega_i(f) \cdot \Delta x_i < \varepsilon, $$
>     其中 $\omega_i(f)$ 是 $f$ 在子区间 $[x_{i-1}, x_i]$ 上的振幅（[[ANL-DEF-027]]）。

## 几何/直觉理解

> Darboux 准则把"可积性"转化为"**上下和差能任意小**"——
> 即"外接矩形面积"与"内接矩形面积"能挤压到任意接近。
>
> 等价地：$\sum \omega_i \Delta x_i$ 度量"在每段子区间上 $f$ 的振幅 $\times$ 段长"——
> 它是函数振荡程度的"加权和"，能任意小意味着 $f$ "几乎不振荡"或"振荡集合很薄"。

## 证明

> 仅证 1 ⇔ 3（最实用）。1 ⇔ 2 见 [[ANL-DEF-026]]。

**证明（1 ⇒ 3）**：设 $f$ 可积，$I := \int_a^b f$。任给 $\varepsilon > 0$。

由 [[ANL-DEF-026]]，$\exists \delta > 0$ 使对任意 $\|P\| < \delta$ 与任意标记，$|S(f, P, \boldsymbol{\xi}) - I| < \varepsilon/4$。

固定一个 $\|P\| < \delta$ 的分割 $P$。在每个子区间 $[x_{i-1}, x_i]$ 上：

- 取 $\boldsymbol{\xi}$ 使 $\xi_i$ 接近 $f$ 的最大点（由 sup 性质，对 $\varepsilon/(4(b-a))$ 任意接近 $M_i$）：
    $f(\xi_i) > M_i - \varepsilon/(4(b-a))$
    故 $S(f, P, \boldsymbol{\xi}) > U(f, P) - \varepsilon/4$，得 $U(f, P) < S(f, P, \boldsymbol{\xi}) + \varepsilon/4 < I + \varepsilon/2$。
- 取 $\boldsymbol{\xi}'$ 使 $f(\xi_i') < m_i + \varepsilon/(4(b-a))$，类似得 $L(f, P) > I - \varepsilon/2$。

合并：$U(f, P) - L(f, P) < (I + \varepsilon/2) - (I - \varepsilon/2) = \varepsilon$。$\blacksquare$

**证明（3 ⇒ 1）**：设 $\forall \varepsilon, \exists P_\varepsilon$ 使 $U(f, P_\varepsilon) - L(f, P_\varepsilon) < \varepsilon$。

记 $\overline I := \overline{\int_a^b} f$，$\underline I := \underline{\int_a^b} f$。
由 [[ANL-DEF-025]] 性质 $L(f, P_\varepsilon) \leq \underline I \leq \overline I \leq U(f, P_\varepsilon)$，故
$$
0 \leq \overline I - \underline I \leq U(f, P_\varepsilon) - L(f, P_\varepsilon) < \varepsilon.
$$
由 $\varepsilon$ 任意，$\overline I = \underline I =: I$。

下证 $f$ 是 Riemann 可积且积分值为 $I$。任给 $\varepsilon > 0$，取 $P_\varepsilon$ 使 $U(f, P_\varepsilon) - L(f, P_\varepsilon) < \varepsilon/2$。
对任意标记 $\boldsymbol{\xi}$，
$$
L(f, P_\varepsilon) \leq S(f, P_\varepsilon, \boldsymbol{\xi}) \leq U(f, P_\varepsilon),
\quad L(f, P_\varepsilon) \leq I \leq U(f, P_\varepsilon).
$$
两式相减：$|S - I| \leq U - L < \varepsilon/2 < \varepsilon$。

> **注**：上述论证仅对**特定**分割 $P_\varepsilon$ 给出 $|S - I| < \varepsilon$。
> 完整证明 Riemann 可积性（"对任意 $\|P\| < \delta$ 都成立"）需要利用 Darboux 准则的"加细一致性"——
> 详见教材 §9.2 的精细分析。$\blacksquare$

## 常见错误

- ✗ 把 Darboux 准则的 "$\exists$ 分割" 误读为 "$\forall$ 分割"。
  正确：**存在某个**分割使 $U - L < \varepsilon$ 即可——这等价于 $\overline I = \underline I$，
  与"对一切充分细的分割"是等价表述但形式不同。
- ✗ 漏掉"$f$ 有界"前提。
  无界函数不能定义 $M_i, m_i$（可能 $= \pm\infty$），Darboux 和无意义。
  无界函数的可积性需借助反常积分（[[ANL-DEF-029]]，待建）框架。
- ✗ 误以为"$\omega_i \to 0$（$\|P\| \to 0$）"等价于可积。
  反例：Dirichlet 函数（$f = 1_\mathbb{Q}$）每个子区间上 $\omega_i \equiv 1$，
  $\sum \omega_i \Delta x_i = b - a$ 无论怎样分割都不为零——故不可积。
  关键：可积要求**振幅与段长的加权和**任意小，不仅是局部 $\omega_i$ 小。

## 推论与应用

- **核心推论 1**：[[ANL-THM-027]] 闭区间连续 ⇒ 可积（用 Cantor 一致连续 + Darboux 准则）
- **核心推论 2**：[[ANL-THM-028]] 单调函数 ⇒ 可积（直接套用）
- **推论 3**：闭区间上**仅在有限多点不连续**的有界函数可积
  （证明：把这些点用任意小的子区间覆盖；其余部分连续，振幅可控）
- **进阶**（Lebesgue 准则）：有界 $f$ 在 $[a, b]$ 上 Riemann 可积 $\iff$ $f$ 的不连续点集**测度为零**

## 链接

- 前置：[[ANL-DEF-025]] Darboux 上下和、[[ANL-DEF-026]] Riemann 可积、[[ANL-DEF-027]] 振幅
- 直接应用：[[ANL-THM-027]]、[[ANL-THM-028]]
- 进阶（不在本知识库 M2 范围）：Lebesgue 可积性准则
