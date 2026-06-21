---
title: "反常积分收敛判别（比较 / Cauchy / Abel-Dirichlet）"
type: theorem
id: ANL-THM-035
subject: analysis
chapter: 04-integration
tags:
  - 积分
  - 反常积分
  - 收敛判别
depends:
  - ANL-DEF-029
  - ANL-DEF-030
  - ANL-THM-029
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §11.1, §11.2"
difficulty: 4
related:
  - ANL-DEF-029
  - ANL-DEF-030
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 三大类判别法

> 下文以 [[ANL-DEF-029]] 无穷限反常积分 $\int_a^{+\infty} f$ 为例。瑕积分 [[ANL-DEF-030]] 类似。

### 形式 1：Cauchy 收敛准则

> 设 $f$ 在 $[a, T]$ 上对每个 $T > a$ 都可积。则 $\displaystyle \int_a^{+\infty} f$ 收敛 $\iff$
> 对任意 $\varepsilon > 0$，$\exists M > a$ 使得对一切 $T_2 > T_1 > M$，
> $$
> \left| \int_{T_1}^{T_2} f(x) \, dx \right| < \varepsilon.
> $$
>
> 与函数极限的 Cauchy 准则平行（[[ANL-THM-007]] 数列版），是判别"积分尾部任意小"的工具。

### 形式 2：比较判别法

> 设 $f, g$ 在 $[a, +\infty)$ 上非负，且对所有 $x \geq a$（或仅"够大的 $x$"）有 $0 \leq f(x) \leq g(x)$。
>
> - 若 $\displaystyle \int_a^{+\infty} g$ 收敛，则 $\displaystyle \int_a^{+\infty} f$ 收敛
> - 若 $\displaystyle \int_a^{+\infty} f$ 发散，则 $\displaystyle \int_a^{+\infty} g$ 发散

**极限形式**（更实用）：

> 设 $f, g \geq 0$ 且 $\displaystyle \lim_{x \to +\infty} \frac{f(x)}{g(x)} = c$。
>
> - 若 $0 < c < +\infty$：$\int f$ 与 $\int g$ **同时**收敛或同时发散
> - 若 $c = 0$：$\int g$ 收敛 $\Rightarrow$ $\int f$ 收敛（"$f$ 比 $g$ 衰减更快"）
> - 若 $c = +\infty$：$\int g$ 发散 $\Rightarrow$ $\int f$ 发散（"$f$ 衰减更慢"）

### 形式 3：Abel / Dirichlet 判别法

> 用于乘积形式 $\int f g$ 的收敛性，**不要求** $f, g$ 保号。

**Dirichlet 判别**：

> 设
>
> 1. $f$ 在 $[a, +\infty)$ 上**单调**且 $\displaystyle \lim_{x \to +\infty} f(x) = 0$
> 2. $g$ 在 $[a, +\infty)$ 上可积，且其变限积分 $G(T) := \int_a^T g(x) \, dx$ **有界**（不必收敛）
>
> 则 $\displaystyle \int_a^{+\infty} f(x) g(x) \, dx$ **收敛**。

**Abel 判别**：

> 设
>
> 1. $f$ 在 $[a, +\infty)$ 上**单调有界**
> 2. $\displaystyle \int_a^{+\infty} g$ **收敛**
>
> 则 $\displaystyle \int_a^{+\infty} f g$ **收敛**。

## 几何/直觉理解

> **Cauchy 准则**：积分收敛 $\iff$ 尾部 $\int_{T_1}^{T_2} f$ 能任意小 — 把"收敛到某极限"的问题转为"尾部自身的 Cauchy 性"
>
> **比较判别**："正函数 + 谁衰减得快"：
> $f \leq g$ + $\int g$ 收敛 ⇒ $f$ 衰减不慢于 $g$ ⇒ $\int f$ 也收敛。
> 类比数列版：$\sum a_n$ 收敛 + $0 \leq b_n \leq a_n$ ⇒ $\sum b_n$ 收敛。
>
> **Dirichlet 判别**："$f$ 衰减、$g$ 振荡且部分和有界" 的情形——
> 即使 $g$ 不可积（如 $g = \sin x$），振荡 + $f$ 衰减仍可让乘积收敛。

