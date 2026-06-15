---
title: "级数的 Cauchy 收敛准则"
type: theorem
id: ANL-THM-037
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 收敛
  - Cauchy
depends:
  - ANL-DEF-033
  - ANL-THM-007
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §12.1"
difficulty: 3
related:
  - ANL-THM-036
  - ANL-DEF-034
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

> 级数 $\sum_{n=1}^{\infty} a_n$（$a_n \in \mathbb{R}$）。

## 结论

> $\sum a_n$ **收敛**（[[ANL-DEF-033]]）当且仅当：对任意 $\varepsilon > 0$，存在 $N$，使得对一切 $m > n > N$，
> $$
> \left| \sum_{k=n+1}^{m} a_k \right| = |a_{n+1} + a_{n+2} + \cdots + a_m| < \varepsilon.
> $$

即：**任意一段足够靠后的连续项之和都可任意小**。

## 几何/直觉理解

级数收敛要求部分和数列 $\{S_n\}$ 收敛。在 $\mathbb{R}$ 中"数列收敛 $\iff$ 数列是 Cauchy 列"（[[ANL-THM-007]]），而部分和的差恰是一段连续项之和：
$$
S_m - S_n = \sum_{k=n+1}^{m} a_k.
$$
于是"$\{S_n\}$ 是 Cauchy 列"翻译成级数语言，就是"任意靠后的**项段和**可任意小"。

直觉上：收敛 $\iff$ 无论从多靠后开始、连续累加多少项，新增的总贡献都微不足道。这把对"总和"的判定，转化为对"**局部尾段**"的控制，无须知道和是多少——这正是 Cauchy 准则的威力所在。

## 证明

**证明：** 设 $\{S_n\}$ 为部分和数列。由定义（[[ANL-DEF-033]]），$\sum a_n$ 收敛 $\iff$ $\{S_n\}$ 收敛。

由数列的 Cauchy 收敛准则（[[ANL-THM-007]]），$\{S_n\}$ 收敛 $\iff$ $\{S_n\}$ 是 Cauchy 列，即
$$
\forall \varepsilon > 0,\ \exists N,\ \forall m, n > N:\ |S_m - S_n| < \varepsilon.
$$

不妨设 $m > n$（$m = n$ 时差为 $0$；$m < n$ 时对称）。此时
$$
S_m - S_n = \sum_{k=1}^{m} a_k - \sum_{k=1}^{n} a_k = \sum_{k=n+1}^{m} a_k.
$$

代入即得：$\sum a_n$ 收敛 $\iff$ $\forall \varepsilon > 0,\ \exists N,\ \forall m > n > N:\ \left|\sum_{k=n+1}^{m} a_k\right| < \varepsilon$。$\qquad\blacksquare$

## 常见错误

- ✗ 只验证**相邻两项**之差：取 $m = n+1$ 得 $|a_{n+1}| < \varepsilon$，这只是通项趋零（[[ANL-THM-036]]），是必要非充分条件。
    **反例**：调和级数 $\sum 1/n$，相邻项 $\to 0$ 满足，但取 $m = 2n$ 时
    $$
    \sum_{k=n+1}^{2n} \frac{1}{k} \ge n \cdot \frac{1}{2n} = \frac{1}{2} \not\to 0,
    $$
    项段和不趋于零，故发散。**必须对一切 $m > n$ 的项段和成立**。
- ✗ 把绝对值放进求和号：误用 $\sum_{k=n+1}^m |a_k| < \varepsilon$ 作为收敛准则。
    这其实是**绝对收敛**（[[ANL-DEF-034]]）的准则，比收敛强。条件收敛级数满足原准则却不满足此式。
- ✗ 在 $\mathbb{Q}$ 等不完备空间套用。等价性依赖 $\mathbb{R}$ 完备性（同 [[ANL-THM-007]]）。

## 推论与应用

- **必要条件**（[[ANL-THM-036]]）：取 $m = n+1$ 即得 $a_n \to 0$
- **绝对收敛 ⇒ 收敛**（[[ANL-DEF-034]]）：由 $\left|\sum_{k=n+1}^m a_k\right| \le \sum_{k=n+1}^m |a_k|$ 直接推出
- 无须求和即可判敛散，是 Abel/Dirichlet 等判别法的理论基础

## 跨专业应用

- **数值分析**：以"尾段和 $< \text{tol}$"作为级数求和的截断终止判据
- **信号处理**：判定 Fourier 部分和列收敛而不必显式求极限（同 [[ANL-THM-007]]）
