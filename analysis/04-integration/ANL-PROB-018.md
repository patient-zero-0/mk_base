---
title: "积分中值定理的应用：估值、极限与不等式"
type: problem
id: ANL-PROB-018
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 积分中值定理
  - 极限
  - 估值
depends:
  - ANL-THM-030
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §9.4 习题（综合改编）"
difficulty: 3
tests:
  - ANL-THM-030
related:
  - ANL-THM-013
  - ANL-THM-029
  - ANL-THM-031
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

1. **存在性应用**：设 $f$ 在 $[a,b]$ 上连续。证明存在 $\xi \in [a,b]$ 使
    $$
    \int_a^b f(x)\,dx = f(\xi)(b - a),
    $$
    并说明为何这里 $\xi$ 可取到**开区间** $(a,b)$ 内（当 $f$ 不为常数时）。

2. **极限计算**：求
    $$
    \lim_{n\to\infty} \int_0^1 \frac{x^n}{1 + x}\,dx.
    $$

3. **加权中值定理**：设 $f$ 连续、$g$ 在 $[a,b]$ 上可积且**不变号**（$g \ge 0$）。证明存在 $\xi\in[a,b]$ 使
    $$
    \int_a^b f(x)g(x)\,dx = f(\xi)\int_a^b g(x)\,dx.
    $$

4. **第二中值定理应用**：设 $f$ 在 $[a,b]$ 上单调，$g$ 可积。利用积分第二中值定理证明：若 $\left|\int_a^x g\right| \le M$ 对一切 $x\in[a,b]$，则
    $$
    \left| \int_a^b f(x)g(x)\,dx \right| \le M\big(|f(a)| + 2|f(b)|\big).
    $$

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：连续函数取到最值 $m, M$，由单调性 $m(b-a)\le \int_a^b f\le M(b-a)$，再用介值定理（[[ANL-THM-013]]）。开区间结论：若 $\xi$ 只能取端点会迫使 $f$ 恒等于平均值。
- **第 2 题**：用加权中值定理（第 3 题，取 $g = x^n \ge 0$）写出 $\int_0^1 \frac{x^n}{1+x}dx = \frac{1}{1+\xi_n}\cdot\frac{1}{n+1}$，再夹逼。或直接估 $0\le \int \le \int_0^1 x^n dx = \frac{1}{n+1}$。
- **第 3 题**：与第 1 题同法，利用 $m\,g \le fg \le M\,g$（$g\ge0$ 是关键）后积分，再用介值定理。
- **第 4 题**：积分第二中值定理（[[ANL-THM-030]] 推广形）：$f$ 单调时 $\int_a^b fg = f(a)\int_a^\eta g + f(b)\int_\eta^b g$。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题：积分第一中值定理

$f$ 在闭区间 $[a,b]$ 上连续，故取到最小值 $m$ 与最大值 $M$（最值定理）。由积分**单调性**（[[ANL-THM-029]]），对 $m \le f(x) \le M$ 积分：
$$
m(b-a) \le \int_a^b f(x)\,dx \le M(b-a),
$$
即平均值 $\mu := \dfrac{1}{b-a}\int_a^b f \in [m, M]$。由**介值定理**（[[ANL-THM-013]]），存在 $\xi\in[a,b]$ 使 $f(\xi) = \mu$，即 $\int_a^b f = f(\xi)(b-a)$。$\quad\blacksquare$

**开区间论断**：若 $f$ 非常数，设 $f$ 在 $x_1$ 取 $m$、$x_2$ 取 $M$ 且 $m<M$。则 $\mu\in[m,M]$。

- 若 $m < \mu < M$：由介值定理 $f=\mu$ 的点必在 $x_1,x_2$ 之间，属 $(a,b)$。
- 若 $\mu = m$：则 $\int_a^b (f - m) = 0$，而 $f - m \ge 0$ 连续 $\Rightarrow f\equiv m$，与非常数矛盾；$\mu = M$ 同理排除。

故 $\mu\in(m,M)$，$\xi$ 可取在 $(a,b)$ 内。

