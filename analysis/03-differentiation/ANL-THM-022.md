---
title: "Lagrange 中值定理"
type: theorem
id: ANL-THM-022
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - 中值定理
  - 闭区间
depends:
  - ANL-DEF-014
  - ANL-DEF-012
  - ANL-THM-021
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §6.1"
difficulty: 3
related:
  - ANL-THM-021
  - ANL-THM-023
  - ANL-THM-025
applications:
  - "数值分析：Newton 法、误差估计"
  - "经济学：边际分析的严格化基础"
  - "微分方程：解的一致估计"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $f : [a, b] \to \mathbb{R}$ 满足：

1. $f$ 在闭区间 $[a, b]$ 上**连续**（[[ANL-DEF-012]]）；
2. $f$ 在开区间 $(a, b)$ 内**可导**（[[ANL-DEF-014]]）。

## 结论

> 存在 $\xi \in (a, b)$ 使得
> $$
> f'(\xi) = \frac{f(b) - f(a)}{b - a}.
> $$
>
> 等价写法：$f(b) - f(a) = f'(\xi)(b - a)$（"有限增量公式"）。

## 几何/直觉理解

> 曲线 $y = f(x)$ 上从 $(a, f(a))$ 到 $(b, f(b))$ 的**割线**斜率为 $\dfrac{f(b) - f(a)}{b - a}$。
> 定理断言：曲线上**至少存在一点**，其**切线**与该割线**平行**。
>
> 几何画面：把割线一根棍子，沿曲线"上下平移"——一定会在某处与曲线"相切"。
>
> Rolle 定理（[[ANL-THM-021]]）是其特例（$f(a) = f(b)$ 时割线斜率 = 0，切线水平）。
> Lagrange 是 Rolle 的"倾斜版本"。

## 证明

**证明：** 思路：构造辅助函数把"切线斜率 = 割线斜率"转化为"导数为零"，再用 Rolle。

设
$$
g(x) := f(x) - \frac{f(b) - f(a)}{b - a}(x - a).
$$

$g$ 在 $[a, b]$ 连续（连续函数减去线性函数），在 $(a, b)$ 可导（可导函数减去可导函数），且
$$
g(a) = f(a) - 0 = f(a),\quad g(b) = f(b) - \frac{f(b) - f(a)}{b - a}(b - a) = f(b) - (f(b) - f(a)) = f(a).
$$

故 $g(a) = g(b) = f(a)$。由 [[ANL-THM-021]] Rolle 定理，$\exists \xi \in (a, b)$ 使 $g'(\xi) = 0$。

计算：
$$
g'(x) = f'(x) - \frac{f(b) - f(a)}{b - a}.
$$

故 $g'(\xi) = 0 \iff f'(\xi) = \dfrac{f(b) - f(a)}{b - a}$。$\blacksquare$

## 常见错误

- ✗ 把 $\xi$ 当作具体值，写成 $\xi = (a+b)/2$ 或类似。
  $\xi$ 是定理保证的**存在**点，具体位置依赖 $f$，**不可指定**。
  反例：$f(x) = x^3$ 在 $[0, 1]$ 上，$f'(\xi) = 3 \xi^2 = 1 \Rightarrow \xi = 1/\sqrt{3} \neq 0.5$。
- ✗ 漏掉端点连续 / 内点可导的区分。
  端点不要求可导（$f$ 可能在端点处仅单侧可导）。这点常被忽略。
- ✗ 把"有限增量公式"乱用为"无限小增量公式"$df = f'(x) dx$。
  Lagrange 给出的是**有限**增量的精确表达（含某点 $\xi$），
  而微分（[[ANL-DEF-015]]）是**无限小**的近似。两者都重要但不能混。
- ✗ 用 Lagrange 推出 $f$ 单调时漏掉"导数符号"。
  正确：若 $f'(x) > 0$ 在 $(a, b)$ 上恒成立，则 $f$ 在 $[a, b]$ 上**严格递增**——
  这正是"$f' > 0 \Rightarrow$ 单调"的严格证明（用 Lagrange）。

## 推论与应用

- **导数符号 ⇒ 单调性**：$f' > 0$（$\geq 0$）在区间上 ⇒ $f$ 严格（不严格）递增
- **导数估计 ⇒ 函数估计**：$|f'| \leq M$ 在 $(a, b)$ 上 ⇒ $|f(x) - f(y)| \leq M|x - y|$（Lipschitz）
- **零导函数 ⇒ 常数**：$f' \equiv 0$ 在区间上 ⇒ $f$ 恒为常数
- **进一步推广**：[[ANL-THM-023]] Cauchy 中值定理
- **Taylor 公式基础**：[[ANL-THM-025]] 的 Lagrange 余项形式即 Lagrange 中值定理的高阶版本

## 跨专业应用

- **数值分析**：Newton 法收敛性证明，根的存在性 + 唯一性论证常基于 Lagrange
- **微分方程**：解的存在性、唯一性、连续依赖性 estimates 常通过 Lagrange 化为积分估计
- **经济学**：边际成本曲线在某区间的"平均"刻画 = 该区间端点函数值之差除以区间长度
