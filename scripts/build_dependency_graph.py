#!/usr/bin/env python3
"""
build_dependency_graph.py
扫描全库条目 frontmatter，输出依赖图 JSON。

节点：每条 .md 条目（id/title/type/subject/chapter/status/difficulty/tags）
边：  depends / uses / illustrates / tests / corollaries / related 关系

用法：
  python3 scripts/build_dependency_graph.py
  python3 scripts/build_dependency_graph.py --output _meta/dependency-graph.json
  python3 scripts/build_dependency_graph.py --report   # 仅打印统计，不写文件
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

# Windows 控制台默认 GBK 编码无法打印中文/emoji，强制 stdout/stderr 走 UTF-8。
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

CONTENT_DIRS = ["analysis", "algebra", "_cross"]

# 边类型 → 字段名映射；语义上 depends/uses 表示"前置依赖"，illustrates/tests
# 表示"演示/考察"指向，related/corollaries 是横向/派生关系。
EDGE_FIELDS = ["depends", "uses", "illustrates", "tests", "corollaries", "related"]

NODE_FIELDS = (
    "id", "title", "type", "subject", "chapter",
    "status", "difficulty", "tags",
)


def extract_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def collect_entries() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for d in CONTENT_DIRS:
        root = Path(d)
        if not root.exists():
            continue
        for md in sorted(root.rglob("*.md")):
            fm = extract_frontmatter(md)
            if not fm.get("id"):
                continue
            entries.append({"_path": str(md).replace("\\", "/"), **fm})
    return entries


def build_nodes(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    nodes: list[dict[str, Any]] = []
    for fm in entries:
        node = {key: fm.get(key) for key in NODE_FIELDS}
        node["path"] = fm["_path"]
        nodes.append(node)
    return nodes


def build_edges(
    entries: list[dict[str, Any]],
    known_ids: set[str],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """返回 (有效边, 悬空边)。"""
    edges: list[dict[str, str]] = []
    dangling: list[dict[str, str]] = []
    for fm in entries:
        source_id = fm["id"]
        for field in EDGE_FIELDS:
            val = fm.get(field)
            if not val:
                continue
            targets = [val] if isinstance(val, str) else list(val)
            for target in targets:
                target_id = str(target)
                edge = {"from": source_id, "to": target_id, "kind": field}
                if target_id in known_ids:
                    edges.append(edge)
                else:
                    dangling.append(edge)
    return edges, dangling


def compute_stats(
    nodes: list[dict[str, Any]],
    edges: list[dict[str, str]],
) -> dict[str, Any]:
    return {
        "total_nodes": len(nodes),
        "total_edges": len(edges),
        "by_subject": dict(Counter(n["subject"] for n in nodes)),
        "by_chapter": dict(Counter(f"{n['subject']}/{n['chapter']}" for n in nodes)),
        "by_type": dict(Counter(n["type"] for n in nodes)),
        "by_status": dict(Counter(n["status"] for n in nodes)),
        "by_edge_kind": dict(Counter(e["kind"] for e in edges)),
    }


def render_report(stats: dict[str, Any], dangling: list[dict[str, str]]) -> str:
    lines: list[str] = []
    lines.append("─" * 50)
    lines.append("依赖图统计")
    lines.append("─" * 50)
    lines.append(f"  节点总数：{stats['total_nodes']}")
    lines.append(f"  边总数：  {stats['total_edges']}")
    lines.append("")
    lines.append("  按学科：" + ", ".join(
        f"{k}={v}" for k, v in sorted(stats["by_subject"].items())
    ))
    lines.append("  按类型：" + ", ".join(
        f"{k}={v}" for k, v in sorted(stats["by_type"].items())
    ))
    lines.append("  按状态：" + ", ".join(
        f"{k}={v}" for k, v in sorted(stats["by_status"].items())
    ))
    lines.append("  按边类型：" + ", ".join(
        f"{k}={v}" for k, v in sorted(stats["by_edge_kind"].items())
    ))
    lines.append("")
    lines.append("  按章节：")
    for k, v in sorted(stats["by_chapter"].items()):
        lines.append(f"    · {k}: {v}")
    if dangling:
        lines.append("")
        lines.append(f"  ⚠ 悬空边 {len(dangling)} 条：")
        for e in dangling:
            lines.append(f"    · {e['from']} --[{e['kind']}]--> {e['to']}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="构建条目依赖图 JSON")
    parser.add_argument(
        "--output",
        default="_meta/dependency-graph.json",
        help="输出 JSON 路径（默认：_meta/dependency-graph.json）",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="仅打印统计报告，不写文件",
    )
    args = parser.parse_args()

    print("扫描全库 frontmatter……")
    entries = collect_entries()
    print(f"  已收录 {len(entries)} 个条目")

    nodes = build_nodes(entries)
    known_ids = {str(fm["id"]) for fm in entries}
    edges, dangling = build_edges(entries, known_ids)
    stats = compute_stats(nodes, edges)

    print(render_report(stats, dangling))

    if args.report:
        return 1 if dangling else 0

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "schema_version": 1,
        "stats": stats,
        "nodes": nodes,
        "edges": edges,
        "dangling_edges": dangling,
    }
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"\n✅ 已写入 {output_path}")
    return 1 if dangling else 0


if __name__ == "__main__":
    sys.exit(main())
