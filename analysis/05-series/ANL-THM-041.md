---
title: "积分判别法（Cauchy 积分判别法）"
type: theorem
id: ANL-THM-041
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 正项级数
  - 积分判别法
depends:
  - ANL-DEF-033
  - ANL-DEF-029
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §12.2"
difficulty: 3
related:
  - ANL-THM-035
  - ANL-THM-038
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

> 设 $f : [1, +\infty) \to \mathbb{R}$ **非负、单调递减**，且令 $a_n = f(n)$。

## 结论

> 级数 $\sum_{n=1}^{\infty} a_n$ 与反常积分（[[ANL-DEF-029]]）$\displaystyle \int_1^{\infty} f(x)\,dx$ **同敛散**。

更进一步，部分和与积分的差
$$
d_n := \sum_{k=1}^{n} a_k - \int_1^{n} f(x)\,dx
$$
单调递减且有界，故 $\lim_{n\to\infty} d_n$ 存在（这正是 Euler 常数 $\gamma$ 的来源，见应用）。

## 几何/直觉理解

把级数 $\sum f(n)$ 看成一排**宽为 $1$、高为 $f(n)$ 的矩形面积之和**，把积分 $\int_1^\infty f$ 看成曲线 $y=f(x)$ 下方的面积。$f$ 单调递减时，矩形面积与曲边面积**互相夹逼**：

$$
\int_{n}^{n+1} f(x)\,dx \le f(n) \le \int_{n-1}^{n} f(x)\,dx.
$$

（左：矩形以右端点高 $f(n)$ 为高，被压在曲线下；右：以左端点高为高，盖住曲线。）

于是"无穷个矩形面积之和有限 $\iff$ 曲线下总面积有限"——级数与积分的敛散被牢牢绑定。这把**离散求和**问题转化为可用 Newton–Leibniz 求原函数的**连续积分**问题，是判定 $p$-级数等的最锐利工具。

## 证明

**证明：** 因 $f$ 非负递减，对整数 $k \ge 2$，在 $[k-1, k]$ 上 $f(k) \le f(x) \le f(k-1)$，积分得
$$
f(k) \le \int_{k-1}^{k} f(x)\,dx \le f(k-1).
$$

**对左端求和**（$k = 2$ 到 $n$）：
$$
\sum_{k=2}^{n} a_k \le \int_1^{n} f(x)\,dx. \tag{1}
$$

**对右端求和**（$k = 2$ 到 $n$）：
$$
\int_1^{n} f(x)\,dx \le \sum_{k=2}^{n} a_{k-1} = \sum_{k=1}^{n-1} a_k. \tag{2}
$$

记 $S_n = \sum_{k=1}^n a_k$，$I_n = \int_1^n f$。由 (1)(2)：
$$
S_n - a_1 \le I_n \le S_{n-1}. \tag{3}
$$

- 若 $\int_1^\infty f$ **收敛**：$\{I_n\}$ 有上界，由 (3) 左式 $S_n \le a_1 + I_n$ 有上界。正项级数部分和单调递增有上界 ⇒ 收敛。
- 若 $\int_1^\infty f$ **发散**（$f \ge 0$ ⇒ $I_n \to +\infty$）：由 (3) 右式 $S_{n-1} \ge I_n \to +\infty$ ⇒ $\sum a_n$ 发散。

故二者同敛散。

**关于 $d_n$**：由 $d_n - d_{n-1} = a_n - \int_{n-1}^{n} f \le 0$（左不等式 $f(n) \le \int_{n-1}^n f$）知 $\{d_n\}$ 递减；又由 (3) 右式 $I_n \le S_{n-1}$ 得 $d_n = S_n - I_n \ge S_n - S_{n-1} = a_n \ge 0$，故 $\{d_n\}$ 有下界 $0$。单调递减有下界 ⇒ $\{d_n\}$ 收敛。$\qquad\blacksquare$

## 常见错误

- ✗ 忽略**单调递减**前提就用积分。若 $f$ 非单调，矩形与积分的夹逼失效。**反例**：$f$ 在整数点取 $0$、在别处取大值，则 $\sum f(n) = 0$ 收敛而 $\int f$ 可发散。
- ✗ 忘记 $f$ 须**非负**。变号时积分判别法不适用（积分与求和的单调性论证崩溃）。
- ✗ 误认为"级数的和 $=$ 积分的值"。二者只**同敛散**，数值一般不等（差为 $\lim d_n$，如 $\gamma$）。
- ✗ 从有限项起 $f$ 才单调递减也可用（改变有限项不影响敛散），却误以为必须全程单调。

## 推论与应用

- **$p$-级数判定**（[[ANL-THM-038]] 的标尺由此确立）：$\sum_{n=1}^\infty \dfrac{1}{n^p}$ 收敛 $\iff p > 1$（详见例题）
- **对数 $p$-级数**：$\sum \dfrac{1}{n (\ln n)^p}$ 收敛 $\iff p > 1$
- **Euler–Mascheroni 常数**：取 $f(x) = 1/x$，$d_n = \sum_{k=1}^n \frac1k - \ln n \to \gamma \approx 0.5772$

## 跨专业应用

- **算法分析**：调和级数 $\sum 1/k \approx \ln n$ 给出快排等算法的平均比较次数
- **物理**：用积分估计离散能级求和（配分函数的连续近似）
