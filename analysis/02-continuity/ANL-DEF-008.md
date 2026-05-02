---
title: "函数极限的 ε-δ 定义"
type: definition
id: ANL-DEF-008
subject: analysis
chapter: 02-continuity
tags:
  - 极限
  - ε-δ
  - 函数
depends: []
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §3.1"
difficulty: 2
related:
  - ANL-DEF-012
  - ANL-DEF-024
  - ANL-EX-007
---

## 定义陈述

设 $f$ 在 $x_0$ 的某去心邻域内有定义。称
$$
\lim_{x \to x_0} f(x) = L,
$$
若
$$
\forall \varepsilon > 0, \quad \exists \delta > 0, \quad \forall x : \quad 0 < |x - x_0| < \delta \implies |f(x) - L| < \varepsilon.
$$

注意条件 $0 < |x - x_0|$ 意味着**不要求 $f(x_0) = L$，甚至不要求 $f$ 在 $x_0$ 有定义**。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 函数极限 | 涉及 $x \to x_0$ 的趋向行为 |
| 数列极限 [[ANL-DEF-004]] | 离散的 $n \to \infty$ |
| 函数连续 [[ANL-DEF-012]] | 极限值等于 $f(x_0)$ 且 $f(x_0)$ 有定义 |

## 直觉理解

ε-δ 定义可看作"挑战—应战"的双人博弈：

1. **裁判（ε）出招**：给出 $y$ 轴方向的目标精度 $\varepsilon$。
2. **你（δ）应战**：在 $x$ 轴方向找一个开区间宽度 $\delta$，
   使得**该区间内除 $x_0$ 外**所有 $x$ 对应的 $f(x)$ 全部落入 $y$ 轴 $\varepsilon$-管中。
3. 任意 ε 都赢得了对应的 δ ⇔ 极限存在为 $L$。

量词顺序的关键：$\delta$ **依赖** $\varepsilon$（一般 ε 越小 δ 越小），但**不依赖具体的 $x$**。

## 常见错误

- ✗ 漏掉条件 $0 < |x - x_0|$，要求"$|x - x_0| < \delta \implies |f(x) - L| < \varepsilon$"。
  这隐含要求 $f(x_0) = L$，把"极限存在"误升级为"在 $x_0$ 处连续"。
- ✗ 认为 $\delta$ 只能依赖 $\varepsilon$ 不能依赖 $x_0$。
  事实上 $\delta = \delta(\varepsilon, x_0)$ 是允许的；要求 $\delta$ 仅依赖 $\varepsilon$ 是更强的"一致连续"条件 [[ANL-DEF-024]]。

## 链接

- 用于定义：[[ANL-DEF-012]] 函数连续、[[ANL-DEF-024]] 一致连续
- 用于例题：[[ANL-EX-007]]
