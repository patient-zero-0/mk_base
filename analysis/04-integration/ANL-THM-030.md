---
title: "积分中值定理"
type: theorem
id: ANL-THM-030
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 中值定理
  - 平均值
depends:
  - ANL-DEF-026
  - ANL-DEF-012
  - ANL-THM-013
  - ANL-THM-014
  - ANL-THM-027
  - ANL-THM-029
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §9.5"
difficulty: 3
related:
  - ANL-THM-022
  - ANL-THM-029
applications:
  - "概率论：连续随机变量取值的'平均位置'描述"
  - "物理：连续介质的'代表点'刻画"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件与结论

### 形式 1（连续函数版 / 第一积分中值定理）

**条件**：$f : [a, b] \to \mathbb{R}$ 连续（[[ANL-DEF-012]]）。

**结论**：存在 $\xi \in [a, b]$ 使
$$
\int_a^b f(x) \, dx = f(\xi) \cdot (b - a).
$$

> 等价说法：函数 $f$ 在 $[a, b]$ 上的"积分平均值" $\dfrac{1}{b-a} \int_a^b f$ 等于 $f$ 在某点 $\xi$ 处的取值。

### 形式 2（带权版 / 推广形式）

**条件**：$f$ 连续，$g$ 在 $[a, b]$ 上可积且**保号**（如 $g(x) \geq 0$ 处处成立）。

**结论**：存在 $\xi \in [a, b]$ 使
$$
\int_a^b f(x) g(x) \, dx = f(\xi) \int_a^b g(x) \, dx.
$$

> 形式 1 是 $g \equiv 1$ 的特例。
> 几何上 $g$ 是"权函数"，给出"加权平均"$f(\xi) = \dfrac{\int f g}{\int g}$。

## 几何/直觉理解

> 中值定理告诉你：连续函数的"平均"必由函数在某点的"实际值"实现——
> 这是连续性 + [[ANL-THM-013]] 介值定理的积分版本。
>
> 几何画面：$\int_a^b f$ 等于"曲线下方面积"。设这个面积为 $S$，
> 则 $S = f(\xi)(b-a)$ 表示——存在某矩形高度 $f(\xi)$，使矩形面积恰好等于曲线下方面积。
> 由介值定理，连续函数确实能取到这个高度。
>
> 这与 [[ANL-THM-022]] Lagrange 中值定理（"必有切线斜率 = 割线斜率"）形式平行——
> 都是"必有某点函数值实现某种'平均'"。

## 证明

### 证明（形式 1）

**证明：** 由 $f$ 连续 + 闭区间 + [[ANL-THM-014]] 最值定理，$f$ 取得最大 $M$ 与最小 $m$。
即 $m \leq f(x) \leq M$ 对所有 $x \in [a, b]$。

由 [[ANL-THM-029]] 性质 5（积分均值在 $[m, M]$ 内）：
$$
m(b - a) \leq \int_a^b f \leq M(b - a).
$$

记 $A := \dfrac{1}{b - a} \int_a^b f$，则 $m \leq A \leq M$。

由 [[ANL-THM-013]] 介值定理（$f$ 连续 + $A$ 在最值之间），$\exists \xi \in [a, b]$ 使 $f(\xi) = A$，即
$$
f(\xi) = \frac{1}{b-a} \int_a^b f \iff \int_a^b f = f(\xi)(b - a). \quad\blacksquare
$$

### 证明（形式 2）

**证明：** 不妨 $\int_a^b g > 0$（若 $= 0$，由 $g \geq 0$ 连续可积 + 平凡论证，结论平凡）。

由 $f$ 连续 + 最值 $m \leq f \leq M$，结合 $g \geq 0$：
$$
m \cdot g(x) \leq f(x) g(x) \leq M \cdot g(x).
$$

由 [[ANL-THM-029]] 单调性：
$$
m \int_a^b g \leq \int_a^b fg \leq M \int_a^b g.
$$

记 $A := \dfrac{\int_a^b fg}{\int_a^b g}$，则 $m \leq A \leq M$。
由 [[ANL-THM-013]] 介值定理，$\exists \xi \in [a, b]$ 使 $f(\xi) = A$。$\blacksquare$

## 常见错误

- ✗ 把 $\xi$ 当作具体值（如 $\xi = (a+b)/2$）。
  $\xi$ 是定理保证的**存在**点，具体位置依赖 $f$，**不可指定**。
  反例：$f(x) = x^2$ 在 $[0, 1]$ 上，$\int f = 1/3$，故 $f(\xi) = 1/3$，$\xi = 1/\sqrt{3} \neq 0.5$。
- ✗ 漏掉"$f$ 连续"前提。
  反例：$f(x) = \begin{cases} 0, & x < 1/2 \\ 1, & x \geq 1/2 \end{cases}$ 在 $[0, 1]$ 上可积，
  $\int f = 1/2$，故"应有" $f(\xi) = 1/2$——但 $f$ 取值仅 $0$ 或 $1$，**不取到** $1/2$。
  本质：缺连续性 ⇒ 介值定理失效。
- ✗ 形式 2 漏掉"$g$ 保号"条件。
  反例：$f(x) = 1, g(x) = \sin(2\pi x)$ 在 $[0, 1]$ 上。
  $\int g = 0$，"$f(\xi) = \int fg / \int g$" 分母为零，公式无意义。
- ✗ 把"$\xi \in [a, b]$"误读为"$\xi \in (a, b)$"（开区间）。
  本定理保证 $\xi$ 可以**取到端点**——这与 [[ANL-THM-022]] Lagrange（开区间）不同。
  形式 1 严格来说，对常数函数 $f \equiv c$，任何 $\xi \in [a, b]$ 都是中值点。

## 推论与应用

- **直接应用**：积分平均与函数取值的精确联系
- **进阶（第二积分中值定理）**：$f$ 单调，$g$ 可积，则 $\exists \xi \in [a, b]$ 使
    $\int_a^b fg = f(a) \int_a^\xi g + f(b) \int_\xi^b g$（教材 §9.5，本知识库不展开）
- **微积分基本定理**：[[ANL-THM-031]] 变限积分可微的证明使用本定理（连续版）
- **物理应用**：温度场 $T(x)$ 在区间上的"代表温度"$T(\xi)$ 等于其积分平均

## 链接

- 前置：[[ANL-DEF-012]] 函数连续、[[ANL-DEF-026]] Riemann 可积、[[ANL-THM-013]] 介值定理、[[ANL-THM-014]] 最值定理、[[ANL-THM-027]] 连续可积、[[ANL-THM-029]] 积分基本性质
- 关联：[[ANL-THM-022]] Lagrange 中值定理（导数版本，结构平行）
- 用于：[[ANL-THM-031]] 变限积分函数可微性证明

## 跨专业应用

- **概率论**：$E[g(X)] = \int g(x) p(x) \, dx$，本定理给出"存在某 $x_0$ 使 $g(x_0) = E[g(X)]$"
- **物理**：连续介质中"等效温度"、"质心"等以积分定义的物理量都来自中值思想
