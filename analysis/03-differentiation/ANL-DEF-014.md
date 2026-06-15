---
title: "导数"
type: definition
id: ANL-DEF-014
subject: analysis
chapter: 03-differentiation
tags:
  - 微分
  - 导数
  - 极限
depends:
  - ANL-DEF-008
  - ANL-DEF-012
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §4.1"
difficulty: 2
related:
  - ANL-DEF-015
  - ANL-DEF-016
applications:
  - "物理：瞬时速度、加速度作为位置/速度对时间的导数"
  - "经济学：边际成本、边际效用——产量微小变化下的收益变化率"
  - "工程：误差传播的一阶近似（微分形式）"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义陈述

设 $f : I \to \mathbb{R}$，$I$ 为开区间，$x_0 \in I$。若极限
$$
f'(x_0) := \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}
$$
存在（且有限），则称 $f$ 在 $x_0$ **可导**，称该极限值为 $f$ 在 $x_0$ 的**导数**，
记作 $f'(x_0)$ 或 $\dfrac{df}{dx}\bigg|_{x=x_0}$。

若 $f$ 在 $I$ 的每一点可导，则得到**导函数** $f' : I \to \mathbb{R}$。

**ε-δ 等价表述**：$f'(x_0) = A$ 当且仅当
$$
\forall \varepsilon > 0,\ \exists \delta > 0:\ 0 < |\Delta x| < \delta \implies \left| \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} - A \right| < \varepsilon.
$$

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 在 $x_0$ 连续 [[ANL-DEF-012]] | 仅要求 $\lim_{x \to x_0} f(x) = f(x_0)$，不涉及变化率 |
| 在 $x_0$ 可导 | 要求差商极限存在——比连续严格 |
| 单侧导数 [[ANL-DEF-016]] | 把极限改为 $\Delta x \to 0^+$ 或 $0^-$ |
| 微分 [[ANL-DEF-015]] | 是导数与自变量微元的乘积 $dy = f'(x) \, dx$，**结果是一个量**，不是过程 |

## 直觉理解

> 导数 $= $ **瞬时变化率** $= $ 函数图像在该点切线的斜率。
>
> 差商 $\dfrac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$ 是过 $(x_0, f(x_0))$ 与
> $(x_0 + \Delta x, f(x_0 + \Delta x))$ 两点**割线**的斜率。
> 让 $\Delta x \to 0$，割线"绕 $(x_0, f(x_0))$ 旋转"逼近**切线**，
> 切线斜率即 $f'(x_0)$。

**核心意义**：导数把"函数在一点附近的局部行为"压缩成单个数。
若 $f'(x_0) > 0$，函数在 $x_0$ 附近"上行"；若 $f'(x_0) = 0$，函数在 $x_0$ 处"局部水平"，
是极值候选点（[[ANL-THM-020]]）；若 $f'(x_0) < 0$，函数"下行"。

**量词顺序**：先给 $\varepsilon$，再找 $\delta$。$\delta$ 依赖于 $\varepsilon$（且通常依赖 $x_0$），
含义是"差商误差可任意小"。

## 链接

- 前置：[[ANL-DEF-008]] 函数极限、[[ANL-DEF-012]] 函数连续
- 直接推论：[[ANL-THM-016]] 可导 ⇒ 连续
- 计算工具：[[ANL-THM-017]] 求导四则运算、[[ANL-THM-018]] 链式法则
- 例题：[[ANL-EX-008]]

## 跨专业应用

- **物理**：位置 $s(t)$ 对时间的导数 $s'(t)$ 是瞬时速度；速度对时间的导数是加速度
- **经济学**：成本函数 $C(q)$ 的导数 $C'(q)$ 是边际成本（多生产 1 单位的额外成本）
- **工程**：测量误差 $\Delta x$ 经函数 $f$ 后近似传播为 $\Delta y \approx f'(x_0)\,\Delta x$
