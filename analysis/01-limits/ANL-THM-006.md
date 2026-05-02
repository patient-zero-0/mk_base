---
title: "单调有界定理"
type: theorem
id: ANL-THM-006
subject: analysis
chapter: 01-limits
tags:
  - 极限
  - 完备性
  - 单调
depends:
  - ANL-DEF-003
  - ANL-DEF-004
  - ANL-DEF-005
uses:
  - ANL-AX-001
status: draft
source: "华东师范大学《数学分析》第5版 §2.4"
difficulty: 3
related:
  - ANL-THM-007
applications:
  - "数值分析：迭代法收敛性的标准论证手法"
  - "经济学：边际递减效用模型中长期效用的存在性"
---

## 条件

> 设 $\{a_n\}$ 是单调递增的实数列，且**有上界**，即存在 $M \in \mathbb{R}$ 使得 $a_n \leq M$ 对所有 $n$ 成立。

## 结论

> 则 $\{a_n\}$ 收敛，且
> $$
> \lim_{n \to \infty} a_n = \sup_{n \geq 1} a_n.
> $$

对单调递减且有下界的数列，结论对应为收敛于 $\inf_n a_n$。

## 几何/直觉理解

把数列想成"只往上爬、被天花板挡住的人"：

- 爬不停（单调），又跑不出去（有界）→ 必然贴近天花板停下；
- 而"天花板"中**最低的那块**就是 $\sup_n a_n$。

**两个条件缺一不可**：

- 单调但无界（如 $a_n = n$）→ 跑向无穷；
- 有界但不单调（如 $(-1)^n$）→ 来回振荡。

只有同时满足，才能"既不跑掉、也不乱跳"。

## 证明

**证明：** 由有界性，集合 $S = \{a_n : n \in \mathbb{N}^*\}$ 非空且有上界。
据 [[ANL-AX-001]] 确界原理，$L := \sup S$ 存在于 $\mathbb{R}$。
下证 $\displaystyle \lim_{n \to \infty} a_n = L$。

任取 $\varepsilon > 0$。由 $L$ 是最小上界，$L - \varepsilon$ 不再是上界，
故存在 $N \in \mathbb{N}^*$ 使得 $a_N > L - \varepsilon$。

对一切 $n > N$，由单调性 $a_n \geq a_N > L - \varepsilon$；
又因 $L$ 是上界，$a_n \leq L < L + \varepsilon$。两侧合并：
$$
L - \varepsilon < a_n \leq L \implies |a_n - L| < \varepsilon.
$$

由 $\varepsilon$ 任意，依 [[ANL-DEF-004]]，$\displaystyle \lim_{n \to \infty} a_n = L = \sup_n a_n$。$\blacksquare$

## 常见错误

- ✗ 在 $\mathbb{Q}$ 上使用确界原理。
  反例：$a_n = (1 + 1/n)^n \in \mathbb{Q}$ 单调有界，但极限 $e \notin \mathbb{Q}$。
  原因：定理依赖 $\mathbb{R}$ 的完备性（[[ANL-AX-001]]），$\mathbb{Q}$ 缺此性质。
- ✗ 只验证"前若干项单调"或"从某项起单调"就直接套用。
  从 $N_0$ 起单调有界确实仍能用——但应明确丢弃前 $N_0 - 1$ 项后再应用本定理，避免与"全程单调"混淆。
- ✗ 把"单调有界"换成"有界递增子列存在"。
  反例：$a_n = (-1)^n + 1/n$ 不单调，但有递增子列且有界——原数列本身不收敛。

## 推论与应用

- 直接推论：单调递减有下界的数列收敛于 $\inf_n a_n$
- 用于证明 $e$ 的存在性、迭代法收敛性、变分序列收敛性

## 跨专业应用

- **数值分析**：Picard 迭代、二分法等算法的收敛性论证
- **经济学**：边际效用递减下累积效用 $\sum u_n$ 部分和数列单调有上界 → 长期效用存在
