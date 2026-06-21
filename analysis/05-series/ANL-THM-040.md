---
title: "根值判别法（Cauchy 判别法）"
type: theorem
id: ANL-THM-040
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 正项级数
  - 根值判别法
depends:
  - ANL-DEF-033
  - ANL-THM-038
  - ANL-THM-036
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §12.2"
difficulty: 3
related:
  - ANL-THM-039
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

> 设 $\sum a_n$ 为正项级数，$a_n \ge 0$。记
> $$
> q = \lim_{n \to \infty} \sqrt[n]{a_n} \quad (\text{允许 } q = +\infty)
> $$
> （更一般地可取上极限 $q = \varlimsup_{n\to\infty} \sqrt[n]{a_n}$，结论不变）。

## 结论

> - 若 $q < 1$，则 $\sum a_n$ **收敛**；
> - 若 $q > 1$（含 $q = +\infty$），则 $\sum a_n$ **发散**；
> - 若 $q = 1$，本判别法**失效**。

## 几何/直觉理解

根值 $\sqrt[n]{a_n}$ 直接问："若把 $a_n$ 看成某公比的 $n$ 次幂，这个公比是多少？"——即 $a_n \approx q^n$。于是与几何级数 $\sum q^n$ 比较（[[ANL-THM-038]]）：$q<1$ 收敛、$q>1$ 发散。

根值判别法特别适合通项本身带 **$n$ 次幂结构**的级数，如 $\sum \left(\frac{n}{2n+1}\right)^n$、$\sum \frac{1}{(\ln n)^n}$——开 $n$ 次方后幂次直接脱去。

> **比值与根值的强弱**：凡比值判别法能判定（$\lim \frac{a_{n+1}}{a_n} = q \ne 1$）者，根值判别法必能判定且给出同一个 $q$（因 $\lim \frac{a_{n+1}}{a_n} = q \Rightarrow \lim \sqrt[n]{a_n} = q$）。但反之不然：存在比值振荡（极限不存在）而根值仍可判定的级数。故**根值判别法严格强于比值判别法**——代价是根号常比相邻项之比更难算。

## 证明

**证明：**

**情形 $q < 1$。** 取 $r$ 使 $q < r < 1$。由（上）极限定义，存在 $N$，使 $n \ge N$ 时 $\sqrt[n]{a_n} < r$，即
$$
a_n < r^n \quad (n \ge N).
$$
右端为公比 $r \in (0,1)$ 的几何级数（收敛）。由比较判别法（[[ANL-THM-038]]），$\sum a_n$ 收敛。

**情形 $q > 1$。** 则有无穷多个 $n$ 使 $\sqrt[n]{a_n} > 1$，即 $a_n > 1$。故 $a_n \not\to 0$，由收敛必要条件（[[ANL-THM-036]]）的逆否，$\sum a_n$ 发散。

**情形 $q = 1$。** 见反例，无法判定。$\qquad\blacksquare$

## 常见错误

- ✗ $q = 1$ 时下结论。**反例**：$\sum 1/n$ 与 $\sum 1/n^2$ 均有 $\sqrt[n]{a_n} \to 1$（因 $\sqrt[n]{n} \to 1$），却一发散一收敛。
- ✗ 误以为比值判别法（[[ANL-THM-039]]）失效时根值也必失效。根值更强：比值 $=1$ 或振荡时，根值仍可能给出 $q \ne 1$。
- ✗ 对非正项级数直接套用。应考察 $\sqrt[n]{|a_n|}$ 判断**绝对收敛**。
- ✗ 用普通极限而忽略上极限版本。当 $\sqrt[n]{a_n}$ 无极限时，须用 $\varlimsup$ 形式，结论仍成立。

## 推论与应用

- 与比值判别法（[[ANL-THM-039]]）互补：含 $n$ 次幂用根值，含阶乘用比值
- 是 Cauchy–Hadamard 幂级数收敛半径公式 $R = 1 / \varlimsup \sqrt[n]{|c_n|}$ 的直接来源

## 跨专业应用

- **信息论 / 编码**：码字数量的指数增长率（信道容量）用根式刻画
- **动力系统**：判定轨道级数的收敛，根值即 Lyapunov 型指数
