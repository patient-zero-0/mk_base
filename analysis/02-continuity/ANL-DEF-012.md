---
title: "函数连续"
type: definition
id: ANL-DEF-012
subject: analysis
chapter: 02-continuity
tags:
  - 连续
  - ε-δ
  - 函数
depends:
  - ANL-DEF-008
uses: []
status: review
source: "华东师范大学《数学分析》第5版 §3.3"
difficulty: 2
related:
  - ANL-DEF-024
---

## 定义陈述

设 $f$ 在 $x_0$ 的某邻域（含 $x_0$）内有定义。

**$f$ 在 $x_0$ 连续**，若 $\displaystyle \lim_{x \to x_0} f(x) = f(x_0)$，等价地：

$$
\forall \varepsilon > 0, \quad \exists \delta > 0, \quad \forall x : \quad |x - x_0| < \delta \implies |f(x) - f(x_0)| < \varepsilon.
$$

**$f$ 在区间 $I$ 上连续**，若 $f$ 在 $I$ 的每一点都连续。

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 极限存在 [[ANL-DEF-008]] | 不要求 $f(x_0)$ 有定义，也不要求等于 $L$ |
| 在 $x_0$ 连续 | $f(x_0)$ 有定义且等于极限值 |
| 一致连续 [[ANL-DEF-024]] | $\delta$ 对区间所有点共用 |

## 直觉理解

连续 = "**$f(x_0)$ 等于极限值**"。
图像上看：函数图在 $x_0$ 处不"跳跃"、不"破洞"、不"无定义"。
注意此处条件已是 $|x - x_0| < \delta$（不再是 $0 < |x - x_0|$）——$x = x_0$ 这一点
也参与论证，而 $|f(x_0) - f(x_0)| = 0 < \varepsilon$ 自动成立，故等价。

## 常见错误

- ✗ 把"$f$ 在 $[a,b]$ 上连续"理解为"$\delta$ 只依赖 $\varepsilon$"。
  这其实是更强的**一致连续**条件 [[ANL-DEF-024]]，在闭区间上两者等价（Cantor 定理），
  但在开区间或无界区间上可分离——典型反例 $f(x) = 1/x$ 在 $(0, 1)$ 上连续但非一致连续。

## 链接

- 前置：[[ANL-DEF-008]] 函数极限的 ε-δ 定义
- 升级版本：[[ANL-DEF-024]] 一致连续
