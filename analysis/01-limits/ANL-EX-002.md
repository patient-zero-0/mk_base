---
title: "用极限四则运算求多项式 / 有理式极限"
type: example
id: ANL-EX-002
subject: analysis
chapter: 01-limits
tags:
  - 极限
  - 四则运算
  - 例题
depends:
  - ANL-THM-004
  - ANL-DEF-004
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §2.2 例 5–7"
difficulty: 2
illustrates:
  - ANL-THM-004
related:
  - ANL-THM-005
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

利用 [[ANL-THM-004]] 极限四则运算，求下列极限：

1. $\displaystyle \lim_{n \to \infty} \frac{2 n^2 + 3 n - 1}{5 n^2 - n + 4}$；
2. $\displaystyle \lim_{n \to \infty} \frac{n^2 + n}{n^3 - 2}$；
3. $\displaystyle \lim_{n \to \infty} \left( \sqrt{n^2 + n} - n \right)$。

## 分析

> **第 1、2 题**：分子分母同时是多项式，分子分母**同除分母最高次幂**，
> 把"$\infty / \infty$"型化为"已知简单极限的四则运算"。

---

> **第 3 题**：$\sqrt{n^2 + n} - n \approx n - n = 0$ 看似 $\infty - \infty$ 不定型。
> **关键技巧：分子有理化**——乘以 $(\sqrt{n^2 + n} + n) / (\sqrt{n^2 + n} + n)$，
> 把根号差转化为多项式商，再用四则运算。

## 证明 / 解答

### 第 1 题

**解：** 分子分母同除 $n^2$（分母最高次幂）：
$$
\frac{2 n^2 + 3 n - 1}{5 n^2 - n + 4}
= \frac{2 + 3/n - 1/n^2}{5 - 1/n + 4/n^2}.
$$

由 $1/n \to 0, 1/n^2 \to 0$，及 [[ANL-THM-004]] 加减运算：
分子 $\to 2 + 0 - 0 = 2$；分母 $\to 5 - 0 + 0 = 5 \neq 0$。

由除法运算：
$$
\lim_{n \to \infty} \frac{2 n^2 + 3 n - 1}{5 n^2 - n + 4} = \frac{2}{5}.
$$
$\blacksquare$

### 第 2 题

**解：** 分子分母同除 $n^3$：
$$
\frac{n^2 + n}{n^3 - 2} = \frac{1/n + 1/n^2}{1 - 2/n^3}.
$$

由 $1/n \to 0, 1/n^2 \to 0, 2/n^3 \to 0$：
分子 $\to 0 + 0 = 0$；分母 $\to 1 - 0 = 1 \neq 0$。

故 $\displaystyle \lim_{n \to \infty} \frac{n^2 + n}{n^3 - 2} = 0$。$\blacksquare$

### 第 3 题

**解：** 分子有理化：
$$
\sqrt{n^2 + n} - n = \frac{(n^2 + n) - n^2}{\sqrt{n^2 + n} + n} = \frac{n}{\sqrt{n^2 + n} + n}.
$$

分子分母同除 $n$：
$$
\frac{n}{\sqrt{n^2 + n} + n} = \frac{1}{\sqrt{1 + 1/n} + 1}.
$$

由 $1/n \to 0$ 及连续性 $\sqrt{1 + 1/n} \to \sqrt{1 + 0} = 1$（开根可视为四则的极限推广，严格证明需连续函数）：
分母 $\to 1 + 1 = 2$。

故 $\displaystyle \lim_{n \to \infty} \left( \sqrt{n^2 + n} - n \right) = \frac{1}{2}$。$\blacksquare$

## 关键技巧

- **同除最高次幂**：处理"$\infty / \infty$"型多项式之比的标准首选。规则：分母最高次幂决定分母极限是否非零。
- **分子有理化**：处理"$\infty - \infty$"型根号差。模板：$\sqrt{f} - \sqrt{g} = (f - g) / (\sqrt{f} + \sqrt{g})$。
- **极限封闭于四则**：只要每个子式分别收敛、且分母极限非零，最终结果可"逐步代入"。
- **必须验证分母极限非零**：除法运算的前提条件，否则需另寻方法。

## 变式

- **变式 1**：$\displaystyle \lim_{n \to \infty} \frac{n^2 - 3 n + 1}{n + 1}$（提示：分母低于分子，结果发散到 $+\infty$）。
- **变式 2**：$\displaystyle \lim_{n \to \infty} \left( \sqrt{n + 1} - \sqrt{n} \right)$（提示：有理化后用 $1/n \to 0$）。
- **变式 3**：$\displaystyle \lim_{n \to \infty} n \left( \sqrt{n^2 + 1} - n \right)$（结合 1 与 3 的技巧）。
