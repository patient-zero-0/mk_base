---
title: "Weierstrass 判别法（M-判别法）"
type: theorem
id: ANL-THM-044
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 一致收敛
  - Weierstrass
depends:
  - ANL-DEF-036
  - ANL-THM-037
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §13.1"
difficulty: 3
related:
  - ANL-THM-038
  - ANL-THM-045
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

> 设函数项级数 $\sum_{n=1}^{\infty} f_n(x)$ 定义在 $E \subseteq \mathbb{R}$ 上。若存在**正项数列** $\{M_n\}$ 使得
>
> 1. **逐项控制**：$|f_n(x)| \le M_n$ 对一切 $x \in E$ 与一切 $n$ 成立；
> 2. **控制级数收敛**：数项级数 $\sum_{n=1}^{\infty} M_n$ 收敛。

## 结论

> 则 $\sum f_n(x)$ 在 $E$ 上**一致收敛**（且**绝对收敛**）（[[ANL-DEF-036]]）。

## 几何/直觉理解

Weierstrass 判别法把"函数项级数一致收敛"这个带 $x$ 维度的难题，**降维**成一个普通数项级数 $\sum M_n$ 的收敛问题：只要每个通项函数的"最大可能高度" $M_n$ 加起来有限，那么无论 $x$ 取何值，尾部 $\sum_{k>n} f_k(x)$ 都被同一个可任意小的数 $\sum_{k>n} M_k$ 压住——这正是"$N$ 与 $x$ 无关"的一致性来源。

形象地说：$\sum M_n$ 是一道"**统一的天花板**"，把所有 $x$ 处的级数尾巴一起按在 $\varepsilon$-管道内。它是判定一致收敛**最常用、最省力**的工具，代价是要求绝对收敛——故对条件收敛的函数项级数（如 $\sum \frac{(-1)^n}{n}\,$ 型）无能为力，那时需改用 Abel/Dirichlet 一致收敛判别（[[ANL-THM-043]] 的函数版）。

## 证明

**证明：** 关键是**一致收敛的 Cauchy 准则**——它是数项级数 Cauchy 准则（[[ANL-THM-037]]）的函数版：$\sum f_n$ 在 $E$ 上一致收敛 $\iff$
$$
\forall \varepsilon > 0,\ \exists N,\ \forall m > n > N,\ \forall x \in E:\ \left|\sum_{k=n+1}^{m} f_k(x)\right| < \varepsilon.
$$

现验证此准则。由 $\sum M_n$ 收敛，对其用数项级数 Cauchy 准则（[[ANL-THM-037]]）：任给 $\varepsilon > 0$，存在 $N$，使 $\forall m > n > N$，
$$
\sum_{k=n+1}^{m} M_k < \varepsilon.
$$

于是对**一切** $x \in E$，由逐项控制 $|f_k(x)| \le M_k$ 与三角不等式：
$$
\left|\sum_{k=n+1}^{m} f_k(x)\right| \le \sum_{k=n+1}^{m} |f_k(x)| \le \sum_{k=n+1}^{m} M_k < \varepsilon.
$$

该 $N$ 与 $x$ **无关**，故一致收敛的 Cauchy 准则成立，$\sum f_n$ 在 $E$ 上一致收敛。

中间一步 $\sum |f_k(x)| \le \sum M_k$ 同时表明逐点**绝对收敛**。$\qquad\blacksquare$

## 常见错误

- ✗ 找的 $M_n$ 不是 $|f_n(x)|$ 在 $E$ 上的**上界**，而只在部分点成立。必须 $\sup_{x\in E}|f_n(x)| \le M_n$。
- ✗ $M_n$ 取得过松导致 $\sum M_n$ 发散，便断言"不一致收敛"。**M-判别法只是充分条件**：$\sum M_n$ 发散不能推出 $\sum f_n$ 不一致收敛（也许换更紧的 $M_n$ 就行，或该级数虽一致收敛但非绝对收敛）。
- ✗ 用于**条件收敛**型函数项级数。M-判别法蕴含绝对收敛，对靠正负相消才一致收敛的级数失效，应改用 Abel/Dirichlet 一致判别。
- ✗ 误以为一致收敛区间可任意扩大。$M_n = \sup_E |f_n|$ 依赖 $E$：如 $\sum \frac{x^n}{n^2}$ 在 $[-1,1]$ 上 $M_n = 1/n^2$ 可用，但在 $(-1,1)$ 外失效。

## 推论与应用

- 一致收敛 ⇒ 可逐项取极限 / 积分 / （在条件下）求导（[[ANL-THM-045]]）
- 与正项级数判别法（[[ANL-THM-038]]）配套：先估 $M_n = \sup|f_n|$，再用比较 / 比值 / 积分判别 $\sum M_n$
- 是幂级数在收敛区间内闭一致收敛的标准证法

## 跨专业应用

- **Fourier 分析**：$\sum \frac{\cos nx}{n^2}$ 等三角级数由 $M_n = 1/n^2$ 立得一致收敛，从而和函数连续
- **概率论**：特征函数 / 母函数级数在紧集上一致收敛，支持逐项求导算矩
