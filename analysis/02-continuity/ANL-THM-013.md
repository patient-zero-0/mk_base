---
title: "介值定理（Intermediate Value Theorem, IVT）"
type: theorem
id: ANL-THM-013
subject: analysis
chapter: 02-continuity
tags:
  - 连续
  - IVT
  - 闭区间
depends:
  - ANL-DEF-012
uses:
  - ANL-AX-001
status: draft
source: "华东师范大学《数学分析》第5版 §4.2"
difficulty: 3
related:
  - ANL-THM-014
  - ANL-THM-015
applications:
  - "数值分析：二分法寻根的理论基础"
  - "经济学：连续效用函数的均衡价格存在性"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设 $f : [a, b] \to \mathbb{R}$ 在闭区间 $[a, b]$ 上**连续**（按 [[ANL-DEF-012]]），
$f(a) \neq f(b)$，$\eta$ 介于 $f(a)$ 与 $f(b)$ 之间（即 $\min\{f(a), f(b)\} < \eta < \max\{f(a), f(b)\}$）。

## 结论

> 存在 $\xi \in (a, b)$ 使 $f(\xi) = \eta$。

特别地（**零点定理**）：若 $f(a) \cdot f(b) < 0$，则存在 $\xi \in (a, b)$ 使 $f(\xi) = 0$。

## 几何/直觉理解

把 $f$ 的图像想成一条不能"跳跃"的连续曲线，从 $(a, f(a))$ 一笔画到 $(b, f(b))$。
设想 $f(a) < \eta < f(b)$，画一条水平直线 $y = \eta$。
连续曲线从 $\eta$ 之**下**走到 $\eta$ 之**上**——既然不许跳跃，**必然穿过**水平线。
穿过点的横坐标即为所求 $\xi$。

**两个条件缺一不可**：

- 仅闭区间不连续：反例 $f(x) = \mathrm{sgn}(x)$ 在 $[-1, 1]$ 上从 $-1$ 跳到 $1$，跳过了 $\eta = 0$。
- 仅连续但区间无界 / 不闭：本定理可推广到任意区间，但需重新分析端点行为。

## 证明（区间二分法 / 构造性证明）

**证明：** 不失一般性设 $f(a) < \eta < f(b)$。考虑集合
$$
S = \{x \in [a, b] : f(x) < \eta\}.
$$
$a \in S$（因 $f(a) < \eta$），$S \subseteq [a, b]$ 故有上界 $b$。由 [[ANL-AX-001]]，$\xi := \sup S$ 存在。

显然 $\xi \in [a, b]$。下证 $f(\xi) = \eta$。

**第一步：** $f(\xi) \leq \eta$。
对任意 $\varepsilon > 0$，由 $\xi = \sup S$ 知 $\xi - \varepsilon$ 不再是上界，故 $\exists x_\varepsilon \in S \cap (\xi - \varepsilon, \xi]$，即 $f(x_\varepsilon) < \eta$ 且 $|x_\varepsilon - \xi| < \varepsilon$。
让 $\varepsilon \to 0$ 得 $x_\varepsilon \to \xi$；由 $f$ 在 $\xi$ 连续，$f(x_\varepsilon) \to f(\xi)$。
取极限并用保号性：$f(\xi) \leq \eta$。

**第二步：** $f(\xi) \geq \eta$。
若 $\xi = b$，由 $f(b) > \eta$ 直接得 $f(\xi) > \eta$，结合第一步矛盾——故 $\xi < b$。
对 $x \in (\xi, b]$，由 $\xi = \sup S$ 知 $x \notin S$，即 $f(x) \geq \eta$。
由 $f$ 在 $\xi$ 右连续：取 $x \to \xi^+$，得 $f(\xi) \geq \eta$。

**结论：** $f(\xi) = \eta$。又因 $f(a) < \eta = f(\xi)$，$\xi \neq a$；类似 $\xi \neq b$。故 $\xi \in (a, b)$。$\blacksquare$

## 常见错误

- ✗ 把"连续"换成"可微"或"单调"。可微 ⇒ 连续，故可微版本是本定理的**特例**；单调连续函数的 IVT 反而更强（结论可加强为"恰好一个 $\xi$"）。
- ✗ 把闭区间 $[a, b]$ 换成开区间 $(a, b)$ 仍直接套用。
  反例：$f(x) = 1/x$ 在 $(0, 1)$ 上连续，$f(0^+) = +\infty, f(1) = 1$，但定义域不是闭区间，谈不上 $f(a)$。
- ✗ 误用反向："若 $\eta = f(\xi)$ 对某 $\xi$ 成立，则 $\eta$ 在 $f(a), f(b)$ 之间"。
  反例：$f(x) = \sin(\pi x)$ 在 $[0, 2]$ 上 $f(0) = f(2) = 0$，但 $f(0.5) = 1$ 不在区间端点值"之间"。
  本定理给出**单向**蕴含。

## 推论

- **零点定理（Bolzano）**：连续函数若两端点函数值反号，区间内有零点。
- **不动点定理（一维）**：连续函数 $f : [a, b] \to [a, b]$ 必有不动点 $\xi = f(\xi)$（应用 IVT 到 $g(x) = f(x) - x$）。
- **介值像区间**：连续函数把闭区间映为闭区间（结合 [[ANL-THM-014]] 最值定理）。

## 链接

- 前置：[[ANL-DEF-012]]、[[ANL-AX-001]]
- 姐妹定理：[[ANL-THM-014]] 最值定理、[[ANL-THM-015]] Cantor 一致连续定理
- 公理依据：实数完备性 [[ANL-AX-001]]——在 $\mathbb{Q}$ 中 IVT 失效（如 $f(x) = x^2 - 2$ 在 $\mathbb{Q} \cap [1, 2]$ 上无零点）

## 跨专业应用

- **数值分析**：**二分法**寻根算法的理论基础——本定理保证零点存在，区间二分给出收敛构造
- **经济学**：连续供需函数 → 均衡价格存在（应用零点定理到超额需求函数）
- **博弈论**：Brouwer 不动点定理（高维 IVT 推广）→ Nash 均衡存在性
