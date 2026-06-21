---
title: "一致收敛与连续、可积、可导的交换"
type: theorem
id: ANL-THM-045
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 一致收敛
  - 极限交换
depends:
  - ANL-DEF-036
  - ANL-DEF-012
  - ANL-DEF-026
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §13.2"
difficulty: 5
related:
  - ANL-THM-029
  - ANL-THM-032
  - ANL-THM-044
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

> 设函数项级数 $\sum f_n$ 的部分和函数列为 $\{S_n\}$，和函数为 $S$（[[ANL-DEF-035]]），区间 $[a,b]$。下分三个定理陈述（条件各异）。

## 结论

> **(I) 连续性定理（极限与极限交换）。** 若每个 $f_n$ 在 $[a,b]$ 上连续（[[ANL-DEF-012]]），且 $\sum f_n \rightrightarrows S$（一致收敛，[[ANL-DEF-036]]），则 $S$ 在 $[a,b]$ 上连续。即对 $x_0 \in [a,b]$，
> $$
> \lim_{x \to x_0} \sum_{n=1}^{\infty} f_n(x) = \sum_{n=1}^{\infty} \lim_{x \to x_0} f_n(x).
> $$
>
> **(II) 逐项积分定理。** 若每个 $f_n$ 在 $[a,b]$ 上连续（或可积，[[ANL-DEF-026]]），且 $\sum f_n \rightrightarrows S$，则 $S$ 可积且
> $$
> \int_a^b \sum_{n=1}^{\infty} f_n(x)\,dx = \sum_{n=1}^{\infty} \int_a^b f_n(x)\,dx.
> $$
>
> **(III) 逐项求导定理。** 若每个 $f_n$ 在 $[a,b]$ 上有连续导数，$\sum f_n$ 在某点 $x_0 \in [a,b]$ 收敛，且**导数级数** $\sum f_n' \rightrightarrows g$ 一致收敛，则 $\sum f_n \rightrightarrows S$，$S$ 可导且
> $$
> S'(x) = \left(\sum_{n=1}^{\infty} f_n(x)\right)' = \sum_{n=1}^{\infty} f_n'(x).
> $$

## 几何/直觉理解

这是整个一致收敛理论的**目的所在**：什么时候"无穷求和"能与"取极限 / 积分 / 求导"**交换次序**？

逐点收敛**不够**——反例 $f_n(x)=x^n$ 于 $[0,1]$（[[ANL-DEF-036]]）：连续函数的逐点极限不连续，连续性丢失。根源是收敛"步调不齐"：某些点附近 $S_n$ 还远未稳定，极限运算就被它"拽歪"。

**一致收敛**保证整条曲线一起进入 $\varepsilon$-管道，于是：

- **连续 (I)**：管道窄到一定程度后，$S$ 与连续的 $S_n$ 处处只差 $\varepsilon$，连续性被"复制"给 $S$；
- **积分 (II)**：积分是"面积平均"，曲线整体逼近 ⇒ 面积逼近，误差 $\le (b-a)\cdot\sup|S-S_n| \to 0$，最稳健；
- **求导 (III)**：**最苛刻**。导数对局部抖动极敏感，仅 $S_n \rightrightarrows S$ 远不够，必须**导数级数自身一致收敛**——求导不是"继承"而是要"重新挣得"。

> 口诀：**积分要求最弱（函数一致收敛即可），求导要求最强（导数级数也得一致收敛）**。

## 证明

**(I) 连续性。** 设 $x_0 \in [a,b]$，任给 $\varepsilon > 0$。由一致收敛，存在 $N$ 使 $\sup_{x}|S(x) - S_N(x)| < \varepsilon/3$。$S_N$ 是有限个连续函数之和，故在 $x_0$ 连续：存在 $\delta>0$，$|x - x_0|<\delta$ 时 $|S_N(x) - S_N(x_0)| < \varepsilon/3$。于是
$$
|S(x) - S(x_0)| \le |S(x) - S_N(x)| + |S_N(x) - S_N(x_0)| + |S_N(x_0) - S(x_0)| < \frac\varepsilon3 + \frac\varepsilon3 + \frac\varepsilon3 = \varepsilon.
$$
故 $S$ 在 $x_0$ 连续。$\quad\blacksquare$

