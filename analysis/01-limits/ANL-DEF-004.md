---
title: "数列收敛（ε-N 定义）"
type: definition
id: ANL-DEF-004
subject: analysis
chapter: 01-limits
tags:
  - 极限
  - ε-N
  - 数列
depends:
  - ANL-DEF-001
uses: []
status: review
source: "华东师范大学《数学分析》第5版 §2.1"
difficulty: 2
related:
  - ANL-DEF-002
  - ANL-THM-006
  - ANL-THM-007
---

## 定义陈述

> 数列 $\{a_n\}$ **收敛于** $L \in \mathbb{R}$，记作 $\displaystyle \lim_{n \to \infty} a_n = L$，若

$$
\forall \varepsilon > 0, \quad \exists N \in \mathbb{N}^*, \quad \forall n > N : \quad |a_n - L| < \varepsilon.
$$

不存在这样的 $L$ 时，称 $\{a_n\}$ **发散**。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 收敛 | 唯一的极限值 $L$ 存在 |
| 有界 [[ANL-DEF-005]] | 项被某常数夹住，不必收敛（$(-1)^n$ 反例） |
| Cauchy 列 [[ANL-DEF-002]] | 项与项之间靠拢，不直接引用 $L$ |

## 直觉理解

把 $\varepsilon$ 看作"裁判给的精度要求"：
> 任你给出多严格的精度 $\varepsilon$，我都能找到一个起点 $N$，
> **从此之后**所有项都落在 $L$ 的 $\varepsilon$-邻域里。

关键是**量词顺序**：$N$ 依赖于 $\varepsilon$（精度越严，$N$ 越大），
但**不依赖于 $n$**——一旦确定 $N$，"$\forall n > N$" 是一票全包。

## 常见错误

- ✗ 写成"$\exists N, \forall \varepsilon > 0, \forall n > N: |a_n - L| < \varepsilon$"。
  这要求**同一个 $N$** 对所有 $\varepsilon$ 都管用，等价于"$a_n = L$ 当 $n > N$"，把收敛降级成最终常数列。
- ✗ 认为"$|a_n - L|$ 单调减小"是收敛的必要条件。
  反例：$a_n = \tfrac{1 + (-1)^n}{n}$ 收敛于 $0$（夹逼于 $0$ 与 $2/n$），但 $|a_n - 0|$ 取值在 $0$ 与 $2/n$ 间跳跃，**不单调**。
  收敛只要求"距离最终任意小"，并不要求"距离持续单调缩小"。

## 链接

- 用于定义：[[ANL-DEF-002]] Cauchy 列
- 用于定理：[[ANL-THM-006]]、[[ANL-THM-007]]