## 证明（Dirichlet 判别）

> 仅证 Dirichlet（Abel 类似）。比较判别用单调有界（[[ANL-THM-006]]）；Cauchy 准则用极限的 Cauchy 性。

**证明**：用 Cauchy 收敛准则（形式 1）。任给 $\varepsilon > 0$。

由 $G$ 有界，$\exists M_1 > 0$ 使 $|G(T)| \leq M_1$ 对所有 $T \geq a$；故 $\left| \int_{T_1}^{T_2} g \right| = |G(T_2) - G(T_1)| \leq 2 M_1$。

由 $f \to 0$（$x \to \infty$），$\exists T_0 > a$ 使 $|f(x)| < \dfrac{\varepsilon}{4 M_1}$（$x > T_0$）。

对 $T_2 > T_1 > T_0$，应用[第二积分中值定理（教材 §9.5 推广形式）] (本批未单独立条目，参 [[ANL-THM-030]] 推广提及)：

存在 $\xi \in [T_1, T_2]$ 使
$$
\int_{T_1}^{T_2} f(x) g(x) \, dx = f(T_1) \int_{T_1}^\xi g \, dx + f(T_2) \int_\xi^{T_2} g \, dx.
$$

每一项绝对值 $\leq |f(T_1)| \cdot 2 M_1$ 或 $|f(T_2)| \cdot 2 M_1$，故
$$
\left| \int_{T_1}^{T_2} fg \right| \leq |f(T_1)| \cdot 2M_1 + |f(T_2)| \cdot 2M_1 < \frac{\varepsilon}{4M_1} \cdot 4 M_1 = \varepsilon.
$$

由 Cauchy 准则，$\int_a^{+\infty} fg$ 收敛。$\blacksquare$

> 注：上述论证用到的"第二积分中值定理"是 [[ANL-THM-030]] 积分中值定理的推广形式（华师大 §9.5）。

## 常见错误

- ✗ **比较判别忽略保号条件**。
  反例：$\int_1^\infty \dfrac{\sin x}{x} dx$ **收敛**（条件收敛，[[ANL-EX-015]]），
  但 $\int_1^\infty \dfrac{|\sin x|}{x} dx$ **发散**——比较判别只能判定**绝对收敛**，不能判定条件收敛。
- ✗ **Dirichlet 判别忽略"$f$ 单调"**。
  反例：$f(x) = \sin x / x$，虽然 $f \to 0$ 但**不单调**，Dirichlet 判别失效。
  $\int (\sin x / x) \cdot \sin x \, dx$ 的收敛性需用其他方法。
- ✗ **混淆 Cauchy 准则与 Cauchy 主值**。
  本条目的"Cauchy 准则"是收敛性判定；"Cauchy 主值积分"是另一种较弱的收敛概念（详见 [[ANL-DEF-029]]）。
- ✗ 用比较判别判定**绝对收敛**后误以为"原积分一定收敛"。**对**——绝对收敛**确实**蕴含收敛。
  但反过来：条件收敛**不一定**绝对收敛。

## 推论与应用

- **绝对收敛蕴含收敛**：$\int |f|$ 收敛 ⇒ $\int f$ 收敛（用比较判别 + $|f|, |f| - f, f - (-|f|)$ 的拆分）
- **常见判别策略**：
    | 被判别 | 推荐工具 |
    |---|---|
    | $\int 1/x^p$ 形 | p-判别（直接计算） |
    | $\int (\text{多项式分式})$ | 极限形比较判别 |
    | $\int (\text{衰减} \times \text{振荡})$ | Dirichlet 判别 |
    | $\int (\text{衰减} \times \text{收敛积分})$ | Abel 判别 |
- **应用**：[[ANL-EX-014]] Γ 函数（用比较判别）、[[ANL-EX-015]] $\int \sin x/x$（用 Dirichlet）

## 链接

- 前置：[[ANL-DEF-029]] 反常积分（无穷限）、[[ANL-DEF-030]] 瑕积分、[[ANL-THM-029]] 积分基本性质
- 应用：[[ANL-EX-014]]、[[ANL-EX-015]]
- 关联：[[ANL-THM-007]] 数列 Cauchy 准则（结构平行）、级数判别法（[[ANL-THM-038]] 等）
