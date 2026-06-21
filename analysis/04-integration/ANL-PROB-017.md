---
title: "积分不等式：Cauchy–Schwarz、Hölder 与 Minkowski"
type: problem
id: ANL-PROB-017
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 不等式
  - Cauchy-Schwarz
  - Hölder
depends:
  - ANL-THM-029
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §9.4 习题（综合改编）"
difficulty: 4
tests:
  - ANL-THM-029
  - ANL-DEF-026
related:
  - ANL-THM-030
  - ANL-PROB-014
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

设 $f, g$ 在 $[a,b]$ 上连续（故可积，[[ANL-DEF-026]]）。

1. **Cauchy–Schwarz 积分不等式**：证明
    $$
    \left( \int_a^b f(x)g(x)\,dx \right)^2 \le \left( \int_a^b f(x)^2\,dx \right)\left( \int_a^b g(x)^2\,dx \right),
    $$
    并指出等号成立的充要条件。

2. **Young 不等式**：设 $p, q > 1$ 满足 $\dfrac{1}{p} + \dfrac{1}{q} = 1$。证明对任意 $A, B \ge 0$，
    $$
    AB \le \frac{A^p}{p} + \frac{B^q}{q}.
    $$

3. **Hölder 积分不等式**：用第 2 题证明
    $$
    \int_a^b |f(x)g(x)|\,dx \le \left( \int_a^b |f(x)|^p\,dx \right)^{1/p}\left( \int_a^b |g(x)|^q\,dx \right)^{1/q}.
    $$
    （$p = q = 2$ 即第 1 题的绝对值形式。）

4. **Minkowski 积分不等式**：由 Hölder 推出，对 $p \ge 1$，
    $$
    \left( \int_a^b |f+g|^p\,dx \right)^{1/p} \le \left( \int_a^b |f|^p\,dx \right)^{1/p} + \left( \int_a^b |g|^p\,dx \right)^{1/p}.
    $$

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**（判别式法）：对任意 $t\in\mathbb{R}$，$\int_a^b (f + t g)^2\,dx \ge 0$。展开成关于 $t$ 的二次三项式 $At^2 + 2Bt + C$，由非负得判别式 $\le 0$。用到积分的线性性与非负性（[[ANL-THM-029]]）。
- **第 2 题**：固定 $B$，对 $\varphi(A) = \frac{A^p}{p} + \frac{B^q}{q} - AB$ 求极小；或用 $\ln$ 的凹性（[[ANL-PROB-014]] 思路）。
- **第 3 题**：先归一化。设 $\|f\|_p := (\int|f|^p)^{1/p}>0,\ \|g\|_q>0$，令 $A = \frac{|f(x)|}{\|f\|_p},\ B = \frac{|g(x)|}{\|g\|_q}$ 代入 Young 后两边积分。
- **第 4 题**：$|f+g|^p = |f+g|\cdot|f+g|^{p-1} \le (|f|+|g|)|f+g|^{p-1}$，对两项分别用 Hölder（注意 $(p-1)q = p$）。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题：Cauchy–Schwarz

记 $A = \int_a^b f^2,\ B = \int_a^b fg,\ C = \int_a^b g^2$。对任意 $t\in\mathbb{R}$，被积函数 $(f+tg)^2 \ge 0$，由积分的**单调性/非负性**（[[ANL-THM-029]]）：
$$
0 \le \int_a^b (f + tg)^2\,dx = t^2\!\int_a^b g^2 + 2t\!\int_a^b fg + \int_a^b f^2 = C\,t^2 + 2B\,t + A,
$$
这里用了**线性性**（[[ANL-THM-029]]）展开。

**情形 $C = 0$**：$g^2$ 连续非负且积分为 $0$ $\Rightarrow$ $g\equiv 0$，则 $B=0$，不等式两边均为 $0$，成立。

**情形 $C > 0$**：上式是关于 $t$ 的、首项系数为正的二次三项式，恒 $\ge 0$，故判别式
$$
(2B)^2 - 4CA \le 0 \;\Longrightarrow\; B^2 \le AC,
$$
即 $\left(\int_a^b fg\right)^2 \le \left(\int_a^b f^2\right)\left(\int_a^b g^2\right)$。$\quad\blacksquare$

**等号条件**：$B^2 = AC$ $\iff$ 判别式 $=0$ $\iff$ 存在 $t_0$ 使 $\int_a^b (f + t_0 g)^2 = 0$ $\iff$（连续函数）$f + t_0 g \equiv 0$，即 **$f, g$ 线性相关**（或 $g\equiv 0$）。

### 第 2 题：Young 不等式

