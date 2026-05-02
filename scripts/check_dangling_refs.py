#!/usr/bin/env python3
"""
check_dangling_refs.py
扫描全库所有条目的依赖引用字段，检测是否存在悬空 ID。

悬空 ID：在 depends / uses / illustrates / tests 字段中被引用，
          但在仓库中找不到对应 id 的 .md 文件。

用法：
  python3 scripts/check_dangling_refs.py
  python3 scripts/check_dangling_refs.py --report   # 输出到 _meta/dangling.md
"""

import sys
import re
import yaml
import argparse
from pathlib import Path
from collections import defaultdict

REF_FIELDS = ["depends", "uses", "illustrates", "tests", "corollaries", "related"]
CONTENT_DIRS = ["analysis", "algebra", "_cross"]

def extract_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}

def collect_all_ids() -> dict[str, Path]:
    """收集全库所有条目的 id → 文件路径 映射。"""
    id_map: dict[str, Path] = {}
    for d in CONTENT_DIRS:
        for md in Path(d).rglob("*.md"):
            fm = extract_frontmatter(md)
            entry_id = fm.get("id")
            if entry_id:
                id_map[str(entry_id)] = md
    return id_map

def collect_references(id_map: dict) -> dict[str, list[tuple[str, str]]]:
    """
    收集所有引用关系。
    返回 {被引用ID: [(引用者ID, 字段名), ...]}
    """
    refs: dict[str, list] = defaultdict(list)
    for d in CONTENT_DIRS:
        for md in Path(d).rglob("*.md"):
            fm = extract_frontmatter(md)
            source_id = fm.get("id", str(md))
            for field in REF_FIELDS:
                val = fm.get(field)
                if not val:
                    continue
                if isinstance(val, str):
                    val = [val]
                if isinstance(val, list):
                    for ref_id in val:
                        refs[str(ref_id)].append((source_id, field))
    return refs

def main():
    parser = argparse.ArgumentParser(description="检测悬空引用")
    parser.add_argument("--report", action="store_true", help="将结果写入 _meta/dangling.md")
    args = parser.parse_args()

    print("扫描全库 ID……")
    id_map = collect_all_ids()
    print(f"  已收录 {len(id_map)} 个条目 ID")

    print("扫描引用关系……")
    refs = collect_references(id_map)

    # 找出悬空引用
    dangling: dict[str, list] = {}
    for ref_id, sources in refs.items():
        if ref_id not in id_map:
            dangling[ref_id] = sources

    print(f"\n{'─' * 50}")
    if not dangling:
        print("✅ 无悬空引用")
        if args.report:
            _write_report({})
        sys.exit(0)

    print(f"❌ 发现 {len(dangling)} 个悬空 ID：\n")
    for ref_id, sources in sorted(dangling.items()):
        print(f"  {ref_id}")
        for source_id, field in sources:
            print(f"    ← {source_id}（字段：{field}）")

    if args.report:
        _write_report(dangling)
        print(f"\n报告已写入 _meta/dangling.md")

    print(f"\n请先创建缺失条目，或从引用字段中移除对应 ID。")
    sys.exit(1)

def _write_report(dangling: dict):
    Path("_meta").mkdir(exist_ok=True)
    lines = ["# 悬空引用报告\n", f"_自动生成，共 {len(dangling)} 个悬空 ID_\n\n"]
    if not dangling:
        lines.append("无悬空引用。\n")
    else:
        lines.append("| 悬空 ID | 被引用于 | 字段 |\n")
        lines.append("|---|---|---|\n")
        for ref_id, sources in sorted(dangling.items()):
            for source_id, field in sources:
                lines.append(f"| `{ref_id}` | `{source_id}` | {field} |\n")
    Path("_meta/dangling.md").write_text("".join(lines), encoding="utf-8")

if __name__ == "__main__":
    main()
