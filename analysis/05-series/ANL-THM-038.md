---
title: "正项级数的比较判别法"
type: theorem
id: ANL-THM-038
subject: analysis
chapter: 05-series
tags:
  - 级数
  - 正项级数
  - 比较判别法
depends:
  - ANL-DEF-033
  - ANL-THM-006
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §12.2"
difficulty: 3
related:
  - ANL-THM-037
  - ANL-DEF-034
applications:
  - "数值分析：以 p-级数 / 几何级数为标尺估计算法误差级数的敛散"
  - "概率论：判定离散随机变量矩级数 $\\sum n^k p_n$ 是否收敛（期望、方差是否存在）"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

> 设 $\sum a_n$ 与 $\sum b_n$ 均为**正项级数**（$a_n \ge 0,\ b_n \ge 0$），且从某项 $N_0$ 起满足
> $$
> 0 \le a_n \le b_n \quad (n \ge N_0).
> $$

## 结论

> 1. **（基本形）** 若 $\sum b_n$ 收敛，则 $\sum a_n$ 收敛；
>    等价地（逆否），若 $\sum a_n$ 发散，则 $\sum b_n$ 发散。
>
> 2. **（极限形）** 若 $a_n, b_n > 0$ 且 $\displaystyle \lim_{n \to \infty} \frac{a_n}{b_n} = \ell$，则
>    - $0 < \ell < +\infty$：$\sum a_n$ 与 $\sum b_n$ **同敛散**；
>    - $\ell = 0$：$\sum b_n$ 收敛 $\Rightarrow$ $\sum a_n$ 收敛；
>    - $\ell = +\infty$：$\sum b_n$ 发散 $\Rightarrow$ $\sum a_n$ 发散。

## 几何/直觉理解

正项级数的部分和 $\{S_n\}$ 是**单调递增**的（每加一个非负项只增不减），因此由单调有界定理（[[ANL-THM-006]]）：**正项级数收敛 $\iff$ 部分和有上界**。这把收敛判定简化为"是否有界"的问题。

比较判别法就是"**大的收敛，小的更收敛；小的发散，大的更发散**"：

- 若被一个收敛级数 $\sum b_n$ 从上方控制，则 $\sum a_n$ 的部分和也被压在有限范围内，故收敛；
- 若它从上方控制一个发散级数，则自己的部分和也被顶到无穷，故发散。

**极限形**是基本形的实用升级：只要 $a_n$ 与 $b_n$ **同阶无穷小**（$a_n/b_n \to \ell \in (0,\infty)$），二者敛散一致。这使我们能拿待判级数与标准级数（几何级数、$p$-级数）比"阶数"，而不必死磕逐项不等式。

## 证明

**第 1 部分（基本形）。** 不妨设 $a_n \le b_n$ 对一切 $n \ge 1$ 成立（改变有限项不影响敛散）。记部分和 $A_n = \sum_{k=1}^n a_k,\ B_n = \sum_{k=1}^n b_k$，二者均单调递增。由 $a_n \le b_n$ 得 $A_n \le B_n$。

设 $\sum b_n$ 收敛，则 $\{B_n\}$ 收敛，故有上界 $M$：$B_n \le M$。于是 $A_n \le B_n \le M$，即 $\{A_n\}$ 单调递增且有上界。由单调有界定理（[[ANL-THM-006]]），$\{A_n\}$ 收敛，即 $\sum a_n$ 收敛。

逆否命题（$\sum a_n$ 发散 $\Rightarrow \sum b_n$ 发散）由上述等价转述即得。$\qquad\blacksquare$

**第 2 部分（极限形）。** 设 $a_n, b_n > 0$，$\dfrac{a_n}{b_n} \to \ell$。

**$0 < \ell < +\infty$：** 取 $\varepsilon = \dfrac{\ell}{2} > 0$，存在 $N$ 使 $n \ge N$ 时 $\left|\dfrac{a_n}{b_n} - \ell\right| < \dfrac{\ell}{2}$，即
$$
\frac{\ell}{2} b_n < a_n < \frac{3\ell}{2} b_n \quad (n \ge N).
$$
由右不等式与第 1 部分：$\sum b_n$ 收敛 $\Rightarrow \sum a_n$ 收敛；由左不等式：$\sum a_n$ 收敛 $\Rightarrow \sum b_n$ 收敛。故同敛散。

**$\ell = 0$：** 取 $\varepsilon = 1$，存在 $N$ 使 $n \ge N$ 时 $a_n < b_n$。由第 1 部分，$\sum b_n$ 收敛 $\Rightarrow \sum a_n$ 收敛。

**$\ell = +\infty$：** 则 $\dfrac{b_n}{a_n} \to 0$，由上一情形（角色互换），$\sum a_n$ 收敛 $\Rightarrow \sum b_n$ 收敛；逆否即 $\sum b_n$ 发散 $\Rightarrow \sum a_n$ 发散。$\qquad\blacksquare$

## 常见错误

- ✗ 把判别法用于**非正项级数**。本判别法**仅对正项级数**（或同号级数）成立，因核心是"部分和单调"。
    **反例**：$a_n = \dfrac{(-1)^n}{\sqrt n},\ b_n = \dfrac{1}{\sqrt n}$，$|a_n| \le b_n$ 但 $\sum b_n$ 发散，不能推出 $\sum a_n$ 敛散（实际 $\sum a_n$ 条件收敛，见 [[ANL-DEF-034]]）。对一般级数应先取绝对值再比较。
- ✗ 极限形中 $\ell = 0$ 却由"$\sum b_n$ **发散**"推 $\sum a_n$ 发散。$\ell = 0$ 时只有"收敛方向"可用：$\sum b_n$ 收敛 $\Rightarrow \sum a_n$ 收敛，反向无效。
- ✗ 只验证有限个 $n$ 的不等式 $a_n \le b_n$ 就下结论。需**从某项起恒成立**（对一切大 $n$）。
- ✗ 忘记"改变有限项不影响敛散"，纠结前几项不满足不等式。

## 推论与应用

- 与标准级数比较是判敛散的主力工具：几何级数 $\sum r^n$（$|r|<1$ 收敛）、$p$-级数 $\sum 1/n^p$（$p>1$ 收敛，$p \le 1$ 发散）
- 极限形把"逐项不等式"放宽为"同阶估计"，配合等价无穷小极为高效
- 为绝对收敛判定（[[ANL-DEF-034]]）提供逐项控制手段

## 跨专业应用

- **数值分析**：用 $p$-级数 / 几何级数作"标尺"估计算法误差级数的敛散
- **概率论**：判定离散随机变量矩级数 $\sum n^k p_n$ 是否收敛（期望、方差是否存在）
