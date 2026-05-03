---
title: "一致连续"
type: definition
id: ANL-DEF-024
subject: analysis
chapter: 02-continuity
tags:
  - 连续
  - ε-δ
  - 一致性
depends:
  - ANL-DEF-008
  - ANL-DEF-012
uses: []
status: review
source: "华东师范大学《数学分析》第5版 §4.2"
difficulty: 3
related:
  - ANL-PROB-031
applications:
  - "数值分析：插值和数值积分误差的一致估计"
  - "信号处理：连续信号采样的稳定性"
---

## 定义陈述

设 $f : I \to \mathbb{R}$，$I \subseteq \mathbb{R}$ 为区间。

**$f$ 在 $I$ 上一致连续**，若：
$$
\forall \varepsilon > 0, \quad \exists \delta > 0, \quad \forall x_1, x_2 \in I : \quad |x_1 - x_2| < \delta \implies |f(x_1) - f(x_2)| < \varepsilon.
$$

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 在 $x_0$ 连续 [[ANL-DEF-012]] | $\delta = \delta(\varepsilon, x_0)$，**逐点**保证 |
| 在 $I$ 上每点连续 | 各点 $\delta$ 不必互通，可能 $\inf_{x \in I} \delta(\varepsilon, x) = 0$ |
| 一致连续 | $\delta = \delta(\varepsilon)$ **对全 $I$ 共用** |

## 直觉理解

> 普通连续：先**指定一个点 $x_0$**，再针对这个点找 δ。
> 不同的点可以用不同的 δ。
>
> 一致连续：必须**先定好一个 δ**，
> 然后这个 δ 要对区间上**所有点对** $(x_1, x_2)$ 同时生效。
>
> 区别就在于 **δ 是否依赖 $x_0$**。

直观图像：把 $f$ 的图像与一个宽 $\delta$、高 $\varepsilon$ 的"水平窗口"沿 $x$ 轴拖动——
若任何位置上窗口都能"罩住" $f$ 的相邻部分，则 $f$ 一致连续。
对于陡峭程度无界增长的函数（如 $f(x) = x^2$ 在 $\mathbb{R}$ 上），找不到对所有位置都够小的 $\delta$。

## 常见错误

- ✗ 认为"区间上每点连续"就等于一致连续。
  反例：$f(x) = 1/x$ 在 $(0, 1)$ 上每点连续，但 $\delta(\varepsilon, x_0) \to 0$ 当 $x_0 \to 0^+$，故非一致连续。
  另一类反例：[[ANL-PROB-031]] 中 $\sin(x^2)$ 在 $\mathbb{R}$ 上每点连续但非一致连续。
- ✗ 漏掉"$\forall x_1, x_2$"，写成"$\forall x_1 \in I, \exists x_2$"。
  量词错位会得到几乎平凡的命题，丧失"区间整体"含义。

## 链接

- 前置：[[ANL-DEF-008]]、[[ANL-DEF-012]]
- 关键定理（待建）：Cantor 定理（闭区间上连续 ⇒ 一致连续）
- 例题：[[ANL-PROB-031]]

## 跨专业应用

- **数值分析**：一致连续保证以网格步长 $h \to 0$ 的均匀逼近误差一致趋零
- **信号处理**：连续信号 $f(t)$ 在采样间隔 $\delta$ 下的最大失真可由 $\varepsilon$ 控制
