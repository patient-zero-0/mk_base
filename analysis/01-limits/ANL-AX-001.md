---
title: "确界原理"
type: definition
id: ANL-AX-001
subject: analysis
chapter: 01-limits
tags:
  - 实数完备性
  - 公理
depends: []
uses: []
status: review
source: "华东师范大学《数学分析》第5版 §1.5"
difficulty: 2
related:
  - ANL-THM-006
  - ANL-THM-007
applications:
  - "数值分析：定义浮点系统的极限行为"
  - "经济学：单调有界效用序列的存在性论证"
---

## 定义陈述

> **确界原理**是 $\mathbb{R}$ 的基本性质，可作为公理引入，亦可由戴德金分割等价导出。

设 $S \subseteq \mathbb{R}$ 非空。

- 若 $S$ 有上界，则 $S$ 在 $\mathbb{R}$ 中存在**最小上界**，记作 $\sup S$。
- 若 $S$ 有下界，则 $S$ 在 $\mathbb{R}$ 中存在**最大下界**，记作 $\inf S$。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 最大值 $\max S$ | 必须 $\in S$ |
| 上确界 $\sup S$ | 不必属于 $S$，但任何更小的数都不再是上界 |
| 上界 | 不要求最小，只要 $\geq S$ 中所有元素即可 |

## 直觉理解

$\mathbb{R}$ 像一根没有缝隙的连续直线：任何能"被某根杆挡住"的非空集合，都能找到一根**最贴近它的杆**。
对比 $\mathbb{Q}$：集合 $\{x \in \mathbb{Q} : x^2 < 2\}$ 在 $\mathbb{Q}$ 内有上界（如 $2$），但找不到最小的，因为最小上界 $\sqrt{2} \notin \mathbb{Q}$。
确界原理刻画的正是 $\mathbb{R}$ 比 $\mathbb{Q}$ "多出来的那些点"——即实数的**完备性**。

## 链接

- 用于定理：[[ANL-THM-006]]、[[ANL-THM-007]]
- 等价表述：闭区间套定理、Bolzano–Weierstrass 定理、Cauchy 收敛准则

## 跨专业应用

- **数值分析**：浮点序列的舍入累积存在确界，论证算法稳定性需用此性质
- **经济学**：序列效用 $u_n$ 单调上升且有"满意度上限"时，长期效用 $\sup u_n$ 存在
