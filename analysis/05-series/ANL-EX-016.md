---
title: "调和级数发散与 p-级数敛散（积分判别法应用）"
type: example
id: ANL-EX-016
subject: analysis
chapter: 05-series
tags:
  - 级数
  - p-级数
  - 积分判别法
depends:
  - ANL-THM-041
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §12.2 例题"
difficulty: 3
illustrates:
  - ANL-THM-041
related:
  - ANL-THM-038
  - ANL-THM-036
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

讨论 **$p$-级数** $\displaystyle \sum_{n=1}^{\infty} \frac{1}{n^p}$（$p \in \mathbb{R}$）的敛散性，并特别说明 $p = 1$（**调和级数**）的情形。作为推广，再判定 $\displaystyle \sum_{n=2}^{\infty} \frac{1}{n(\ln n)^p}$。

## 分析

$p$-级数是衡量"多项式衰减速度"的**标准标尺**：几乎所有比较判别法（[[ANL-THM-038]]）都拿它当参照。但比值/根值判别法对它一律给出极限 $1$（失效），故必须用**积分判别法**（[[ANL-THM-041]]）——把离散求和换成可求原函数的连续积分。关键前提：$f(x) = 1/x^p$ 在 $p > 0$ 时非负且单调递减，满足积分判别法条件。

## 证明 / 解答

**解：**

**情形 $p \le 0$：** 通项 $\dfrac{1}{n^p} = n^{-p} \not\to 0$（$p<0$ 时趋于 $\infty$，$p=0$ 时恒为 $1$）。由收敛必要条件（[[ANL-THM-036]]），级数**发散**。

**情形 $p > 0$：** 取 $f(x) = \dfrac{1}{x^p}$，在 $[1, \infty)$ 上非负、连续、单调递减，且 $f(n) = \dfrac{1}{n^p}$。由积分判别法（[[ANL-THM-041]]），级数与 $\displaystyle\int_1^\infty \frac{dx}{x^p}$ 同敛散。

计算反常积分：

- **$p \ne 1$**：
    $$
    \int_1^{A} x^{-p}\,dx = \left[\frac{x^{1-p}}{1-p}\right]_1^{A} = \frac{A^{1-p} - 1}{1-p}.
    $$
    当 $A \to \infty$：$p > 1$ 时 $A^{1-p} \to 0$，积分收敛于 $\dfrac{1}{p-1}$；$0 < p < 1$ 时 $A^{1-p} \to \infty$，积分发散。
- **$p = 1$**（调和级数）：
    $$
    \int_1^{A} \frac{dx}{x} = \ln A \to +\infty,
    $$
    积分**发散**。

**结论：**
$$
\boxed{\ \sum_{n=1}^{\infty} \frac{1}{n^p} \text{ 收敛} \iff p > 1.\ }
$$
特别地，调和级数 $\sum \dfrac{1}{n}$（$p=1$）**发散**——尽管其通项趋于零。$\quad\blacksquare$

**推广（对数 $p$-级数）：** 对 $\displaystyle\sum_{n=2}^{\infty} \frac{1}{n(\ln n)^p}$，取 $f(x) = \dfrac{1}{x(\ln x)^p}$（$x \ge 2$ 非负递减）。令 $u = \ln x$，$du = dx/x$：
$$
\int_2^{\infty} \frac{dx}{x(\ln x)^p} = \int_{\ln 2}^{\infty} \frac{du}{u^p},
$$
归化为 $p$-级数同型积分。故 $\displaystyle\sum \frac{1}{n(\ln n)^p}$ 收敛 $\iff p > 1$。$\quad\blacksquare$

## 关键技巧

- **积分判别法对付 $q=1$ 临界**：比值/根值判别法对 $p$-级数全部失效（极限均为 $1$），积分判别法是判定多项式衰减级数的"标准答案"。
- **换元降阶**：对数 $p$-级数通过 $u = \ln x$ 化归为普通 $p$-级数，这一"取对数变量"技巧可层层嵌套（$\sum \frac{1}{n \ln n (\ln\ln n)^p}$ 同理）。
- **临界值记忆**：$p$-级数、对数 $p$-级数的分界点都是 $p = 1$，且临界 $p=1$ 处恰好发散。

## 变式

- **变式 1**：判定 $\displaystyle\sum \frac{1}{n^p (\ln n)^q}$ 的敛散（按 $p$ 与 $1$ 的大小分类，$p=1$ 时再看 $q$）。
- **变式 2**：用比较判别法（[[ANL-THM-038]]）而非积分判别法证明 $\sum 1/n^2$ 收敛（提示：$\frac{1}{n^2} \le \frac{1}{n(n-1)} = \frac{1}{n-1} - \frac{1}{n}$，裂项）。
- **变式 3**：估计调和级数部分和 $H_n = \sum_{k=1}^n \frac1k$ 的增长阶，证明 $H_n = \ln n + \gamma + o(1)$。
