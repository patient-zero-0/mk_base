---
title: "Dirichlet 函数不可积构造与 Riemann 函数可积对比"
type: problem
id: ANL-PROB-015
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 反例构造
  - 可积性
  - Darboux 准则
depends:
  - ANL-THM-026
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §9.1 习题（改编）"
difficulty: 4
tests:
  - ANL-THM-026
  - ANL-DEF-025
  - ANL-DEF-027
related:
  - ANL-DEF-026
  - ANL-THM-027
  - ANL-THM-028
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

记 $\mathbb{Q}$ 为有理数集。定义 **Dirichlet 函数**
$$
D(x) = \begin{cases} 1, & x \in \mathbb{Q}, \\ 0, & x \notin \mathbb{Q}. \end{cases}
$$

1. **不可积证明**：证明 $D$ 在 $[0,1]$ 上**不 Riemann 可积**，并指出它的上、下 Darboux 积分分别等于多少。

2. **有界变差无关**：$D$ 处处有界（$0 \le D \le 1$），却不可积。这与"闭区间连续 ⇒ 可积"（[[ANL-THM-027]]）、"单调 ⇒ 可积"（[[ANL-THM-028]]）有何区别？请用 $D$ 的**不连续点集**说明它为何两条充分条件都不满足。

3. **对比：Riemann（Thomae）函数可积**：定义
    $$
    R(x) = \begin{cases} \dfrac{1}{q}, & x = \dfrac{p}{q} \in (0,1],\ \gcd(p,q)=1,\ q>0, \\[4pt] 0, & x \notin \mathbb{Q}\ \text{或}\ x = 0. \end{cases}
    $$
    证明 $R$ 在 $[0,1]$ 上**可积**且 $\displaystyle\int_0^1 R(x)\,dx = 0$。

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：用 Darboux 准则（[[ANL-THM-026]]）。关键事实：有理数与无理数在 $[0,1]$ 中都**稠密**，故任何小区间内既有有理点又有无理点。算每个子区间上的振幅（[[ANL-DEF-027]]）。
- **第 3 题**：固定 $\varepsilon>0$，只有**有限**个点满足 $R(x)\ge \varepsilon$（即分母 $q\le 1/\varepsilon$ 的既约分数）。把这有限个点用总长可任意小的小区间盖住，其余区间上 $R<\varepsilon$。这正是 Darboux 准则中"控制大振幅子区间总长"的标准套路。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题：Dirichlet 函数不可积

设 $P : 0 = x_0 < x_1 < \cdots < x_n = 1$ 为 $[0,1]$ 的任一分割（[[ANL-DEF-025]]）。

在每个子区间 $[x_{i-1}, x_i]$ 上，由有理数与无理数的**稠密性**：
$$
M_i = \sup_{[x_{i-1},x_i]} D = 1, \qquad m_i = \inf_{[x_{i-1},x_i]} D = 0.
$$

于是上、下 Darboux 和
$$
U(P, D) = \sum_{i=1}^n M_i \,\Delta x_i = \sum_{i=1}^n 1\cdot \Delta x_i = 1, \qquad
L(P, D) = \sum_{i=1}^n m_i \,\Delta x_i = 0,
$$
对**一切**分割 $P$ 成立。因此上、下 Darboux 积分
$$
\overline{\int_0^1} D = \inf_P U(P,D) = 1, \qquad \underline{\int_0^1} D = \sup_P L(P,D) = 0.
$$

由于
$$
U(P,D) - L(P,D) = 1 \not\to 0 \quad(\text{对一切 }P),
$$
Darboux 准则（[[ANL-THM-026]]）的可积条件 $\inf_P\big(U-L\big)=0$ 不成立，故 $D$ 在 $[0,1]$ 上**不可积**。$\quad\blacksquare$

> 等价地：每个子区间上振幅 $\omega_i = M_i - m_i = 1$，故 $\sum \omega_i \Delta x_i = 1$ 不能任意小。

### 第 2 题：与两条充分条件的关系

$D$ 在 $[0,1]$ 上**处处不连续**（[[ANL-DEF-026]] 要求的可积性允许少量不连续点，但 $D$ 的不连续点集是整个 $[0,1]$）：

