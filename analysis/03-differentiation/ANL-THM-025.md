---
title: "Taylor 公式（Peano 余项与 Lagrange 余项）"
type: theorem
id: ANL-THM-025
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - Taylor 公式
  - 多项式逼近
  - 余项
depends:
  - ANL-DEF-014
  - ANL-DEF-017
  - ANL-THM-022
  - ANL-THM-023
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §6.3"
difficulty: 4
related:
  - ANL-THM-022
  - ANL-THM-023
applications:
  - "数值分析：函数计算、ODE 数值解、差分格式精度"
  - "信号处理：函数局部行为的多项式建模"
  - "物理：小振幅近似（如单摆 $\\sin\\theta \\approx \\theta$）"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件与结论

### 形式 1（Peano 余项 / 局部 Taylor 公式）

**条件**：设 $f$ 在 $x_0$ 的某邻域内 $n - 1$ 阶可导，并在 $x_0$ 处 $n$ 阶可导（[[ANL-DEF-017]]）。

**结论**：当 $x \to x_0$，
$$
f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!} (x - x_0)^k + o\big((x - x_0)^n\big).
$$

记号：右端前面的多项式称为 $f$ 在 $x_0$ 处的 **$n$ 次 Taylor 多项式**，记 $T_n(x; x_0)$。

### 形式 2（Lagrange 余项 / 整体 Taylor 公式）

**条件**：设 $f$ 在闭区间 $[x_0, x]$（或 $[x, x_0]$）上 $n$ 阶连续可导，
在开区间内 $n + 1$ 阶可导。

**结论**：存在 $\xi$ 介于 $x_0$ 与 $x$ 之间使
$$
f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!} (x - x_0)^k + \frac{f^{(n+1)}(\xi)}{(n+1)!} (x - x_0)^{n+1}.
$$

## 几何/直觉理解

> Taylor 公式断言：**充分光滑的函数在一点附近，可以被多项式精确逼近**。
> $T_n$ 是与 $f$ 在 $x_0$ 处"前 $n$ 阶导数全部相等"的唯一多项式（次数 $\leq n$）——
> 它是 $f$ 在该点的"最佳 $n$ 次多项式近似"。
>
> 余项告诉你近似的误差：
>
> - **Peano 余项 $o((x-x_0)^n)$**：误差比 $(x-x_0)^n$ "高阶地小"，仅描述 $x \to x_0$ 的渐近行为
> - **Lagrange 余项**：给出**精确的误差**表达 $\dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}$，可估计 $|R_n|$ 的上界

**层级直觉**：

| $n$ | 多项式 $T_n$ | 几何意义 |
|---|---|---|
| 0 | $f(x_0)$ | 用常数近似 |
| 1 | $f(x_0) + f'(x_0)(x-x_0)$ | 用切线近似（即 [[ANL-DEF-015]] 微分） |
| 2 | 加 $\dfrac{f''(x_0)}{2}(x-x_0)^2$ | 用切抛物线近似 |
| $n$ | 加 $\dfrac{f^{(n)}(x_0)}{n!}(x-x_0)^n$ | 第 $n$ 阶曲率信息 |

## 证明

### 形式 1（Peano 余项）

**证明：** 用归纳 + L'Hospital 类型论证。
设 $R_n(x) := f(x) - T_n(x; x_0)$。需证 $R_n(x) = o((x-x_0)^n)$，即
$$
\lim_{x \to x_0} \frac{R_n(x)}{(x-x_0)^n} = 0.
$$

注意 $R_n^{(k)}(x_0) = 0$（$k = 0, 1, \ldots, n$，由 $T_n$ 的构造）。

对 $\dfrac{R_n(x)}{(x-x_0)^n}$ 应用 L'Hospital 法则 $n - 1$ 次（每次分子分母都趋于 $0$）：
$$
\lim_{x \to x_0} \frac{R_n(x)}{(x - x_0)^n} = \lim_{x \to x_0} \frac{R_n^{(n-1)}(x)}{n! (x - x_0)}.
$$

而
$$
\lim_{x \to x_0} \frac{R_n^{(n-1)}(x)}{x - x_0} = \lim_{x \to x_0} \frac{R_n^{(n-1)}(x) - R_n^{(n-1)}(x_0)}{x - x_0} = R_n^{(n)}(x_0) = 0.
$$

最后一步：$R_n^{(n)}(x_0) = f^{(n)}(x_0) - T_n^{(n)}(x_0) = f^{(n)}(x_0) - f^{(n)}(x_0) = 0$。

合并：原极限 = $\dfrac{0}{n!} = 0$。$\blacksquare$

> 注：上述论证中"$n$ 阶导数 $R_n^{(n)}(x_0)$ 存在"用了 $f$ 在 $x_0$ 处 $n$ 阶可导的条件，
> 而中间步骤的 L'Hospital 在邻域内的 $n-1$ 阶导数则用了 $f$ 在邻域内 $n-1$ 阶可导。

### 形式 2（Lagrange 余项）

