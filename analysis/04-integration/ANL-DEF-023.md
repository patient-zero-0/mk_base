---
title: "Riemann 和"
type: definition
id: ANL-DEF-023
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - Riemann 积分
  - 求和
depends:
  - ANL-DEF-022
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §9.1"
difficulty: 2
related:
  - ANL-DEF-025
  - ANL-DEF-026
applications:
  - "数值分析：矩形 / 梯形 / Simpson 求积公式"
  - "概率论：连续随机变量期望的逼近 $\\sum f(\\xi_i) \\Delta x_i$"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设 $f : [a, b] \to \mathbb{R}$，$P = \{x_0, x_1, \ldots, x_n\}$ 为 $[a, b]$ 的分割（[[ANL-DEF-022]]）。
在每个子区间 $[x_{i-1}, x_i]$ 中**任选**一个**标记点** $\xi_i \in [x_{i-1}, x_i]$（$i = 1, \ldots, n$），
得到**带标记的分割**（$P, \boldsymbol{\xi}$）。

**Riemann 和** 定义为
$$
S(f, P, \boldsymbol{\xi}) := \sum_{i=1}^{n} f(\xi_i) \cdot \Delta x_i = \sum_{i=1}^{n} f(\xi_i)(x_i - x_{i-1}).
$$

## 几何含义

> Riemann 和 $S(f, P, \boldsymbol{\xi})$ 等于以 $f(\xi_i)$ 为高、$\Delta x_i$ 为宽的 $n$ 个**矩形面积之和**——
> 是曲线下方面积的一个**矩形近似**。

```text
     f
     │  ▆▆▆          ▇▇
     │ ▆ │▆▆        ▇│▇▇
     │▆  │ │▆▆▆    ▇▇│ │▇
     │   │ │   ▆▆▆▇▇ │ │
     │ ξ₁│ξ₂│  ξ₃│  ξ₄ │ξ₅
     └──┴──┴───┴──┴───┴── x
       x₁ x₂  x₃ x₄  x₅
```

## 与 Darboux 和的对比

设 $f$ 有界，$M_i := \sup_{[x_{i-1}, x_i]} f$，$m_i := \inf_{[x_{i-1}, x_i]} f$。
$$
L(f, P) := \sum m_i \Delta x_i \leq S(f, P, \boldsymbol{\xi}) \leq \sum M_i \Delta x_i =: U(f, P).
$$

即对任意标记 $\boldsymbol{\xi}$，Riemann 和介于 [[ANL-DEF-025]] 下和与上和之间。

> **关键差别**：
>
> - **Riemann 和**依赖于**分割 + 标记**两者。变标记同一分割能产生不同 Riemann 和。
> - **Darboux 和**仅依赖于分割（$M_i, m_i$ 由分割与函数决定，不需选标记）。
>
> Darboux 和扮演 Riemann 和的"上下界"，使得证明可积性时不必处理标记的选择，
> 仅需控制分割的精细度。

## 选标记的常见特殊情形

| 标记选取 | 名称 | 备注 |
|---|---|---|
| $\xi_i = x_{i-1}$（左端点） | **左 Riemann 和** $L_n$ | 数值分析"矩形法"的一种 |
| $\xi_i = x_i$（右端点） | **右 Riemann 和** $R_n$ | 同上 |
| $\xi_i = (x_{i-1} + x_i) / 2$ | **中点 Riemann 和** $M_n$ | 比左右更精确（误差 $O(\Delta^2)$） |
| $f(\xi_i) = M_i$ | **上和** | 仅当 $f$ 在子区间上取得最大时可选 |
| $f(\xi_i) = m_i$ | **下和** | 同上对应最小值 |

## 直觉理解

> Riemann 和 = "把曲线下方面积**用矩形拼出来**"。
> 取的标记越密、越随便都不影响极限——只要分割模 $\|P\| \to 0$，
> 矩形拼出的面积总会逼近"真正的曲线下方面积"。
> 这正是 Riemann 可积性（[[ANL-DEF-026]]）的精神。

**为什么可以"任选"标记？**
直觉上：如果 $f$ 不剧烈振荡，子区间内的 $f$ 值差不多，故任选 $\xi_i$ 都接近"该子区间的代表值"。
一致连续函数（[[ANL-DEF-024]]）天然满足这点，所以连续函数 Riemann 可积（[[ANL-THM-027]]）。

## 链接

- 前置：[[ANL-DEF-022]] 分割
- 上下界：[[ANL-DEF-025]] Darboux 上下和
- 极限定义：[[ANL-DEF-026]] Riemann 可积

## 跨专业应用

- **数值分析**：矩形法、梯形法、Simpson 法都是 Riemann 和的特定标记选择
- **概率论**：连续随机变量 $X$ 的期望 $E[g(X)] = \int g(x) p(x) dx$ 的离散化逼近就是 Riemann 和
