---
title: "Lipschitz / Hölder 连续与一致连续的关系"
type: problem
id: ANL-PROB-010
subject: analysis
chapter: 02-continuity
tags:
  - Lipschitz
  - Hölder
  - 一致连续
  - 边界判定
depends:
  - ANL-DEF-024
  - ANL-DEF-012
uses: []
status: stable
source: "华东师范大学《数学分析》第5版 §4.2 拓展习题"
difficulty: 4
tests:
  - ANL-DEF-024
related:
  - ANL-PROB-009
applications:
  - "PDE：解的正则性分级（Lipschitz vs Hölder）"
  - "概率论：随机过程样本路径的连续性等级"
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供。 -->

## 定义铺垫

设 $f : I \to \mathbb{R}$，$I \subseteq \mathbb{R}$ 区间。

- **Lipschitz 连续**：$\exists L > 0$，$\forall x, y \in I : |f(x) - f(y)| \leq L|x - y|$。
- **$\alpha$-Hölder 连续**（$\alpha \in (0, 1]$）：$\exists C > 0$，$\forall x, y \in I : |f(x) - f(y)| \leq C|x - y|^\alpha$。

注意 Lipschitz = $1$-Hölder。

## 题目

证明或反驳下列命题；当反驳时给出反例：

1. **真命题候选**：Lipschitz 连续 ⇒ 一致连续。
2. **真命题候选**：$\alpha$-Hölder 连续（$\alpha \in (0, 1]$）⇒ 一致连续。
3. **真命题候选**：一致连续 ⇒ Lipschitz 连续。
4. **真命题候选**：在闭区间 $[a, b]$ 上，可微 + $|f'(x)| \leq L \forall x$ ⇒ Lipschitz。
5. **真命题候选**：在 $\mathbb{R}$ 上 Lipschitz ⇒ 在 $\mathbb{R}$ 上有界。
6. **真命题候选**：$f, g$ 都 Lipschitz ⇒ $f \cdot g$ Lipschitz。

## 提示

<details><summary>点击展开提示</summary>

- 第 1、2 题：直接由定义推 ε-δ。
- 第 3 题：找反例——在闭区间上一致连续但非 Lipschitz 的函数。
- 第 4 题：中值定理 + 导数估计。
- 第 5 题：$f(x) = x$ 是 Lipschitz 但无界。
- 第 6 题：在无界域上反例——$f(x) = g(x) = x$ 都 Lipschitz，但 $f \cdot g = x^2$ 不是。

</details>

## 解答

<details><summary>点击展开完整解答</summary>

### 第 1 题：✅ Lipschitz ⇒ 一致连续

**证明**：设 $|f(x) - f(y)| \leq L|x - y|$。任给 $\varepsilon > 0$，取 $\delta = \varepsilon / L$。
$\forall x, y \in I : |x - y| < \delta \implies |f(x) - f(y)| \leq L \delta = \varepsilon$。$\blacksquare$

### 第 2 题：✅ Hölder ⇒ 一致连续

**证明**：设 $|f(x) - f(y)| \leq C|x - y|^\alpha$。任给 $\varepsilon > 0$，取 $\delta = (\varepsilon/C)^{1/\alpha}$。
$\forall x, y \in I : |x - y| < \delta \implies |f(x) - f(y)| \leq C \delta^\alpha = \varepsilon$。$\blacksquare$

### 第 3 题：❌ 一致连续 ⇏ Lipschitz

**反例**：$f(x) = \sqrt{x}$ 在 $[0, 1]$ 上。

- **一致连续**：闭区间 + 连续 ⇒ 由 [[ANL-THM-015]] Cantor 一致连续。或直接用 $|\sqrt{a} - \sqrt{b}| \leq \sqrt{|a-b|}$（即 $1/2$-Hölder）。
- **非 Lipschitz**：若 $|\sqrt{x} - \sqrt{0}| \leq L|x|$ 即 $\sqrt{x} \leq Lx$ 即 $1/\sqrt{x} \leq L$ 对所有 $x \in (0, 1]$ 成立，
  但 $1/\sqrt{x} \to \infty$ 当 $x \to 0^+$，无任何 $L$ 满足——故非 Lipschitz。$\blacksquare$

