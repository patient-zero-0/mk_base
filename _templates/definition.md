---
title: "<在此处填写定义标题，例如：一致连续>"
type: definition
id: ANL-DEF-XXX            # 三位数字编号，按章节顺序递增
subject: analysis          # analysis | algebra | cross
chapter: 01-limits         # 与目录名一致
tags:                      # 至少 2 个
  - 极限
  - ε-δ
depends: []                # 前置概念 ID 列表，可为 []
uses: []                   # 依赖的公理 ID 列表，可为 []
status: draft              # draft | review | stable
source: "华东师范大学《数学分析》第5版 §X.Y"
difficulty: 2              # 1–5 整数
related: []                # 相关但非依赖的条目 ID（可选）
applications: []           # 跨专业应用场景（可选）
---

<!-- 正文以 H2 开头。条目标题统一由 frontmatter `title` 字段提供，避免与 markdownlint MD025 冲突。 -->

## 定义陈述

> 用一句到一段话给出严格的数学定义。所有量词（∀、∃）使用 LaTeX 写法
> （`\forall`、`\exists`），不要混用 Unicode 数学符号。

设 ……，称 …… 是 ……，若

$$
\forall \varepsilon > 0, \quad \exists \delta > 0, \quad \cdots
$$

## 与相近概念的区别

| 概念 | 关键差别 |
|---|---|
| 概念 A | …… |
| 概念 B | …… |

## 直觉理解

> 必填板块。先给比喻、再解释比喻为何成立；含量词的定义须解释量词顺序的含义。
> 写作要点参考 `refs/style-guide.md`。

## 链接

- 用于定理：[[ANL-THM-XXX]]
- 在例题中应用：[[ANL-EX-XXX]]

<!-- applications 字段非空时，本节才必须出现 -->
## 跨专业应用

- **领域 A**：……
- **领域 B**：……
