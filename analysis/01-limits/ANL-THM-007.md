---
title: "Cauchy 收敛准则"
type: theorem
id: ANL-THM-007
subject: analysis
chapter: 01-limits
tags:
  - 极限
  - 完备性
  - Cauchy
depends:
  - ANL-DEF-001
  - ANL-DEF-002
  - ANL-DEF-004
  - ANL-THM-008
uses:
  - ANL-AX-001
status: stable
source: "华东师范大学《数学分析》第5版 §2.3"
difficulty: 4
related:
  - ANL-THM-006
applications:
  - "信号处理：判定 Fourier 部分和列收敛而无须显式求和"
  - "数值分析：迭代法终止条件设计"
---

## 条件

> 数列 $\{a_n\} \subseteq \mathbb{R}$。

## 结论

> $\{a_n\}$ 收敛 $\iff$ $\{a_n\}$ 是 Cauchy 列。即：

$$
\exists L \in \mathbb{R}: \lim_{n \to \infty} a_n = L
\iff
\forall \varepsilon > 0,\ \exists N,\ \forall m, n > N: |a_m - a_n| < \varepsilon.
$$

## 几何/直觉理解

收敛要求"项靠近一个**预先指定的目标** $L$"——而许多场合（无穷级数、迭代）中目标值正是要找的未知量。
Cauchy 准则把判定收敛性"内化"：只看数列**自身项之间**的距离是否最终任意小，无须引用极限。
直觉上：项越往后挤得越紧 ⇔ 项最终都聚集在某个点附近。

但这一等价**完全依赖 $\mathbb{R}$ 的完备性**：
在 $\mathbb{Q}$ 中，逼近 $\sqrt{2}$ 的数列是 Cauchy 列却不收敛——目标点 $\sqrt{2}$ 不在 $\mathbb{Q}$ 中。

## 证明

**证明：**

**($\Rightarrow$)** 设 $a_n \to L$。任给 $\varepsilon > 0$，存在 $N$ 使 $\forall n > N: |a_n - L| < \varepsilon / 2$。
对 $m, n > N$：
$$
|a_m - a_n| \leq |a_m - L| + |L - a_n| < \varepsilon / 2 + \varepsilon / 2 = \varepsilon.
$$
故 $\{a_n\}$ 是 Cauchy 列。

**($\Leftarrow$)** 设 $\{a_n\}$ 是 Cauchy 列。

**第 1 步：有界性。** 取 $\varepsilon = 1$，存在 $N_0$ 使 $\forall n > N_0: |a_n - a_{N_0 + 1}| < 1$。
故对 $n > N_0$，$|a_n| < |a_{N_0 + 1}| + 1$。前 $N_0$ 项有限个，整体有界。

**第 2 步：抽取收敛子列。** 由有界性 + Bolzano–Weierstrass 定理（依 [[ANL-AX-001]] 确界原理），
存在子列 $\{a_{n_k}\}$ 收敛于某 $L \in \mathbb{R}$。

**第 3 步：原数列收敛于同一 $L$。** 任给 $\varepsilon > 0$：

- 由 Cauchy 性，$\exists N_1: \forall m, n > N_1: |a_m - a_n| < \varepsilon / 2$；
- 由子列收敛，$\exists K: \forall k > K: |a_{n_k} - L| < \varepsilon / 2$，且可取 $n_k > N_1$。

固定一个这样的 $n_k$，对任意 $n > N_1$：
$$
|a_n - L| \leq |a_n - a_{n_k}| + |a_{n_k} - L| < \varepsilon / 2 + \varepsilon / 2 = \varepsilon.
$$

依 [[ANL-DEF-004]]，$\displaystyle \lim_{n \to \infty} a_n = L$。$\blacksquare$

## 常见错误

- ✗ 把 Cauchy 条件写为"$\forall \varepsilon > 0, \exists N, \forall n > N: |a_{n+1} - a_n| < \varepsilon$"。
  反例：调和部分和 $H_n = \sum_{k=1}^n 1/k$ 满足相邻差 $\to 0$，但 $H_n \to \infty$ 发散。
  必须是**任意两项** $a_m, a_n$。
- ✗ 在 $\mathbb{Q}$ 中直接套用本结论。
  反例：取 $a_n$ 为 $\sqrt{2}$ 的十进制截断 $1, 1.4, 1.41, 1.414, \ldots$，在 $\mathbb{Q}$ 中是 Cauchy 列，
  但极限 $\sqrt{2} \notin \mathbb{Q}$。等价性强依赖完备性。
- ✗ 颠倒量词："$\exists N, \forall \varepsilon, \forall m, n > N: \ldots$"。
  这等价于"从某项起 $a_m = a_n$"，把准则降级为最终常数列。

## 推论与应用

- 任何完备度量空间中"收敛 ⇔ Cauchy"
- 用于无穷级数收敛的 Cauchy 判别法、迭代法误差估计

## 跨专业应用

- **信号处理**：判定 Fourier 部分和数列收敛，不必显式求出极限
- **数值分析**：迭代算法以"$|x_m - x_n| < \text{tol}$"作终止条件，正源自此准则
