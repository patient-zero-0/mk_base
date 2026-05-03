---
title: "Bolzano–Weierstrass 定理的应用：证明命题"
type: problem
id: ANL-PROB-007
subject: analysis
chapter: 01-limits
tags:
  - Bolzano-Weierstrass
  - 子列
  - 综合应用
depends:
  - ANL-THM-008
  - ANL-DEF-006
  - ANL-DEF-005
uses: []
status: review
source: "华东师范大学《数学分析》第5版 §7.3 习题"
difficulty: 4
tests:
  - ANL-THM-008
related:
  - ANL-THM-007
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

利用 [[ANL-THM-008]] Bolzano–Weierstrass 定理证明：

1. **有界 + 唯一积聚点 ⇒ 收敛**：设 $\{a_n\}$ 有界且仅有一个积聚点 $L$（即 $L$ 是 $\{a_n\}$ 唯一的子列极限），则 $\{a_n\} \to L$。

2. **构造唯一积聚点反例（违反"有界"条件）**：举出一个**无界**数列，仅有一个积聚点但不收敛。

## 提示

<details><summary>点击展开提示</summary>

- 第 1 题：反证。假设 $a_n \not\to L$，则 $\exists \varepsilon_0 > 0$ 与子列 $a_{n_k}$ 满足 $|a_{n_k} - L| \geq \varepsilon_0$。该子列也有界，由 [[ANL-THM-008]] 它有收敛子列收敛于 $L'$；论证 $L' \neq L$，矛盾于"唯一积聚点"。
- 第 2 题：构造一个交替"靠近 0"和"飞向无穷"的序列。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题

**证明（反证法）**：假设 $\{a_n\}$ 不收敛于 $L$。

由 [[ANL-DEF-004]] 反命题：
$$
\exists \varepsilon_0 > 0, \forall N, \exists n > N : |a_n - L| \geq \varepsilon_0.
$$

由此可构造子列 $\{a_{n_k}\}$（取 $n_1$ 为某 $|a_n - L| \geq \varepsilon_0$ 的最小下标，$n_2 > n_1$ 满足同条件，以此类推），
对所有 $k$ 有 $|a_{n_k} - L| \geq \varepsilon_0$。

由 $\{a_n\}$ 有界，子列 $\{a_{n_k}\}$ 也有界。由 [[ANL-THM-008]] Bolzano–Weierstrass 定理（应用于子列），存在它的子子列 $\{a_{n_{k_j}}\}$ 收敛，设 $a_{n_{k_j}} \to L'$。

由 $|a_{n_k} - L| \geq \varepsilon_0$ 对所有 $k$，子子列也满足 $|a_{n_{k_j}} - L| \geq \varepsilon_0$。
取极限保号性：$|L' - L| \geq \varepsilon_0 > 0$，故 $L' \neq L$。

但 $L'$ 是 $\{a_n\}$ 的子列（即 $\{a_{n_{k_j}}\}$）的极限，按定义 $L'$ 也是 $\{a_n\}$ 的**积聚点**。

这与"$L$ 是唯一积聚点"矛盾。故 $a_n \to L$。$\blacksquare$

### 第 2 题

**构造：** 定义
$$
a_n = \begin{cases} 0 & n \text{ 为偶数} \\ n & n \text{ 为奇数} \end{cases}
$$
即 $\{a_n\} = 1, 0, 3, 0, 5, 0, 7, 0, \ldots$。

**验证**：

- **唯一积聚点**：偶数项子列 $a_{2k} = 0 \to 0$，故 $0$ 是积聚点。
  奇数项子列 $a_{2k-1} = 2k - 1 \to +\infty$，**不收敛**——故 $+\infty$ 不计为有限积聚点。
  任何有限值 $L \neq 0$ 都不是积聚点（任何 $L$ 的小邻域只含有限多偶数项 $0$ 之外，无邻近无穷大项）。
- **无界**：奇数项子列趋向 $\infty$，故无上界。
- **不收敛**：$\{a_n\}$ 包含发散到 $\infty$ 的子列，依 [[ANL-DEF-004]] 不收敛于任何有限值。

故构造的 $\{a_n\}$ 满足：唯一积聚点 $0$，但**不收敛**。$\blacksquare$

> 这正说明第 1 题的"有界"条件**不可省略**。

</details>

## 考察点

- [[ANL-THM-008]] Bolzano–Weierstrass 定理的"反向"应用——把"有界 + 子列控制"转化为整体收敛
- "积聚点 = 子列极限"的等价转化
- 构造反例时"端点失效"的标准模式（无界 / 不闭）

## 备注

**积聚点严格定义**：

> $L$ 是 $\{a_n\}$ 的**积聚点**（accumulation point），若存在 $\{a_n\}$ 的子列 $\{a_{n_k}\}$ 使 $a_{n_k} \to L$。

**与"极限"的区别**：

- 极限：**整个数列**趋向单一值。
- 积聚点：**某个子列**趋向某值——一个数列可有多个积聚点。

**例子**：$\{(-1)^n\}$ 的积聚点集合 $= \{-1, 1\}$（两个）；
$\{\sin n\}$ 的积聚点集合 $= [-1, 1]$（连续区间，需用 Weyl 等分布定理）。

第 1 题的命题可总结为口诀："**有界 + 积聚点唯一 ⇔ 收敛**"——是 B–W 定理在收敛性判定中最常用的形式。
