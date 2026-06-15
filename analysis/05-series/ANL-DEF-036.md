---
title: "逐点收敛与一致收敛"
type: definition
id: ANL-DEF-036
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 一致收敛
  - 逐点收敛
depends:
  - ANL-DEF-035
  - ANL-DEF-004
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §13.1"
difficulty: 4
related:
  - ANL-DEF-024
  - ANL-THM-044
  - ANL-THM-045
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设函数列 $\{S_n\}$ 定义在 $E \subseteq \mathbb{R}$ 上，$S : E \to \mathbb{R}$（对函数项级数，$S_n$ 取部分和函数，$S$ 为和函数，[[ANL-DEF-035]]）。

**逐点收敛**：称 $S_n$ 在 $E$ 上**逐点收敛**于 $S$，若对每个固定的 $x \in E$，数列 $\{S_n(x)\}$ 收敛于 $S(x)$（[[ANL-DEF-004]]）：
$$
\forall x \in E,\ \forall \varepsilon > 0,\ \exists N(\varepsilon, x),\ \forall n > N:\ |S_n(x) - S(x)| < \varepsilon.
$$

**一致收敛**：称 $S_n$ 在 $E$ 上**一致收敛**于 $S$，记 $S_n \rightrightarrows S$，若
$$
\forall \varepsilon > 0,\ \exists N(\varepsilon),\ \forall n > N,\ \forall x \in E:\ |S_n(x) - S(x)| < \varepsilon.
$$

> **唯一差别在于 $N$**：逐点收敛允许 $N$ 依赖于 $x$（不同点收敛快慢可不同）；
> 一致收敛要求 $N$ **对所有 $x$ 统一**（同一个 $N$ 管住全体点）。这就是量词 $\forall x$ 与 $\exists N$ 的**先后顺序**之差。

**等价刻画（确界判据）**：$S_n \rightrightarrows S$ 于 $E$ $\iff$
$$
\lim_{n \to \infty} \sup_{x \in E} |S_n(x) - S(x)| = 0.
$$

## 与相近概念的区别

| 概念 | 量词顺序 | 几何含义 |
|---|---|---|
| 逐点收敛 | $\forall x\ \exists N$ | 每个点各自收敛，快慢可不同 |
| 一致收敛 | $\exists N\ \forall x$ | 整条曲线一起进入 $\varepsilon$-带 |
| 一致连续（[[ANL-DEF-024]]） | $\exists \delta\ \forall x$ | $\delta$ 对全体点统一（量词结构同构） |

> **一致收敛 ⇒ 逐点收敛**，反之不然。一致收敛是逐点收敛 + "$N$ 与 $x$ 无关"的加强。

## 直觉理解

把 $S_n$ 与极限 $S$ 的图像画在一起，并在 $S$ 周围画一条宽 $\pm\varepsilon$ 的"**$\varepsilon$-管道**"。

- **逐点收敛**：对每个 $x$，曲线 $S_n$ 在该点最终钻进管道——但不同 $x$ 进入的"时刻 $N$"可以天差地别，可能永远找不到一个时刻让**整条**曲线都在管道内。
- **一致收敛**：存在一个统一时刻 $N$，过了它之后**整条曲线 $S_n$ 完全躺在管道里**，无一处越界。

**经典反例（逐点收敛但不一致）**：$f_n(x) = x^n$ 于 $[0,1]$。逐点极限
$$
S(x) = \begin{cases} 0, & 0 \le x < 1, \\ 1, & x = 1, \end{cases}
$$
但 $\sup_{[0,1]} |x^n - S(x)| = \sup_{x<1} x^n = 1 \not\to 0$，故**不一致收敛**。其后果是：连续函数 $x^n$ 的逐点极限 $S$ **不连续**——这正是一致收敛之所以重要的根本原因（[[ANL-THM-045]]）。

> 一句话：**逐点收敛只保证"终点对"，一致收敛额外保证"步调齐"**。唯有步调齐整，极限才会继承连续 / 可积 / 可导等好性质。

## 链接

- 函数项级数与函数列：[[ANL-DEF-035]]
- 量词结构同构的一致连续：[[ANL-DEF-024]]
- 一致收敛的充分判据：[[ANL-THM-044]] Weierstrass M-test
- 一致收敛的核心后果（连续 / 可积 / 可导交换）：[[ANL-THM-045]]
