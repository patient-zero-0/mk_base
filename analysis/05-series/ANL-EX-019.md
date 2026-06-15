---
title: "常见初等函数的 Maclaurin 展开"
type: example
id: ANL-EX-019
subject: analysis
chapter: 05-series
tags:
  - 级数
  - Maclaurin 级数
  - 幂级数展开
depends:
  - ANL-DEF-039
  - ANL-THM-046
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §14.2 例题"
difficulty: 3
illustrates:
  - ANL-DEF-039
  - ANL-THM-046
related:
  - ANL-THM-025
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

求下列函数的 Maclaurin 级数（[[ANL-DEF-039]]）及收敛域，并验证收敛到原函数：

1. $e^x$
2. $\sin x$ 与 $\cos x$
3. $\ln(1+x)$
4. $(1+x)^\alpha$（$\alpha \in \mathbb{R}$，二项级数）

## 分析

两条路线：(a) **直接法**——算各阶导数代入系数公式 $c_n = \frac{f^{(n)}(0)}{n!}$，再用 Taylor 余项（[[ANL-THM-025]]）验证 $R_n \to 0$；(b) **间接法**——从已知展开出发，借逐项求导 / 积分（[[ANL-THM-046]]）或代换快速导出新展开。$\ln(1+x)$ 用间接法（对几何级数积分）最省力。

## 证明 / 解答

**解：**

**第 1 题（$e^x$）：** $f^{(n)}(x)=e^x$，$f^{(n)}(0)=1$，故 $c_n = 1/n!$：
$$
e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots
$$
**收敛域 $\mathbb{R}$**（$R=\infty$，由 $c_n=1/n!$ 及比值式）。**余项验证**：对固定 $x$，$|R_n(x)| = \left|\frac{e^\xi}{(n+1)!}x^{n+1}\right| \le \frac{e^{|x|}|x|^{n+1}}{(n+1)!} \to 0$（阶乘压倒幂）。故处处收敛到 $e^x$。$\quad\blacksquare$

**第 2 题（$\sin x, \cos x$）：** $\sin$ 的各阶导在 $0$ 处循环取 $0,1,0,-1$，故
$$
\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!}x^{2n+1} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots,
$$
$$
\cos x = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!}x^{2n} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots.
$$
两者**收敛域均为 $\mathbb{R}$**；余项 $|R_n(x)|\le \frac{|x|^{n+1}}{(n+1)!}\to0$（各阶导有界于 $1$）。注意 $\cos x = (\sin x)'$ 恰由逐项求导（[[ANL-THM-046]]）得到，互相印证。$\quad\blacksquare$

**第 3 题（$\ln(1+x)$，间接法）：** 从几何级数 $\dfrac{1}{1+t} = \sum_{n=0}^\infty (-1)^n t^n$（$|t|<1$）出发，在 $[0,x]$ 上逐项积分（[[ANL-THM-046]]）：
$$
\ln(1+x) = \int_0^x \frac{dt}{1+t} = \sum_{n=0}^{\infty} (-1)^n \frac{x^{n+1}}{n+1} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots
$$
**收敛半径 $R=1$**。端点：$x=1$ 得交错调和级数 $\sum\frac{(-1)^{n}}{n+1}$ 收敛（Leibniz），$x=-1$ 得 $-\sum\frac1{n+1}$ 发散。故**收敛域 $(-1, 1]$**，且 $\ln 2 = 1 - \frac12 + \frac13 - \cdots$。$\quad\blacksquare$

**第 4 题（二项级数）：** $f(x)=(1+x)^\alpha$，$f^{(n)}(0)=\alpha(\alpha-1)\cdots(\alpha-n+1)$，故
$$
(1+x)^\alpha = \sum_{n=0}^{\infty} \binom{\alpha}{n} x^n,\qquad \binom{\alpha}{n} = \frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}.
$$
当 $\alpha$ 非非负整数时**收敛半径 $R=1$**（比值 $\to1$）。$\alpha$ 为非负整数时退化为有限项（多项式，$R=\infty$）。$\quad\blacksquare$

## 关键技巧

- **直接法配余项**：$e^x,\sin,\cos$ 因各阶导有界 / 受阶乘压制，余项 $\frac{M|x|^{n+1}}{(n+1)!}\to0$，处处收敛。
- **间接法（逐项积分 / 求导）**：$\ln(1+x)$ 对 $\frac1{1+t}$ 积分、$\arctan x$ 对 $\frac1{1+t^2}$ 积分，远比硬算 $n$ 阶导高效（[[ANL-THM-046]] 保证合法）。
- **端点单独判**：收敛半径定内部，两端点务必各代入用 Leibniz / $p$-级数判，常出现"一端收敛一端发散"。
- **五个母展开**（$e^x,\sin x,\cos x,\frac{1}{1-x},(1+x)^\alpha$）记熟后，多数展开靠代换 / 微积分组合导出。

## 变式

- **变式 1**：由 $\frac{1}{1+t^2}=\sum(-1)^n t^{2n}$ 积分求 $\arctan x = \sum_{n=0}^\infty \frac{(-1)^n}{2n+1}x^{2n+1}$，并导出 $\frac\pi4 = 1-\frac13+\frac15-\cdots$（$x=1$，Leibniz 公式）。
- **变式 2**：用 $\alpha=-\frac12$ 的二项级数展开 $\frac{1}{\sqrt{1+x}}$。
- **变式 3**：由 $\sin x$ 展开求 $\displaystyle\lim_{x\to0}\frac{\sin x - x}{x^3} = -\frac{1}{6}$（与 L'Hospital 法则 [[ANL-THM-024]] 对照）。
