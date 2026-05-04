#!/usr/bin/env python3
"""
build_dependency_graph.py
扫描全库条目的 frontmatter，构建 depends/uses/illustrates/tests 关系图，
输出到 _meta/dependency-graph.md（含 Mermaid 渲染块）。

用法：
  python3 scripts/build_dependency_graph.py
  python3 scripts/build_dependency_graph.py --by-chapter   # 按章节分图输出
  python3 scripts/build_dependency_graph.py --json         # 同时输出 JSON 给前端用
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

# ── 配置 ─────────────────────────────────────────────────────────────────────

CONTENT_DIRS = ["analysis", "algebra", "_cross"]

# frontmatter 中表达"依赖"的字段（指向其他条目 ID）
DEPENDENCY_FIELDS = {
    "depends": "依赖",
    "uses": "公理",
    "illustrates": "演示",
    "tests": "考察",
}

# 类型 → 节点形状（Mermaid 语法）
TYPE_SHAPE = {
    "definition": ("[", "]"),       # 矩形
    "theorem":    ("{{", "}}"),     # 六边形
    "example":    ("(", ")"),       # 圆角矩形
    "problem":    ("([", "])"),     # 体育场形
}

# 类型 → 颜色 class 名
TYPE_CLASS = {
    "definition": "defNode",
    "theorem":    "thmNode",
    "example":    "exNode",
    "problem":    "probNode",
}

CLASS_DEFS = """\
classDef defNode  fill:#e8f0f7,stroke:#1e3a5f,stroke-width:1px;
classDef thmNode  fill:#fef4e0,stroke:#c9a961,stroke-width:1.5px;
classDef exNode   fill:#eef5ee,stroke:#5a8a5a,stroke-width:1px;
classDef probNode fill:#f7eaea,stroke:#a55a5a,stroke-width:1px;
"""


# ── 数据收集 ─────────────────────────────────────────────────────────────────

def extract_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def collect_entries() -> dict[str, dict]:
    """收集所有条目的 frontmatter 摘要 (id → meta)。"""
    entries: dict[str, dict] = {}
    for d in CONTENT_DIRS:
        for md in Path(d).rglob("*.md"):
            fm = extract_frontmatter(md)
            entry_id = fm.get("id")
            if not entry_id:
                continue
            entries[str(entry_id)] = {
                "id":      entry_id,
                "title":   fm.get("title", entry_id),
                "type":    fm.get("type", "definition"),
                "subject": fm.get("subject", "?"),
                "chapter": fm.get("chapter", "?"),
                "status":  fm.get("status", "draft"),
                "deps":    _collect_refs(fm),
                "path":    str(md).replace("\\", "/"),
            }
    return entries


def _collect_refs(fm: dict) -> list[tuple[str, str]]:
    """从 frontmatter 收集所有依赖引用，返回 [(目标 ID, 字段类型), ...]。"""
    refs: list[tuple[str, str]] = []
    for field in DEPENDENCY_FIELDS:
        val = fm.get(field)
        if not val:
            continue
        if isinstance(val, str):
            val = [val]
        if not isinstance(val, list):
            continue
        for ref in val:
            refs.append((str(ref), field))
    return refs


# ── Mermaid 输出 ─────────────────────────────────────────────────────────────

def _node_label(meta: dict) -> str:
    """生成 Mermaid 节点的 [shape] label，含 ID 与短标题。"""
    open_b, close_b = TYPE_SHAPE.get(meta["type"], ("[", "]"))
    title = meta["title"]
    # 防止 Mermaid 把括号 / 引号当语法
    title = title.replace('"', '”').replace("(", "（").replace(")", "）")
    if len(title) > 18:
        title = title[:17] + "…"
    label = f'{meta["id"]}<br/>{title}'
    return f'  {meta["id"]}{open_b}"{label}"{close_b}'


def _edge_style(field: str) -> str:
    """字段类型 → Mermaid 边样式。"""
    return {
        "depends":     "-->",
        "uses":        "-.-> ",      # 虚线
        "illustrates": "==>",        # 粗实线
        "tests":       "-..-> ",
    }.get(field, "-->")


def render_global_mermaid(entries: dict[str, dict]) -> str:
    """生成全库依赖图（适合作总览）。"""
    lines = ["```mermaid", "graph LR"]

    # 节点
    for meta in entries.values():
        lines.append(_node_label(meta))

    # 边
    for meta in entries.values():
        for ref_id, field in meta["deps"]:
            if ref_id in entries:
                arrow = _edge_style(field)
                lines.append(f'  {ref_id} {arrow} {meta["id"]}')

    # class 应用
    by_type: dict[str, list[str]] = defaultdict(list)
    for meta in entries.values():
        cls = TYPE_CLASS.get(meta["type"], "defNode")
        by_type[cls].append(meta["id"])
    for cls, ids in by_type.items():
        lines.append(f"  class {','.join(ids)} {cls}")

    # class 定义
    for line in CLASS_DEFS.strip().splitlines():
        lines.append(f"  {line}")

    lines.append("```")
    return "\n".join(lines)


def render_chapter_mermaid(
    entries: dict[str, dict], chapter: str
) -> str:
    """单章节依赖图——只含本章节条目 + 跨章节入边的指向（虚线）。"""
    in_chap = {e_id: m for e_id, m in entries.items() if m["chapter"] == chapter}

    lines = ["```mermaid", "graph LR"]

    # 节点
    for meta in in_chap.values():
        lines.append(_node_label(meta))

    # 跨章节入边（虚线表达"上游来自其他章节"）
    cross_chap_targets: set[str] = set()
    for meta in in_chap.values():
        for ref_id, field in meta["deps"]:
            if ref_id not in entries:
                continue
            ref_meta = entries[ref_id]
            if ref_meta["chapter"] == chapter:
                arrow = _edge_style(field)
                lines.append(f'  {ref_id} {arrow} {meta["id"]}')
            else:
                cross_chap_targets.add(ref_id)
                lines.append(
                    f'  {ref_id}>"{ref_id}<br/>(其他章节)"] -.-> {meta["id"]}'
                )

    # class 应用
    by_type: dict[str, list[str]] = defaultdict(list)
    for meta in in_chap.values():
        cls = TYPE_CLASS.get(meta["type"], "defNode")
        by_type[cls].append(meta["id"])
    for cls, ids in by_type.items():
        lines.append(f"  class {','.join(ids)} {cls}")

    for line in CLASS_DEFS.strip().splitlines():
        lines.append(f"  {line}")

    lines.append("```")
    return "\n".join(lines)


# ── Markdown 报告组装 ────────────────────────────────────────────────────────

def render_report(entries: dict[str, dict], by_chapter: bool) -> str:
    by_status: dict[str, int] = defaultdict(int)
    by_type_count: dict[str, int] = defaultdict(int)
    by_chap: dict[str, list[dict]] = defaultdict(list)
    edges_total = 0
    for meta in entries.values():
        by_status[meta["status"]] += 1
        by_type_count[meta["type"]] += 1
        by_chap[f'{meta["subject"]}/{meta["chapter"]}'].append(meta)
        edges_total += len(meta["deps"])

    lines: list[str] = []
    lines.append("# 全库依赖图 · Dependency Graph\n")
    lines.append("> 自动生成。请勿手工编辑——内容由 `scripts/build_dependency_graph.py` 扫描所有条目")
    lines.append("> 的 frontmatter 字段 `depends / uses / illustrates / tests` 构建。\n")

    # 概览
    lines.append("## 概览\n")
    lines.append("| 指标 | 数值 |")
    lines.append("|---|---|")
    lines.append(f"| 条目总数 | {len(entries)} |")
    lines.append(f"| 依赖边总数 | {edges_total} |")
    type_summary = " · ".join(f"{t}={c}" for t, c in sorted(by_type_count.items()))
    lines.append(f"| 类型分布 | {type_summary} |")
    status_summary = " · ".join(f"{s}={c}" for s, c in sorted(by_status.items()))
    lines.append(f"| 状态分布 | {status_summary} |")
    lines.append("")

    # 边类型图例
    lines.append("## 边类型说明\n")
    lines.append("| 字段 | 含义 | Mermaid 箭头 |")
    lines.append("|---|---|---|")
    lines.append("| `depends` | 前置定义 / 定理 | 实线 `-->` |")
    lines.append("| `uses` | 依赖的公理 | 虚线 `-.->` |")
    lines.append("| `illustrates` | 例题演示的对象 | 粗线 `==>` |")
    lines.append("| `tests` | 习题考察的知识点 | 点划线 `-..->` |")
    lines.append("")

    # 节点形状图例
    lines.append("## 节点类型说明\n")
    lines.append("| 类型 | 形状 | 颜色 |")
    lines.append("|---|---|---|")
    lines.append("| 定义 definition | 矩形 `[ ]` | 学院蓝 |")
    lines.append("| 定理 theorem | 六边形 `{{ }}` | 烫金 |")
    lines.append("| 例题 example | 圆角矩形 `( )` | 草绿 |")
    lines.append("| 习题 problem | 体育场形 `([ ])` | 砖红 |")
    lines.append("")

    # 全局图
    lines.append("## 全库总图\n")
    lines.append(render_global_mermaid(entries))
    lines.append("")

    # 按章节分图
    if by_chapter:
        lines.append("## 按章节分图\n")
        for chap_key, metas in sorted(by_chap.items()):
            chap_name = chap_key.split("/", 1)[1]
            lines.append(f"### `{chap_key}` （{len(metas)} 条）\n")
            lines.append(render_chapter_mermaid(entries, chap_name))
            lines.append("")

    # 入度 / 出度排行（识别"枢纽"概念）
    in_deg: dict[str, int] = defaultdict(int)
    out_deg: dict[str, int] = defaultdict(int)
    for meta in entries.values():
        out_deg[meta["id"]] = len(meta["deps"])
        for ref_id, _ in meta["deps"]:
            if ref_id in entries:
                in_deg[ref_id] += 1

    lines.append("## 高入度条目（被引用最多 = 知识基石）\n")
    lines.append("| 排名 | ID | 标题 | 入度 |")
    lines.append("|---|---|---|---|")
    top_in = sorted(in_deg.items(), key=lambda x: -x[1])[:10]
    for i, (eid, deg) in enumerate(top_in, 1):
        title = entries[eid]["title"]
        lines.append(f"| {i} | `{eid}` | {title} | {deg} |")
    lines.append("")

    lines.append("## 高出度条目（依赖最多 = 综合性强）\n")
    lines.append("| 排名 | ID | 标题 | 出度 |")
    lines.append("|---|---|---|---|")
    top_out = sorted(out_deg.items(), key=lambda x: -x[1])[:10]
    for i, (eid, deg) in enumerate(top_out, 1):
        title = entries[eid]["title"]
        lines.append(f"| {i} | `{eid}` | {title} | {deg} |")
    lines.append("")

    return "\n".join(lines)


def render_json(entries: dict[str, dict]) -> str:
    """JSON 输出：用于前端 D3 / Vis.js 等动态可视化。"""
    nodes = [
        {
            "id":      m["id"],
            "title":   m["title"],
            "type":    m["type"],
            "subject": m["subject"],
            "chapter": m["chapter"],
            "status":  m["status"],
        }
        for m in entries.values()
    ]
    edges = []
    for meta in entries.values():
        for ref_id, field in meta["deps"]:
            if ref_id in entries:
                edges.append({"source": ref_id, "target": meta["id"], "type": field})
    return json.dumps(
        {"nodes": nodes, "edges": edges, "schema": "mk-base/dependency-graph/v1"},
        ensure_ascii=False,
        indent=2,
    )


# ── 主程序 ───────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="构建条目依赖图")
    parser.add_argument(
        "--by-chapter",
        action="store_true",
        help="为每个章节单独输出一张子图",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="同时输出 _meta/dependency-graph.json（前端可视化用）",
    )
    args = parser.parse_args()

    entries = collect_entries()
    print(f"扫描到 {len(entries)} 个条目，构建依赖图……")

    Path("_meta").mkdir(exist_ok=True)

    md_path = Path("_meta/dependency-graph.md")
    md_path.write_text(render_report(entries, args.by_chapter), encoding="utf-8")
    print(f"已写入：{md_path}")

    if args.json:
        json_path = Path("_meta/dependency-graph.json")
        json_path.write_text(render_json(entries), encoding="utf-8")
        print(f"已写入：{json_path}")


if __name__ == "__main__":
    main()
