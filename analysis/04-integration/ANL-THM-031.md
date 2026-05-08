---
title: "变限积分函数的连续性与可微性"
type: theorem
id: ANL-THM-031
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 变限积分
  - 微积分基本定理
depends:
  - ANL-DEF-026
  - ANL-DEF-014
  - ANL-DEF-012
  - ANL-DEF-028
  - ANL-THM-027
  - ANL-THM-029
  - ANL-THM-030
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §9.5"
difficulty: 4
related:
  - ANL-THM-030
  - ANL-THM-032
  - ANL-DEF-028
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件与结论

设 $f$ 在 $[a, b]$ 上 **Riemann 可积**（[[ANL-DEF-026]]）。定义**变限积分函数**
$$
\Phi(x) := \int_a^x f(t) \, dt, \quad x \in [a, b].
$$

### 结论 1：连续性

> $\Phi$ 在 $[a, b]$ 上**连续**（[[ANL-DEF-012]]），实际上是 Lipschitz 连续。

### 结论 2：可微性（微积分基本定理 Part 1）

> 若 $f$ 在 $x_0 \in [a, b]$ 处**连续**，则 $\Phi$ 在 $x_0$ 处可导（[[ANL-DEF-014]]），且
> $$
> \Phi'(x_0) = f(x_0).
> $$
>
> **特别地**：若 $f$ 在 $[a, b]$ 上处处连续，则 $\Phi$ 在 $[a, b]$ 上处处可导，
> $\Phi'(x) = f(x)$ 对所有 $x \in [a, b]$ 成立——即 **$\Phi$ 是 $f$ 的一个原函数**（[[ANL-DEF-028]]）。
> 这就是"连续 ⇒ 必有原函数"的存在性证明。

## 几何/直觉理解

> **变限积分**：$\Phi(x)$ 是"从 $a$ 到 $x$ 曲线下方面积"的函数。
> 当 $x$ 增大一点 $\Delta x$，新增的面积近似为 $f(x) \Delta x$（小矩形）。
> 故 $\Phi$ 关于 $x$ 的瞬时变化率正是 $f(x)$——这是"积分与求导互逆"的几何直觉。
>
> **更精确**：$\Phi(x + \Delta x) - \Phi(x) = \int_x^{x+\Delta x} f$，
> 由 [[ANL-THM-030]] 积分中值定理（$f$ 在小区间上连续），存在 $\xi$ 介于 $x$ 与 $x+\Delta x$ 之间使
> $\int_x^{x+\Delta x} f = f(\xi) \Delta x$。
> 当 $\Delta x \to 0$，$\xi \to x$，由 $f$ 在 $x$ 连续 $f(\xi) \to f(x)$。
> 故 $\Phi'(x) = f(x)$。

## 证明

### 证明（结论 1：Lipschitz 连续）

**证明：** $f$ 可积 ⇒ $f$ 有界，$\exists M > 0$ 使 $|f(x)| \leq M$ 对所有 $x \in [a, b]$。

对任意 $x_1, x_2 \in [a, b]$（不妨 $x_1 < x_2$），由 [[ANL-THM-029]] 区间可加性：
$$
\Phi(x_2) - \Phi(x_1) = \int_{x_1}^{x_2} f(t) \, dt.
$$

由 [[ANL-THM-029]] 三角不等式与单调性：
$$
|\Phi(x_2) - \Phi(x_1)| = \left| \int_{x_1}^{x_2} f \right| \leq \int_{x_1}^{x_2} |f| \leq M(x_2 - x_1).
$$

故 $\Phi$ 在 $[a, b]$ 上以常数 $M$ Lipschitz 连续，从而连续。$\blacksquare$

### 证明（结论 2：在连续点处可导）

**证明：** 设 $f$ 在 $x_0 \in [a, b]$ 处连续。证 $\Phi'(x_0) = f(x_0)$。

任给 $\varepsilon > 0$。由 $f$ 在 $x_0$ 连续，$\exists \delta > 0$ 使 $|t - x_0| < \delta \Rightarrow |f(t) - f(x_0)| < \varepsilon$。

