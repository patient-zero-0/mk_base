---
title: "单调函数 ⇒ Riemann 可积"
type: theorem
id: ANL-THM-028
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 单调
  - 可积性
depends:
  - ANL-DEF-026
  - ANL-DEF-027
  - ANL-THM-026
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §9.3"
difficulty: 3
related:
  - ANL-THM-027
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $f : [a, b] \to \mathbb{R}$ 在闭区间 $[a, b]$ 上**单调**（递增或递减）。

> **备注**：单调函数自动**有界**——闭区间端点的函数值就是上下界。
> 故 Darboux 上下和、振幅等概念有意义。

## 结论

> $f$ 在 $[a, b]$ 上 **Riemann 可积**。

## 几何/直觉理解

> 单调函数的振幅有"望远镜抵消"效应：
> 不妨设 $f$ 单调递增，则在子区间 $[x_{i-1}, x_i]$ 上 $M_i = f(x_i)$、$m_i = f(x_{i-1})$，
> 故 $\omega_i = f(x_i) - f(x_{i-1})$。
>
> 振幅之和：
> $$
> \sum_{i=1}^n \omega_i = \sum_{i=1}^n \big[ f(x_i) - f(x_{i-1}) \big] = f(b) - f(a),
> $$
> 这是一个**与分割无关的常数**！
>
> 故振幅加权和 $\sum \omega_i \Delta x_i \leq \|P\| \cdot \sum \omega_i = \|P\| \cdot (f(b) - f(a))$，
> 当 $\|P\| \to 0$ 时趋于 $0$——由 [[ANL-THM-026]] Darboux 准则即得可积。

## 证明

**证明：** 不妨设 $f$ 单调递增（递减情形对偶或考虑 $-f$）。

任给 $\varepsilon > 0$。

**情形 1：$f(b) = f(a)$**。$f$ 单调递增 + 端点相等 ⇒ $f$ 恒为常数 $f(a)$。常数函数显然可积，结论成立。

**情形 2：$f(b) > f(a)$**。取分割 $P$ 满足
$$
\|P\| < \frac{\varepsilon}{f(b) - f(a)}.
$$

在子区间 $[x_{i-1}, x_i]$ 上由 $f$ 递增，$M_i = f(x_i)$、$m_i = f(x_{i-1})$，故
$$
\omega_i = f(x_i) - f(x_{i-1}) \geq 0.
$$

振幅加权和：
$$
\sum_{i=1}^n \omega_i \Delta x_i \leq \|P\| \cdot \sum_{i=1}^n \omega_i = \|P\| \cdot \big[ f(b) - f(a) \big] < \frac{\varepsilon}{f(b)-f(a)} \cdot (f(b) - f(a)) = \varepsilon.
$$

由 [[ANL-THM-026]] Darboux 准则，$f$ 在 $[a, b]$ 上 Riemann 可积。$\blacksquare$

## 常见错误

- ✗ 把"单调"误读为"严格单调"。
  本定理对**非严格**单调（允许相等）也成立——常数函数即极端例子。
- ✗ 误以为单调函数都连续。
  反例：$f(x) = \begin{cases} 0, & x < 0 \\ 1, & x \geq 0 \end{cases}$ 单调递增，
  在 $0$ 处跳跃间断——但仍是 Riemann 可积的。
  这恰恰说明本定理与 [[ANL-THM-027]] **互补**：单调可积允许跳跃间断，连续可积允许非单调。
- ✗ 误以为单调可积函数的不连续点至多有限。
  反例：单调函数的不连续点可以是**可数无穷**（比如 $f(x) = \sum_{q_n < x} 2^{-n}$，其中 $\{q_n\}$ 为 $[a,b]$ 中有理数），
  在每个 $q_n$ 处都跳跃。但仍 Riemann 可积——单调函数的不连续点至多可数（这是 Lebesgue 测度零）。

## 推论与应用

- **应用**：分布函数 $F(x) = P(X \leq x)$（概率论中）在 $\mathbb{R}$ 上单调递增 ⇒ 在任意闭区间上可积
- **比较**（与 [[ANL-THM-027]] 的差异）：
    | 条件 | 不连续点 | 振荡 |
    |---|---|---|
    | 连续 | 无 | $\omega_i \to 0$ uniformly |
    | 单调 | 至多可数 | $\sum \omega_i = f(b) - f(a)$ 有界 |
- **进阶**：单调函数 = 有界变差（BV）的特殊情形——BV 函数也可积

## 链接

- 前置：[[ANL-DEF-026]] Riemann 可积、[[ANL-DEF-027]] 振幅、[[ANL-THM-026]] Darboux 准则
- 关联：[[ANL-THM-027]] 闭区间连续 ⇒ 可积（互补的另一充分条件）
- 进阶：有界变差函数（BV）的可积性（不在本知识库 M2 范围）
