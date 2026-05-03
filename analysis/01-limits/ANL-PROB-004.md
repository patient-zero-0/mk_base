---
title: "用 ε-N 定义证明数列收敛"
type: problem
id: ANL-PROB-004
subject: analysis
chapter: 01-limits
tags:
  - 数列收敛
  - ε-N
  - 证明练习
depends:
  - ANL-DEF-004
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §2.1 习题"
difficulty: 3
tests:
  - ANL-DEF-004
related:
  - ANL-EX-001
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 题目

利用 [[ANL-DEF-004]] ε-N 定义直接证明下列数列收敛：

1. $\displaystyle \lim_{n \to \infty} \frac{3 n + 2}{n + 1} = 3$
2. $\displaystyle \lim_{n \to \infty} \frac{n^2}{n^2 + 1} = 1$
3. $\displaystyle \lim_{n \to \infty} \sqrt{n + 1} - \sqrt{n} = 0$
4. $\displaystyle \lim_{n \to \infty} \frac{(-1)^n}{n^2 + 5} = 0$

## 提示

<details><summary>点击展开提示</summary>

- 第 1 题：化简 $\left|\frac{3n+2}{n+1} - 3\right| = \frac{1}{n+1}$，再控制小于 $\varepsilon$。
- 第 2 题：$\left|\frac{n^2}{n^2+1} - 1\right| = \frac{1}{n^2+1}$。注意 $n^2 + 1 > n^2$ 给出更易控的上界。
- 第 3 题：分子有理化 $\sqrt{n+1} - \sqrt{n} = \frac{1}{\sqrt{n+1} + \sqrt{n}} < \frac{1}{2\sqrt{n}}$。
- 第 4 题：$\left|\frac{(-1)^n}{n^2+5}\right| = \frac{1}{n^2+5} < \frac{1}{n^2}$，进而 $< \frac{1}{n}$。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题

**证明：** 任给 $\varepsilon > 0$。
$$
\left| \frac{3n + 2}{n + 1} - 3 \right| = \left| \frac{3n + 2 - 3(n + 1)}{n + 1} \right| = \frac{1}{n + 1} < \frac{1}{n}.
$$

要使上述 $< \varepsilon$，只需 $n > 1/\varepsilon$。取 $N = \lceil 1/\varepsilon \rceil$，
则 $\forall n > N$ 上述不等式成立。依 [[ANL-DEF-004]]，$\lim_{n \to \infty} \frac{3n+2}{n+1} = 3$。$\blacksquare$

### 第 2 题

**证明：** 任给 $\varepsilon > 0$。
$$
\left| \frac{n^2}{n^2 + 1} - 1 \right| = \frac{1}{n^2 + 1} < \frac{1}{n^2} \leq \frac{1}{n}.
$$

取 $N = \lceil 1/\varepsilon \rceil$，则 $\forall n > N$，$\left| \frac{n^2}{n^2+1} - 1 \right| < \varepsilon$。$\blacksquare$

> 注：取更紧的上界 $\frac{1}{n^2}$ 也行（$N = \lceil 1/\sqrt{\varepsilon} \rceil$），但工程上"够用即可"——$\frac{1}{n}$ 简单且合法。

### 第 3 题

**证明：** 任给 $\varepsilon > 0$。

分子有理化：
$$
\sqrt{n + 1} - \sqrt{n} = \frac{(n + 1) - n}{\sqrt{n + 1} + \sqrt{n}} = \frac{1}{\sqrt{n + 1} + \sqrt{n}} < \frac{1}{2\sqrt{n}}.
$$

要使 $\frac{1}{2\sqrt{n}} < \varepsilon$，即 $\sqrt{n} > \frac{1}{2\varepsilon}$，即 $n > \frac{1}{4 \varepsilon^2}$。

取 $N = \lceil \frac{1}{4\varepsilon^2} \rceil$，$\forall n > N$ 上式成立。$\blacksquare$

### 第 4 题

**证明：** 任给 $\varepsilon > 0$。
$$
\left| \frac{(-1)^n}{n^2 + 5} - 0 \right| = \frac{1}{n^2 + 5} < \frac{1}{n^2} \leq \frac{1}{n}.
$$

（第二个不等式因 $n \geq 1$ 时 $n^2 \geq n$。）

取 $N = \lceil 1/\varepsilon \rceil$ 即可。$\blacksquare$

</details>

## 考察点

- [[ANL-DEF-004]] ε-N 定义的构造性使用
- 通过代数化简把 $|a_n - L|$ 表达为 $1/n$ 量级的标准技巧
- "找 $N$ 不要求最优"——只要满足条件即可

## 备注

ε-N 直接证明的标准模板：

1. 计算 $|a_n - L|$。
2. 用代数手段化简（约分、分子有理化、放大）。
3. 找一个**简单且单调**的上界 $\phi(n)$，使 $|a_n - L| < \phi(n)$。
4. 解 $\phi(n) < \varepsilon$，得 $n > h(\varepsilon)$。
5. 取 $N = \lceil h(\varepsilon) \rceil$ 即可。
