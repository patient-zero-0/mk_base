---
title: "Cauchy–Hadamard 公式与幂级数逐项求导、积分"
type: theorem
id: ANL-THM-046
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 幂级数
  - 收敛半径
  - 逐项运算
depends:
  - ANL-DEF-038
  - ANL-THM-040
  - ANL-THM-045
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §14.1–§14.2"
difficulty: 4
related:
  - ANL-THM-044
  - ANL-DEF-039
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

> 幂级数 $\displaystyle\sum_{n=0}^{\infty} c_n (x - x_0)^n$（[[ANL-DEF-037]]），和函数记为 $S(x)$。

## 结论

> **(I) Cauchy–Hadamard 公式。** 其收敛半径（[[ANL-DEF-038]]）为
> $$
> R = \frac{1}{\varlimsup_{n\to\infty} \sqrt[n]{|c_n|}}
> $$
> （约定 $\frac10 = +\infty$，$\frac{1}{+\infty} = 0$）。当极限 $\lim\left|\dfrac{c_n}{c_{n+1}}\right|$ 存在时，它也等于 $R$。
>
> **(II) 内闭一致收敛。** 对任意 $0 < r < R$，幂级数在 $[x_0 - r,\ x_0 + r]$ 上**一致收敛**。
>
> **(III) 逐项求导与积分。** 在收敛区间 $(x_0 - R,\ x_0 + R)$ 内，$S$ **无穷次可导**，且可逐项求导、逐项积分；所得级数收敛半径**仍为 $R$**：
> $$
> S'(x) = \sum_{n=1}^{\infty} n\,c_n (x - x_0)^{n-1}, \qquad
> \int_{x_0}^{x} S(t)\,dt = \sum_{n=0}^{\infty} \frac{c_n}{n+1}(x - x_0)^{n+1}.
> $$

## 几何/直觉理解

(I) 把根值判别法（[[ANL-THM-040]]）作用到 $\sum|c_n||x-x_0|^n$ 上，根值 $\sqrt[n]{|c_n|\,|x-x_0|^n} = |x-x_0|\sqrt[n]{|c_n|} \to |x-x_0|\cdot\frac1R$。它 $<1 \iff |x-x_0|<R$——收敛半径就是"根值判别法的临界处"。

(II)(III) 的精神是：**幂级数在收敛区间内部表现得和多项式一模一样**。虽然在整个开区间 $(x_0-R, x_0+R)$ 上未必一致收敛（端点附近可能失控），但在任何**内闭区间**上一致收敛（由 Weierstrass M-判别 [[ANL-THM-044]]，以 $r^n$ 为控制），于是一致收敛的交换定理（[[ANL-THM-045]]）允许逐项求导 / 积分。求导 / 积分不改变收敛半径，是因为系数乘 / 除以 $n$ 这类多项式因子开 $n$ 次方后极限为 $1$（$\sqrt[n]{n}\to1$）。

> 一句话：**幂级数是"无穷次多项式"，在收敛区间内可像多项式那样随意微积分，且半径不变**——这是它成为函数表示利器（[[ANL-DEF-039]]）的根本。

## 证明

**(I) Cauchy–Hadamard。** 设 $L = \varlimsup \sqrt[n]{|c_n|}$，$R = 1/L$。对固定 $x$，考察绝对值级数 $\sum |c_n|\,|x-x_0|^n$，其根值
$$
\varlimsup_{n\to\infty} \sqrt[n]{|c_n|\,|x-x_0|^n} = |x-x_0|\cdot\varlimsup\sqrt[n]{|c_n|} = \frac{|x-x_0|}{R}.
$$
由根值判别法（[[ANL-THM-040]]）：$\frac{|x-x_0|}{R}<1$（即 $|x-x_0|<R$）时绝对收敛，$>1$ 时通项不趋零故发散。这恰是收敛半径的定义，故收敛半径 $= R$。$\quad\blacksquare$

**(II) 内闭一致收敛。** 取 $0<r<R$。对 $x\in[x_0-r, x_0+r]$，$|c_n(x-x_0)^n|\le |c_n|\,r^n =: M_n$。由 (I)，$\sum |c_n| r^n$ 收敛（因 $r<R$）。由 Weierstrass M-判别法（[[ANL-THM-044]]），幂级数在 $[x_0-r, x_0+r]$ 上一致收敛。$\quad\blacksquare$

**(III) 逐项运算。** 先证求导级数 $\sum_{n\ge1} n c_n (x-x_0)^{n-1}$ 半径仍为 $R$：由 $\sqrt[n]{n}\to1$，
$$
\varlimsup\sqrt[n]{n|c_n|} = \lim\sqrt[n]{n}\cdot\varlimsup\sqrt[n]{|c_n|} = 1\cdot\frac1R = \frac1R,
$$
故求导级数收敛半径为 $R$。任取 $x\in(x_0-R, x_0+R)$，选 $r$ 使 $|x-x_0|<r<R$；在 $[x_0-r, x_0+r]$ 上原级数与求导级数均一致收敛（由 (II)）。由一致收敛的逐项求导定理（[[ANL-THM-045]] (III)），$S$ 在该区间可导且 $S'(x)=\sum n c_n(x-x_0)^{n-1}$。

逐项积分同理：积分级数 $\sum \frac{c_n}{n+1}(x-x_0)^{n+1}$ 半径为 $R$，在内闭区间上对一致收敛的原级数用逐项积分定理（[[ANL-THM-045]] (II)）即得。

反复对 $S'$ 施加上述结论，知 $S$ 在 $(x_0-R, x_0+R)$ 内**无穷次可导**。$\quad\blacksquare$

## 常见错误

- ✗ 把收敛半径公式写成 $R = \lim\sqrt[n]{|c_n|}$（漏取倒数、漏用上极限）。正确是 $R = 1/\varlimsup\sqrt[n]{|c_n|}$。
- ✗ 用比值式 $R = \lim|c_n/c_{n+1}|$ 时不验证极限存在。系数有"空缺"（如只含偶次幂）时比值振荡，须回到根值（上极限）公式。
- ✗ 误以为幂级数在**整个**开区间 $(x_0-R, x_0+R)$ 上一致收敛。一般只**内闭**一致收敛；端点附近可能不一致。
- ✗ 逐项求导后忘记**端点收敛性可能改变**。半径不变，但端点敛散需重新判定（如 $\sum x^n/n$ 在 $x=-1$ 收敛，求导后 $\sum x^{n-1}$ 在 $x=-1$ 发散）。

## 推论与应用

- 幂级数的和函数在收敛区间内为 $C^\infty$ 解析函数，且 $c_n = \dfrac{S^{(n)}(x_0)}{n!}$（与 Taylor 级数 [[ANL-DEF-039]] 系数一致，**展开唯一**）
- 逐项积分 / 求导是求级数和的标准手法（见例题与 [[ANL-THM-044]] 配套）
- Abel 第二定理：若幂级数在端点收敛，则和函数在该端点单侧连续

## 跨专业应用

- **数值分析**：用幂级数（Taylor 截断）计算 $e^x$、$\ln$、三角函数，逐项求导得导数近似
- **微分方程**：幂级数法（待定系数）求解 ODE，逐项求导代入方程定系数
