---
title: "闭区间连续 ⇒ Riemann 可积"
type: theorem
id: ANL-THM-027
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 连续
  - 可积性
depends:
  - ANL-DEF-012
  - ANL-DEF-026
  - ANL-THM-015
  - ANL-THM-026
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §9.3"
difficulty: 3
related:
  - ANL-THM-028
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $f : [a, b] \to \mathbb{R}$ 在闭区间 $[a, b]$ 上**连续**（[[ANL-DEF-012]]）。

## 结论

> $f$ 在 $[a, b]$ 上 **Riemann 可积**（[[ANL-DEF-026]]）。

## 几何/直觉理解

> 连续函数在闭区间上不会"剧烈振荡"——
> 由 [[ANL-THM-015]] Cantor 一致连续定理，对任意 $\varepsilon$，存在统一的 $\delta$ 使
> $|x - y| < \delta \Rightarrow |f(x) - f(y)| < \varepsilon$。
>
> 把 $[a, b]$ 切成模长 $< \delta$ 的分割，每个子区间上 $f$ 的振幅 $< \varepsilon$。
> 故振幅加权和 $\sum \omega_i \Delta x_i < \varepsilon \cdot (b - a)$ 任意小，由 [[ANL-THM-026]] Darboux 准则即得可积。

## 证明

**证明：** 由 $f$ 在闭区间 $[a, b]$ 上连续，由 [[ANL-THM-015]] **Cantor 一致连续定理**，
$f$ 在 $[a, b]$ 上**一致连续**。

任给 $\varepsilon > 0$。取 $\varepsilon' := \varepsilon / (b - a)$。
由一致连续，$\exists \delta > 0$ 使
$$
\forall x, y \in [a, b]: \quad |x - y| < \delta \implies |f(x) - f(y)| < \varepsilon'.
$$

取分割 $P$ 满足 $\|P\| < \delta$。在每个子区间 $[x_{i-1}, x_i]$ 上，$f$ 连续 ⇒ 取得最大与最小（[[ANL-THM-014]] 最值定理），设 $f(p_i) = M_i$、$f(q_i) = m_i$，其中 $p_i, q_i \in [x_{i-1}, x_i]$。

由 $|p_i - q_i| \leq \Delta x_i \leq \|P\| < \delta$，
$$
\omega_i = M_i - m_i = f(p_i) - f(q_i) \leq |f(p_i) - f(q_i)| < \varepsilon'.
$$

故
$$
U(f, P) - L(f, P) = \sum_{i=1}^n \omega_i \Delta x_i < \varepsilon' \sum \Delta x_i = \varepsilon' (b - a) = \varepsilon.
$$

由 [[ANL-THM-026]] Darboux 准则，$f$ 在 $[a, b]$ 上 Riemann 可积。$\blacksquare$

## 常见错误

- ✗ 漏掉"闭区间"条件。
  反例：$f(x) = 1/x$ 在 $(0, 1]$ 上连续但**无界**，$\omega_i$ 在含 $0$ 的子区间上无穷大，定理失效。
  开区间或半开半闭区间上的可积性需借助反常积分（[[ANL-DEF-029]]，待建）。
- ✗ 误以为闭区间上可积函数都连续。
  反例：阶梯函数（如 $\text{sgn}(x)$ 在 $[-1, 1]$）在 $0$ 处不连续，但仍可积——
  Riemann 可积函数集**严格大于**连续函数集，含有限/可数个间断的有界函数。
- ✗ 不用 Cantor 直接试图证。
  有人尝试：连续 $\Rightarrow$ 任意一致连续。错！——逐点连续不蕴含一致连续（[[ANL-DEF-024]]）。
  必须明确使用 [[ANL-THM-015]] Cantor 定理，**闭区间是关键**。

## 推论与应用

- **直接应用**：所有初等函数（多项式、指数、三角、对数等）在其定义域内的闭区间上 Riemann 可积
- **加强**：闭区间上**有限多点不连续**的有界函数仍可积——证明：把不连续点用小区间盖住，其余分段连续部分套用本定理
- **进阶比较**：
    | 充分条件 | 来源 |
    |---|---|
    | $f$ 连续 | 本定理 |
    | $f$ 单调 | [[ANL-THM-028]] |
    | $f$ 有界 + 不连续点测度为零 | Lebesgue 准则（进阶） |

## 链接

- 前置：[[ANL-DEF-012]] 函数连续、[[ANL-DEF-026]] Riemann 可积、[[ANL-THM-015]] Cantor 一致连续、[[ANL-THM-026]] Darboux 准则
- 关联：[[ANL-THM-028]] 单调可积（独立的另一充分条件）
