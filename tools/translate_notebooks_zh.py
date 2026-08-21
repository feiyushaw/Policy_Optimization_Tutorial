import json
import re
import time
from pathlib import Path

from deep_translator import GoogleTranslator

# 中文化范围：全部主线教程与练习 Notebook。
NOTEBOOKS = [
    "1_policy_optimization_introduction.ipynb",
    "2_policy_gradient.ipynb",
    "3_actor_critic.ipynb",
    "4_deterministic_policy_gradient.ipynb",
    "ex1_evolutionary_policy_optimization.ipynb",
    "ex2_actor_critic.ipynb",
    "ex3_td3.ipynb",
]

JP_RE = re.compile(r"[\u3040-\u30ff]")
PROTECTED_RE = re.compile(
    r"(\$\$.*?\$\$|\$[^\n$]+?\$|`[^`]+`|https?://[^\s)）>]+|\\begin\{.*?\\end\{[^}]+\})",
    re.S,
)

translator = GoogleTranslator(source="ja", target="zh-CN")
cache = {}


def protect(text):
    items = []
    def repl(m):
        token = f"ZXQPH{len(items)}QXZ"
        items.append(m.group(0))
        return token
    return PROTECTED_RE.sub(repl, text), items


def restore(text, items):
    for i, value in enumerate(items):
        text = text.replace(f"ZXQPH{i}QXZ", value)
        text = text.replace(f"ZXQPH {i} QXZ", value)
    return text


def translate_text(text):
    if not text.strip() or not JP_RE.search(text):
        return text
    if text in cache:
        return cache[text]
    safe, items = protect(text)
    chunks = re.split(r"(\n\s*\n)", safe)
    out = []
    for chunk in chunks:
        if not chunk.strip() or not JP_RE.search(chunk):
            out.append(chunk)
            continue
        try:
            translated = translator.translate(chunk)
            out.append(translated if translated else chunk)
            time.sleep(0.08)
        except Exception:
            time.sleep(1.0)
            try:
                translated = translator.translate(chunk)
                out.append(translated if translated else chunk)
            except Exception:
                out.append(chunk)
    result = restore("".join(out), items)
    cache[text] = result
    return result


def translate_code_line(line):
    if not JP_RE.search(line):
        return line
    if "#" in line:
        prefix, comment = line.split("#", 1)
        if JP_RE.search(comment):
            return prefix + "#" + translate_text(comment)
    stripped = line.strip()
    if stripped.startswith(('"""', "'''")) or stripped.endswith(('"""', "'''")):
        indent = line[: len(line) - len(line.lstrip())]
        return indent + translate_text(line[len(indent):])
    return line


def process(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    for cell in data.get("cells", []):
        src = cell.get("source", [])
        as_list = isinstance(src, list)
        text = "".join(src) if as_list else src
        if cell.get("cell_type") == "markdown":
            text = translate_text(text)
        elif cell.get("cell_type") == "code":
            text = "".join(translate_code_line(x) for x in text.splitlines(keepends=True))
        cell["source"] = text.splitlines(keepends=True) if as_list else text
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    for name in NOTEBOOKS:
        process(Path(name))

    remaining = []
    for name in NOTEBOOKS:
        data = json.loads(Path(name).read_text(encoding="utf-8"))
        for i, cell in enumerate(data.get("cells", [])):
            src = cell.get("source", [])
            text = "".join(src) if isinstance(src, list) else src
            if JP_RE.search(text):
                remaining.append(f"{name}: cell {i}")

    report = [
        "Policy Optimization Tutorial Chinese localization report",
        "========================================================",
        f"Notebooks processed: {len(NOTEBOOKS)}",
        f"Cells still containing hiragana/katakana: {len(remaining)}",
        "",
    ]
    report.extend(remaining)
    Path("translation_report.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
    if remaining:
        raise SystemExit("Japanese text remains; see translation_report.txt")


if __name__ == "__main__":
    main()
