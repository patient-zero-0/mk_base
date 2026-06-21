---
title: "原函数与不定积分"
type: definition
id: ANL-DEF-028
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 原函数
  - 不定积分
depends:
  - ANL-DEF-014
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §8.1"
difficulty: 2
related:
  - ANL-THM-022
  - ANL-THM-031
  - ANL-THM-032
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设 $f$ 在区间 $I$ 上有定义。

**原函数（antiderivative / primitive）**：若函数 $F : I \to \mathbb{R}$ 在 $I$ 上**可导**（[[ANL-DEF-014]]），且
$$
F'(x) = f(x), \quad \forall x \in I,
$$
则称 $F$ 是 $f$ 在 $I$ 上的一个**原函数**。

**不定积分**：$f$ 在 $I$ 上的**全体**原函数构成的集合，记作
$$
\int f(x) \, dx.
$$

## 关键性质：原函数差为常数

> 设 $F, G$ 都是 $f$ 在区间 $I$ 上的原函数，则
> $$
> F(x) - G(x) = C, \quad \forall x \in I
> $$
> 其中 $C \in \mathbb{R}$ 是某常数。

**证明**：$(F - G)'(x) = F'(x) - G'(x) = f(x) - f(x) = 0$ 对所有 $x \in I$。
由 [[ANL-THM-022]] Lagrange 中值定理推论（"导函数恒为零 ⇒ 函数为常数"），$F - G$ 在区间 $I$ 上恒为常数。$\blacksquare$

> **重要**：上述结论要求 $I$ 是**区间**——若 $I$ 是不连通集合（如 $(0, 1) \cup (2, 3)$），结论可能失败：
> $F - G$ 仅在每个连通分量上分别为常数，整体未必同一常数。

## 不定积分的标准记法

由原函数差为常数，若 $F$ 是某一原函数，则全体原函数为 $\{ F + C : C \in \mathbb{R} \}$。习惯写作：
$$
\int f(x) \, dx = F(x) + C.
$$

> **记号细节**：$C$ 称为**积分常数**；写"$+ C$"提醒"原函数不唯一"。

## 与定积分的对比

| 概念 | 形式 | 结果是 |
|---|---|---|
| 不定积分（本条目） | $\int f(x) \, dx = F(x) + C$ | 一个**函数族** |
| 定积分（[[ANL-DEF-026]]） | $\int_a^b f(x) \, dx = I$ | 一个**数** |

两者通过 [[ANL-THM-032]] **Newton-Leibniz 公式**联系：
$$
\int_a^b f(x) \, dx = F(b) - F(a) \quad \text{（其中 } F \text{ 是 } f \text{ 的任一原函数）}.
$$

## 直觉理解

> 原函数 = "求导的反操作"。已知导数 $f$，反推位置函数 $F$，使其变化率符合 $f$。
>
> **物理类比**：
>
> - $f(t) = $ 速度 $v(t)$
> - $F(t) = $ 位置 $s(t)$（满足 $s'(t) = v(t)$）
> - 任两条"位置曲线"同样的速度：差一个起始位置常数 $C$
>
> 这就是为什么"任意原函数"差一常数：起点可以任选。

## 原函数的存在性

> **存在性**：连续函数必有原函数（详见 [[ANL-THM-031]] 变限积分给出构造）。
> 即：$f \in C[a, b] \Rightarrow F(x) := \int_a^x f(t) \, dt$ 是 $f$ 的一个原函数。
>
> **不存在性**：不连续函数可能**没有原函数**——
> 反例：$f(x) = \text{sgn}(x)$（符号函数）在 $\mathbb{R}$ 上无原函数。
> 若 $F' = f$，则 $F$ 在 $0$ 两侧斜率分别为 $\pm 1$，由 [[ANL-DEF-016]] 单侧导数知 $F$ 在 $0$ 不可导，矛盾。
> 更深结果：导函数必满足 Darboux 性质（介值性），故"跳跃间断"的 $f$ 无原函数。

## 常用初等函数原函数表（部分）

| $f(x)$ | $F(x)$（一个原函数） |
|---|---|
| $x^n$（$n \neq -1$） | $\dfrac{x^{n+1}}{n+1}$ |
| $1/x$（$x > 0$） | $\ln x$ |
| $e^x$ | $e^x$ |
| $\sin x$ | $-\cos x$ |
| $\cos x$ | $\sin x$ |
| $\sec^2 x$ | $\tan x$ |
| $\dfrac{1}{1+x^2}$ | $\arctan x$ |
| $\dfrac{1}{\sqrt{1-x^2}}$ | $\arcsin x$ |

## 链接

- 前置：[[ANL-DEF-014]] 导数
- 存在性：[[ANL-THM-031]] 变限积分（连续 ⇒ 有原函数）
- 与定积分的桥梁：[[ANL-THM-032]] Newton-Leibniz 公式
- 计算法则：[[ANL-THM-033]] 换元积分法、[[ANL-THM-034]] 分部积分法
- 关键引理：原函数差为常数依赖 [[ANL-THM-022]] Lagrange 推论
