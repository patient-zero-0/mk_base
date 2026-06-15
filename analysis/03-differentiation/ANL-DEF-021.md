---
title: "渐近线（水平 / 垂直 / 斜）"
type: definition
id: ANL-DEF-021
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - 渐近行为
  - 函数图像
depends:
  - ANL-DEF-008
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §6.5"
difficulty: 2
related:
  - ANL-DEF-008
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设 $y = f(x)$ 是定义在适当区间上的函数，图像为平面曲线。

### 水平渐近线

若 $\displaystyle \lim_{x \to +\infty} f(x) = c$（$c \in \mathbb{R}$），则直线 $y = c$ 是 $f$ 图像的**右水平渐近线**。
左水平渐近线类似（$x \to -\infty$）。

### 垂直渐近线

若 $\displaystyle \lim_{x \to x_0^+} f(x) = +\infty$（或 $-\infty$，或 $x \to x_0^-$），则直线 $x = x_0$ 是 $f$ 图像的**垂直渐近线**。

### 斜渐近线

若存在常数 $k \neq 0$ 与 $b$ 使 $\displaystyle \lim_{x \to +\infty} \big[ f(x) - (kx + b) \big] = 0$，
则直线 $y = kx + b$ 是 $f$ 图像的**右斜渐近线**。左侧（$x \to -\infty$）类似。

> 当 $k = 0$ 时即水平渐近线，故"斜渐近线"通常专指 $k \neq 0$ 情形。

## 斜渐近线的求法

> 若 $f$ 有右斜渐近线 $y = kx + b$，则
> $$
> k = \lim_{x \to +\infty} \frac{f(x)}{x}, \qquad b = \lim_{x \to +\infty} \big[ f(x) - kx \big].
> $$
> 反之，若上述两极限都存在且 $k \neq 0$，则 $y = kx + b$ 即为斜渐近线。

**推导**：由定义 $f(x) - kx - b \to 0$，两边除以 $x$ 得 $\dfrac{f(x)}{x} - k - \dfrac{b}{x} \to 0$，
即 $\dfrac{f(x)}{x} \to k$。再由 $f(x) - kx \to b$ 得 $b$ 的求法。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 水平渐近线 $y = c$ | 横向"靠拢"——$x \to \pm\infty$ 时 $f \to c$ |
| 垂直渐近线 $x = x_0$ | 纵向"爆破"——$x \to x_0$ 时 $f \to \pm\infty$ |
| 斜渐近线 $y = kx + b$ | 沿斜线"贴近"——$x \to \pm\infty$ 时 $f - (kx+b) \to 0$ |
| 切线 | 局部信息（$x_0$ 处的线性近似） |
| 渐近线 | 整体信息（$x \to \infty$ 时的极限性 / 边界行为） |

## 直觉理解

> 渐近线是函数图像的"边界引导线"：当变量趋向极限位置（无穷远或某个奇点）时，
> 图像越来越**贴近**这条直线。
>
> **典型例子**：
>
> | 函数 | 渐近线类型 | 渐近线方程 |
> |---|---|---|
> | $f(x) = 1/x$ | 水平 + 垂直 | $y = 0$（$x \to \pm\infty$）；$x = 0$（$x \to 0$） |
> | $f(x) = e^{-x} + x$ | 斜（右） | $y = x$（$x \to +\infty$） |
> | $f(x) = \arctan x$ | 水平 | $y = \pm \pi/2$ |
> | $f(x) = \ln x$ | 垂直 | $x = 0$（$x \to 0^+$） |

## 常见错误

- ✗ 把"$f$ 在某点不连续"等同于"垂直渐近线"。
  反例：$f(x) = \dfrac{\sin x}{x}$（$x \neq 0$）, $f(0) = 1$。
  在 $0$ 处可去间断（极限存在），**没有垂直渐近线**。
  垂直渐近线要求 $f \to \pm\infty$。
- ✗ 求斜渐近线时漏掉左右两端。
  反例：$f(x) = x + e^{-x}$。
  $\lim_{x \to +\infty} f/x = 1$，故 $k = 1$；$\lim_{x \to +\infty}(f - x) = 0$，故 $b = 0$。
  右斜渐近线 $y = x$。但 $\lim_{x \to -\infty} f/x = 1 - \lim e^{-x}/x = -\infty / -\infty$ 不收敛 ⇒ 左侧无斜渐近线。
- ✗ 仅看 $\lim f/x = k$ 就断定有斜渐近线。
  反例：$f(x) = x + \ln x$，$f/x \to 1$，但 $f - x = \ln x \to +\infty$，**没有 $b$**——
  函数比线性"略快地往上跑"，没有斜渐近线。

## 链接

- 前置：[[ANL-DEF-008]] 函数极限
- 应用：作图（曲线大致形态分析）
- 关联：函数渐近行为综合判定
