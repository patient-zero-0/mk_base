---
title: "Taylor 级数与 Maclaurin 级数"
type: definition
id: ANL-DEF-039
subject: analysis
chapter: 05-series
tags:
  - 级数
  - Taylor 级数
  - Maclaurin 级数
depends:
  - ANL-DEF-037
  - ANL-DEF-017
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §14.2"
difficulty: 3
related:
  - ANL-THM-025
  - ANL-THM-046
applications: []
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设函数 $f$ 在 $x_0$ 的某邻域内**任意阶可导**（[[ANL-DEF-017]]）。称幂级数（[[ANL-DEF-037]]）
$$
\sum_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n = f(x_0) + f'(x_0)(x-x_0) + \frac{f''(x_0)}{2!}(x-x_0)^2 + \cdots
$$
为 $f$ 在 $x_0$ 处的 **Taylor 级数**。当 $x_0 = 0$ 时，称
$$
\sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n
$$
为 $f$ 的 **Maclaurin 级数**。

**收敛到 $f$ 的判据**：Taylor 级数在 $x$ 处收敛于 $f(x)$ **当且仅当** Taylor 公式（[[ANL-THM-025]]）的余项趋于零：
$$
R_n(x) = f(x) - \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!}(x-x_0)^k \xrightarrow{n\to\infty} 0.
$$

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| Taylor 公式（[[ANL-THM-025]]） | **有限**展开 $+$ 余项 $R_n$；对有限阶可导即可 |
| Taylor 级数 | **无穷**幂级数；要求任意阶可导 |
| "Taylor 级数收敛" | 幂级数自身有非零收敛半径 |
| "Taylor 级数收敛到 $f$" | 还需 $R_n(x) \to 0$（更强！） |

> **致命陷阱**：Taylor 级数收敛 $\ne$ 收敛到 $f$。见下方 $e^{-1/x^2}$ 反例。

## 直觉理解

Taylor 级数是"**用一点的全部导数信息去重建整个函数**"的尝试：在 $x_0$ 处测得 $f$ 的值、斜率、曲率……（各阶导数），用它们作系数拼出一个幂级数，希望它就等于 $f$。

但这个"重建"可能**失败**——关键在余项 $R_n$ 是否消失：

- **解析函数**（如 $e^x, \sin x, \cos x$）：$R_n \to 0$，Taylor 级数在收敛区间内**忠实还原** $f$；
- **病态反例**：
    $$
    f(x) = \begin{cases} e^{-1/x^2}, & x \ne 0, \\ 0, & x = 0 \end{cases}
    $$
    在 $x_0=0$ 处**所有阶导数都为 $0$**，故其 Maclaurin 级数恒为 $0$；该级数处处收敛，却只在 $x=0$ 一点等于 $f$。此时 Taylor 级数"存在且收敛"，但**完全没还原** $f$。

> 这解释了为何"是否收敛到 $f$"必须回到余项估计（[[ANL-THM-025]]）——光有级数收敛远远不够。一个无穷可导却非解析的函数，其全部导数信息也"漏掉"了它在中心之外的形状。

## 链接

- 作为特殊幂级数：[[ANL-DEF-037]]
- 系数所需的高阶导数：[[ANL-DEF-017]]
- 收敛到 $f$ 的余项判据：[[ANL-THM-025]] Taylor 公式
- 收敛区间内的逐项运算：[[ANL-THM-046]]
