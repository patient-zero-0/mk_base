---
title: "级数收敛的必要条件（通项趋于零）"
type: theorem
id: ANL-THM-036
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 收敛
  - 必要条件
depends:
  - ANL-DEF-033
  - ANL-THM-004
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §12.1"
difficulty: 2
related:
  - ANL-THM-037
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

> 级数 $\sum_{n=1}^{\infty} a_n$ **收敛**（[[ANL-DEF-033]]）。

## 结论

> 则其通项趋于零：
> $$
> \lim_{n \to \infty} a_n = 0.
> $$

等价地（逆否命题，**实用形式**）：若 $a_n \not\to 0$（或极限不存在），则 $\sum a_n$ **发散**。

## 几何/直觉理解

级数收敛意味着部分和 $S_n$ 稳定到总额 $S$。当累计金额已经几乎不变时，"每期新付的钱" $a_n = S_n - S_{n-1}$ 必然越来越小、趋于零——否则总额还在持续变动，不可能稳定。

这是判定**发散**的第一道、也是最廉价的"筛子"：先看通项是否趋零，不趋零直接判发散，无须任何复杂判别法。

> **务必牢记其单向性**：通项趋零是收敛的**必要条件，绝非充分条件**。通过此筛只是"没被立刻否决"，远不能断言收敛。

## 证明

**证明：** 设 $\sum a_n$ 收敛，部分和数列 $\{S_n\}$ 满足 $\lim_{n\to\infty} S_n = S \in \mathbb{R}$（[[ANL-DEF-033]]）。

则子列 $\{S_{n-1}\}$ 同样收敛于 $S$。对 $n \ge 2$，由 $a_n = S_n - S_{n-1}$，用数列极限的四则运算（[[ANL-THM-004]]）：
$$
\lim_{n \to \infty} a_n = \lim_{n \to \infty} (S_n - S_{n-1}) = S - S = 0. \qquad\blacksquare
$$

## 常见错误

- ✗ 把结论当作充分条件："$a_n \to 0 \Rightarrow \sum a_n$ 收敛"。
    **反例（调和级数）**：$a_n = 1/n \to 0$，但 $\sum 1/n$ 发散。
    证明发散：按 $2^k$ 分组，
    $$
    \underbrace{\frac12}_{\ge 1/2} + \underbrace{\frac13+\frac14}_{> 2\cdot\frac14=\frac12} + \underbrace{\frac15+\cdots+\frac18}_{>4\cdot\frac18=\frac12} + \cdots,
    $$
    每组之和 $> 1/2$，故 $S_{2^k} > 1 + k/2 \to +\infty$。
- ✗ 误以为"$a_n \to 0$ 越快越好但不必要"。趋零是**硬性必要条件**：$\sum (-1)^n$ 通项不趋零，立即发散，无须深究。
- ✗ 用本定理去"证明收敛"。它**只能否决**（判发散），永远不能肯定收敛。

## 推论与应用

- 发散判定的"零步筛选"：通项不趋零 ⇒ 发散
- 与 Cauchy 准则（[[ANL-THM-037]]）配合：必要条件是 Cauchy 准则取 $m = n+1$ 的特例

## 跨专业应用

- **数值分析**：迭代/级数算法中，通项不趋零即可提前判定不收敛，省去无谓计算
- **信号处理**：能量有限信号要求其分量平方和收敛，故分量幅度必趋零