- **非连续**：任取 $x_0$，存在有理点列与无理点列同时趋于 $x_0$，其函数值分别为 $1$ 与 $0$，极限不存在，故 $D$ 在 $x_0$ 不连续。所以"闭区间连续 ⇒ 可积"（[[ANL-THM-027]]）的前提**完全不满足**。
- **非单调**：$D$ 在任意小区间上取值在 $\{0,1\}$ 间无穷次跳变，绝非单调，故[[ANL-THM-028]]也不适用。

> **本质**：Riemann 可积 $\iff$ 不连续点集为 **Lebesgue 零测集**（Lebesgue 判据，本课不证）。$D$ 的不连续点集测度为 $1$，故不可积；而下一题的 $R$ 仅在有理点不连续（零测），故可积。

### 第 3 题：Riemann（Thomae）函数可积

**先证可积**（Darboux 准则 [[ANL-THM-026]]）：给定 $\varepsilon > 0$。

**关键有限性**：满足 $R(x) \ge \varepsilon/2$ 的点 $x = p/q$ 须有 $q \le 2/\varepsilon$。这样的既约分数在 $(0,1]$ 中只有**有限**个，记为 $a_1, \ldots, a_N$（$N$ 依赖 $\varepsilon$）。

**构造分割**：把每个 $a_k$ 用一个长度 $< \dfrac{\varepsilon}{2N}$ 的小区间盖住，取分割 $P$ 使这 $N$ 个"坏点"落在总长 $< \varepsilon/2$ 的若干子区间内。将子区间分两类：

- **类 A（含某个 $a_k$）**：振幅 $\omega_i \le 1$（因 $0\le R\le 1$），但其总长 $\sum_{A}\Delta x_i < \varepsilon/2$，故
    $$
    \sum_{i\in A} \omega_i \Delta x_i \le 1\cdot \sum_{i\in A}\Delta x_i < \frac{\varepsilon}{2}.
    $$
- **类 B（不含任何 $a_k$）**：此时区间上处处 $R(x) < \varepsilon/2$，故 $\omega_i \le \varepsilon/2$，于是
    $$
    \sum_{i\in B} \omega_i \Delta x_i \le \frac{\varepsilon}{2}\sum_{i\in B}\Delta x_i \le \frac{\varepsilon}{2}\cdot 1 = \frac{\varepsilon}{2}.
    $$

合计 $U(P,R) - L(P,R) = \sum_i \omega_i \Delta x_i < \varepsilon$。由 $\varepsilon$ 任意，$R$ 在 $[0,1]$ 上**可积**。

**再证积分值为 $0$**：在每个子区间上 $m_i = \inf R = 0$（无理点稠密，$R$ 在无理点为 $0$），故对一切分割 $L(P,R) = 0$，从而下积分 $=0$。由可积性，
$$
\int_0^1 R(x)\,dx = \underline{\int_0^1} R = 0. \quad\blacksquare
$$

</details>

## 考察点

- [[ANL-THM-026]] Darboux 准则的两种等价表述（$U-L\to 0$ 与振幅和 $\sum\omega_i\Delta x_i\to 0$）
- [[ANL-DEF-025]] 上下 Darboux 和的计算
- [[ANL-DEF-027]] 振幅作为不可积性的定量刻画
- 稠密性在确定 $\sup/\inf$ 中的作用
- "控制大振幅子区间总长"——可积性证明的通用技巧

## 备注

**Dirichlet vs Riemann 函数的教学价值**：

| | Dirichlet $D$ | Riemann $R$ |
|---|---|---|
| 连续点 | 无 | 全体无理点 |
| 不连续点集测度 | $1$ | $0$ |
| Riemann 可积 | 否 | 是，积分 $=0$ |
| Lebesgue 可积 | 是（积分 $=0$，因 $\mathbb{Q}$ 零测） | 是 |

这对反例说明：**Riemann 积分对"病态"函数的鉴别力，恰好由不连续点集的测度决定**——这是通向 Lebesgue 积分理论的最自然动机。$D$ 的不可积性也是后续 [[ANL-DEF-026]] 中"可积 ⇒ 几乎处处连续"直观的反面教材。
