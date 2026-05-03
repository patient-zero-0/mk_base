---
title: "复合函数极限：换元与连续性的合法应用"
type: example
id: ANL-EX-005
subject: analysis
chapter: 02-continuity
tags:
  - 函数极限
  - 复合函数
  - 变量代换
  - 例题
depends:
  - ANL-THM-011
  - ANL-DEF-008
  - ANL-DEF-012
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §3.2"
difficulty: 3
illustrates:
  - ANL-THM-011
related:
  - ANL-THM-009
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

利用 [[ANL-THM-011]] 复合函数极限定理，求下列极限或判断其合法性：

1. $\displaystyle \lim_{x \to 0} \frac{\sin(2x)}{2x}$（已知 $\lim_{u \to 0} \frac{\sin u}{u} = 1$）。

2. $\displaystyle \lim_{x \to 0} \frac{\sin(x^2)}{x^2}$。

3. **判断合法性**：以下"换元法"是否正确？
   $$
   \lim_{x \to 0} f(g(x)) \stackrel{?}{=} \lim_{u \to 0} f(u),
   $$
   其中 $g(x) = 0$ 恒等于 $0$，$f(u) = \begin{cases} 1 & u \neq 0 \\ 5 & u = 0 \end{cases}$。

## 分析

> **第 1、2 题**：标准的"换元 + 已知极限"应用。
> 关键是验证 [[ANL-THM-011]] 的条件 (a) 或 (b)。
>
> - 第 1 题：$g(x) = 2x$，当 $x \to 0$ 时 $g(x) \to 0$，**且** $g(x) \neq 0$ 在 $x \neq 0$ 时恒成立——条件 (b) 满足。
> - 第 2 题：$g(x) = x^2$，同理 $g(x) \to 0$ 且 $g(x) \neq 0$（$x \neq 0$ 时）——条件 (b) 满足。
>
> **第 3 题**：检验换元法的边界情形——这是 [[ANL-THM-011]] 设计条件 (a)/(b) 要排除的反例。

## 证明 / 解答

### 第 1 题

**解：** 令 $u = g(x) = 2x$。

- 当 $x \to 0$ 时 $u \to 0$。
- $u = 2x \neq 0$ 当 $x \neq 0$（条件 (b) 满足）。
- 已知 $\lim_{u \to 0} \frac{\sin u}{u} = 1$。

由 [[ANL-THM-011]]：
$$
\lim_{x \to 0} \frac{\sin(2x)}{2x} = \lim_{u \to 0} \frac{\sin u}{u} = 1.
$$
$\blacksquare$

### 第 2 题

**解：** 令 $u = g(x) = x^2$。

- 当 $x \to 0$ 时 $u \to 0^+$（注意 $x^2 \geq 0$，从右侧逼近）。
- $u = x^2 \neq 0$ 当 $x \neq 0$（条件 (b) 满足）。

由 [[ANL-THM-011]]：
$$
\lim_{x \to 0} \frac{\sin(x^2)}{x^2} = \lim_{u \to 0^+} \frac{\sin u}{u} = 1.
$$
（由于 $\sin u/u$ 在 $u = 0$ 附近双侧极限都为 $1$，单侧 $u \to 0^+$ 同值。）
$\blacksquare$

### 第 3 题

**解：判断不合法**。

验证 [[ANL-THM-011]] 条件：

- 条件 1：$\lim_{x \to 0} g(x) = 0$，成立（$g$ 恒为 $0$）。
- 条件 2：$\lim_{u \to 0} f(u) = 1$，成立（$u \neq 0$ 时 $f(u) = 1$）。
- 条件 (a)：$f$ 在 $u_0 = 0$ 是否连续？$f(0) = 5 \neq 1 = \lim_{u \to 0} f(u)$，**不连续**。
- 条件 (b)：是否在 $x_0 = 0$ 的某去心邻域内 $g(x) \neq 0$？$g \equiv 0$，**永不成立**。

**两个条件都不满足** ⇒ 不能直接套换元法。

**实际计算**：$f(g(x)) = f(0) = 5$ 恒成立，故 $\lim_{x \to 0} f(g(x)) = 5$。
而 $\lim_{u \to 0} f(u) = 1$。

显然 $5 \neq 1$——这正是 [[ANL-THM-011]] 用条件 (a)/(b) 排除的"病态"换元情形。

**$\blacksquare$**

## 关键技巧

- **换元前必查 (a)/(b)**：条件 (a) 是 $f$ 在 $u_0$ 处**连续**；条件 (b) 是 $g$ 在 $x_0$ 去心邻域内**不取 $u_0$**。绝大多数初等问题中 (a) 成立（如 $\sin, \cos, e^x, \ln$ 处处连续），可"无脑"换元。
- **第 3 题型常见于人为构造的 piecewise 函数**：实际计算中遇到这类函数（如 $f(0)$ 单独定义为异常值）就要小心。
- **复合极限 ≠ 极限值的复合**：本节核心警告——复合函数的极限与"先求内函数极限再代入"**不总是**相等。

## 变式

- **变式 1**：求 $\displaystyle \lim_{x \to 1} \frac{\sin(\pi x)}{x - 1}$（提示：换元 $u = x - 1$，$\sin(\pi x) = \sin(\pi + \pi u) = -\sin(\pi u)$）。
- **变式 2**：求 $\displaystyle \lim_{x \to \infty} \left(1 + \frac{1}{x^2}\right)^{x^2}$（提示：换元 $u = x^2 \to \infty$，应用 $(1 + 1/u)^u \to e$）。
- **变式 3**：判断 $\lim_{x \to 0} f(g(x)) = \lim_{u \to 0} f(u)$ 在 $g(x) = x \sin(1/x), f(u) = u^2 / |u|$（$u \neq 0$）, $f(0) = 0$ 时是否合法？
