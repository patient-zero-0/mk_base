---
title: "函数项级数一致收敛判定"
type: problem
id: ANL-PROB-022
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 一致收敛
  - 函数项级数
depends:
  - ANL-DEF-036
  - ANL-THM-044
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §13 综合习题"
difficulty: 4
tests:
  - ANL-DEF-036
  - ANL-THM-044
related:
  - ANL-THM-045
  - ANL-THM-043
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

判定下列函数项级数 / 函数列的一致收敛性（[[ANL-DEF-036]]）。

1. $\displaystyle\sum_{n=1}^{\infty} \frac{\sin nx}{n^2}$ 于 $\mathbb{R}$。
2. $\displaystyle\sum_{n=1}^{\infty} x^n$ 于 $(a)\ [0, q]\ (0<q<1)$ 与 $(b)\ [0,1)$。
3. 函数列 $f_n(x) = \dfrac{nx}{1 + n^2 x^2}$ 于 $(a)\ [\delta, 1]\ (\delta>0)$ 与 $(b)\ [0,1]$。
4. $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^n}{n + x^2}$ 于 $\mathbb{R}$。

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：Weierstrass M-判别法（[[ANL-THM-044]]），找与 $x$ 无关的 $M_n$。
- **第 2 题**：(a) M-判别法；(b) 用确界判据 $\sup_{x}|S(x)-S_n(x)|$ 是否 $\to 0$，注意 $x\to1^-$。
- **第 3 题**：求 $\sup_x|f_n(x)|$。提示 $f_n$ 在 $x=1/n$ 处取最大值 $1/2$。
- **第 4 题**：非绝对收敛，M-判别法失效；用 Abel/Dirichlet 一致收敛判别（[[ANL-THM-043]] 的函数版）。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题：M-判别法

对一切 $x\in\mathbb{R}$，$\left|\dfrac{\sin nx}{n^2}\right| \le \dfrac{1}{n^2} =: M_n$，而 $\sum 1/n^2$ 收敛（$p=2>1$）。由 Weierstrass M-判别法（[[ANL-THM-044]]），级数在 $\mathbb{R}$ 上**一致收敛**。$\quad\blacksquare$

> 推论：和函数在 $\mathbb{R}$ 上连续（[[ANL-THM-045]]）。

### 第 2 题：几何级数

**(a) 于 $[0,q]$（$0<q<1$）**：$|x^n| \le q^n =: M_n$，$\sum q^n$ 收敛。由 M-判别法**一致收敛**。

**(b) 于 $[0,1)$**：逐点和 $S(x) = \dfrac{1}{1-x}$，部分和 $S_n(x) = \dfrac{1-x^n}{1-x}$。余项
$$
\sup_{x\in[0,1)} |S(x) - S_n(x)| = \sup_{x\in[0,1)} \frac{x^n}{1-x} = +\infty
$$
（当 $x\to 1^-$ 时该量无界）。由确界判据（[[ANL-DEF-036]]），**不一致收敛**。$\quad\blacksquare$

> 对比 (a)(b)：同一级数在闭子区间 $[0,q]$ 一致收敛、在 $[0,1)$ 不一致——一致收敛**强依赖区间**。

### 第 3 题：函数列确界

求 $\sup_x |f_n(x)|$。令 $f_n'(x)=0$：$f_n(x)=\dfrac{nx}{1+n^2x^2}$ 在 $x=\dfrac1n$ 取最大值 $f_n(1/n)=\dfrac{n\cdot\frac1n}{1+1}=\dfrac12$。逐点极限 $f_n(x)\to 0$（对每个固定 $x$）。

**(a) 于 $[\delta,1]$（$\delta>0$）**：当 $n>1/\delta$ 时最大值点 $1/n<\delta$ 落在区间外，区间上 $f_n$ 递减，故
$$
\sup_{[\delta,1]}|f_n| = f_n(\delta) = \frac{n\delta}{1+n^2\delta^2} \to 0.
$$
由确界判据**一致收敛**于 $0$。

**(b) 于 $[0,1]$**：最大值点 $1/n\in[0,1]$，
$$
\sup_{[0,1]}|f_n - 0| = f_n(1/n) = \frac12 \not\to 0,
$$
故**不一致收敛**。$\quad\blacksquare$

### 第 4 题：Dirichlet 一致收敛判别

该级数对每个 $x$ 是交错级数，但绝对值级数 $\sum \frac{1}{n+x^2}$ 发散（类调和），**M-判别法失效**。

用 Dirichlet 判别法（函数版，[[ANL-THM-043]]）：写 $a_n = (-1)^n$，$b_n(x)=\dfrac{1}{n+x^2}$。

- $a_n=(-1)^n$ 的部分和 $\left|\sum_{k=1}^n (-1)^k\right| \le 1$，**对一切 $x$ 一致有界**；
- $b_n(x)=\dfrac{1}{n+x^2}$ 对每个 $x$ 关于 $n$ 单调递减，且
    $$
    \sup_{x\in\mathbb{R}} b_n(x) = \frac1n \to 0 \quad(\text{即 } b_n \rightrightarrows 0 \text{ 一致趋零}).
    $$

满足 Dirichlet 一致判别条件，故级数在 $\mathbb{R}$ 上**一致收敛**。$\quad\blacksquare$

> 也可用交错级数余项估计：$\left|\sum_{k>n}\frac{(-1)^k}{k+x^2}\right| \le b_{n+1}(x) = \frac{1}{n+1+x^2} \le \frac{1}{n+1} \to 0$ 一致成立。

</details>

## 考察点

- [[ANL-THM-044]] Weierstrass M-判别法（找与 $x$ 无关的控制 $M_n$）
- [[ANL-DEF-036]] 确界判据 $\sup_x|S - S_n| \to 0$ 证一致 / 反证不一致
- 一致收敛对**区间**的敏感性（闭子区间 vs 半开区间）
- M-判别法失效（非绝对收敛）时改用 Dirichlet 一致判别（[[ANL-THM-043]]）

## 备注

**判定一致收敛的方法选择**：

| 情形 | 方法 |
|---|---|
| 绝对收敛、易估上界 | Weierstrass M-判别法 |
| 需证**不**一致收敛 | 确界判据：证 $\sup_x\lvert S-S_n\rvert \not\to 0$ |
| 交错 / 条件收敛型 | Dirichlet / Abel 一致判别；或交错级数余项一致估计 |
| 函数列 | 求 $\sup_x\lvert f_n - f\rvert$（常借助求导找最值点） |

**一致收敛的意义**（[[ANL-THM-045]]）：一旦确立，即可放心交换求和与极限 / 积分 / 求导——这正是判定一致收敛的根本目的。
