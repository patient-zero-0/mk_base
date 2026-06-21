---
title: "分部积分法"
type: theorem
id: ANL-THM-034
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 分部积分
  - 计算法则
depends:
  - ANL-DEF-026
  - ANL-DEF-028
  - ANL-THM-017
  - ANL-THM-027
  - ANL-THM-032
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §8.3, §9.5"
difficulty: 3
related:
  - ANL-THM-033
  - ANL-THM-017
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件与结论

### 不定积分版

**条件**：$u, v$ 在区间 $I$ 上**连续可导**（即 $u', v'$ 都连续）。

**结论**：
$$
\int u(x) v'(x) \, dx = u(x) v(x) - \int v(x) u'(x) \, dx.
$$

差分形式（Leibniz 记号）：$\int u \, dv = uv - \int v \, du$。

### 定积分版

**条件**：$u, v$ 在 $[a, b]$ 上连续可导。

**结论**：
$$
\int_a^b u(x) v'(x) \, dx = u(x) v(x) \Big|_a^b - \int_a^b v(x) u'(x) \, dx = u(b)v(b) - u(a)v(a) - \int_a^b v u' \, dx.
$$

## 几何/直觉理解

> 分部积分是 [[ANL-THM-017]] **求导的乘积法则** $(uv)' = u'v + uv'$ 的"逆向应用"。
> 把乘积法则两边对 $x$ 积分：
> $$
> \int (uv)' \, dx = \int u'v \, dx + \int u v' \, dx,
> $$
> 由 [[ANL-DEF-028]]，$\int (uv)' dx = uv + C$。整理即得分部积分公式。
>
> **使用直觉**：当遇到 $\int (\text{乘积}) dx$，分部把"积分负担"从一边推到另一边——
> "把 $u v'$ 化为 $vu'$"。
> 选择哪个为 $u$（求导方）、哪个为 $dv$（积分方）取决于哪种更简化。

## 证明

### 定积分版（不定积分版可由 [[ANL-DEF-028]] 约束推出）

**证明：** 由 [[ANL-THM-017]] 求导乘积法则，对所有 $x \in [a, b]$：
$$
(uv)'(x) = u'(x) v(x) + u(x) v'(x).
$$

由 $u, v, u', v'$ 都连续，$(uv)'$ 也连续，故在 $[a, b]$ 上可积（[[ANL-THM-027]]）。
对两边在 $[a, b]$ 上积分：
$$
\int_a^b (uv)'(x) \, dx = \int_a^b u'(x) v(x) \, dx + \int_a^b u(x) v'(x) \, dx.
$$

左边由 [[ANL-THM-032]] N-L 公式：$\int_a^b (uv)' dx = u(x)v(x) \big|_a^b = u(b)v(b) - u(a)v(a)$。

整理：
$$
\int_a^b u v' \, dx = u(x)v(x) \big|_a^b - \int_a^b u'v \, dx. \quad\blacksquare
$$

## 常见错误

- ✗ **选择 $u, dv$ 后没有简化**。
  $\int x \cos x \, dx$：选 $u = x, dv = \cos x \, dx$ ⇒ $du = dx, v = \sin x$，
  $\int x \cos x \, dx = x \sin x - \int \sin x \, dx = x \sin x + \cos x + C$ ✓
  错误选择：$u = \cos x, dv = x \, dx$ ⇒ $du = -\sin x \, dx, v = x^2/2$，
  原积分 = $\dfrac{x^2 \cos x}{2} + \int \dfrac{x^2 \sin x}{2} \, dx$ — **更复杂**！
- ✗ **遗忘"$+ C$"**（不定积分时）。
- ✗ **定积分版漏掉端点的 $u(x)v(x)\big|_a^b$ 项**。
  常见错误：$\int_0^1 x e^x dx = -\int_0^1 e^x dx = -(e-1)$（漏掉 $xe^x|_0^1 = e$）。
  正确：$= xe^x|_0^1 - \int_0^1 e^x dx = e - (e-1) = 1$。
- ✗ 与 [[ANL-THM-033]] 换元法搞混。
  分部针对**乘积**形式（$\int u \, dv$）；换元针对**复合**形式（$\int f(g(x))g'(x) dx$）。
  实战中两者常**结合使用**——先换元再分部，或反之。

## 推论与应用

- **常用 LIATE 选 $u$ 经验法则**（按优先级，能选作 $u$ 的优先是更靠前的）：

    | 字母 | 函数类型 | 例 |
    |---|---|---|
    | **L** | 对数 (Logarithm) | $\ln x$ |
    | **I** | 反三角 (Inverse trig) | $\arctan x, \arcsin x$ |
    | **A** | 代数 (Algebraic) | $x^n$（多项式） |
    | **T** | 三角 (Trig) | $\sin x, \cos x$ |
    | **E** | 指数 (Exponential) | $e^x, a^x$ |

    例：$\int x \ln x \, dx$，按 LIATE 选 $u = \ln x$（L），$dv = x \, dx$。

- **递推积分**：分部积分用于建立递推公式，如：
  - $I_n = \int x^n e^x dx \Rightarrow I_n = x^n e^x - n I_{n-1}$
  - $I_n = \int \sin^n x \, dx$（Wallis 公式的来源）

- **应用例题**：[[ANL-EX-013]]

## 链接

- 前置：[[ANL-DEF-026]]、[[ANL-DEF-028]]、[[ANL-THM-017]] 求导乘积法则、[[ANL-THM-027]]、[[ANL-THM-032]] N-L 公式
- 配合：[[ANL-THM-033]] 换元积分法
- 应用：[[ANL-EX-013]] 分部积分典型范例
