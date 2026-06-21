---
title: "几何级数与等比型级数求和"
type: example
id: ANL-EX-017
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 几何级数
  - 求和
depends:
  - ANL-DEF-033
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §12.1 例题"
difficulty: 2
illustrates:
  - ANL-DEF-033
related:
  - ANL-THM-036
  - ANL-THM-039
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

1. 证明**几何级数** $\displaystyle\sum_{n=0}^{\infty} r^n$ 当 $|r| < 1$ 时收敛于 $\dfrac{1}{1-r}$，当 $|r| \ge 1$ 时发散。
2. 求 $\displaystyle\sum_{n=1}^{\infty} \frac{1}{2^n}$、$\displaystyle\sum_{n=0}^{\infty} \frac{(-1)^n}{3^n}$ 的和。
3. 求**算术–几何混合级数** $\displaystyle\sum_{n=1}^{\infty} n x^n$（$|x| < 1$）的和。

## 分析

几何级数是**唯一能直接写出部分和闭式**的标杆级数（[[ANL-DEF-033]]），一切比较 / 比值 / 根值判别法的"参照物"。第 3 题的 $\sum n x^n$ 则示范两种标准手法：**错位相减**（离散版分部求和）与**逐项求导**，二者殊途同归。

## 证明 / 解答

**解：**

**第 1 题：** 设 $r \ne 1$，部分和
$$
S_n = \sum_{k=0}^{n-1} r^k = \frac{1 - r^n}{1 - r}.
$$

- $|r| < 1$：$r^n \to 0$，故 $S_n \to \dfrac{1}{1-r}$，**收敛**且和为 $\dfrac{1}{1-r}$。
- $|r| > 1$：$|r^n| \to \infty$，$S_n$ 无有限极限，**发散**。
- $r = 1$：$S_n = n \to \infty$，发散；$r = -1$：$S_n$ 在 $1, 0$ 间振荡，发散。

（$|r| \ge 1$ 时通项 $r^n \not\to 0$，也可直接由必要条件 [[ANL-THM-036]] 判发散。）$\quad\blacksquare$

**第 2 题：**
$$
\sum_{n=1}^{\infty} \frac{1}{2^n} = \frac{1/2}{1 - 1/2} = 1, \qquad
\sum_{n=0}^{\infty} \frac{(-1)^n}{3^n} = \sum_{n=0}^\infty \left(-\frac13\right)^n = \frac{1}{1 - (-1/3)} = \frac{3}{4}.
$$

**第 3 题（错位相减）：** 设 $T = \displaystyle\sum_{n=1}^{\infty} n x^n$（$|x|<1$ 时收敛，可由比值判别法 [[ANL-THM-039]] 验证）。记部分和
$$
T_N = \sum_{n=1}^{N} n x^n, \qquad x T_N = \sum_{n=1}^{N} n x^{n+1} = \sum_{n=2}^{N+1} (n-1) x^{n}.
$$
相减：
$$
(1-x) T_N = \sum_{n=1}^{N} x^n - N x^{N+1} = \frac{x(1 - x^N)}{1-x} - N x^{N+1}.
$$
令 $N \to \infty$（$|x|<1$ 时 $x^N \to 0$、$N x^{N+1} \to 0$）：
$$
(1-x) T = \frac{x}{1-x} \;\Longrightarrow\; \boxed{\ \sum_{n=1}^{\infty} n x^n = \frac{x}{(1-x)^2}.\ }
$$
$\quad\blacksquare$

> **逐项求导验证**：对 $\sum_{n=0}^\infty x^n = \frac{1}{1-x}$ 两边求导得 $\sum_{n=1}^\infty n x^{n-1} = \frac{1}{(1-x)^2}$，乘 $x$ 即同一结果（逐项求导的合法性属幂级数理论）。

## 关键技巧

- **部分和闭式**：几何级数 $S_n = \frac{1-r^n}{1-r}$ 是少数能显式求和的级数，务必背熟。
- **错位相减**：处理 $\sum n x^n$、$\sum n^2 x^n$ 等"多项式 × 等比"级数的通用离散手法，等价于 Abel 分部求和。
- **公比识别**：先把级数整理成 $\sum (\text{公比})^n$ 形式，注意首项指标（从 $n=0$ 还是 $n=1$ 起）会改变和值。

## 变式

- **变式 1**：求 $\displaystyle\sum_{n=1}^{\infty} \frac{n}{2^n}$（代 $x = 1/2$，得 $\frac{1/2}{(1/2)^2} = 2$）。
- **变式 2**：求 $\displaystyle\sum_{n=1}^{\infty} n^2 x^n$（再对 $\frac{x}{(1-x)^2}$ 求导并乘 $x$，得 $\frac{x(1+x)}{(1-x)^3}$）。
- **变式 3**：循环小数 $0.\overline{27} = 0.272727\cdots$ 用几何级数求其分数表示（$= \frac{27}{99} = \frac{3}{11}$）。
