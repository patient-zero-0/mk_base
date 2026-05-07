---
title: "数列极限的唯一性"
type: theorem
id: ANL-THM-001
subject: analysis
chapter: 01-limits
tags:
  - 极限
  - 唯一性
  - 基础定理
depends:
  - ANL-DEF-004
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §2.1"
difficulty: 2
related:
  - ANL-THM-002
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $\{a_n\}$ 是实数列，假设 $a_n \to L$ 且 $a_n \to L'$（按 [[ANL-DEF-004]]）。

## 结论

> $L = L'$。即收敛数列的极限**唯一**。

## 直觉理解

如果数列同时"贴近 $L$"和"贴近 $L'$"——可一根无穷数列没法同时贴近两个不同的点。
形式化：取 $\varepsilon$ 小于两点距离的一半，从某项起所有项必须**同时**落入两个不相交的小邻域，矛盾。

直观图像：把 $\varepsilon$ 看作"分辨率"。$L \neq L'$ 时存在足够小的 $\varepsilon$ 把它们分开，而极限要求"几乎全部项落入 $L$ 邻域"——同时也要求"几乎全部项落入 $L'$ 邻域"，不可能。

## 证明

**证明：** 反证。设 $L \neq L'$，记 $\varepsilon_0 = |L - L'| / 2 > 0$。

由 $a_n \to L$，存在 $N_1$ 使 $\forall n > N_1: |a_n - L| < \varepsilon_0$。
由 $a_n \to L'$，存在 $N_2$ 使 $\forall n > N_2: |a_n - L'| < \varepsilon_0$。

取 $N = \max\{N_1, N_2\}$，对任意 $n > N$：
$$
|L - L'| \leq |L - a_n| + |a_n - L'| < \varepsilon_0 + \varepsilon_0 = |L - L'|.
$$

得 $|L - L'| < |L - L'|$，矛盾。故 $L = L'$。$\blacksquare$

## 常见错误

- ✗ 把"极限唯一"等同于"序列只趋向一个值"——前者是**结论**，后者是定义本身。
  唯一性需要**证明**，因为定义只说"存在 $L$ 使 …"，不直接排除多个 $L$。
- ✗ 推广到"序列任何积聚点也唯一"——错。$\{(-1)^n\}$ 有两个积聚点 $\pm 1$，但既然没有极限就不违反唯一性。
  唯一性的前提是**收敛**。

## 链接

- 用于定理：[[ANL-THM-002]] 收敛数列必有界（论证依赖唯一性）
- 推广至函数极限、度量空间极限等场景
