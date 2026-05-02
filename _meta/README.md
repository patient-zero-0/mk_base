# _meta · 索引与统计

本目录存放自动/半自动维护的元数据文件，**不属于知识条目本身**。

| 文件 | 说明 | 维护方式 |
|---|---|---|
| `index.md` | 全库条目索引（按章节分组） | 半自动（`scripts/build_index.py`，待开发） |
| `todo.md` | 悬空引用待办清单 | 自动（`check_dangling_refs.py --report`） |
| `dangling.md` | 最近一次悬空引用扫描报告 | 自动（CI 生成） |
| `analytics.json` | Cloudflare Web Analytics 每日 PV 同步结果 | 自动（cron job，待接入） |
| `dependency-graph.json` | 条目依赖图，用于前端「关系视图」 | 半自动（待开发） |

> 这些文件由工具维护，请勿手工编辑（除非工具尚未实现该字段）。
