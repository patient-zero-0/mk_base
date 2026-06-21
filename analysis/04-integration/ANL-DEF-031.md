---
title: "变限积分函数"
type: definition
id: ANL-DEF-031
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 变限积分
  - 函数构造
depends:
  - ANL-DEF-026
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §9.5"
difficulty: 2
related:
  - ANL-THM-031
  - ANL-DEF-028
  - ANL-THM-032
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设 $f$ 在 $[a, b]$ 上 Riemann 可积（[[ANL-DEF-026]]）。**$f$ 的变上限积分函数**定义为
$$
\Phi : [a, b] \to \mathbb{R}, \quad \Phi(x) := \int_a^x f(t) \, dt.
$$

类似地，**变下限积分函数**：
$$
\Psi(x) := \int_x^b f(t) \, dt.
$$

由 [[ANL-DEF-026]] 区间可加性约定，$\Phi(a) = 0$、$\Psi(b) = 0$；且 $\Phi(x) + \Psi(x) = \int_a^b f$（常数）。

## 一般化：变上下限积分

设 $u, v : [c, d] \to [a, b]$，定义
$$
G(x) := \int_{u(x)}^{v(x)} f(t) \, dt.
$$
当 $u, v$ 可导时，$G$ 的导数由 [[ANL-THM-031]] 与 [[ANL-THM-018]] 链式法则给出：
$$
G'(x) = f(v(x)) \cdot v'(x) - f(u(x)) \cdot u'(x) \quad (\text{在 } f \text{ 连续点}).
$$

## 关键性质（详见 [[ANL-THM-031]]）

> 设 $f$ 在 $[a, b]$ 上 Riemann 可积。则
>
> 1. $\Phi$ 在 $[a, b]$ 上**连续**（实际上 Lipschitz 连续，常数 $= \sup |f|$）
> 2. 在 $f$ 的**连续点** $x_0$ 处，$\Phi$ 可导且 $\Phi'(x_0) = f(x_0)$
> 3. 若 $f$ 在 $[a, b]$ 上处处连续，$\Phi$ 是 $f$ 的一个**原函数**（[[ANL-DEF-028]]）
>
> 证明见 [[ANL-THM-031]]。

## 直觉理解

> 把"积分"视为一种"操作"，把"$f$"作为输入，"$\Phi$"作为输出（一个新函数，下标 = 积分上限）。
>
> **几何**：固定起点 $a$、变化终点 $x$，$\Phi(x)$ = 从 $a$ 到 $x$ 的曲线下方面积。
> 当 $x$ 增大，新增面积 $\approx f(x) \Delta x$（小矩形）——这就是 $\Phi'(x) = f(x)$ 的几何来源。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 定积分 $\int_a^b f$ | 一个**数** |
| 变限积分 $\Phi(x) = \int_a^x f$ | 一个**函数**（参数 $x$ 是积分上限） |
| 不定积分 $\int f \, dx = F + C$ | 一个**函数族**（[[ANL-DEF-028]]） |
| 原函数 | 满足 $F' = f$ 的具体函数（不唯一） |

> 三者通过 [[ANL-THM-032]] **N-L 公式**联系：连续 $f$ 的原函数 = 任意常数偏移的变限积分函数。
> 即 $F = \Phi + C \iff F' = f$（在区间上）。

## 链接

- 前置：[[ANL-DEF-026]] Riemann 可积
- 性质：[[ANL-THM-031]] 变限积分的连续性与可微性
- 与原函数：[[ANL-DEF-028]] 原函数（连续 $f$ 的原函数 = 变限积分 + $C$）
- 计算桥梁：[[ANL-THM-032]] Newton-Leibniz 公式
