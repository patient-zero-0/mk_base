# Makefile · 本地快捷命令
# 等同于 CI 检查，提交前运行 `make check` 确保一次通过

.PHONY: check check-frontmatter check-refs check-katex check-lint build graph

## 一键运行全部 CI 检查（等同于 check.yml）
check: check-frontmatter check-refs check-katex check-lint
	@echo ""
	@echo "✅ 全部检查通过，可以提交 PR。"

## 检查 frontmatter 必填字段（全库）
check-frontmatter:
	@echo "── [1/4] frontmatter 完整性 ────────────────"
	python3 scripts/check_frontmatter.py --all

## 检查悬空引用
check-refs:
	@echo "── [2/4] 悬空引用扫描 ──────────────────────"
	python3 scripts/check_dangling_refs.py

## 检查 LaTeX 语法
check-katex:
	@echo "── [3/4] LaTeX 语法验证 ─────────────────────"
	node scripts/check_katex.js --all

## 检查 Markdown 格式
check-lint:
	@echo "── [4/4] Markdown 格式规范 ──────────────────"
	npx markdownlint 'analysis/**/*.md' 'algebra/**/*.md' '_cross/**/*.md' \
		--ignore node_modules \
		--config .markdownlint.json

## 本地构建静态站点（需安装 Quartz）
build:
	npx quartz build

## 生成悬空引用报告到 _meta/dangling.md
report-dangling:
	python3 scripts/check_dangling_refs.py --report

## 构建依赖图到 _meta/dependency-graph.{md,json}
graph:
	python3 scripts/build_dependency_graph.py --by-chapter --json

## 安装依赖
install:
	npm install
	pip install pyyaml