对 $0 < |\Delta x| < \delta$（不妨 $\Delta x > 0$，反向类似），考察
$$
\frac{\Phi(x_0 + \Delta x) - \Phi(x_0)}{\Delta x} - f(x_0) = \frac{1}{\Delta x} \int_{x_0}^{x_0 + \Delta x} f(t) \, dt - f(x_0).
$$

把 $f(x_0)$ 写为 $\dfrac{1}{\Delta x} \int_{x_0}^{x_0 + \Delta x} f(x_0) \, dt$（常数积分），合并：
$$
= \frac{1}{\Delta x} \int_{x_0}^{x_0 + \Delta x} \big[ f(t) - f(x_0) \big] \, dt.
$$

对 $t \in [x_0, x_0 + \Delta x]$（在 $\delta$ 邻域内），$|f(t) - f(x_0)| < \varepsilon$。由 [[ANL-THM-029]] 单调性 + 三角不等式：
$$
\left| \frac{1}{\Delta x} \int_{x_0}^{x_0+\Delta x} \big[ f(t) - f(x_0) \big] \, dt \right| \leq \frac{1}{\Delta x} \cdot \varepsilon \cdot \Delta x = \varepsilon.
$$

故
$$
\left| \frac{\Phi(x_0 + \Delta x) - \Phi(x_0)}{\Delta x} - f(x_0) \right| < \varepsilon.
$$

由 $\varepsilon$ 任意，$\Phi'(x_0)$ 存在且 $= f(x_0)$。$\blacksquare$

## 常见错误

- ✗ 误以为"$f$ 可积 ⇒ $\Phi$ 可导"。
  反例：$f(x) = \text{sgn}(x)$ 在 $[-1, 1]$ 可积，$\Phi(x) = |x| - 1$（取 $a = -1$），但 $\Phi$ 在 $0$ 处不可导。
  正确：可积仅给出 $\Phi$ 连续；**可导**需要 $f$ 在该点连续。
- ✗ 把"$\Phi$ 在 $x_0$ 可导 ⇒ $f$ 在 $x_0$ 连续"当作真命题。
  事实：$\Phi'(x_0)$ 存在**不蕴含** $f$ 在 $x_0$ 连续——
  反例：$f$ 在 $x_0$ 处可去间断（$\lim f(x) \neq f(x_0)$ 但极限存在），
  $\Phi'(x_0) = \lim_{x \to x_0} f(x) \neq f(x_0)$，但 $\Phi'$ 可能仍存在。
- ✗ 求 $\Phi(x) = \int_a^{u(x)} f(t) \, dt$（变限是 $u(x)$）的导数时漏链式法则。
  正确：$\Phi'(x) = f(u(x)) \cdot u'(x)$（[[ANL-THM-018]] 链式法则）。
- ✗ 把 $\int_{u(x)}^{v(x)} f$ 拆分时方向错误。
  正确：$\dfrac{d}{dx} \int_{u(x)}^{v(x)} f(t) \, dt = f(v(x)) v'(x) - f(u(x)) u'(x)$（**两端**都要算 + 注意符号）。

## 推论与应用

- **推论 1（连续函数必有原函数）**：$f \in C[a, b]$ ⇒ $\Phi(x) = \int_a^x f$ 是 $f$ 的原函数（[[ANL-DEF-028]]）
- **推论 2（Newton-Leibniz 公式）**：[[ANL-THM-032]] 由本定理与"原函数差为常数"导出
- **应用**：积分上限函数的求导（含链式法则的复合形式）

## 链接

- 前置：[[ANL-DEF-026]]、[[ANL-DEF-014]]、[[ANL-DEF-012]]、[[ANL-DEF-028]]、[[ANL-THM-027]]、[[ANL-THM-029]]、[[ANL-THM-030]]
- 关键应用：[[ANL-THM-032]] Newton-Leibniz 公式（本定理 + 原函数差为常数）
- 几何对偶：积分中值定理 [[ANL-THM-030]] 给出 $\Phi$ 增量的精确表达
