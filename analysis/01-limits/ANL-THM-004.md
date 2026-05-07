---
title: "数列极限的四则运算"
type: theorem
id: ANL-THM-004
subject: analysis
chapter: 01-limits
tags:
  - 极限
  - 四则运算
  - 基础定理
depends:
  - ANL-DEF-004
  - ANL-DEF-005
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §2.2"
difficulty: 3
related:
  - ANL-THM-002
  - ANL-THM-003
  - ANL-EX-002
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $\{a_n\}, \{b_n\}$ 是收敛数列，$a_n \to A$，$b_n \to B$（按 [[ANL-DEF-004]]）。

## 结论

下列四则运算极限均成立：

1. **加法**：$\displaystyle \lim_{n \to \infty}(a_n + b_n) = A + B$。
2. **减法**：$\displaystyle \lim_{n \to \infty}(a_n - b_n) = A - B$。
3. **乘法**：$\displaystyle \lim_{n \to \infty}(a_n \cdot b_n) = A \cdot B$。
4. **除法**：若 $B \neq 0$，则**从某项起 $b_n \neq 0$**，且 $\displaystyle \lim_{n \to \infty} \frac{a_n}{b_n} = \frac{A}{B}$。

特别地，对常数 $c$：$\lim c \cdot a_n = c \cdot A$。

## 直觉理解

收敛 = "$a_n$ 几乎等于 $A$，$b_n$ 几乎等于 $B$"。
"几乎相等"经过四则运算的扰动，仍然"几乎相等"于运算结果 $A \star B$——只要扰动不被运算放大失控。

- 加减：扰动直接相加，受控；
- 乘法：需要因子有界（由 [[ANL-THM-002]]，收敛即有界）才能控制 $a_n b_n - AB$；
- 除法：需要分母**远离 0**（这是 $B \neq 0$ 后从某项起 $|b_n| \geq |B|/2$ 的关键作用）。

## 证明（以乘法为例）

**证明（乘法）**：要证 $|a_n b_n - AB| \to 0$。

**关键拆分**：
$$
a_n b_n - AB = a_n b_n - a_n B + a_n B - AB = a_n (b_n - B) + B (a_n - A).
$$

由 [[ANL-THM-002]]，$\{a_n\}$ 有界，存在 $M > 0: |a_n| \leq M$。
任给 $\varepsilon > 0$：

- 由 $a_n \to A$，$\exists N_1, \forall n > N_1: |a_n - A| < \varepsilon / (2|B| + 1)$；
- 由 $b_n \to B$，$\exists N_2, \forall n > N_2: |b_n - B| < \varepsilon / (2M)$。

取 $N = \max\{N_1, N_2\}$，对任意 $n > N$：
$$
|a_n b_n - AB| \leq |a_n||b_n - B| + |B||a_n - A| < M \cdot \frac{\varepsilon}{2M} + |B| \cdot \frac{\varepsilon}{2|B| + 1} < \varepsilon.
$$
$\blacksquare$

加法 / 减法证明从略（更直接，使用三角不等式）。除法 = 乘法 × 倒数，需先证 $1/b_n \to 1/B$（关键：$|b_n| \geq |B|/2$ 从某项起，由保号性 [[ANL-THM-003]] 应用于 $|b_n|$）。

## 常见错误

- ✗ **滥用四则运算于发散数列**。
  反例：$a_n = n, b_n = -n$ 都发散，但 $a_n + b_n = 0 \to 0$ 收敛。
  四则运算定理**要求**两数列**都先收敛**，否则不能直接套用。
- ✗ **乘法定理推广到"项数随 $n$ 变的求和 / 求积"**。
  四则运算只对**有限个、固定数量**的项封闭。
  反例：$\lim_{n} \underbrace{(1/n + 1/n + \cdots + 1/n)}_{n \text{ 个}} = \lim_{n} 1 = 1 \neq 0 = \underbrace{0 + 0 + \cdots}_{\text{逐项极限}}$。
  当项数 $n$ 本身是变量时，"逐项取极限再加"与"先加再取极限"不可交换。
- ✗ **0 / 0 直接套用除法**。
  $a_n / b_n$ 当 $A = B = 0$ 时**不定型**，必须先化简（如 L'Hôpital、夹逼、变量代换）。
- ✗ 忽视除法中的 "$B \neq 0$ 才有从某项起 $b_n \neq 0$"。
  若 $B = 0$，分母可能取 0，分式无定义；本定理不覆盖 $B = 0$ 情形。

## 推论

- **多项式极限**：若 $a_n \to A$，则 $P(a_n) \to P(A)$ 对任何多项式 $P$。
- **有理函数极限**：若 $a_n \to A$ 且 $Q(A) \neq 0$，则 $P(a_n) / Q(a_n) \to P(A) / Q(A)$。

例题应用见 [[ANL-EX-002]]。

## 链接

- 前置：[[ANL-DEF-004]]、[[ANL-DEF-005]]
- 关联：[[ANL-THM-002]] 收敛必有界（乘法证明的核心）、[[ANL-THM-003]] 保号性（除法证明所需）
- 推广：[[ANL-THM-009]] 函数极限的四则运算
