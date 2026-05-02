---
title: "数列"
type: definition
id: ANL-DEF-001
subject: analysis
chapter: 01-limits
tags:
  - 数列
  - 基础概念
depends: []
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §2.1"
difficulty: 1
related:
  - ANL-DEF-003
  - ANL-DEF-004
  - ANL-DEF-005
---

## 定义陈述

> 一个**数列**是从 $\mathbb{N}$（或 $\mathbb{N}^*$）到 $\mathbb{R}$ 的映射。

形式上，数列 $\{a_n\}$ 是函数 $a : \mathbb{N}^* \to \mathbb{R}$，将 $n \mapsto a_n$。
通常按下标顺序写作 $a_1, a_2, a_3, \ldots, a_n, \ldots$。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 数列 $\{a_n\}$ | 定义域为 $\mathbb{N}^*$，离散 |
| 函数 $f(x)$ | 定义域为 $\mathbb{R}$ 的子集，连续 |
| 集合 $\{a_n : n \geq 1\}$ | 不计顺序、不计重复 |

## 直觉理解

数列就是"按整数标号排好的一串实数"。**顺序很重要**：$1, 2, 1, 2, \ldots$ 和 $2, 1, 2, 1, \ldots$ 是不同的数列。
把它想象成一行无穷无尽的小格子，第 $n$ 个格子里放着实数 $a_n$。
讨论数列的"行为"时，我们关心**当 $n$ 越来越大时格子里的数往哪走**——这就是极限的源头。

## 链接

- 用于定义：[[ANL-DEF-003]] 单调数列、[[ANL-DEF-004]] 收敛数列、[[ANL-DEF-005]] 有界数列
- 用于定理：[[ANL-THM-006]]、[[ANL-THM-007]]
