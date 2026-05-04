# Stable 升级二审报告（2026-05-04）

审校范围：47 条 `status: review` 条目（analysis/01-limits 25 条 + analysis/02-continuity 22 条）
审校口径：CONTRIBUTING.md §7 严格二审；潜在数学错误、论证跳跃、反例驳力不足均标记。

## 1. 逐条结论表

| ID | 档次 | 关键问题 |
|---|---|---|
| ANL-AX-001 | ✅ | — |
| ANL-DEF-001 | ✅ | — |
| ANL-DEF-002 | ✅ | — |
| ANL-DEF-003 | ✅ | — |
| ANL-DEF-004 | ✅ | — |
| ANL-DEF-005 | ✅ | — |
| ANL-DEF-006 | ✅ | — |
| ANL-DEF-007 | 🟡 | "运算约定"小表把 $a/0$ 写为"严格未定义，仅在带极限时讨论"，措辞容易误读为"$a/0$ 在某种语境下定义"；建议改为"在 $\mathbb{R}$ 中无定义；带极限时按±∞ 不定型处理" |
| ANL-DEF-009 | ✅ | — |
| ANL-EX-001 | ✅ | — |
| ANL-EX-002 | 🟡 | 第 3 题 L88：以"开根可视为四则的极限推广，严格证明需连续函数"一笔带过 $\sqrt{1+1/n}\to 1$；建议改为"由 $\sqrt{\cdot}$ 在 $1$ 处连续（待建定理）" |
| ANL-EX-003 | ✅ | — |
| ANL-PROB-004 | ✅ | — |
| ANL-PROB-005 | 🟡 | 第 3 题 L100-110：交错求和的"配对/重排"叙述含 $m$ 奇/偶分情形，细节跳跃；可改写为"标准 Leibniz 余项估计 $|b_n-b_m|\le \frac{1}{m+1}$，证明见教材§13.2"或补一行清晰式 |
| ANL-PROB-006 | ✅ | — |
| ANL-PROB-007 | ✅ | — |
| ANL-PROB-008 | ✅ | — |
| ANL-THM-001 | ✅ | — |
| ANL-THM-002 | ✅ | — |
| ANL-THM-003 | ✅ | — |
| ANL-THM-004 | ✅ | — |
| ANL-THM-005 | ✅ | — |
| ANL-THM-006 | ✅ | — |
| ANL-THM-007 | ✅ | — |
| ANL-THM-008 | ✅ | — |
| ANL-DEF-008 | ✅ | — |
| ANL-DEF-010 | ✅ | — |
| ANL-DEF-011 | ✅ | — |
| ANL-DEF-012 | ✅ | — |
| ANL-DEF-013 | ✅ | — |
| ANL-DEF-024 | ✅ | — |
| ANL-EX-004 | ✅ | — |
| ANL-EX-005 | ✅ | — |
| ANL-EX-007 | ✅ | — |
| ANL-PROB-001 | ✅ | — |
| ANL-PROB-002 | ✅ | — |
| ANL-PROB-003 | 🟡 | 第 2 题 L86：异号性论证"$M = f(x_M)\ge f(0)$ 或 $f(1)$" 措辞含混；建议改为"$M\ge \max\{f(0),f(1)\}>0$（因二者异号，必有一为正）" |
| ANL-PROB-009 | 🟠 | 第 4 题：解答记录 3 次错误尝试再"修正"得正确结论，混乱；第 5 题：$|f'|\le 1$、"详细估计略"、"重叠粘合(略)"多处跳跃；需重写两题为干净证明 |
| ANL-PROB-010 | ✅ | — |
| ANL-PROB-031 | ✅ | — |
| ANL-THM-009 | ✅ | — |
| ANL-THM-010 | ✅ | — |
| ANL-THM-011 | ✅ | — |
| ANL-THM-012 | ✅ | — |
| ANL-THM-013 | ✅ | — |
| ANL-THM-014 | ✅ | — |
| ANL-THM-015 | ✅ | — |

合计：✅ 直接 41，🟡 轻修 5，🟠 重审 1，❌ 回退 0。

