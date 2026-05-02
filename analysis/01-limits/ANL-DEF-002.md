---
title: "Cauchy 列（基本列）"
type: definition
id: ANL-DEF-002
subject: analysis
chapter: 01-limits
tags:
  - 数列
  - Cauchy
  - 完备性
depends:
  - ANL-DEF-001
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §2.3"
difficulty: 3
related:
  - ANL-THM-007
  - ANL-AX-001
---

## 定义陈述

> 数列 $\{a_n\}$ 是 **Cauchy 列**（也称**基本列**），若

$$
\forall \varepsilon > 0, \quad \exists N \in \mathbb{N}^*, \quad \forall m, n > N : \quad |a_m - a_n| < \varepsilon.
$$

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 收敛数列 [[ANL-DEF-004]] | 项**与极限值** $L$ 越来越近 |
| Cauchy 列 | **项与项之间**越来越近，不引用极限 |

在 $\mathbb{R}$ 中两者等价；在 $\mathbb{Q}$ 中前者强于后者。

## 直觉理解

收敛数列的定义需要"先知道一个目标 $L$"——但实际研究中目标常常未知。
Cauchy 列把判定收敛性变成了一个**只关乎数列自身**的内部条件：
> 当下标足够靠后时，**任何两项之间**的距离都被 $\varepsilon$ 控住。

形象地说：数列在数轴上"自己挤成一团"——挤得越后越紧。
关键不是"挤向哪里"，而是"内部不再分散"。

## 常见错误

- ✗ 把条件写成"$\forall \varepsilon > 0, \exists N, \forall n > N: |a_{n+1} - a_n| < \varepsilon$"。
  反例：$a_n = \sum_{k=1}^n \frac{1}{k}$ 满足 $|a_{n+1} - a_n| = \frac{1}{n+1} \to 0$，但调和级数发散。
  必须是**任意两项** $a_m, a_n$ 而非仅相邻两项。

## 链接

- 用于定理：[[ANL-THM-007]] Cauchy 收敛准则
- 公理依据：[[ANL-AX-001]] 确界原理（建立等价性所需）
