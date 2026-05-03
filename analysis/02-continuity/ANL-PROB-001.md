---
title: "判定与构造间断点"
type: problem
id: ANL-PROB-001
subject: analysis
chapter: 02-continuity
tags:
  - 间断点
  - 单侧极限
  - 反例构造
depends:
  - ANL-DEF-011
  - ANL-DEF-013
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §3.3 习题"
difficulty: 3
tests:
  - ANL-DEF-013
  - ANL-DEF-011
related:
  - ANL-DEF-024
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

判断或构造下列函数的间断点类型：

1. $f(x) = \dfrac{x^2 - 1}{x - 1}$，定义域 $\mathbb{R} \setminus \{1\}$。指出 $x_0 = 1$ 的间断类型。

2. $g(x) = \begin{cases} x^2 & x < 0 \\ 1 & x = 0 \\ x + 1 & x > 0 \end{cases}$。指出 $x_0 = 0$ 的间断类型。

3. $h(x) = \dfrac{1}{x^2 - 4}$。找出所有间断点并分类。

4. **构造**：给出一个函数 $\phi : \mathbb{R} \to \mathbb{R}$，使其在 $x_0 = 0$ 处发生**振荡间断**，且 $\phi$ 在其他点处处连续。

## 提示

<details><summary>点击展开提示</summary>

- 第 1 题：$x^2 - 1 = (x - 1)(x + 1)$，约分。
- 第 2 题：分别求 $g(0^-)$ 和 $g(0^+)$，对比 $g(0)$。
- 第 3 题：分母 $x^2 - 4 = (x-2)(x+2)$。
- 第 4 题：经典构造形如 $\phi(x) = \sin(1/x)$（$x \neq 0$），$\phi(0) := 0$；
  其他点连续性由复合函数连续性保证。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题

$f(x) = \dfrac{x^2 - 1}{x - 1} = x + 1$（$x \neq 1$）。

$f(1^-) = f(1^+) = 1 + 1 = 2$，但 $f(1)$ **未定义**。

⇒ **可去间断点**（重新定义 $f(1) := 2$ 即可使其在 $\mathbb{R}$ 上连续）。

### 第 2 题

- $g(0^-) = \lim_{x \to 0^-} x^2 = 0$
- $g(0^+) = \lim_{x \to 0^+} (x + 1) = 1$

两个单侧极限都存在但 $0 \neq 1$。

⇒ **跳跃间断点**，跳跃量 $|1 - 0| = 1$。
（注意：即便我们重新定义 $g(0) = 0$ 或 $g(0) = 1$，仍无法消除跳跃。）

### 第 3 题

分母 $x^2 - 4 = 0$ 当 $x = \pm 2$。$h$ 在 $\mathbb{R} \setminus \{-2, 2\}$ 处连续。

**$x_0 = 2$**：

- $h(2^-) = \lim_{x \to 2^-} \dfrac{1}{(x-2)(x+2)} = \dfrac{1}{0^- \cdot 4} = -\infty$
- $h(2^+) = \dfrac{1}{0^+ \cdot 4} = +\infty$

至少一侧 $= \pm\infty$ ⇒ **无穷间断点**。

**$x_0 = -2$**：

- $h((-2)^-) = \dfrac{1}{(\to -4) \cdot 0^-} = +\infty$
- $h((-2)^+) = \dfrac{1}{(-4) \cdot 0^+} = -\infty$

⇒ 同样是**无穷间断点**。

### 第 4 题（构造）

取
$$
\phi(x) = \begin{cases} \sin(1/x) & x \neq 0 \\ 0 & x = 0 \end{cases}
$$

**$x_0 = 0$ 处**：
取 $x_n = \tfrac{1}{n\pi} \to 0$，$\phi(x_n) = \sin(n\pi) = 0 \to 0$。
取 $y_n = \tfrac{2}{(4n+1)\pi} \to 0$，$\phi(y_n) = \sin(\tfrac{(4n+1)\pi}{2}) = 1 \to 1$。
两个数列都 $\to 0$ 但 $\phi$ 像收敛于不同极限——由 Heine 归结原则反向，
$\lim_{x \to 0} \phi(x)$ **不存在**，且不为 $\pm\infty$（$|\phi| \leq 1$）。

⇒ **振荡间断点**。

**$x \neq 0$ 处**：$1/x$ 是连续函数，$\sin$ 是连续函数，复合函数连续 ⇒ $\phi$ 连续。$\blacksquare$

</details>

## 考察点

- [[ANL-DEF-011]] 单侧极限的计算
- [[ANL-DEF-013]] 间断点四种类型的判定路径

## 备注

- 第 3 题展示了同一函数在不同间断点可以有**不同的"无穷符号"组合**——左 $-\infty$、右 $+\infty$ 与左 $+\infty$、右 $-\infty$，本质都是"无穷间断"。
- 第 4 题的振荡间断 $\sin(1/x)$ 是分析中最重要的反例之一，与 [[ANL-DEF-024]] 一致连续性的反例（$x \sin(1/x)$、$\sin(x^2)$）一脉相承——都涉及"局部频率随 $x$ 变化无界"。
