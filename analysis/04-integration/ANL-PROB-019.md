---
title: "变限积分求导综合：链式法则、L'Hospital 与 Leibniz 公式"
type: problem
id: ANL-PROB-019
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 变限积分
  - 求导
  - L'Hospital
depends:
  - ANL-THM-031
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §9.5 习题（综合改编）"
difficulty: 3
tests:
  - ANL-THM-031
related:
  - ANL-THM-032
  - ANL-THM-024
  - ANL-THM-018
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

设 $f$ 连续，下列函数中 $u, v$ 均可导。

1. **复合上限**：求 $\dfrac{d}{dx}\displaystyle\int_a^{x^2} \sin(t^2)\,dt$。

2. **双变限一般公式**：证明
    $$
    \frac{d}{dx}\int_{u(x)}^{v(x)} f(t)\,dt = f\big(v(x)\big)v'(x) - f\big(u(x)\big)u'(x),
    $$
    并据此求 $\dfrac{d}{dx}\displaystyle\int_{x}^{x^2}\frac{dt}{\ln t}$（$x>1$）。

3. **L'Hospital 与变限积分**：求
    $$
    \lim_{x\to 0} \frac{\displaystyle\int_0^x \sin(t^2)\,dt}{x^3}.
    $$

4. **被积函数含参（Leibniz 规则）**：设 $f$ 连续，定义 $\displaystyle F(x) = \int_0^x (x - t)\,f(t)\,dt$。证明 $F$ 二阶可导且 $F''(x) = f(x)$，$F(0) = F'(0) = 0$。

## 提示

<details><summary>点击展开提示</summary>

- **第 1 题**：记 $\Phi(y)=\int_a^y \sin(t^2)dt$，由变限积分可微性（[[ANL-THM-031]]）$\Phi'(y)=\sin(y^2)$，再用链式法则（[[ANL-THM-018]]）$\frac{d}{dx}\Phi(x^2)$。
- **第 2 题**：拆 $\int_{u}^{v} = \int_{c}^{v} - \int_{c}^{u}$，各用第 1 题方法。
- **第 3 题**：分子分母 $\to 0$，用 L'Hospital（[[ANL-THM-024]]）；分子求导用 [[ANL-THM-031]]，再用等价无穷小 $\sin(x^2)\sim x^2$。
- **第 4 题**：先把 $F(x)=x\int_0^x f(t)dt - \int_0^x t f(t)dt$ 拆开（$x$ 提出积分号外），再逐项求导（乘积法则 + [[ANL-THM-031]]）。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题：复合上限

设 $\Phi(y) = \displaystyle\int_a^y \sin(t^2)\,dt$。因 $\sin(t^2)$ 连续，由变限积分可微性（[[ANL-THM-031]]）$\Phi'(y) = \sin(y^2)$。所求为 $\dfrac{d}{dx}\Phi(x^2)$，由链式法则（[[ANL-THM-018]]）：
$$
\frac{d}{dx}\int_a^{x^2} \sin(t^2)\,dt = \Phi'(x^2)\cdot (x^2)' = \sin(x^4)\cdot 2x = 2x\sin(x^4). \quad\blacksquare
$$

### 第 2 题：双变限公式

取任一常数 $c$ 落在积分区间内。由区间可加性
$$
\int_{u(x)}^{v(x)} f = \int_{c}^{v(x)} f - \int_{c}^{u(x)} f.
$$
对每项用第 1 题方法（[[ANL-THM-031]] + 链式法则 [[ANL-THM-018]]）：
$$
\frac{d}{dx}\int_{c}^{v(x)} f = f(v(x))v'(x), \qquad \frac{d}{dx}\int_{c}^{u(x)} f = f(u(x))u'(x).
$$
相减即得
$$
\frac{d}{dx}\int_{u(x)}^{v(x)} f(t)\,dt = f(v(x))v'(x) - f(u(x))u'(x). \quad\blacksquare
$$

