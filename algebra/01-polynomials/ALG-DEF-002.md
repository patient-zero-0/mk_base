---
title: "多项式的整除"
type: definition
id: ALG-DEF-002
subject: algebra
chapter: 01-polynomials
tags:
  - 多项式
  - 整除
depends:
  - ALG-DEF-001
uses: []
status: draft
source: "丘维声《高等代数》第3版 §1.2"
difficulty: 2
related:
  - ALG-THM-001
  - ALG-THM-002
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设 $f(x), g(x) \in K[x]$。称 $g(x)$ **整除** $f(x)$（记作 $g(x) \mid f(x)$），
若存在 $q(x) \in K[x]$ 使
$$
f(x) = g(x) \cdot q(x).
$$

此时也称 $g(x)$ 是 $f(x)$ 的**因式**，$f(x)$ 是 $g(x)$ 的**倍式**。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| $g \mid f$（整除） | 存在多项式商，余式 = 0 |
| $f / g$（带余除法） | 一般有非零余式 $r(x)$，$\deg r < \deg g$ |
| 公因式 | 同时整除两个或多个多项式 |

整除性**依赖底域** $K$：$x^2 + 1$ 在 $\mathbb{R}[x]$ 中不可分解，但在 $\mathbb{C}[x]$ 中 $= (x - i)(x + i)$。

## 直觉理解

整除性是"乘法可逆"的镜像——`g | f` 意味着"$f$ 是 $g$ 的整数倍"，没有余下零碎。
类比整数：$3 \mid 12$（12 = 3 × 4），$3 \nmid 13$（13 = 3 × 4 + 1，余 1）。
多项式整除完全平行：把"整数 → 多项式""带余除法的余数 → 余式"对应过来。

**关键差别**：整数有"绝对值最小"的自然次序；多项式以**次数**作为"大小"度量。
$\deg(fg) = \deg f + \deg g$ 是整除论证的核心工具。

## 基本性质

设 $f, g, h \in K[x]$：

- 反身性：$f \mid f$。
- 传递性：$f \mid g, g \mid h \implies f \mid h$。
- 线性组合：$f \mid g, f \mid h \implies f \mid (a g + b h)$ 对任意 $a, b \in K[x]$。
- 单位等价：$f \mid g$ 且 $g \mid f \iff f = c \cdot g$ 对某 $c \in K \setminus \{0\}$。

## 链接

- 前置：[[ALG-DEF-001]]
- 用于定理：[[ALG-THM-001]] 带余除法、[[ALG-THM-002]] 唯一分解定理
