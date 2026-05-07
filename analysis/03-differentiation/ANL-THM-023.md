---
title: "Cauchy 中值定理"
type: theorem
id: ANL-THM-023
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - 中值定理
  - 参数化
depends:
  - ANL-DEF-014
  - ANL-DEF-012
  - ANL-THM-021
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §6.1"
difficulty: 3
related:
  - ANL-THM-022
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $f, g : [a, b] \to \mathbb{R}$ 同时满足：

1. $f, g$ 在闭区间 $[a, b]$ 上连续（[[ANL-DEF-012]]）；
2. $f, g$ 在开区间 $(a, b)$ 内可导（[[ANL-DEF-014]]）；
3. $g'(x) \neq 0$ 对所有 $x \in (a, b)$ 成立。

## 结论

> 存在 $\xi \in (a, b)$ 使得
> $$
> \frac{f(b) - f(a)}{g(b) - g(a)} = \frac{f'(\xi)}{g'(\xi)}.
> $$
>
> **注**：条件 3 + Rolle 定理保证 $g(a) \neq g(b)$（否则会有 $g'$ 在 $(a,b)$ 内有零点），故分母非零。

## 几何/直觉理解

> 把 $(g(t), f(t))$ 看作平面上参数曲线（参数 $t \in [a, b]$）。
> 起点 $(g(a), f(a))$，终点 $(g(b), f(b))$，**割线**斜率为
> $$
> \frac{f(b) - f(a)}{g(b) - g(a)}.
> $$
> 曲线在参数 $t$ 处的**切线**方向为 $(g'(t), f'(t))$，斜率为 $\dfrac{f'(t)}{g'(t)}$。
>
> Cauchy 定理断言：参数曲线上至少有一处切线**平行**于起终点连线（割线）。
> 这是 Lagrange 定理（[[ANL-THM-022]]）的"参数化"版本——
> Lagrange 是 $g(x) = x$ 的特例（此时 $g'(x) \equiv 1$）。

## 证明

**证明：** 思路：构造辅助函数后用 Rolle。

设
$$
\varphi(x) := f(x) - \frac{f(b) - f(a)}{g(b) - g(a)} \cdot \big[ g(x) - g(a) \big].
$$

由条件 1, 2，$\varphi$ 在 $[a, b]$ 连续、在 $(a, b)$ 可导。计算端点值：
$$
\varphi(a) = f(a) - 0 = f(a),
$$
$$
\varphi(b) = f(b) - \frac{f(b) - f(a)}{g(b) - g(a)} \cdot \big[ g(b) - g(a) \big] = f(b) - (f(b) - f(a)) = f(a).
$$

故 $\varphi(a) = \varphi(b) = f(a)$。由 [[ANL-THM-021]] Rolle 定理，$\exists \xi \in (a, b)$ 使
$$
\varphi'(\xi) = 0 \iff f'(\xi) - \frac{f(b) - f(a)}{g(b) - g(a)} \cdot g'(\xi) = 0.
$$

由条件 3，$g'(\xi) \neq 0$，两边除以 $g'(\xi)$：
$$
\frac{f'(\xi)}{g'(\xi)} = \frac{f(b) - f(a)}{g(b) - g(a)}. \quad\blacksquare
$$

## 常见错误

- ✗ 漏掉条件 3（$g' \neq 0$）。
  反例：$f(x) = x^3$，$g(x) = x^2$ 在 $[-1, 1]$ 上。
  $g'(0) = 0$，$g(b) - g(a) = 1 - 1 = 0$，定理结论分母为零，公式无意义。
- ✗ 误用以下"伪证法"：分别对 $f, g$ 用 Lagrange，得 $f(b) - f(a) = f'(\xi_1)(b-a)$ 与 $g(b) - g(a) = g'(\xi_2)(b-a)$，相除得 $\dfrac{f'(\xi_1)}{g'(\xi_2)}$。
  错误：$\xi_1, \xi_2$ **不一定相等**，无法合并为单一 $\xi$。
  Cauchy 定理的精髓是断言**同一个** $\xi$ 同时作用于分子分母——这是它强于"两次 Lagrange"的根本理由。
- ✗ 把 Cauchy 中值定理的 $\xi$ 视作"$f, g$ 各自 Lagrange 的 $\xi$ 的某种平均"。
  没有这样的平均关系；$\xi$ 由整体的辅助函数 $\varphi$ 决定。

## 推论与应用

- **Lagrange 中值定理**：取 $g(x) = x$ 即得 [[ANL-THM-022]]
- **L'Hospital 法则**：[[ANL-THM-024]] 的核心证明工具——把 $\dfrac{f}{g}$ 的极限化为 $\dfrac{f'(\xi)}{g'(\xi)}$
- **Taylor 余项**：Lagrange 余项形式（[[ANL-THM-025]]）的证明用 Cauchy 中值定理对辅助函数迭代

## 跨专业应用

- **数值分析**：L'Hospital 法则用于处理 $0/0$ 与 $\infty/\infty$ 型极限——本定理是基础
