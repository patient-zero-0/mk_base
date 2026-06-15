---
title: "微分"
type: definition
id: ANL-DEF-015
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - 线性近似
  - 导数
depends:
  - ANL-DEF-014
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §4.5"
difficulty: 2
related:
  - ANL-DEF-014
applications:
  - "数值分析：一阶 Taylor 近似 $f(x_0+h)\\approx f(x_0)+f'(x_0)h$ 的误差控制"
  - "工程：测量误差传播 $\\Delta y \\approx f'(x_0) \\Delta x$"
  - "物理：体积/压强等量在小扰动下的线性近似"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设 $f : I \to \mathbb{R}$ 在 $x_0 \in I$ 可导（[[ANL-DEF-014]]）。给自变量增量 $\Delta x$，
**$f$ 在 $x_0$ 关于 $\Delta x$ 的微分**定义为
$$
df \big|_{x_0} := f'(x_0) \cdot \Delta x.
$$

约定 $\Delta x = dx$（即把自变量微元写成 $dx$），上式记作
$$
\boxed{\,dy = f'(x_0) \, dx.\,}
$$

**等价刻画**：$f$ 在 $x_0$ 可微（即微分存在）当且仅当
$$
\Delta y := f(x_0 + \Delta x) - f(x_0) = A \cdot \Delta x + o(\Delta x),\quad (\Delta x \to 0)
$$
其中 $A = f'(x_0)$。即"函数增量等于线性主部加高阶无穷小"。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 函数增量 $\Delta y$ | 真实增量，等于 $f(x_0+\Delta x) - f(x_0)$ |
| 微分 $dy$ | $\Delta y$ 的**线性主部**，等于 $f'(x_0)\Delta x$ |
| 导数 $f'(x_0)$ [[ANL-DEF-014]] | 一个数（变化率） |
| 微分 $dy$ | 一个量（导数 $\times$ 自变量微元） |

> 一维情形："**可微 $\iff$ 可导**"。多元情形则不同，需独立定义。

## 直觉理解

> 微分把曲线在 $x_0$ 附近**线性化**：在显微镜下看 $f$ 的图像，越靠近 $x_0$，
> 函数越像它的切线 $y = f(x_0) + f'(x_0)(x - x_0)$。
>
> $dy$ 就是沿切线走 $\Delta x$ 时纵坐标的变化；
> 真实 $\Delta y$ 则是沿曲线走的变化。
> 两者之差 $\Delta y - dy = o(\Delta x)$ 比 $\Delta x$ "更高阶地小"。

**几何画面**：

```text
  y
  │       曲线 y=f(x)
  │       ╱
  │      ╱  ← Δy（真实增量）
  │     ╱
  │   ┄┄┄┄  ← dy（沿切线，线性主部）
  │  ╱
  │ ╱        切线 y=f(x₀)+f'(x₀)(x-x₀)
  └────────── x
       x₀   x₀+Δx
```

差额 $\Delta y - dy$ 是图中"曲线与切线之间的小弯月"——它是 $o(\Delta x)$。

## 链接

- 前置：[[ANL-DEF-014]] 导数
- 用于：Taylor 公式（[[ANL-THM-025]]）的零阶截断
- 应用例题：[[ANL-EX-008]] 用定义求初等函数导数

## 跨专业应用

- **数值分析**：用 $f(x_0+h) \approx f(x_0) + f'(x_0)h$ 做一阶近似计算，误差为 $o(h)$
- **工程**：自变量测量误差 $\Delta x$ 经过 $f$ 后近似为 $|\Delta y| \approx |f'(x_0)| \cdot |\Delta x|$
- **物理**：理想气体 $pV = nRT$，固定 $T$ 时 $V$ 关于 $p$ 的微分给出体积响应