### 第 2 题：极限计算

被积函数在 $[0,1]$ 上满足 $0 \le \dfrac{x^n}{1+x} \le x^n$（因 $1+x\ge 1$）。由单调性（[[ANL-THM-029]]）：
$$
0 \le \int_0^1 \frac{x^n}{1+x}\,dx \le \int_0^1 x^n\,dx = \frac{1}{n+1} \xrightarrow{n\to\infty} 0.
$$
由夹逼，$\displaystyle\lim_{n\to\infty}\int_0^1 \frac{x^n}{1+x}\,dx = 0$。$\quad\blacksquare$

> **加权中值定理视角**（第 3 题）：取 $f(x)=\frac{1}{1+x}$（连续），$g(x)=x^n\ge 0$，则存在 $\xi_n\in[0,1]$ 使
> $$\int_0^1 \frac{x^n}{1+x}\,dx = \frac{1}{1+\xi_n}\int_0^1 x^n\,dx = \frac{1}{1+\xi_n}\cdot\frac{1}{n+1}.$$
> 由 $\frac{1}{1+\xi_n}\in[\frac12,1]$ 有界，整体 $\to 0$，结论一致。

### 第 3 题：加权（推广）第一中值定理

$f$ 连续，取最值 $m, M$。因 $g \ge 0$，有 $m\,g(x) \le f(x)g(x) \le M\,g(x)$。积分（[[ANL-THM-029]]）：
$$
m\int_a^b g \le \int_a^b fg \le M\int_a^b g.
$$

**情形 $\int_a^b g = 0$**：上式夹出 $\int_a^b fg = 0$，任取 $\xi$ 等式成立。

**情形 $\int_a^b g > 0$**：令 $\mu = \dfrac{\int_a^b fg}{\int_a^b g}\in[m,M]$，由介值定理（[[ANL-THM-013]]）存在 $\xi$ 使 $f(\xi)=\mu$，即得证。$\quad\blacksquare$

### 第 4 题：积分第二中值定理应用

由积分第二中值定理（[[ANL-THM-030]]，$f$ 单调形式）：存在 $\eta\in[a,b]$ 使
$$
\int_a^b f(x)g(x)\,dx = f(a)\int_a^{\eta} g(x)\,dx + f(b)\int_{\eta}^{b} g(x)\,dx.
$$

记 $G(x) = \int_a^x g$，则 $\int_a^\eta g = G(\eta)$，$\int_\eta^b g = G(b) - G(\eta)$，且 $|G(x)|\le M$。于是
$$
\left|\int_a^b fg\right| \le |f(a)|\,|G(\eta)| + |f(b)|\,|G(b) - G(\eta)| \le |f(a)|M + |f(b)|\big(|G(b)| + |G(\eta)|\big).
$$

由 $|G(b)|\le M,\ |G(\eta)|\le M$：
$$
\left|\int_a^b fg\right| \le |f(a)|M + |f(b)|(M + M) = M\big(|f(a)| + 2|f(b)|\big). \quad\blacksquare
$$

</details>

## 考察点

- [[ANL-THM-030]] 积分第一中值定理（含加权形）与第二中值定理
- [[ANL-THM-013]] 介值定理——把"平均值落在 $[m,M]$"翻译成"被某点取到"
- [[ANL-THM-029]] 积分单调性是所有估值的出发点
- 夹逼法求含参积分极限
- "连续非负且积分为零 ⇒ 恒为零"导出严格开区间结论

## 备注

**第一中值定理的几何意义**：曲线 $y=f(x)$ 下方面积 $\int_a^b f$ 等于以 $f(\xi)$ 为高、$(b-a)$ 为底的矩形面积——存在某高度的矩形与曲边梯形等面积。

**第二中值定理的威力**：它是反常积分 Abel/Dirichlet 判别法（[[ANL-THM-035]]）的核心引擎——把"被积函数 $\times$ 单调因子"的积分用端点值 + 部分积分上界控制住，正是第 4 题不等式的来源。
