---
title: "有界数列"
type: definition
id: ANL-DEF-005
subject: analysis
chapter: 01-limits
tags:
  - 数列
  - 有界性
depends:
  - ANL-DEF-001
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §2.2"
difficulty: 1
related:
  - ANL-THM-006
  - ANL-AX-001
---

## 定义陈述

设 $\{a_n\}$ 是数列。

- **上有界**：$\exists M \in \mathbb{R}, \quad \forall n : \quad a_n \leq M$。
- **下有界**：$\exists m \in \mathbb{R}, \quad \forall n : \quad a_n \geq m$。
- **有界**：同时上有界与下有界，等价于 $\exists M > 0, \forall n: |a_n| \leq M$。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 有界 | 全体项被同一常数夹住 |
| 收敛 [[ANL-DEF-004]] | 严格更强：必有界，且项趋于固定值 |
| 局部有界 | 仅在某段下标内有界，整体不必 |

## 直觉理解

把数列想象成被关在围栏里的一群点：**有界**=围栏存在；**收敛**=所有点最终都聚在围栏内某一处。
有界是收敛的**必要非充分**条件——不收敛但有界的最小例子就是 $a_n = (-1)^n$，永远在 $\pm 1$ 间跳跃。

## 链接

- 用于定理：[[ANL-THM-006]] 单调有界定理
- 等价描述借助：[[ANL-AX-001]] 确界原理
