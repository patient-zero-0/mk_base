---
title: "单调数列"
type: definition
id: ANL-DEF-003
subject: analysis
chapter: 01-limits
tags:
  - 数列
  - 单调性
depends:
  - ANL-DEF-001
uses: []
status: review
source: "华东师范大学《数学分析》第5版 §2.2"
difficulty: 1
related:
  - ANL-THM-006
---

## 定义陈述

设 $\{a_n\}$ 是数列。

- $\{a_n\}$ **单调递增**：$\forall n \in \mathbb{N}^*, \quad a_n \leq a_{n+1}$。
- $\{a_n\}$ **严格单调递增**：$\forall n \in \mathbb{N}^*, \quad a_n < a_{n+1}$。
- 单调递减、严格单调递减类似。

凡满足上述任一种者，统称为**单调数列**。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 单调 | 全部 $n$ 都满足比较关系 |
| 最终单调 | 仅当 $n \geq N_0$ 后才单调 |
| 局部单调 | 在某区间内有单调子段，整体不必 |

## 直觉理解

把数列想成时间序列：单调递增就是"只往上爬，不回头"。
注意"$\leq$"允许相邻两项相等（如常数列也是单调递增的）；
"$<$"则禁止停顿——这是后续讨论严格单调子列时的关键区别。

## 链接

- 用于定理：[[ANL-THM-006]] 单调有界定理
