#!/usr/bin/env node
/**
 * check_katex.js
 * 提取 Markdown 文件中的 LaTeX 公式，用 KaTeX 尝试渲染，报告语法错误。
 *
 * 用法：
 *   node scripts/check_katex.js path/to/file.md
 *   node scripts/check_katex.js --all
 *   node scripts/check_katex.js --changed-only --base <sha>
 */

const katex = require("katex");
const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");
const { globSync } = require("glob");

// ── 提取公式 ──────────────────────────────────────────────────────────────

/**
 * 从 Markdown 文本中提取所有 LaTeX 公式。
 * 返回 [{formula, displayMode, line}]
 */
function extractFormulas(text) {
  const results = [];
  const lines = text.split("\n");

  let inCodeBlock = false;
  let blockBuffer = [];
  let blockStartLine = -1;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // 跳过代码块
    if (line.trim().startsWith("```")) {
      inCodeBlock = !inCodeBlock;
      continue;
    }
    if (inCodeBlock) continue;

    // 独立公式块 $$...$$（可能跨行）
    if (line.trim() === "$$") {
      if (blockBuffer.length === 0) {
        blockStartLine = i + 1;
      } else {
        results.push({
          formula: blockBuffer.join("\n"),
          displayMode: true,
          line: blockStartLine,
        });
        blockBuffer = [];
        blockStartLine = -1;
      }
      continue;
    }
    if (blockStartLine >= 0) {
      blockBuffer.push(line);
      continue;
    }

    // 行内 $...$ 公式（单行）
    const inlineRegex = /\$([^$\n]+?)\$/g;
    let match;
    while ((match = inlineRegex.exec(line)) !== null) {
      results.push({
        formula: match[1],
        displayMode: false,
        line: i + 1,
      });
    }

    // 行内独立 $$...$$ 公式
    const displayInlineRegex = /\$\$([^$]+?)\$\$/g;
    while ((match = displayInlineRegex.exec(line)) !== null) {
      results.push({
        formula: match[1],
        displayMode: true,
        line: i + 1,
      });
    }
  }

  return results;
}

// ── 检查单个文件 ───────────────────────────────────────────────────────────

function checkFile(filePath) {
  const text = fs.readFileSync(filePath, "utf-8");
  const formulas = extractFormulas(text);
  const errors = [];

  for (const { formula, displayMode, line } of formulas) {
    try {
      katex.renderToString(formula, {
        displayMode,
        throwOnError: true,
        strict: "warn",
      });
    } catch (e) {
      errors.push({ line, formula, error: e.message });
    }
  }

  return { total: formulas.length, errors };
}

// ── 获取文件列表 ───────────────────────────────────────────────────────────

function getChangedFiles(baseSha) {
  try {
    const output = execSync(
      `git diff --name-only --diff-filter=AM ${baseSha} HEAD`,
      { encoding: "utf-8" }
    );
    return output
      .trim()
      .split("\n")
      .filter(
        (f) =>
          f.endsWith(".md") &&
          /^(analysis|algebra|_cross)/.test(f) &&
          fs.existsSync(f)
      );
  } catch {
    return [];
  }
}

function getAllFiles() {
  return globSync("{analysis,algebra,_cross}/**/*.md");
}

// ── 主程序 ────────────────────────────────────────────────────────────────

const args = process.argv.slice(2);
let files = [];

if (args.includes("--all")) {
  files = getAllFiles();
} else if (args.includes("--changed-only")) {
  const baseIdx = args.indexOf("--base");
  const base = baseIdx >= 0 ? args[baseIdx + 1] : "HEAD~1";
  files = getChangedFiles(base);
} else {
  files = args.filter((a) => !a.startsWith("--") && a.endsWith(".md"));
}

if (files.length === 0) {
  console.log("✅ 无需检查的文件");
  process.exit(0);
}

let totalErrors = 0;
let totalFormulas = 0;

for (const file of files) {
  const { total, errors } = checkFile(file);
  totalFormulas += total;

  if (errors.length > 0) {
    console.log(`\n❌ ${file}（${total} 个公式，${errors.length} 个错误）`);
    for (const { line, formula, error } of errors) {
      console.log(`   行 ${line}：$${formula}$`);
      console.log(`           └─ ${error}`);
    }
    totalErrors += errors.length;
  } else {
    console.log(`✅ ${file}（${total} 个公式）`);
  }
}

console.log(`\n${"─".repeat(50)}`);
if (totalErrors > 0) {
  console.log(
    `共检查 ${totalFormulas} 个公式，发现 ${totalErrors} 个 LaTeX 错误。`
  );
  process.exit(1);
} else {
  console.log(`共检查 ${totalFormulas} 个公式，全部通过。`);
  process.exit(0);
}
