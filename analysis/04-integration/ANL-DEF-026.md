---
title: "Riemann 可积与定积分"
type: definition
id: ANL-DEF-026
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - Riemann 积分
  - 定积分
depends:
  - ANL-DEF-022
  - ANL-DEF-023
  - ANL-DEF-025
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §9.1, §9.2"
difficulty: 3
related:
  - ANL-DEF-027
applications:
  - "物理：功 $W = \\int F \\, dx$、电荷 $Q = \\int I \\, dt$"
  - "几何：曲线下方面积、弧长、旋转体体积"
  - "概率论：连续随机变量分布函数 $F(x) = \\int_{-\\infty}^x p(t) \\, dt$"
  - "信号处理：信号能量 $E = \\int |f(t)|^2 \\, dt$"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述（Riemann 极限形式）

设 $f : [a, b] \to \mathbb{R}$ 有界。若存在实数 $I$，对任意 $\varepsilon > 0$，存在 $\delta > 0$，使得对 $[a, b]$ 的**任意**分割 $P$（[[ANL-DEF-022]]）满足 $\|P\| < \delta$ 与**任意**标记 $\boldsymbol{\xi}$，
$$
\big| S(f, P, \boldsymbol{\xi}) - I \big| < \varepsilon
$$
（其中 $S(f, P, \boldsymbol{\xi})$ 是 [[ANL-DEF-023]] Riemann 和），则称 $f$ 在 $[a, b]$ 上 **Riemann 可积**。
此时 $I$ 称为 $f$ 在 $[a, b]$ 上的**定积分**，记作
$$
\int_a^b f(x) \, dx \quad \text{或简记} \quad \int_a^b f.
$$

记号约定：
$$
\int_a^a f := 0, \qquad \int_b^a f := -\int_a^b f.
$$

## Darboux 等价定义

> 设 $f$ 在 $[a, b]$ 上有界。$f$ 在 $[a, b]$ 上 Riemann 可积 $\iff$
> $$
> \underline{\int_a^b} f = \overline{\int_a^b} f,
> $$
> 即 [[ANL-DEF-025]] 上积分与下积分相等。
>
> 此时 $\displaystyle \int_a^b f = \underline{\int_a^b} f = \overline{\int_a^b} f = \lim_{\|P\| \to 0} U(f, P) = \lim_{\|P\| \to 0} L(f, P)$。
>
> 等价证明属 Riemann–Darboux 定理，详见教材 §9.2 或 [[ANL-THM-026]]（M2 Batch 6 待建）。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| Riemann 可积 | $\|P\| \to 0$ 时所有 Riemann 和有共同极限（标记任意） |
| 上积分 / 下积分 | 上 / 下和的 $\inf$ / $\sup$ — 单独存在但未必相等 |
| 不定积分（原函数） | $\int f \, dx = F(x) + C$，关心反求导（[[ANL-DEF-028]] 待建） |
| 定积分 | 一个**数**，等于上下积分相等时的共同值 |
| Lebesgue 可积 | 更广义的可积概念，处理更多函数（如 Dirichlet 函数） |

## 直觉理解

> Riemann 可积 = "**任凭怎么切、怎么取标记，矩形面积之和最终都收敛到同一个数**"。
>
> "切" = 选分割 $P$（只要 $\|P\|$ 越来越小）；
> "取标记" = 选 $\xi_i$（左、右、中点、随机都行）；
> "同一个数" = 不论选择，极限唯一存在。
>
> 这是**真正"鲁棒"**的可积概念——若不同切法给出不同极限，就说明这函数太"狂野"，
> 不该谈"曲线下方面积"。
>
> **Dirichlet 函数反例**：
> $f(x) = \begin{cases} 1, & x \in \mathbb{Q} \\ 0, & x \notin \mathbb{Q} \end{cases}$
> 取有理标记 $\Rightarrow$ Riemann 和恒为 $b - a$；取无理标记 $\Rightarrow$ Riemann 和恒为 $0$。
> 极限不一致，故 $f$ 在任何 $[a, b]$ 上**不**Riemann 可积。
> （但它 Lebesgue 可积，积分 $= 0$——这是 Lebesgue 比 Riemann 强的著名例子。）

## 等价的 Cauchy 收敛条件

> $f$ 在 $[a, b]$ 上 Riemann 可积 $\iff$ 对任意 $\varepsilon > 0$，存在 $\delta > 0$，使对任意两分割 $P_1, P_2$（$\|P_1\|, \|P_2\| < \delta$）与对应标记，
> $$
> \big| S(f, P_1, \boldsymbol{\xi}_1) - S(f, P_2, \boldsymbol{\xi}_2) \big| < \varepsilon.
> $$
>
> 即 Riemann 和"自身的 Cauchy 性"。这与函数极限的 Cauchy 准则平行（[[ANL-THM-007]] 数列版的推广）。

## 一些可积条件（先列结论，证明在后续条目）

下列函数在 $[a, b]$ 上 Riemann 可积：

- 连续函数（[[ANL-THM-027]] 待建）
- 单调函数（[[ANL-THM-028]] 待建）
- 仅在有限个点不连续的有界函数
- 更一般地：**几乎处处连续**的有界函数（Lebesgue 准则，进阶内容）

## 链接

- 前置：[[ANL-DEF-022]] 分割、[[ANL-DEF-023]] Riemann 和、[[ANL-DEF-025]] Darboux 上下和
- 充要条件：[[ANL-THM-026]] Darboux 准则（M2 Batch 6 待建）
- 充分条件：[[ANL-THM-027]] 连续 ⇒ 可积、[[ANL-THM-028]] 单调 ⇒ 可积（M2 Batch 6 待建）
- 计算工具：[[ANL-THM-032]] Newton-Leibniz 公式（M2 Batch 7 待建）

## 跨专业应用

- **物理**：功 $W = \int F(x) \, dx$、电荷 $Q = \int I(t) \, dt$、动能 $\int v \, dp$ 等"累加效应"全部为定积分
- **几何**：曲线 $y = f(x)$ 在 $[a, b]$ 上方与 $x$ 轴所夹面积 $S = \int_a^b f(x) \, dx$（$f \geq 0$）
- **概率论**：连续随机变量 $X$ 落入区间 $[a, b]$ 的概率 $P(a \leq X \leq b) = \int_a^b p(x) \, dx$
- **信号处理**：信号 $f(t)$ 在 $[a, b]$ 上的能量 $E = \int_a^b |f(t)|^2 \, dt$；Fourier 变换基础
