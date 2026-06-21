---
title: "数项级数敛散综合判定（5 题混合）"
type: problem
id: ANL-PROB-020
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 敛散判定
  - 综合
depends:
  - ANL-THM-038
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §12 综合习题"
difficulty: 3
tests:
  - ANL-THM-038
  - ANL-THM-039
  - ANL-THM-040
  - ANL-THM-041
  - ANL-THM-042
related:
  - ANL-THM-043
  - ANL-DEF-034
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

判定下列级数的敛散性；若收敛，指出是绝对收敛还是条件收敛（[[ANL-DEF-034]]）。

1. $\displaystyle\sum_{n=1}^{\infty} \frac{n^2 + 1}{n^4 + n + 1}$
2. $\displaystyle\sum_{n=1}^{\infty} \frac{3^n \, n!}{n^n}$
3. $\displaystyle\sum_{n=1}^{\infty} \left(\frac{n}{n+1}\right)^{n^2}$
4. $\displaystyle\sum_{n=2}^{\infty} \frac{1}{n \ln n}$
5. $\displaystyle\sum_{n=1}^{\infty} (-1)^{n-1} \frac{1}{\sqrt{n}}$

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：极限比较法（[[ANL-THM-038]]）与 $p$-级数 $\sum 1/n^2$ 比。
- **第 2 题**：含阶乘 + 幂，用比值判别法（[[ANL-THM-039]]），注意 $(1+1/n)^n \to e$ 与 $3$ 的大小。
- **第 3 题**：整体 $n$ 次（实为 $n^2$ 次）幂，用根值判别法（[[ANL-THM-040]]）。
- **第 4 题**：比值 / 根值都给 $1$，用积分判别法（[[ANL-THM-041]]）。
- **第 5 题**：交错级数，Leibniz（[[ANL-THM-042]]）判收敛，再看绝对值级数。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题：极限比较法

通项 $a_n = \dfrac{n^2+1}{n^4+n+1} \sim \dfrac{n^2}{n^4} = \dfrac{1}{n^2}$（$n\to\infty$）。取 $b_n = 1/n^2$，
$$
\lim_{n\to\infty}\frac{a_n}{b_n} = \lim \frac{(n^2+1)n^2}{n^4+n+1} = 1 \in (0,\infty).
$$
由极限比较法（[[ANL-THM-038]]），与收敛的 $p$-级数 $\sum 1/n^2$（$p=2>1$）同敛散，故**收敛**。正项级数，**绝对收敛**。$\quad\blacksquare$

### 第 2 题：比值判别法

$a_n = \dfrac{3^n n!}{n^n}$，
$$
\frac{a_{n+1}}{a_n} = \frac{3^{n+1}(n+1)!}{(n+1)^{n+1}}\cdot\frac{n^n}{3^n n!} = 3\cdot\frac{(n+1)\,n^n}{(n+1)^{n+1}} = 3\left(\frac{n}{n+1}\right)^n = \frac{3}{(1+\frac1n)^n} \to \frac{3}{e}.
$$
因 $\dfrac{3}{e} \approx 1.10 > 1$，由比值判别法（[[ANL-THM-039]]）**发散**。$\quad\blacksquare$

### 第 3 题：根值判别法

$a_n = \left(\dfrac{n}{n+1}\right)^{n^2}$，
$$
\sqrt[n]{a_n} = \left(\frac{n}{n+1}\right)^{n} = \frac{1}{(1+\frac1n)^n} \to \frac1e < 1.
$$
由根值判别法（[[ANL-THM-040]]）**收敛**，正项级数故**绝对收敛**。$\quad\blacksquare$

### 第 4 题：积分判别法

$a_n = \dfrac{1}{n\ln n}$。比值、根值均 $\to 1$（失效）。取 $f(x)=\dfrac{1}{x\ln x}$（$x\ge2$ 正、递减），令 $u=\ln x$：
$$
\int_2^{\infty}\frac{dx}{x\ln x} = \int_{\ln 2}^{\infty}\frac{du}{u} = \lim_{A\to\infty}(\ln A - \ln\ln 2) = +\infty.
$$
积分发散，由积分判别法（[[ANL-THM-041]]）级数**发散**。$\quad\blacksquare$

> 对比：$\sum \frac{1}{n(\ln n)^2}$ 收敛（$p=2>1$）。临界 $p=1$ 处发散，与 $p$-级数同构。

### 第 5 题：Leibniz 判别 + 绝对值分析

$b_n = \dfrac{1}{\sqrt n}$ 单调递减且 $\to 0$，由 Leibniz 判别法（[[ANL-THM-042]]）$\sum (-1)^{n-1}\frac{1}{\sqrt n}$ **收敛**。

但绝对值级数 $\sum \dfrac{1}{\sqrt n} = \sum \dfrac{1}{n^{1/2}}$ 是 $p=\frac12 \le 1$ 的 $p$-级数，**发散**。

故原级数**条件收敛**（[[ANL-DEF-034]]）。$\quad\blacksquare$

</details>

## 考察点

- [[ANL-THM-038]] 极限比较法 + $p$-级数标尺
- [[ANL-THM-039]] 比值判别（阶乘型，$3/e$ 的临界）
- [[ANL-THM-040]] 根值判别（$n$ 次幂型）
- [[ANL-THM-041]] 积分判别（比值/根值失效的对数型）
- [[ANL-THM-042]] Leibniz 判别 + 绝对/条件收敛区分

## 备注

**判别法选择决策树**：

| 通项特征 | 首选判别法 |
|---|---|
| 有理式 / 多项式比 | 极限比较（与 $p$-级数比） |
| 含 $n!$ 或连乘 | 比值判别法 |
| 整体为 $n$ 次幂 | 根值判别法 |
| 比值 / 根值给 $1$（含 $\ln n$） | 积分判别法 |
| 交错符号 | Leibniz，再查绝对值级数 |
| 振荡因子 × 单调因子 | Abel / Dirichlet（[[ANL-THM-043]]） |

**核心提醒**：判定"是否收敛"后，对变号级数务必追问"**绝对还是条件**"——这决定了能否随意重排求和。