## 2. 直接升 stable 的 ID 列表（41 条）

```
ANL-AX-001
ANL-DEF-001 ANL-DEF-003 ANL-DEF-004 ANL-DEF-005 ANL-DEF-006 ANL-DEF-009
ANL-DEF-002
ANL-EX-001 ANL-EX-003
ANL-PROB-004 ANL-PROB-006 ANL-PROB-007 ANL-PROB-008
ANL-THM-001 ANL-THM-002 ANL-THM-003 ANL-THM-004 ANL-THM-005 ANL-THM-006 ANL-THM-007 ANL-THM-008
ANL-DEF-008 ANL-DEF-010 ANL-DEF-011 ANL-DEF-012 ANL-DEF-013 ANL-DEF-024
ANL-EX-004 ANL-EX-005 ANL-EX-007
ANL-PROB-001 ANL-PROB-002 ANL-PROB-010 ANL-PROB-031
ANL-THM-009 ANL-THM-010 ANL-THM-011 ANL-THM-012 ANL-THM-013 ANL-THM-014 ANL-THM-015
```

## 3. 轻修后升 stable（5 条，附行号建议）

- **ANL-DEF-007**（L83）：把 $a/0$ 行的措辞调整为"在 $\mathbb{R}$ 中无定义；含极限时视为 $\pm\infty$ 不定型"。
- **ANL-EX-002**（L88）：把"开根可视为四则的极限推广"明确为"由 $\sqrt{\cdot}$ 在 $1$ 处的连续性（[[ANL-DEF-012]] 函数连续）"。
- **ANL-PROB-005**（L100-114）：交错级数估计可一句"由 Leibniz 交错级数余项性质 $|b_n - b_m| \le 1/(m+1)$"取代当前略乱的两段重排叙述。
- **ANL-PROB-003**（L85-87）：把"$M\geq f(0)$ 或 $f(1)$"改写为"由 $f(0)f(1)<0$，二者必有一为正，故 $M\geq\max\{f(0),f(1)\}>0$；同理 $m<0$"。

## 4. 保留 review 重审（1 条）

- **ANL-PROB-009**（连续与一致连续 6 题）：阻断性问题
  - **第 4 题（$x^2\sin(1/x)$ 在 $\mathbb{R}$ 上）**（L92-128）：解答把 3 次失败的反例尝试**写在正文中**，再得出"修正答案"（结论正确，但呈现方式不达 stable 标准）。需重写为单一干净证明：用 $f'(x)=2x\sin(1/x)-\cos(1/x)$ 全局有界 + MVT ⇒ Lipschitz ⇒ 一致连续。
  - **第 5 题（$\sin x/x$）**（L132-145）：用"$|f'|\le 1$"未给证、"详细估计略"、"合并两段（粘合）"三处关键跳跃；需补：(i) 显式估 $|f'(x)|=|(\cos x\cdot x-\sin x)/x^2|\le 1$（用 $|\sin x|\le |x|$ 及 $|\sin x-x\cos x|$ 的 Taylor 估计）或 (ii) 改用"$f$ 闭区间一致连续 + $f$ 在 $|x|\to\infty$ 一致小 ⇒ 整体一致连续"。

## 5. 共性深层问题（≤ 3 条）

1. **"略" / "可证" / "类似"** 在 PROB 类条目中频出（最严重 ANL-PROB-009），与 stable"任何论证步骤跳跃需读者补非平凡推理"的口径不符。建议升 stable 前把所有"略"展开或链至专门定理。
2. **解答正文不应保留"试错过程"**：ANL-PROB-009 第 4 题把多个失败构造记录于解答区。这种风格在 review 阶段可作"过程展示"，但 stable 应只留最终干净证明（试错过程可放"备注"块）。
3. **"严格证明需连续函数"等前向引用** 在 ANL-EX-002、部分 PROB 中出现。建议明确 link 到对应定理，而非以括号注脚一笔带过——若被引用条目尚未建（如 Cantor 已建、复合函数极限已建），把链接补全；若未建，写明"待建：xxx 定理"。

