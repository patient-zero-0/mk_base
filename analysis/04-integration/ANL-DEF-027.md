---
title: "振幅（Oscillation）"
type: definition
id: ANL-DEF-027
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 振幅
  - 可积性
depends:
  - ANL-DEF-005
uses:
  - ANL-AX-001
status: draft
source: "华东师范大学《数学分析》第5版 §9.2"
difficulty: 2
related:
  - ANL-DEF-025
  - ANL-DEF-026
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设 $f : E \to \mathbb{R}$ 在非空集 $E \subseteq \mathbb{R}$ 上有界（[[ANL-DEF-005]] 推广至函数）。

**$f$ 在 $E$ 上的振幅**（oscillation）定义为
$$
\omega(f, E) := \sup_{x \in E} f(x) - \inf_{x \in E} f(x).
$$

由 [[ANL-AX-001]] 确界原理，$\sup$ 与 $\inf$ 都存在；又 $\sup \geq \inf$，故 $\omega(f, E) \geq 0$。

**等价表达**（差对的上确界）：
$$
\omega(f, E) = \sup \big\{ |f(x) - f(y)| : x, y \in E \big\}.
$$

> **证明**："$\geq$"：取 $x, y \in E$，由 sup-inf 性质 $f(x) - f(y) \leq M - m = \omega$，故 $|f(x) - f(y)| \leq \omega$。
> "$\leq$"：对任 $\varepsilon > 0$，取 $x_\varepsilon$ 使 $f(x_\varepsilon) > M - \varepsilon/2$、$y_\varepsilon$ 使 $f(y_\varepsilon) < m + \varepsilon/2$，
> 则 $|f(x_\varepsilon) - f(y_\varepsilon)| > M - m - \varepsilon = \omega - \varepsilon$。由 $\varepsilon$ 任意，$\sup |f(x) - f(y)| \geq \omega$。

## 在分割上的振幅记号

对子区间 $[x_{i-1}, x_i]$，记 $\omega_i := \omega(f, [x_{i-1}, x_i]) = M_i - m_i$（[[ANL-DEF-025]] 中 $M_i, m_i$）。

由此**Darboux 上下和之差**可写成：
$$
U(f, P) - L(f, P) = \sum_{i=1}^{n} (M_i - m_i) \Delta x_i = \sum_{i=1}^{n} \omega_i \Delta x_i.
$$

> **核心意义**：**$U - L = \sum \omega_i \Delta x_i$ 是 Riemann 可积性的"误差度量"**。
> Riemann 可积 $\iff \forall \varepsilon > 0, \exists$ 分割 $P$ 使 $\sum \omega_i \Delta x_i < \varepsilon$（即 [[ANL-THM-026]] Darboux 准则）。
> 这把"上下积分相等"的判断**完全转化为**"振幅的加权和能任意小"。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 振幅 $\omega(f, E)$ | $E$ 上 $f$ 的"全局变化范围" |
| 模长 $\|P\|$（[[ANL-DEF-022]]） | 分割中**最长子区间的长度** |
| 局部振幅 $\omega_i = \omega(f, [x_{i-1}, x_i])$ | 子区间上的振幅，依赖分割 |
| 函数连续性 | 在点 $x_0$ 处 $\omega(f, [x_0 - \delta, x_0 + \delta]) \to 0$（$\delta \to 0$）当且仅当 $f$ 在 $x_0$ 连续 |

> **连续性的振幅刻画**：$f$ 在 $x_0$ 连续 $\iff$ $\displaystyle \lim_{\delta \to 0^+} \omega(f, (x_0 - \delta, x_0 + \delta) \cap E) = 0$。
> 这是 [[ANL-DEF-012]] 函数连续的"振幅版本"。

## 直觉理解

> 振幅 $\omega(f, E)$ = "在 $E$ 上 $f$ 最大值与最小值的差"——衡量 $f$ 在 $E$ 上"波动多大"。
>
> 振幅小 = 函数在该集合上"几乎是常数"；
> 振幅大 = 函数在该集合上"变化剧烈"。
>
> **几何**：振幅就是 $f$ 在 $E$ 上图像的"垂直跨度"。

**示例**（$E = [0, 1]$）：

| $f(x)$ | $\omega(f, [0, 1])$ |
|---|---|
| 常数 $c$ | $0$ |
| $x$ | $1$ |
| $x^2$ | $1$ |
| $\sin x$ | $\sin 1 \approx 0.841$ |
| $\sin(1/x)$（$x \neq 0$, 任补 $f(0)$） | $2$（值取遍 $[-1, 1]$） |
| Dirichlet 函数 | $1$ |

## 振幅的可加性（次可加）

设 $E = E_1 \cup E_2$（不必不交），则
$$
\omega(f, E) \leq \omega(f, E_1) + \omega(f, E_2),
$$
但等号不一定成立——比如 $E_1, E_2$ 不交且 $f$ 在两者上各为不同常数，等号取得；而若 $E_1, E_2$ 重叠且共享中间值，可能严格 $<$。

## 链接

- 前置：[[ANL-DEF-005]] 有界、[[ANL-AX-001]] 确界原理
- 关键关系：$U(f, P) - L(f, P) = \sum \omega_i \Delta x_i$，把振幅嵌入 [[ANL-DEF-025]]
- 用于：[[ANL-THM-026]] Riemann 可积的 Darboux 准则（M2 Batch 6 待建）
- 与连续性的关系：$f$ 在 $x_0$ 连续 $\iff$ 振幅在 $x_0$ 邻域趋零
