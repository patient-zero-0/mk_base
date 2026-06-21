---
title: "Darboux 上下和"
type: definition
id: ANL-DEF-025
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - Darboux
  - 上和下和
depends:
  - ANL-DEF-022
  - ANL-DEF-005
uses:
  - ANL-AX-001
status: stable
source: "华东师范大学《数学分析》第5版 §9.2"
difficulty: 3
related:
  - ANL-DEF-022
  - ANL-DEF-023
  - ANL-DEF-026
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设 $f : [a, b] \to \mathbb{R}$ **有界**（[[ANL-DEF-005]] 推广至函数），$P = \{x_0, \ldots, x_n\}$ 是 $[a, b]$ 的分割（[[ANL-DEF-022]]）。

记每个子区间 $[x_{i-1}, x_i]$ 上的上下确界（依 [[ANL-AX-001]] 确界原理保证存在）：
$$
M_i := \sup_{x \in [x_{i-1}, x_i]} f(x), \qquad m_i := \inf_{x \in [x_{i-1}, x_i]} f(x).
$$

**Darboux 上和**（U 和）：
$$
U(f, P) := \sum_{i=1}^{n} M_i \cdot \Delta x_i.
$$

**Darboux 下和**（L 和）：
$$
L(f, P) := \sum_{i=1}^{n} m_i \cdot \Delta x_i.
$$

显然 $L(f, P) \leq U(f, P)$。

## 关键性质

### 性质 1：与 Riemann 和的关系

对任意标记 $\boldsymbol{\xi}$：
$$
L(f, P) \leq S(f, P, \boldsymbol{\xi}) \leq U(f, P).
$$

> **直觉**：对每个子区间，$m_i \leq f(\xi_i) \leq M_i$ ⇒ 求和后保持不等式。

### 性质 2：加细使下和 ↗、上和 ↘

若 $P'$ 是 $P$ 的加细（$P' \supseteq P$），则
$$
L(f, P) \leq L(f, P') \leq U(f, P') \leq U(f, P).
$$

> **直觉**（以下和为例）：在子区间 $[x_{i-1}, x_i]$ 中插入一点 $y$，把它分成两段。
> 在两段上分别取下确界，**至少**与原来的 $m_i$ 一样大（更小的范围 ⇒ 更大的 inf 或不变）。
> 故下和不减。上和对偶。

### 性质 3：任意下和 ≤ 任意上和

对任意两分割 $P_1, P_2$（不必互相加细）：
$$
L(f, P_1) \leq U(f, P_2).
$$

**证明梗概**：取公共加细 $P^* = P_1 \cup P_2$，$L(f, P_1) \leq L(f, P^*) \leq U(f, P^*) \leq U(f, P_2)$。

### 性质 4：上下积分

由性质 3，集合 $\{ L(f, P) \}_P$ 有上界（任一 $U(f, P_2)$），故有上确界：
$$
\underline{\int_a^b} f := \sup_P L(f, P) \quad (\text{下积分}).
$$
类似地：
$$
\overline{\int_a^b} f := \inf_P U(f, P) \quad (\text{上积分}).
$$
由性质 3，$\underline{\int_a^b} f \leq \overline{\int_a^b} f$。

## 直觉理解

> 把曲线 $y = f(x)$ 想成一座山的轮廓，分割把 $[a, b]$ 切成若干段。
>
> - **上和** $U(f, P)$ 是用每段中**最高**值为高度的矩形拼成的"**外接矩形面积之和**"——总面积**不小于**曲线下方面积。
> - **下和** $L(f, P)$ 是用每段中**最低**值为高度的矩形拼成的"**内接矩形面积之和**"——总面积**不大于**曲线下方面积。
>
> 加细分割时：每段更小，最高值不会更高（仅可能保持或下降），最低值不会更低（仅可能保持或上升），
> 所以上和"挤"得更紧（递减），下和"撑"得更紧（递增）。
> 当 $\|P\| \to 0$，**理想情形是**上下和"挤压"为同一极限——即曲线下方面积的真值。

```text
   上和              下和
   ┃▒▒┃▒▒▒▒▒┃           ┃▒▒┃▒▒▒┃
   ┃▒▒┃    ┃▒▒          ┃▒▒┃   ┃
   ┃▒▒┃    ┃            ┃   ┃  ┃
   曲线在中间，上和高估、下和低估
```

## 链接

- 前置：[[ANL-DEF-022]] 分割、[[ANL-DEF-005]] 有界、[[ANL-AX-001]] 确界原理
- 关联：[[ANL-DEF-023]] Riemann 和（夹于上下和之间）
- 用于：[[ANL-DEF-026]] Riemann 可积（上下积分相等的判定）
- 可积充要条件：[[ANL-THM-026]] Darboux 准则
