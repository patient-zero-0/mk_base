---
title: "比值与根值判别法的典型应用"
type: example
id: ANL-EX-018
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 比值判别法
  - 根值判别法
depends:
  - ANL-THM-039
  - ANL-THM-040
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §12.2 例题"
difficulty: 3
illustrates:
  - ANL-THM-039
  - ANL-THM-040
related:
  - ANL-THM-038
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

判定下列正项级数的敛散性，并体会比值（[[ANL-THM-039]]）与根值（[[ANL-THM-040]]）判别法各自的适用场景：

1. $\displaystyle\sum_{n=1}^{\infty} \frac{n!}{n^n}$
2. $\displaystyle\sum_{n=1}^{\infty} \frac{n^2}{2^n}$
3. $\displaystyle\sum_{n=1}^{\infty} \left(\frac{n}{2n+1}\right)^n$
4. $\displaystyle\sum_{n=1}^{\infty} \frac{2^n + 1}{3^n - 1}$

## 分析

选判别法的经验法则：

- 通项含 **阶乘 / 连乘** ⇒ 优先**比值**（相邻项一除，阶乘大量约简）；
- 通项整体是 **$n$ 次幂** ⇒ 优先**根值**（开 $n$ 次方直接脱幂）；
- 通项是 **幂的比值（等比型）** ⇒ 两者皆可，或直接与几何级数比较（[[ANL-THM-038]]）。

## 证明 / 解答

**解：**

**第 1 题（比值）：** $a_n = \dfrac{n!}{n^n}$，
$$
\frac{a_{n+1}}{a_n} = \frac{(n+1)!}{(n+1)^{n+1}} \cdot \frac{n^n}{n!} = \frac{(n+1)\, n^n}{(n+1)^{n+1}} = \frac{n^n}{(n+1)^n} = \left(\frac{n}{n+1}\right)^n = \frac{1}{\left(1 + \frac1n\right)^n}.
$$
故 $\displaystyle\lim_{n\to\infty}\frac{a_{n+1}}{a_n} = \frac{1}{e} < 1$，由比值判别法**收敛**。$\quad\blacksquare$

**第 2 题（比值）：** $a_n = \dfrac{n^2}{2^n}$，
$$
\frac{a_{n+1}}{a_n} = \frac{(n+1)^2}{2^{n+1}}\cdot\frac{2^n}{n^2} = \frac12\left(\frac{n+1}{n}\right)^2 \to \frac12 < 1,
$$
**收敛**。（根值亦可：$\sqrt[n]{n^2/2^n} = \frac{(\sqrt[n]{n})^2}{2} \to \frac12$。）$\quad\blacksquare$

**第 3 题（根值）：** $a_n = \left(\dfrac{n}{2n+1}\right)^n$，整体为 $n$ 次幂，
$$
\sqrt[n]{a_n} = \frac{n}{2n+1} \to \frac12 < 1,
$$
由根值判别法**收敛**。（此题用比值会很繁琐，体现根值对"$n$ 次幂"结构的优势。）$\quad\blacksquare$

**第 4 题（根值 / 比较）：** $a_n = \dfrac{2^n + 1}{3^n - 1}$。根值：
$$
\sqrt[n]{a_n} = \frac{\sqrt[n]{2^n + 1}}{\sqrt[n]{3^n - 1}} = \frac{2\sqrt[n]{1 + 2^{-n}}}{3\sqrt[n]{1 - 3^{-n}}} \to \frac{2}{3} < 1,
$$
**收敛**。（或比较：$a_n \sim (2/3)^n$，与几何级数 [[ANL-THM-038]] 同敛散。）$\quad\blacksquare$

## 关键技巧

- **$(1+1/n)^n \to e$**：第 1 题的核心极限，阶乘型级数判敛的常客；由此 $\sum n!/n^n$ 收敛而 $\sum n!/(2^n)$ 等发散（比值 $\to \infty$）。
- **$\sqrt[n]{n} \to 1$、$\sqrt[n]{C} \to 1$**：根值计算的万能简化，使多项式因子与常数因子在开 $n$ 次方后"消失"。
- **选对工具省一半功夫**：阶乘用比值、纯 $n$ 次幂用根值；两者给出相同极限时（理论上根值更强），挑好算的那个。
- **临界 $q=1$ 要换法**：若比值 / 根值给出 $1$，立即转积分判别法（见 [[ANL-THM-038]] 标尺与 $p$-级数）。

## 变式

- **变式 1**：判定 $\displaystyle\sum \frac{n^n}{n!}$（比值 $\to e > 1$，**发散**——与第 1 题互为倒数，体会 $e$ 的临界角色）。
- **变式 2**：判定 $\displaystyle\sum \frac{(n!)^2}{(2n)!}$（比值 $\to \frac14 < 1$，收敛）。
- **变式 3**：构造一个比值极限不存在、但根值判别法仍可判定收敛的级数（提示：$a_n = 2^{-n + (-1)^n}$，比值在 $2,\,1/8$ 间振荡，而 $\sqrt[n]{a_n} \to 1/2$）。
