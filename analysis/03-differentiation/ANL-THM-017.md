---
title: "求导四则运算"
type: theorem
id: ANL-THM-017
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - 四则运算
  - 计算法则
depends:
  - ANL-DEF-014
  - ANL-THM-016
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §4.2"
difficulty: 3
related:
  - ANL-THM-009
  - ANL-THM-018
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $f, g : I \to \mathbb{R}$ 在 $x_0 \in I$ 处可导（[[ANL-DEF-014]]）。

## 结论

下列函数在 $x_0$ 处均可导，并满足相应公式：

> **和差**：
> $$ (f \pm g)'(x_0) = f'(x_0) \pm g'(x_0). $$
>
> **数乘**：对常数 $c \in \mathbb{R}$，
> $$ (c f)'(x_0) = c \cdot f'(x_0). $$
>
> **乘积（Leibniz 法则）**：
> $$ (fg)'(x_0) = f'(x_0) g(x_0) + f(x_0) g'(x_0). $$
>
> **商**：若进一步 $g(x_0) \neq 0$，
> $$ \left( \frac{f}{g} \right)'(x_0) = \frac{f'(x_0) g(x_0) - f(x_0) g'(x_0)}{g(x_0)^2}. $$

## 几何/直觉理解

> **乘积法则**最容易直觉化：把 $fg$ 看作一个矩形面积，边长分别是 $f, g$。
> 当 $x_0$ 微移 $\Delta x$，矩形面积增量近似为
> $$
> \Delta(fg) \approx \underbrace{f \cdot \Delta g}_{\text{右边长不变, 上沿增}} + \underbrace{g \cdot \Delta f}_{\text{下沿不变, 右边长增}} + \underbrace{\Delta f \cdot \Delta g}_{\text{角落小矩形, } o(\Delta x)}.
> $$
> 除以 $\Delta x$ 取极限即得 $(fg)' = f' g + f g'$。
>
> **商法则**记忆口诀：「**分母平方为分母**，**分子分母乘**减**分母分子乘**」。
> 推导可由乘积法则 $(f/g) \cdot g = f$ 两边求导得到。

## 证明

> 仅证乘积法则；和差/数乘平凡，商可由乘积法则 + 链式法则推出。

**证明（乘积法则）：** 考察差商
$$
\frac{(fg)(x_0 + h) - (fg)(x_0)}{h} = \frac{f(x_0+h) g(x_0+h) - f(x_0) g(x_0)}{h}.
$$

加减项 $f(x_0) g(x_0+h)$：
$$
= \frac{f(x_0+h) g(x_0+h) - f(x_0) g(x_0+h) + f(x_0) g(x_0+h) - f(x_0) g(x_0)}{h}
$$
$$
= \underbrace{\frac{f(x_0+h) - f(x_0)}{h}}_{\to f'(x_0)} \cdot g(x_0+h) + f(x_0) \cdot \underbrace{\frac{g(x_0+h) - g(x_0)}{h}}_{\to g'(x_0)}.
$$

由 [[ANL-THM-016]]，$g$ 在 $x_0$ 可导 ⇒ $g$ 连续 ⇒ $g(x_0+h) \to g(x_0)$。
由 [[ANL-THM-009]] 函数极限四则运算：
$$
\lim_{h \to 0} \frac{(fg)(x_0+h) - (fg)(x_0)}{h} = f'(x_0) \cdot g(x_0) + f(x_0) \cdot g'(x_0). \quad\blacksquare
$$

## 常见错误

- ✗ 把乘积法则误写成 $(fg)' = f' g'$（"分别求导"）。
  反例：$f(x) = g(x) = x$，则 $(x \cdot x)' = (x^2)' = 2x \neq 1 \cdot 1 = f' g'$。
- ✗ 商法则分子顺序错写为 $f g' - f' g$。
  正确顺序是 $f' g - f g'$（"分子先求导在前"）。
  记法：$(f/g)' = f'/g$ 的修正项是减去 $f g'/g^2$。
- ✗ 应用商法则时遗漏 $g(x_0) \neq 0$ 条件。
  若 $g(x_0) = 0$，$f/g$ 在 $x_0$ 处可能根本无定义，公式失效。
- ✗ 对乘积法则证明中"加减 $f(x_0)g(x_0+h)$"的技巧不熟。
  这是分析学常见的"加减项 + 重组"手法（与 [[ANL-THM-009]] 证明并行），
  目的是把双增量 $\Delta f \cdot \Delta g$ 拆为可控项。

## 推论与应用

- 推论：多项式 $p(x) = \sum a_k x^k$ 处处可导，$p'(x) = \sum k a_k x^{k-1}$
- 推论：有理函数 $p/q$ 在 $q \neq 0$ 处可导
- 推论：归纳可得 $\left( \prod_{i=1}^n f_i \right)' = \sum_{i=1}^n f_1 \cdots f_i' \cdots f_n$
- 与 [[ANL-THM-018]] 链式法则合用，可计算几乎一切初等函数的导数
- 应用：[[ANL-EX-008]]
