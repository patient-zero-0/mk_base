---
title: "复合函数的极限（变量代换定理）"
type: theorem
id: ANL-THM-011
subject: analysis
chapter: 02-continuity
tags:
  - 函数极限
  - 复合函数
  - 变量代换
depends:
  - ANL-DEF-008
  - ANL-DEF-012
uses: []
status: draft
source: "华东师范大学《数学分析》第5版 §3.2"
difficulty: 4
related:
  - ANL-THM-009
  - ANL-EX-005
applications:
  - "L'Hôpital 法则的变量代换前置条件"
  - "数值分析：参数化迭代收敛性的链式分析"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 条件

设：

1. $\lim_{x \to x_0} g(x) = u_0$（按 [[ANL-DEF-008]]）；
2. $\lim_{u \to u_0} f(u) = A$；
3. **下列条件之一**成立：
   - **(a)** $f$ 在 $u_0$ 处连续（按 [[ANL-DEF-012]]，即 $A = f(u_0)$）；**或**
   - **(b)** 存在 $x_0$ 的某去心邻域，使 $g(x) \neq u_0$ 在该邻域内成立。

## 结论

> $\displaystyle \lim_{x \to x_0} f\big(g(x)\big) = A$。

## 几何/直觉理解

复合函数 $f \circ g$ 把"$x \to x_0$"通过中间桥 $g$ 转化为"$u \to u_0$"，
再由 $f$ 转化为最终值 $A$。

**为什么需要条件 (a) 或 (b)**：

中间桥可能"恰好踩在 $u_0$ 上"——若 $g(x) = u_0$ 对无穷多 $x$ 成立，那么
$f(g(x)) = f(u_0)$ 由 $f$ 在 $u_0$ 的**取值**决定，而非**极限**决定。
此时 $f(u_0)$ 与 $\lim_{u \to u_0} f(u)$ 可能不等。

**反例**（违反 (a) 与 (b) 的双重失败）：

$$
g(x) = 0 \text{（恒等于 } 0\text{）}, \quad
f(u) = \begin{cases} 1 & u \neq 0 \\ 5 & u = 0 \end{cases}.
$$

那么 $\lim_{u \to 0} f(u) = 1$，但 $f(g(x)) = f(0) = 5$ 恒成立，故 $\lim_{x \to 0} f(g(x)) = 5 \neq 1$。

加上条件 (a)（$f$ 在 $u_0$ 连续，即 $f(u_0) = \lim_{u \to u_0} f$）或 (b)（$g(x) \neq u_0$）即可排除此反例。

## 证明（条件 (b)）

**证明：** 任给 $\varepsilon > 0$。

由 $f \to A$（条件 2）：$\exists \eta > 0, \forall u : 0 < |u - u_0| < \eta \implies |f(u) - A| < \varepsilon$。

由 $g \to u_0$（条件 1）：$\exists \delta_1 > 0, \forall x : 0 < |x - x_0| < \delta_1 \implies |g(x) - u_0| < \eta$。

由条件 (b)：$\exists \delta_2 > 0, \forall x : 0 < |x - x_0| < \delta_2 \implies g(x) \neq u_0$。

取 $\delta = \min\{\delta_1, \delta_2\}$。对 $0 < |x - x_0| < \delta$：

- $g(x) \neq u_0$（由 $\delta_2$）
- $|g(x) - u_0| < \eta$（由 $\delta_1$）

合起来：$0 < |g(x) - u_0| < \eta$，故 $|f(g(x)) - A| < \varepsilon$。$\blacksquare$

条件 (a) 的证明类似：连续性允许 $g(x) = u_0$，因为此时 $f(g(x)) = f(u_0) = A$ 直接成立。

## 常见错误

- ✗ **遗漏条件 (a)/(b)**。
  最经典的"无害"应用：求 $\lim_{x \to 0} \sin(1 - \cos x)$。
  令 $u = 1 - \cos x \to 0$，$f(u) = \sin u$ 在 $0$ 处连续 ⇒ $\sin u \to \sin 0 = 0$。
  这里 (a) 成立——$\sin$ 处处连续——所以可以"无脑"换元。
  但若 $f$ 在 $u_0$ 不连续，必须验证 (b)。
- ✗ **认为 $\lim g = u_0$ 自动蕴含"$g(x)$ 经常等于 $u_0$"**。
  反例：$g(x) = x$ 于 $x_0 = 0$，$g(x) = 0 \iff x = 0$，**去心邻域**内 $g \neq u_0$，(b) 成立。
  反过来，常数函数 $g \equiv u_0$ 处处取 $u_0$，(b) 失败——只能靠 (a) 救场。

## 推论

- **变量代换法的合法性**：求 $\lim_{x \to a} F(\phi(x))$ 时，若 $\phi$ 单射或 $F$ 在 $\phi(a)$ 连续，可放心换元 $u = \phi(x)$。
- **L'Hôpital 法则的前置条件之一**：要求被代换的中间函数满足本定理的 (a) 或 (b)。
- **连续函数的复合保连续**：$f, g$ 都连续 ⇒ $f \circ g$ 连续（条件 (a) 自动满足）。

## 链接

- 前置：[[ANL-DEF-008]]、[[ANL-DEF-012]]
- 应用：[[ANL-THM-009]] 与 [[ANL-EX-005]] 复合函数连续例题
- 推广：度量空间、拓扑空间中的连续映射复合

## 跨专业应用

- **数值分析**：迭代序列 $x_{n+1} = g(x_n)$ 的极限分析常用复合函数极限链式定理
- **物理**：相空间变量代换（如球坐标 ↔ 笛卡尔坐标）下的极限传递性