**应用**：$\displaystyle\int_{x}^{x^2}\frac{dt}{\ln t}$，$f(t)=\frac{1}{\ln t}$，$u=x,\ v=x^2$：
$$
\frac{d}{dx}\int_{x}^{x^2}\frac{dt}{\ln t} = \frac{1}{\ln(x^2)}\cdot 2x - \frac{1}{\ln x}\cdot 1 = \frac{2x}{2\ln x} - \frac{1}{\ln x} = \frac{x - 1}{\ln x}.
$$

### 第 3 题：L'Hospital 与变限积分

当 $x\to 0$，分子 $\int_0^x \sin(t^2)dt \to 0$，分母 $x^3\to 0$，为 $\frac00$ 型。由 L'Hospital（[[ANL-THM-024]]），分子求导用 [[ANL-THM-031]]：
$$
\lim_{x\to 0}\frac{\int_0^x \sin(t^2)\,dt}{x^3}
\overset{\text{L'H}}{=} \lim_{x\to 0}\frac{\sin(x^2)}{3x^2}.
$$
由等价无穷小 $\sin(x^2)\sim x^2$（$x\to 0$）：
$$
= \lim_{x\to 0}\frac{x^2}{3x^2} = \frac{1}{3}. \quad\blacksquare
$$

### 第 4 题：被积函数含参（Leibniz 规则）

把 $x$ 从积分号内提出（积分对 $t$ 进行，$x$ 视作常数）：
$$
F(x) = \int_0^x (x - t)f(t)\,dt = x\underbrace{\int_0^x f(t)\,dt}_{=:G(x)} - \underbrace{\int_0^x t f(t)\,dt}_{=:H(x)}.
$$

$f$ 连续 $\Rightarrow$ $tf(t)$ 连续，由变限积分可微性（[[ANL-THM-031]]）：$G'(x) = f(x),\ H'(x) = x f(x)$。

**一阶导**（乘积法则）：
$$
F'(x) = \big(1\cdot G(x) + x\,G'(x)\big) - H'(x) = G(x) + x f(x) - x f(x) = G(x) = \int_0^x f(t)\,dt.
$$

**二阶导**：再用 [[ANL-THM-031]]：
$$
F''(x) = G'(x) = f(x).
$$

**初值**：$F(0) = \int_0^0 (0-t)f(t)\,dt = 0$，$F'(0) = G(0) = \int_0^0 f = 0$。$\quad\blacksquare$

> 这说明 $F$ 是满足 $y'' = f,\ y(0)=y'(0)=0$ 的解——把二阶 ODE 的初值问题用"二重积分核 $(x-t)$"一次性写出，即 **Duhamel/Cauchy 公式**的一维特例。

</details>

## 考察点

- [[ANL-THM-031]] 变限积分函数的可微性 $\frac{d}{dx}\int_a^x f = f(x)$
- [[ANL-THM-018]] 链式法则处理复合上下限
- [[ANL-THM-024]] L'Hospital 法则与变限积分配合求极限
- 被积函数含参时"先把参数提出积分号"再用乘积法则（Leibniz 规则的初等版）
- 等价无穷小在最终极限化简中的使用

## 备注

**三类变限积分求导小结**：

| 形式 | 导数 |
|---|---|
| $\dfrac{d}{dx}\int_a^x f(t)\,dt$ | $f(x)$（[[ANL-THM-031]]） |
| $\dfrac{d}{dx}\int_{u(x)}^{v(x)} f(t)\,dt$ | $f(v)v' - f(u)u'$（本题第 2） |
| $\dfrac{d}{dx}\int_{u(x)}^{v(x)} f(x,t)\,dt$ | $\int_u^v \partial_x f\,dt + f(x,v)v' - f(x,u)u'$（一般 Leibniz，多元） |

第三行的一般 Leibniz 规则需偏导（多元微积分），本题第 4 题是其"被积函数关于 $x$ 线性、可手工提出"的初等特例。变限积分求导是连接**微分与积分**的枢纽——它正是 Newton–Leibniz 公式（[[ANL-THM-032]]）成立的微观机制。
