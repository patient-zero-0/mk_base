---
title: "一元多项式"
type: definition
id: ALG-DEF-001
subject: algebra
chapter: 01-polynomials
tags:
  - 多项式
  - 基础概念
depends: []
uses: []
status: draft
source: "丘维声《高等代数》第3版 §1.1"
difficulty: 1
related:
  - ALG-DEF-002
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设 $K$ 是数域（如 $\mathbb{Q}, \mathbb{R}, \mathbb{C}$），$x$ 是不定元。
形如
$$
f(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0, \quad a_i \in K, \quad a_n \neq 0
$$
的表达式称为 $K$ **上的一元多项式**，称 $n$ 为 $f(x)$ 的**次数**，记作 $\deg f = n$。

约定**零多项式** $0$ 的次数为 $-\infty$（或不定义）。

记号 $K[x]$ 表示 $K$ 上一元多项式的全体。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 多项式 $f(x)$ | 形式表达式，$x$ 是符号 |
| 多项式函数 $\hat{f}: K \to K$ | $\hat{f}(c) = a_n c^n + \cdots + a_0$，需具体代值 |
| 形式幂级数 | 允许无穷项 $\sum_{i \geq 0} a_i x^i$ |

在数域 $\mathbb{R}, \mathbb{C}$ 上，多项式与对应的多项式函数一一对应；
但在有限域上两者可不同（如 $\mathbb{F}_2$ 上 $x^2 + x$ 与 $0$ 函数相同但**不是**同一多项式）。

## 直觉理解

把多项式想成"$x$ 的不同次数权重摆在一起的有限组合"。
**形式表达 ≠ 函数**：$f(x)$ 是符号串，承载系数信息；$\hat f$ 是赋值后的输出。
本课程**多数情形**把它们当作等价（通过 $K = \mathbb{Q}, \mathbb{R}, \mathbb{C}$ 中的同一性），
但讨论"系数本身"时（如带余除法、整除性），必须把多项式视为**形式对象**。

## 链接

- 用于定义：[[ALG-DEF-002]] 多项式的整除关系
- 用于定理：[[ALG-THM-001]] 带余除法、[[ALG-THM-002]] 唯一分解定理
