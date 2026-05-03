# MK_Base · 数学专业知识库

> 公开 · 永久免费 · 不收集个人数据 · 仅匿名 PV 统计

结构化的数学专业知识库，覆盖**数学分析**与**高等代数**两门核心课程。
以「条目」为最小单元，标注前置依赖、跨课关联与跨专业应用场景，
面向数学专业学生、跨专业学习者与科研用户。

---

## 快速导航

| 文档 | 作用 |
|---|---|
| [PROJECT.md](PROJECT.md) | 项目全局上下文（必读） |
| [ARCHITECTURE.md](ARCHITECTURE.md) | 当前技术栈与三条核心链路 |
| [STATUS.md](STATUS.md) | 当前里程碑与待办 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 开发规范（条目模板、Git、CI） |
| [refs/](refs/) | 参考资料（教材对照、PRD 摘要、写作指南） |
| [_templates/](_templates/) | 四类条目 Markdown 模板 |

---

## 目录结构

```
MK_Base/
├── PROJECT.md              # 项目全局上下文
├── ARCHITECTURE.md         # 架构活文档
├── STATUS.md               # 里程碑状态
├── CONTRIBUTING.md         # 开发规范
├── README.md               # 本文件
├── Makefile                # 本地一键检查
├── package.json            # Node 依赖（KaTeX、markdownlint）
├── .github/workflows/      # CI/CD（check.yml + deploy.yml）
├── scripts/                # frontmatter / 悬空引用 / KaTeX 检查脚本
├── refs/                   # 参考资料
├── _templates/             # 四类条目模板
├── _meta/                  # 索引、依赖图、待办、analytics
├── analysis/               # 数学分析条目（按章节）
│   ├── 01-limits/
│   ├── 02-continuity/
│   ├── 03-differentiation/
│   ├── 04-integration/
│   └── 05-series/
├── algebra/                # 高等代数条目（按章节）
│   ├── 01-polynomials/
│   ├── 02-determinants/
│   ├── 03-linear-equations/
│   ├── 04-linear-spaces/
│   └── 05-linear-maps/
└── _cross/                 # 跨课关联条目
```

---

## 本地开发

### 一键检查（提交 PR 前必跑）

```bash
make check
```

等同于 CI 中的 `check.yml`，运行四项闸门：

1. frontmatter 必填字段完整性
2. depends / uses 悬空引用扫描
3. LaTeX 公式 KaTeX 语法验证
4. Markdown 格式规范（markdownlint）

### 安装依赖

```bash
make install
# 或
npm install
pip install pyyaml
```

---

## 贡献流程

1. 从 `main` 创建 `draft/<主题>` 分支
2. 从 `_templates/` 复制对应类型的模板
3. 填写完整 frontmatter，撰写内容
4. 本地运行 `make check`
5. 推送并发起 PR，等待 CI 全绿 + Code Review
6. merge 后 Cloudflare Pages 自动发布

详细规范见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 许可与承诺

- **内容许可**：CC BY-SA 4.0（条目正文）
- **代码许可**：MIT（脚本与配置）
- **不收费承诺**：永远公开免费，无任何付费墙
- **隐私承诺**：不收集个人数据，无 Cookie，无用户账号

---

*PRD 完整版本：`数学知识库_PRD_v1.5.docx`*
*最后更新：2026-05-03（M1 进行中，30 条目 / 25 条 review）*
