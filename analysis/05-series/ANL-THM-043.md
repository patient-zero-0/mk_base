---
title: "Abel 判别法与 Dirichlet 判别法（级数版）"
type: theorem
id: ANL-THM-043
subject: analysis
chapter: 05-series
tags:
  - 级数
  - Abel 判别法
  - Dirichlet 判别法
depends:
  - ANL-DEF-033
  - ANL-THM-037
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §12.3"
difficulty: 4
related:
  - ANL-THM-042
  - ANL-DEF-034
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

考察形如 $\sum a_n b_n$ 的级数。记 $A_n = \sum_{k=1}^n a_k$。

> **Dirichlet 判别法**：若
>
> 1. $A_n$ **有界**（$\exists M,\ |A_n| \le M$ 对一切 $n$）；
> 2. $\{b_n\}$ **单调**且 $b_n \to 0$，
>
> 则 $\sum a_n b_n$ 收敛。
>
> **Abel 判别法**：若
>
> 1. $\sum a_n$ **收敛**；
> 2. $\{b_n\}$ **单调有界**，
>
> 则 $\sum a_n b_n$ 收敛。

## 结论

> 上述两组条件下，级数 $\sum a_n b_n$ 均**收敛**（[[ANL-DEF-033]]）。

## 几何/直觉理解

二者都处理"**振荡因子 $a_n$ × 缓变因子 $b_n$**"的乘积级数，核心是**Abel 求和（分部求和）**——离散版的"分部积分"：把求和的"求导"挪到容易控制的因子上。

- **Dirichlet**：$a_n$ 自身不收敛，但其部分和被"困"在有界范围内（如 $a_n = (-1)^n$ 或 $a_n=\cos n\theta$ 反复抵消）。只要再乘上一个单调趋零的"刹车" $b_n$，振荡贡献被逐步压灭，级数收敛。
- **Abel**：$\sum a_n$ 本已收敛，再乘一个单调有界因子 $b_n$ 不会破坏收敛——单调有界的 $b_n$ 像一个"温和的调制"，至多重新分配权重而不引入发散。

> Leibniz 判别法（[[ANL-THM-042]]）是 Dirichlet 的特例：取 $a_n = (-1)^{n-1}$（部分和 $A_n \in \{0,1\}$ 有界），$b_n$ 单调趋零即得。

## 证明

**关键工具：Abel 分部求和。** 设 $S_p = \sum_{k=n+1}^{p} a_k$（约定 $S_n = 0$），则 $a_k = S_k - S_{k-1}$（$k \ge n+1$），于是
$$
\sum_{k=n+1}^{m} a_k b_k = \sum_{k=n+1}^{m}(S_k - S_{k-1}) b_k = S_m b_m + \sum_{k=n+1}^{m-1} S_k (b_k - b_{k+1}). \tag{$\ast$}
$$

**Dirichlet 判别法证明。** 由 $|A_n| \le M$，$|S_k| = |A_k - A_n| \le 2M$。$\{b_n\}$ 单调使 $b_k - b_{k+1}$ 不变号，故
$$
\sum_{k=n+1}^{m-1} |b_k - b_{k+1}| = \Big|\sum_{k=n+1}^{m-1}(b_k - b_{k+1})\Big| = |b_{n+1} - b_m| \le |b_{n+1}| + |b_m|.
$$
对 $(\ast)$ 取绝对值：
$$
\left|\sum_{k=n+1}^{m} a_k b_k\right| \le 2M|b_m| + 2M\big(|b_{n+1}| + |b_m|\big) = 2M\big(|b_{n+1}| + 2|b_m|\big).
$$
因 $b_n \to 0$，任给 $\varepsilon > 0$，当 $n, m$ 充分大时右端 $< \varepsilon$。由级数 Cauchy 准则（[[ANL-THM-037]]），$\sum a_n b_n$ 收敛。$\qquad\blacksquare$

**Abel 判别法证明。** $\{b_n\}$ 单调有界 ⇒ 收敛，设 $b_n \to b$。令 $c_n = b_n - b$，则 $\{c_n\}$ **单调且趋于 $0$**。分解
$$
a_n b_n = b\,a_n + a_n c_n.
$$

- $\sum b\,a_n = b \sum a_n$ 收敛（已知 $\sum a_n$ 收敛）；
- $\sum a_n c_n$：$\sum a_n$ 收敛 ⇒ 其部分和 $A_n$ 收敛 ⇒ **有界**；$c_n$ 单调趋零。由刚证的 Dirichlet 判别法，$\sum a_n c_n$ 收敛。

两收敛级数之和收敛，故 $\sum a_n b_n$ 收敛。$\qquad\blacksquare$

## 常见错误

- ✗ Dirichlet 中漏掉"$b_n \to 0$"，只用单调有界。**反例**：$a_n = (-1)^n$（部分和有界），$b_n = 1$（单调有界但不趋零），则 $\sum (-1)^n$ 发散。趋零不可省。
- ✗ Abel 中误加"$b_n \to 0$"或"$\sum a_n$ 只需部分和有界"。Abel 要求 $\sum a_n$ **真收敛**且 $b_n$ 只需单调**有界**；与 Dirichlet 的条件不可混搭。
- ✗ 忘记 $\{b_n\}$ 的**单调性**，导致 $\sum|b_k - b_{k+1}|$ 不能裂项为 $|b_{n+1}-b_m|$。无单调性时该和可能发散，证明失效。
- ✗ 误用于求和值。两判别法只判**收敛性**，不给出级数和。

## 推论与应用

- **Leibniz 判别法**（[[ANL-THM-042]]）：Dirichlet 取 $a_n = (-1)^{n-1}$ 的特例
- 判定 $\sum \dfrac{\sin n\theta}{n}$、$\sum \dfrac{\cos n\theta}{n^p}$ 等三角级数收敛（$\sum \cos/\sin$ 部分和有界）
- 是条件收敛（[[ANL-DEF-034]]）级数的主力判别工具

## 跨专业应用

- **信号处理**：判定调制信号 $\sum a_n b_n$（载波 × 缓变包络）对应级数的收敛
- **Fourier 分析**：三角级数 $\sum \frac{\sin n x}{n}$ 的逐点收敛由 Dirichlet 判别保证
