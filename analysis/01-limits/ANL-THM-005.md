---
title: "数列夹逼定理（夹挤定理）"
type: theorem
id: ANL-THM-005
subject: analysis
chapter: 01-limits
tags:
  - 极限
  - 夹逼
  - 基础定理
depends:
  - ANL-DEF-004
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §2.2"
difficulty: 2
related:
  - ANL-EX-001
applications:
  - "数值分析：截断误差的上下界控制"
  - '概率论：随机变量收敛的"夹逼"判定'
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $\{a_n\}, \{b_n\}, \{c_n\}$ 是实数列，满足：

1. **夹挤关系**：$\exists N_0, \forall n > N_0: a_n \leq b_n \leq c_n$；
2. **同一极限**：$a_n \to L$ 且 $c_n \to L$（同一个 $L$）。

## 结论

> $b_n \to L$。

## 几何/直觉理解

把三个数列想成三辆车：$\{a_n\}$ 在最下面，$\{c_n\}$ 在最上面，$\{b_n\}$ 被夹在中间。
若上下两辆车都开向同一个目的地 $L$，那么中间这辆**没得选**，必须也开向 $L$。

**两个条件缺一不可**：

- 仅有夹挤而极限不同：例如 $a_n = 0, c_n = 1, b_n = (-1)^n / 2 + 1/2$，无法判定 $b_n$ 极限。
- 仅有相同极限而无夹挤关系：例如 $a_n = 1/n \to 0$, $c_n = 1/n \to 0$, 但 $b_n = (-1)^n$ 不被夹住。

## 证明

**证明：** 任给 $\varepsilon > 0$。

由 $a_n \to L$：$\exists N_1, \forall n > N_1: L - \varepsilon < a_n < L + \varepsilon$。
由 $c_n \to L$：$\exists N_2, \forall n > N_2: L - \varepsilon < c_n < L + \varepsilon$。

取 $N = \max\{N_0, N_1, N_2\}$。对任意 $n > N$：
$$
L - \varepsilon < a_n \leq b_n \leq c_n < L + \varepsilon \implies |b_n - L| < \varepsilon.
$$

依 [[ANL-DEF-004]]，$b_n \to L$。$\blacksquare$

## 常见错误

- ✗ 把"两侧极限同为 $L$"弱化为"$a_n - c_n \to 0$"。
  反例：$a_n = n, c_n = n + 1/n$，差趋于 0，但都不收敛，无法直接得到 $b_n$ 收敛。必须**都收敛于同一具体值**。
- ✗ 忽视"从某项起"的限定。
  反例：若仅在 $n \leq 100$ 处满足夹挤、之后不满足，结论不成立。
  夹挤关系只需"最终成立"——但必须最终成立。

## 应用要点

夹逼定理常配合**已知极限的标准数列**使用：

| 已知 | 典型应用 |
|---|---|
| $1/n \to 0$ | 夹住 $\sin(n)/n$、$\cos(n)/n$ 等振荡 / 衰减项 |
| $r^n \to 0$（$\|r\| < 1$） | 夹住几何衰减项 |
| $1/n^k \to 0$ | 夹住多项式衰减项 |
| $(1 + 1/n)^n \to e$ | 配合估计指数型表达式 |

例题见 [[ANL-EX-001]]。

## 链接

- 推广：函数极限的夹逼定理（待建）
- 与 [[ANL-THM-006]] 单调有界定理并列为求极限的两大基本工具

## 跨专业应用

- **数值分析**：当算法误差被两个易估上下界夹住，误差极限可由两端夹逼判定
- **概率论**：随机变量序列的几乎处处收敛常通过夹逼上下控制变量得到
