---
title: "Cantor 定理（闭区间连续 ⇒ 一致连续）"
type: theorem
id: ANL-THM-015
subject: analysis
chapter: 02-continuity
tags:
  - 连续
  - 一致连续
  - 闭区间
depends:
  - ANL-DEF-012
  - ANL-DEF-024
  - ANL-DEF-004
  - ANL-DEF-006
uses:
  - ANL-THM-008
status: draft
source: "华东师范大学《数学分析》第5版 §4.2"
difficulty: 4
related:
  - ANL-THM-013
  - ANL-THM-014
  - ANL-PROB-031
applications:
  - "数值分析：闭区间上插值 / 数值积分的均匀误差估计"
  - "概率论：连续随机变量分布函数在紧支集上的均匀逼近"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $f : [a, b] \to \mathbb{R}$ 在**闭区间** $[a, b]$ 上**逐点连续**（按 [[ANL-DEF-012]]）。

## 结论

> $f$ 在 $[a, b]$ 上**一致连续**（按 [[ANL-DEF-024]]），即
> $$
> \forall \varepsilon > 0, \exists \delta > 0, \forall x_1, x_2 \in [a, b]:\ |x_1 - x_2| < \delta \implies |f(x_1) - f(x_2)| < \varepsilon.
> $$

## 几何/直觉理解

逐点连续 = "在每一点 $x_0$，$\delta$ 可视 $x_0$ 而定"——不同点可用不同 $\delta$。
一致连续 = "存在一个**全局** $\delta$，对所有点都管用"。

普通连续到一致连续的提升，需要"$\delta$ 不随 $x_0$ 退化到 0"。
**闭区间提供两个关键性质**：

1. **闭**：端点附近 $\delta$ 不会"逃跑"——$f(x) = 1/x$ 在 $(0, 1]$ 不一致连续，正因 $x \to 0^+$ 时 $\delta \to 0$。
2. **有界**：长度有限——$f(x) = x^2$ 在 $\mathbb{R}$ 不一致连续（局部斜率 $|f'(x)| = 2|x| \to \infty$）。

把这两点合起来，闭区间的"紧致性"将逐点信息**整合**为全局信息。

## 证明（用 Bolzano–Weierstrass，反证）

**证明：** 反证。设 $f$ 不一致连续。由 [[ANL-DEF-024]] 的反命题：
存在 $\varepsilon_0 > 0$，使**对每个 $n \in \mathbb{N}^*$**，存在 $x_n, y_n \in [a, b]$ 满足
$$
|x_n - y_n| < 1/n \quad \text{但} \quad |f(x_n) - f(y_n)| \geq \varepsilon_0.
$$

**第一步：抽取收敛子列。** $\{x_n\} \subseteq [a, b]$ 有界，由 [[ANL-THM-008]] Bolzano–Weierstrass 定理，
存在子列 $x_{n_k} \to x^* \in [a, b]$（闭区间含极限点）。

由 $|y_{n_k} - x_{n_k}| < 1/n_k \to 0$ 及 $x_{n_k} \to x^*$，得 $y_{n_k} \to x^*$。

**第二步：连续性导出矛盾。** $f$ 在 $x^*$ 连续。任给阈值 $\varepsilon_0 / 2 > 0$，
存在 $\delta > 0$ 使 $\forall x \in [a, b]: |x - x^*| < \delta \implies |f(x) - f(x^*)| < \varepsilon_0 / 2$。

由 $x_{n_k} \to x^*, y_{n_k} \to x^*$，存在 $K$ 使 $\forall k > K: |x_{n_k} - x^*| < \delta$ 且 $|y_{n_k} - x^*| < \delta$。
故 $|f(x_{n_k}) - f(x^*)| < \varepsilon_0 / 2$ 且 $|f(y_{n_k}) - f(x^*)| < \varepsilon_0 / 2$，
由三角不等式：
$$
|f(x_{n_k}) - f(y_{n_k})| \leq |f(x_{n_k}) - f(x^*)| + |f(x^*) - f(y_{n_k})| < \varepsilon_0.
$$

但构造时 $|f(x_{n_k}) - f(y_{n_k})| \geq \varepsilon_0$，矛盾。$\blacksquare$

## 常见错误

- ✗ 把"闭区间"换成"开区间"。
  反例：$f(x) = 1/x$ 在 $(0, 1]$ 连续但**不**一致连续（$x \to 0^+$ 时 $\delta \to 0$）。
- ✗ 把"有界区间"换成"无界区间"。
  反例：$f(x) = \sin(x^2)$ 在 $\mathbb{R}$ 上连续但不一致连续（详见 [[ANL-PROB-031]]），
  $f(x) = x^2$ 在 $\mathbb{R}$ 同理。
- ✗ 把结论错记为"连续 ⇒ 处处可微"。
  Cantor 定理只把"逐点连续"提升为"一致连续"，**不**蕴含可微。
  反例：$f(x) = |x|$ 在 $[-1, 1]$ 上一致连续但 $x = 0$ 不可微。

## 推论

- **闭区间上连续函数 = 一致连续 + 有界 + 取得最值**——三大性质（[[ANL-THM-014]]、[[ANL-THM-015]]）共同刻画"闭区间连续函数的紧致性"。
- **数值分析常用形式**：闭区间上连续函数可用阶梯 / 多项式**均匀逼近**至任意精度（Stone–Weierstrass 定理的初阶应用）。

## 链接

- 前置：[[ANL-DEF-012]]、[[ANL-DEF-024]]、[[ANL-DEF-004]]、[[ANL-DEF-006]]
- 关键工具：[[ANL-THM-008]] Bolzano–Weierstrass
- 反例 / 比较：[[ANL-PROB-031]]（在无界区间上反例）
- 推广：紧致拓扑空间上连续函数自动一致连续（拓扑学）

## 跨专业应用

- **数值分析**：闭区间上连续函数的**均匀逼近误差**可由 $\delta$ 一致控制——支撑插值、数值积分（如复化梯形公式）的误差估计
- **信号处理**：紧支集上的连续信号一致连续 → 采样间隔 $\delta$ 决定的失真上界对信号上各点一致成立
- **概率论**：紧支集上的连续随机变量分布函数 $F$ 一致连续 → Glivenko–Cantelli 类定理的基础