> 这是 1/2-Hölder 但非 1-Hölder（= Lipschitz）的典型，对应导数 $f'(x) = 1/(2\sqrt{x})$ 在 $0$ 附近无界。

### 第 4 题：✅ 闭区间 + 导数有界 ⇒ Lipschitz

**证明**：对任意 $x, y \in [a, b]$，由中值定理，$\exists \xi$ 介于 $x, y$ 之间使
$$
f(x) - f(y) = f'(\xi)(x - y).
$$

故 $|f(x) - f(y)| \leq L |x - y|$ 对所有 $x, y$ 成立。$\blacksquare$

> 推广：开区间 $(a, b)$ 上同样成立，但导数有界条件**对所有 $x \in (a, b)$**成立即可。

### 第 5 题：❌ Lipschitz 不蕴含有界

**反例**：$f(x) = x$ 在 $\mathbb{R}$ 上。

- Lipschitz：$|x - y| \leq 1 \cdot |x - y|$。
- 但 $f$ 无界（$x \to \pm\infty$ 时 $f \to \pm\infty$）。

> Lipschitz 是**斜率**的全局有界，**不**等于函数值的全局有界。

### 第 6 题：❌ Lipschitz 函数的乘积不一定 Lipschitz

**反例**：$f(x) = g(x) = x$ 在 $\mathbb{R}$ 上都 Lipschitz（常数 $1$）。
但 $h(x) = f(x) g(x) = x^2$，$|h(x) - h(y)| = |x^2 - y^2| = |x + y| |x - y|$，
当 $|x + y| \to \infty$ 时不存在全局 Lipschitz 常数。

故 $h = x^2$ 不 Lipschitz。$\blacksquare$

> **何时乘积仍 Lipschitz**？需附加 $f, g$ **有界**条件：
> $|fg(x) - fg(y)| \leq |f(x)| |g(x) - g(y)| + |g(y)| |f(x) - f(y)| \leq M_f L_g |x-y| + M_g L_f |x-y|$。
> 即在**有界 Lipschitz 函数空间**上，乘积封闭。

</details>

## 考察点

- 三个连续性级别（Lipschitz ⊂ Hölder ⊂ 一致连续 ⊂ 连续）的严格包含关系
- 中值定理与 Lipschitz 的等价（在可微情形下）
- 反例构造：用边界端点的导数发散打破 Lipschitz；用无界域打破乘积闭性

## 备注

**连续性等级体系**：

```text
连续 ⊋ 一致连续 ⊋ α-Hölder 连续（α ∈ (0,1)）⊋ Lipschitz（= 1-Hölder）⊋ C¹（连续可微）⊋ C∞ ⊋ 解析
```

> 等级越高，函数越"光滑/规则"——但也越"严格/罕见"。

**典型示例对照**：

| 函数 | 域 | 连续 | 一致连续 | Hölder（α<1） | Lipschitz |
|---|---|---|---|---|---|
| $x$ | $\mathbb{R}$ | ✅ | ✅ | ✅ | ✅ |
| $\sin x$ | $\mathbb{R}$ | ✅ | ✅ | ✅ | ✅ |
| $\sqrt{x}$ | $[0, 1]$ | ✅ | ✅ | ✅ (α=1/2) | ❌ |
| $\|x\|^{1/3}$ | $[-1, 1]$ | ✅ | ✅ | ✅ (α=1/3) | ❌ |
| $x^2$ | $\mathbb{R}$ | ✅ | ❌ | ❌ | ❌ |
| Dirichlet $\mathbb{1}_\mathbb{Q}$ | $\mathbb{R}$ | ❌ | ❌ | ❌ | ❌ |

## 跨专业应用

- **偏微分方程（PDE）**：解的正则性常按 Lipschitz / Hölder 分级（如 Sobolev 嵌入定理：$W^{1,p}$ 在某条件下嵌入 $C^{0,\alpha}$）
- **概率论**：Brownian 运动的样本路径**几乎处处** $\alpha$-Hölder（$\alpha < 1/2$）但**几乎处处不**可微——是非 Lipschitz 但 Hölder 连续的著名实例
- **机器学习**：神经网络的 Lipschitz 常数控制对抗鲁棒性（小的输入扰动 $\Rightarrow$ 受控的输出扰动）