**证明：** 不妨设 $x > x_0$。设
$$
R_n(t) := f(x) - \sum_{k=0}^{n} \frac{f^{(k)}(t)}{k!}(x - t)^k, \quad t \in [x_0, x].
$$

注意 $R_n(x) = 0$（求和中只保留 $k=0$ 项 $f(x)$，与减去 $f(x)$ 抵消）。

对 $t$ 求导（注意 $f^{(k)}(t)$ 与 $(x-t)^k$ 都依赖 $t$，用乘积法则 + 链式法则）：

$$
R_n'(t) = -\sum_{k=0}^{n} \left[ \frac{f^{(k+1)}(t)}{k!}(x-t)^k - \frac{f^{(k)}(t)}{(k-1)!}(x-t)^{k-1} \right]_{k \geq 1 \text{ 时}} - f'(t).
$$

化简（典型望远镜抵消）：
$$
R_n'(t) = -\frac{f^{(n+1)}(t)}{n!}(x - t)^n.
$$

对 $G(t) := (x - t)^{n+1}$，$G'(t) = -(n+1)(x-t)^n$。两者在 $[x_0, x]$ 上满足
[[ANL-THM-023]] Cauchy 中值定理条件（$G' \neq 0$ 在 $(x_0, x)$ 内），故 $\exists \xi \in (x_0, x)$ 使
$$
\frac{R_n(x_0) - R_n(x)}{G(x_0) - G(x)} = \frac{R_n'(\xi)}{G'(\xi)}.
$$

代入 $R_n(x) = 0$, $G(x) = 0$, $G(x_0) = (x - x_0)^{n+1}$：
$$
\frac{R_n(x_0)}{(x - x_0)^{n+1}} = \frac{-f^{(n+1)}(\xi)(x-\xi)^n / n!}{-(n+1)(x-\xi)^n} = \frac{f^{(n+1)}(\xi)}{(n+1)!}.
$$

故
$$
R_n(x_0) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - x_0)^{n+1}.
$$

而由定义，$R_n(x_0) = f(x) - T_n(x; x_0)$。整理即得 Lagrange 余项形式。$\blacksquare$

## 常见错误

- ✗ 把 Peano 余项当作误差估计使用。
  Peano 形式仅在 $x \to x_0$ 时给"高阶小"信息，**不能**用于估计具体 $|x - x_0|$ 处的误差大小。
  误差估计必须用 Lagrange 余项（或积分余项）。
- ✗ 把 Taylor 公式与"Taylor 级数"混淆。
  Taylor 公式（本条目）是**有限项 + 余项**，对**有限光滑性**的函数都成立。
  Taylor 级数（[[ANL-DEF-039]]）是**无穷级数**，要求级数收敛**且收敛到 $f$**——
  后者并非对所有 $C^\infty$ 函数都成立（反例：$f(x) = e^{-1/x^2}$，$x \neq 0$；$f(0) = 0$。
  其在 $0$ 处 Taylor 级数恒为 $0$，但 $f \not\equiv 0$）。
- ✗ 在 Lagrange 余项中把 $\xi$ 当作具体数。
  $\xi$ 仅由定理保证存在；估计上界时应取 $\xi$ 在区间上的"最坏值"
  $|R_n| \leq \dfrac{\sup_{[x_0, x]} |f^{(n+1)}|}{(n+1)!} |x - x_0|^{n+1}$。
- ✗ 漏掉 $n+1$ 阶可导条件直接套用 Lagrange 形式。
  Peano 形式只需 $n$ 阶导在 $x_0$ 存在；Lagrange 形式需 $n+1$ 阶导在整个区间上存在。
  两条件强度不同，对应的余项形式与适用范围不同。

## 推论与应用

- **L'Hospital 法则的替代品**：很多 $0/0$ 极限可用 Taylor 展开求解（例：$\lim_{x \to 0} \dfrac{\sin x - x}{x^3} = -\dfrac{1}{6}$ 由 $\sin x = x - \dfrac{x^3}{6} + o(x^3)$）
- **不等式证明**：$\sin x \leq x$（$x \geq 0$）、$e^x \geq 1 + x$、$\ln(1+x) \leq x$ 等都可由低阶 Taylor 推得
- **极值的二阶充分条件**：若 $f'(x_0) = 0, f''(x_0) > 0$，则 $x_0$ 为严格局部极小（用 2 阶 Taylor 在 $x_0$ 处展开）
- **数值计算**：科学计算中 $\sin, \cos, \exp, \ln$ 的实现常基于 Taylor 截断 + 误差估计
- **微分方程**：解的局部级数表示

## 跨专业应用

- **数值分析**：差分格式 $\dfrac{f(x+h) - f(x-h)}{2h}$ 的精度（$O(h^2)$）由 Taylor 推得
- **物理**：单摆方程 $\ddot\theta + \dfrac{g}{\ell}\sin\theta = 0$ 在小振幅时近似为 $\ddot\theta + \dfrac{g}{\ell}\theta = 0$（用 $\sin\theta \approx \theta$）
- **量子力学**：势函数在平衡位置的二次近似 → 简谐振子模型
- **图形学**：Bézier 曲线、样条插值底层与 Taylor 展开思想紧密相关
