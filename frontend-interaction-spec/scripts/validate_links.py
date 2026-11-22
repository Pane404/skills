#!/usr/bin/env python3
"""Validate package-local Markdown links, inline paths, and explicit HTML ids."""

import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\((<[^>\n]+>|[^)\s]+)(?:\s+[^)\n]+)?\)")
CODE = re.compile(r"(`+)([^`\n]+)\1")
INLINE_PATH = re.compile(r"(?:\.\./)*(?:references/)?(?:cards|contracts|topics|index|scripts)/[^\s`]+")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
COMMENT = re.compile(r"<!--[\s\S]*?-->")


class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = Counter()

    def handle_starttag(self, tag, attrs):
        self.ids.update(value for name, value in attrs if name == "id" and value)


def visible_markdown(text):
    fence = None
    visible = []
    for line in text.splitlines():
        mark = FENCE.match(line)
        if fence:
            if mark and mark[1][0] == fence[0] and len(mark[1]) >= len(fence) and not mark[2].strip():
                fence = None
        elif mark:
            fence = mark[1]
        else:
            visible.append(line)
    return COMMENT.sub("", "\n".join(visible))


def check_links(package):
    texts = {path: path.read_text(encoding="utf-8") for path in sorted(package.rglob("*.md"))}
    scans = {path: visible_markdown(text) for path, text in texts.items()}
    anchors = {}
    for path, scan in scans.items():
        parser = AnchorParser()
        parser.feed(CODE.sub("", scan))
        parser.close()
        anchors[path] = parser.ids

    errors = []
    count = 0
    for path, scan in scans.items():
        markdown = [(link.strip("<>"), "链接") for link in LINK.findall(CODE.sub("", scan))]
        inline = [(value, "行内路径") for _, value in CODE.findall(scan)
                  if INLINE_PATH.fullmatch(value) and "…" not in value and "<" not in value]
        for value, kind in markdown + inline:
            label = f"{path.relative_to(package)} {kind}"
            try:
                target = urlsplit(value)
            except ValueError:
                errors.append(f"{label}格式错误 -> {value}")
                continue
            if target.scheme in {"https", "http", "mailto", "tel"}:
                continue
            count += 1
            relative = unquote(target.path)
            if target.scheme or target.netloc or Path(relative).is_absolute():
                errors.append(f"{label}须使用包内相对路径 -> {value}")
                continue
            destination = (path.parent / relative).resolve() if relative else path
            if not destination.is_relative_to(package):
                errors.append(f"{label}超出包根 -> {value}")
            elif not destination.is_file():
                errors.append(f"{label}不可达 -> {value}")
            elif target.fragment and anchors.get(destination, {}).get(unquote(target.fragment)) != 1:
                errors.append(f"{label}锚点需唯一显式 id -> {value}")

    lines = sum(len(text.splitlines()) for text in texts.values())
    if lines > 3000:
        errors.append(f"包内 {lines} 行 > 3000")
    return count, lines, errors


if __name__ == "__main__":
    links, lines, errors = check_links(Path(__file__).resolve().parents[1])
    print(f"links: 检查 {links} 个包内链接与行内路径，包内 {lines} 行 ->", "FAIL" if errors else "PASS")
    for error in errors[:20]:
        print("  -", error)
    sys.exit(bool(errors))
