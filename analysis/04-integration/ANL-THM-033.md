---
title: "换元积分法"
type: theorem
id: ANL-THM-033
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 换元积分
  - 计算法则
depends:
  - ANL-DEF-026
  - ANL-DEF-028
  - ANL-THM-018
  - ANL-THM-027
  - ANL-THM-032
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §8.2, §9.5"
difficulty: 3
related:
  - ANL-THM-018
  - ANL-THM-034
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件与结论

### 不定积分换元（第一类换元法 / 凑微分）

**条件**：$g$ 在区间 $I$ 上可导（[[ANL-DEF-014]]），$f$ 在 $g(I)$ 上连续。

**结论**：
$$
\int f(g(x)) \, g'(x) \, dx = \int f(u) \, du \bigg|_{u = g(x)} = F(g(x)) + C,
$$
其中 $F$ 是 $f$ 的任一原函数（[[ANL-DEF-028]]）。

> **凑微分**：把 $g'(x) \, dx$ 视为 $du$（即 $du = g'(x) dx$），从而把外部对 $x$ 的积分"换成"对 $u$ 的积分。

### 定积分换元（第二类换元法）

**条件**：$g : [\alpha, \beta] \to [a, b]$ 连续可导（即 $g'$ 连续），$g(\alpha) = a$, $g(\beta) = b$；$f$ 在 $[a, b]$ 上连续。

**结论**：
$$
\int_{\alpha}^{\beta} f(g(t)) \, g'(t) \, dt = \int_{a}^{b} f(u) \, du.
$$

> **定积分换元的关键**：
>
> - 上下限随之改变：$x = \alpha \mapsto u = a$，$x = \beta \mapsto u = b$
> - 不需要 $g$ **可逆**或单调——只需 $g$ 连续可导
>
> **第二类换元（"反过来"用）**：若想从 $\int f(u) du$ 出发凑出 $g$，常令 $u = g(t)$，
> 整体替换为 $\int f(g(t)) g'(t) dt$，再求新的积分（要求 $g$ **单调**以保证可逆）。

## 几何/直觉理解

> 换元法是 [[ANL-THM-018]] **链式法则**的"逆向应用"——
> 链式法则告诉你 $(F \circ g)'(x) = F'(g(x)) g'(x) = f(g(x)) g'(x)$，
> 反过来积分就得到换元公式。
>
> **物理画面**（粗略）：要计算 $\int f \, du$，但 $u$ 用 $x$ 的函数 $u = g(x)$ 描述，
> 则把 $du$ 展开为 $g'(x) dx$，整体改写为对 $x$ 的积分；反之亦然。

## 证明

### 不定积分版本

**证明：** 设 $F$ 是 $f$ 的原函数，即 $F'(u) = f(u)$。

由 [[ANL-THM-018]] 链式法则：
$$
\frac{d}{dx} F(g(x)) = F'(g(x)) \cdot g'(x) = f(g(x)) \cdot g'(x).
$$

故 $F \circ g$ 是 $f(g(x)) g'(x)$ 的原函数，由 [[ANL-DEF-028]]：
$$
\int f(g(x)) g'(x) dx = F(g(x)) + C. \quad\blacksquare
$$

### 定积分版本

**证明：** 设 $F$ 是 $f$ 在 $[a, b]$ 上的原函数（由 $f$ 连续 + [[ANL-THM-031]] 变限积分给出）。

由链式法则，$F \circ g$ 是 $f(g(t)) g'(t)$ 的原函数。

由 [[ANL-THM-032]] Newton-Leibniz 公式（应用两次）：
$$
\int_\alpha^\beta f(g(t)) g'(t) dt = F(g(t)) \big|_\alpha^\beta = F(g(\beta)) - F(g(\alpha)) = F(b) - F(a) = \int_a^b f(u) du. \quad\blacksquare
$$

## 常见错误

- ✗ **漏掉上下限替换**。
  错误：$\int_0^1 2x \cos(x^2) dx \neq \int_0^1 \cos u \, du$（左换元 $u = x^2$，右上下限错误）。
  正确：$u = x^2 \Rightarrow x: 0 \to 1$ 时 $u: 0 \to 1$，故 $\int_0^1 \cos u \, du = \sin 1$。
  幸运地此例上下限不变；若 $\int_0^2 2x \cos(x^2) dx$ 则 $u: 0 \to 4$，结果完全不同。
- ✗ **漏掉 $g'(x)$ 因子**或写成错误形式。
  错误："$\int \cos(x^2) dx = \int \cos u \, du$"——这是错的，缺 $g'(x) = 2x$ 因子。
  正确：$\int 2x \cos(x^2) dx = \int \cos u \, du$，但 $\int \cos(x^2) dx$ **不能**通过初等换元化简为初等函数的积分（事实上是 Fresnel 积分）。
- ✗ **第二类换元漏单调性**。
  $\int f(u) du$ 试图换 $u = g(t)$，必须保证 $g$ 在所考虑的范围**单调**（一一对应），否则换元后区间映射模糊。
- ✗ 把"$x = g(t)$ 换元"与"$t = h(x)$ 换元"混淆。
  本质相同（互为反函数），但具体写时上下限替换方向不同——务必算一遍 $x = \alpha$ 时 $t$ 是多少。

## 推论与应用

- **第一类换元（凑微分）**：识别被积函数中"内函数 + 内函数导数"的结构。常见模式：

    | 凑出形式 | 例 |
    |---|---|
    | $f(g(x)) g'(x)$ | $\int 2x \sin(x^2) dx$（$g = x^2$） |
    | $\dfrac{g'(x)}{g(x)}$ | $\int \tan x \, dx = -\ln\lvert\cos x\rvert + C$（$g = \cos x$） |
    | $g'(x) e^{g(x)}$ | $\int 2x e^{x^2} dx = e^{x^2} + C$ |
    | $\dfrac{g'(x)}{1 + g(x)^2}$ | $\int \dfrac{e^x}{1+e^{2x}} dx = \arctan(e^x) + C$ |

- **第二类换元（变量代换）**：常见三角代换：

    | 被积函数含 | 代换 | 化为 |
    |---|---|---|
    | $\sqrt{a^2 - x^2}$ | $x = a \sin t$ | $a\cos t$ |
    | $\sqrt{a^2 + x^2}$ | $x = a \tan t$ | $a \sec t$ |
    | $\sqrt{x^2 - a^2}$ | $x = a \sec t$ | $a \tan t$ |

- **应用例题**：[[ANL-EX-012]]

## 链接

- 前置：[[ANL-DEF-026]] Riemann 可积、[[ANL-DEF-028]] 原函数、[[ANL-THM-018]] 链式法则、[[ANL-THM-027]]、[[ANL-THM-032]] N-L 公式
- 配合：[[ANL-THM-034]] 分部积分法
- 应用：[[ANL-EX-012]] 换元积分典型范例