$A=0$ 或 $B=0$ 时显然。设 $A, B > 0$。由 $\ln$ 在 $(0,\infty)$ 上**严格凹**（$(\ln)'' = -1/x^2 < 0$），对权重 $\frac1p + \frac1q = 1$：
$$
\ln\!\left( \frac{1}{p}A^p + \frac{1}{q}B^q \right) \ge \frac{1}{p}\ln(A^p) + \frac{1}{q}\ln(B^q) = \ln A + \ln B = \ln(AB).
$$
$\ln$ 单调增，故 $\dfrac{A^p}{p} + \dfrac{B^q}{q} \ge AB$。$\quad\blacksquare$

> 等号 $\iff A^p = B^q$。此处凹性论证与 [[ANL-PROB-014]] 的 Jensen 框架同源。

### 第 3 题：Hölder

记 $\|f\|_p = \left(\int_a^b |f|^p\right)^{1/p},\ \|g\|_q = \left(\int_a^b |g|^q\right)^{1/q}$。

**退化情形**：若 $\|f\|_p = 0$，则 $|f|^p$ 连续非负且积分为 $0$ $\Rightarrow f\equiv 0$，左边 $=0$，成立；$\|g\|_q=0$ 同理。

**主情形** $\|f\|_p, \|g\|_q > 0$：对每个 $x$，取 $A = \dfrac{|f(x)|}{\|f\|_p},\ B = \dfrac{|g(x)|}{\|g\|_q}$，由 Young（第 2 题）：
$$
\frac{|f(x)g(x)|}{\|f\|_p\,\|g\|_q} \le \frac{1}{p}\frac{|f(x)|^p}{\|f\|_p^p} + \frac{1}{q}\frac{|g(x)|^q}{\|g\|_q^q}.
$$
两边在 $[a,b]$ 上积分，用线性性（[[ANL-THM-029]]）：
$$
\frac{\int_a^b |fg|}{\|f\|_p\,\|g\|_q} \le \frac{1}{p}\cdot\frac{\|f\|_p^p}{\|f\|_p^p} + \frac{1}{q}\cdot\frac{\|g\|_q^q}{\|g\|_q^q} = \frac{1}{p} + \frac{1}{q} = 1.
$$
即 $\int_a^b |fg| \le \|f\|_p\,\|g\|_q$。$\quad\blacksquare$

### 第 4 题：Minkowski

$p = 1$ 时由 $|f+g|\le |f|+|g|$ 与单调性直接得证。设 $p>1$，取 $q = \dfrac{p}{p-1}$（则 $\frac1p+\frac1q=1$ 且 $(p-1)q = p$）。

若 $\int|f+g|^p = 0$ 则平凡。否则：
$$
\int_a^b |f+g|^p = \int_a^b |f+g|\,|f+g|^{p-1} \le \int_a^b |f|\,|f+g|^{p-1} + \int_a^b |g|\,|f+g|^{p-1}.
$$

对右边两项各用 Hölder（指数 $p, q$），并注意 $\big(|f+g|^{p-1}\big)^q = |f+g|^p$：
$$
\int_a^b |f|\,|f+g|^{p-1} \le \|f\|_p \left(\int_a^b |f+g|^p\right)^{1/q},
$$
$g$ 项同理。相加：
$$
\int_a^b |f+g|^p \le \big(\|f\|_p + \|g\|_p\big)\left(\int_a^b |f+g|^p\right)^{1/q}.
$$

两边除以 $\left(\int|f+g|^p\right)^{1/q}$（正），并用 $1 - \frac1q = \frac1p$：
$$
\left(\int_a^b |f+g|^p\right)^{1/p} \le \|f\|_p + \|g\|_p. \quad\blacksquare
$$

</details>

## 考察点

- [[ANL-THM-029]] 积分线性性与单调性（非负性）——所有积分不等式的两块基石
- 判别式法（二次型非负 ⇒ 判别式 $\le 0$）证 Cauchy–Schwarz
- 凹性 / Young 不等式作为 Hölder 的逐点引擎
- 归一化技巧（除以范数）将逐点估计提升为积分估计
- "连续非负且积分为零 ⇒ 恒为零"在等号 / 退化情形中的反复使用

## 备注

**三大不等式的逻辑链**：
$$
\text{凹性/Young} \;\Rightarrow\; \text{Hölder} \;\Rightarrow\; \text{Minkowski},\qquad \text{Cauchy–Schwarz} = \text{Hölder}|_{p=q=2}.
$$

**与离散版的对偶**：把积分换成有限和、把连续函数换成向量，立刻得到向量内积的 Cauchy–Schwarz、$\ell^p$ 序列的 Hölder/Minkowski。Minkowski 不等式正是 $L^p[a,b]$ 与 $\ell^p$ 成为**赋范空间**（三角不等式）的根据，是泛函分析的入口。

**应用**：

- 概率论：$|\mathbb{E}[XY]| \le \sqrt{\mathbb{E}[X^2]\mathbb{E}[Y^2]}$（相关系数 $|\rho|\le 1$）。
- 信号处理：能量有限信号空间 $L^2$ 的内积结构（[[ANL-THM-030]] 配合可得均值估计）。