**(II) 逐项积分。** 由 (I)，$S$ 连续故可积（[[ANL-DEF-026]]）。记 $S_n = \sum_{k=1}^n f_k$，由积分线性性（[[ANL-THM-029]]）$\int_a^b S_n = \sum_{k=1}^n \int_a^b f_k$。又
$$
\left| \int_a^b S - \int_a^b S_n \right| = \left| \int_a^b (S - S_n) \right| \le \int_a^b |S - S_n| \le (b - a)\sup_{x\in[a,b]}|S(x) - S_n(x)| \to 0,
$$
最后一步由一致收敛（[[ANL-DEF-036]] 确界判据）。故 $\sum_{k=1}^n \int_a^b f_k \to \int_a^b S$，即逐项积分成立。$\quad\blacksquare$

**(III) 逐项求导。** 记 $g = \sum f_n'$（一致收敛极限）。每个 $f_n'$ 连续，由 (I) $g$ 连续；由 (II)（逐项积分用于 $\sum f_n'$ 于 $[x_0, x]$）：
$$
\int_{x_0}^{x} g(t)\,dt = \sum_{n=1}^{\infty} \int_{x_0}^{x} f_n'(t)\,dt = \sum_{n=1}^{\infty} \big(f_n(x) - f_n(x_0)\big) = S(x) - S(x_0),
$$
其中第二个等号用 Newton–Leibniz 公式（[[ANL-THM-032]]），末步用 $\sum f_n(x_0)$ 收敛重排。故
$$
S(x) = S(x_0) + \int_{x_0}^{x} g(t)\,dt.
$$
$g$ 连续，由变限积分求导（微积分基本定理）得 $S$ 可导且 $S'(x) = g(x) = \sum f_n'(x)$。（顺带 $S$ 由上式一致收敛。）$\quad\blacksquare$

## 常见错误

- ✗ 仅凭**逐点收敛**就交换极限 / 积分 / 求导。**反例（连续性丢失）**：$x^n$ 于 $[0,1]$ 逐点极限不连续。
- ✗ **积分反例**：$f_n(x) = n x e^{-nx^2}$ 于 $[0,1]$ 逐点 $\to 0$，但 $\int_0^1 f_n = \frac{1}{2}(1 - e^{-n}) \to \frac12 \ne 0 = \int_0^1 0$。非一致收敛时逐项积分失败。
- ✗ **求导反例**：$f_n(x) = \frac{\sin(nx)}{\sqrt n}$，$f_n \rightrightarrows 0$（因 $\frac{1}{\sqrt n}\to 0$）但 $f_n'(x) = \sqrt n\cos(nx)$ 不收敛。函数一致收敛**不能**推出可逐项求导，必须导数级数一致收敛。
- ✗ 把 (III) 的前提记成"$\sum f_n$ 一致收敛"。正确前提是"**$\sum f_n'$ 一致收敛 + $\sum f_n$ 至少一点收敛**"，由此反推 $\sum f_n$ 一致收敛。

## 推论与应用

- 幂级数在收敛区间内可逐项求导 / 积分（[[ANL-THM-044]] 给出一致收敛）
- 与 Weierstrass M-判别法（[[ANL-THM-044]]）配套：先证一致收敛，再交换运算
- 含参积分连续性 / 可微性的离散对应

## 跨专业应用

- **Fourier 级数**：在适当条件下逐项积分 / 求导，求解热传导、波动方程
- **数值分析**：级数解的逐项微分须先验证导数级数一致收敛，否则数值微分发散
