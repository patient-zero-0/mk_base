---
title: "复合函数求导（链式法则）"
type: theorem
id: ANL-THM-018
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - 链式法则
  - 复合函数
depends:
  - ANL-DEF-014
  - ANL-THM-016
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §4.2"
difficulty: 3
related:
  - ANL-THM-011
  - ANL-THM-017
applications:
  - "深度学习：反向传播算法即多层链式法则的递归应用"
  - "物理：复合时间依赖量的瞬时变化率"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设：

- $g : I \to J$ 在 $x_0 \in I$ 处可导（[[ANL-DEF-014]]）；
- $f : J \to \mathbb{R}$ 在 $u_0 := g(x_0) \in J$ 处可导。

## 结论

> 复合函数 $h := f \circ g$（即 $h(x) = f(g(x))$）在 $x_0$ 处可导，且
> $$
> h'(x_0) = f'(g(x_0)) \cdot g'(x_0).
> $$

Leibniz 记号下："$\dfrac{dh}{dx} = \dfrac{df}{du} \cdot \dfrac{du}{dx}$"——形式上"$du$ 抵消"。

## 几何/直觉理解

> 链式法则把"复合的瞬时变化率"分解为**外函数变化率 $\times$ 内函数变化率**。
>
> 类比传动：$g$ 是齿轮 1，把 $x$ 的转动以倍率 $g'(x_0)$ 传给 $u$；
> $f$ 是齿轮 2，把 $u$ 的转动以倍率 $f'(u_0)$ 传给最终输出。
> 总倍率即两级倍率相乘。

**物理画面**：若 $u(x)$ 是温度随高度变化、$f(u)$ 是某物理量随温度变化，
则 $f(u(x))$ 关于高度的瞬时变化率 = "随温度的变化率" $\times$ "温度随高度的变化率"。

## 证明

**证明：** 设 $\Delta x \neq 0$ 充分小，记 $\Delta u := g(x_0 + \Delta x) - g(x_0)$。

**情形 1：$\Delta x \to 0$ 时存在 $\delta > 0$，$0 < |\Delta x| < \delta \Rightarrow \Delta u \neq 0$。**

直接代入差商：
$$
\frac{h(x_0 + \Delta x) - h(x_0)}{\Delta x} = \frac{f(g(x_0) + \Delta u) - f(g(x_0))}{\Delta u} \cdot \frac{\Delta u}{\Delta x}.
$$

由 [[ANL-THM-016]]，$g$ 在 $x_0$ 可导 ⇒ $g$ 连续 ⇒ $\Delta u \to 0$ 当 $\Delta x \to 0$。
因此

- $\dfrac{f(g(x_0) + \Delta u) - f(g(x_0))}{\Delta u} \to f'(u_0)$（由 $f$ 在 $u_0$ 可导）
- $\dfrac{\Delta u}{\Delta x} \to g'(x_0)$（由 $g$ 在 $x_0$ 可导）

由 [[ANL-THM-009]] 极限的乘积法则得 $h'(x_0) = f'(u_0) \cdot g'(x_0)$。

**情形 2：在每个 $\Delta x \to 0$ 的邻域内都存在 $\Delta x \neq 0$ 使 $\Delta u = 0$。**

> 此情形在严格证明中需单独处理（情形 1 的写法会出现 $0/0$）。
> 引入函数
> $$
> \varphi(u) := \begin{cases}
> \dfrac{f(u_0 + u) - f(u_0)}{u} - f'(u_0), & u \neq 0 \\
> 0, & u = 0
> \end{cases}
> $$
> 由 $f$ 在 $u_0$ 可导，$\lim_{u \to 0} \varphi(u) = 0$。可写
> $$
> f(u_0 + u) - f(u_0) = u \cdot (f'(u_0) + \varphi(u)),
> $$
> 此式对 $u = 0$ 也成立。
> 取 $u = \Delta u$：
> $$
> h(x_0 + \Delta x) - h(x_0) = \Delta u \cdot (f'(u_0) + \varphi(\Delta u)).
> $$
> 除以 $\Delta x$ 取极限（$\Delta u \to 0 \Rightarrow \varphi(\Delta u) \to 0$）：
> $$
> h'(x_0) = g'(x_0) \cdot (f'(u_0) + 0) = f'(u_0) \cdot g'(x_0). \quad\blacksquare
> $$

## 常见错误

- ✗ 漏掉外函数对**内函数值** $g(x_0)$ 求值，写成 $h'(x_0) = f'(x_0) \cdot g'(x_0)$。
  反例：$h(x) = \sin(x^2)$，$g(x) = x^2$，$f(u) = \sin u$。
  正确：$h'(x) = \cos(x^2) \cdot 2x$；错误写法会得 $\cos x \cdot 2x$。
- ✗ 把 Leibniz 记号 $\dfrac{df}{du} \cdot \dfrac{du}{dx}$ 当作"分式相乘"严肃对待。
  这是助记符；严格证明中差商比 $\Delta u / \Delta x$ 不一定与导数比相等，
  必须用上文情形 2 的辅助函数 $\varphi$ 处理 $\Delta u = 0$ 的情形。
- ✗ 多层复合时漏链。$h(x) = f(g(k(x)))$ 时正确公式为
  $h'(x) = f'(g(k(x))) \cdot g'(k(x)) \cdot k'(x)$，三个因子**全部**要算。
- ✗ 把链式法则与乘积法则混用。$h(x) = f(x) \cdot g(x)$ **不是**复合函数，
  应用 [[ANL-THM-017]] 乘积法则 $h' = f'g + fg'$ 而非链式法则。

## 推论与应用

- 推论：反函数求导（详见 [[ANL-THM-019]] 反函数求导）
- 推论：隐函数求导
- 推论：参数方程求导 $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$
- 与 [[ANL-THM-017]] 求导四则一道，覆盖几乎一切初等函数求导

## 跨专业应用

- **深度学习**：神经网络反向传播本质是**多层链式法则**，将损失函数对输出层的梯度
  一层一层地"传"到输入层
- **物理**：温度场 $T(x, y, z)$ 沿轨迹 $\gamma(t) = (x(t), y(t), z(t))$ 的变化率
  $\dfrac{dT}{dt} = T_x \dot x + T_y \dot y + T_z \dot z$（多元链式法则）
- **优化**：梯度下降法的更新规则用到链式法则的多元版本
