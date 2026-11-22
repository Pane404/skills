#!/usr/bin/env python3
"""Validate the package layers and the exact targets of maintained route tables."""

import posixpath
import re
import sys
from pathlib import Path


HARD = "contracts/hard-rules.md"
OVERLAY = "contracts/overlay-contract.md"
FIELD = HARD + "#field-validation"
STATUS = HARD + "#status-feedback"
DATA = "topics/data-display-notes.md"
FLOWS = "topics/page-flows.md"

# A destination may be a card ID or a reference path. Tuples specify ordered alternatives.
QUICK_ROUTES = {
    "保存成功 / 操作成功": STATUS,
    "页内对象级提示（贴字段/区块）": "L3-01",
    "系统级通告（贴整页/跨路由）": "L3-02",
    "异步通知 / 通知中心": "L3-05",
    "表单校验失败 / 字段报错": FIELD,
    "区块请求失败": "L3-10",
    "空结果 / 无数据": "L3-09",
    "加载中 / 骨架屏": "L3-08",
    "断网 / 离线": "L3-13",
    "弹窗 / 模态 / modal": "L4-01",
    "紧急阻断 / 安全确认": "L4-02",
    "删除确认 / 二次确认": "L4-03",
    "气泡确认 / popconfirm": "L4-04",
    "popover / 列设置 / 筛选": "L4-06",
    "tooltip / 悬停说明": "L4-07",
    "peek / hover 预览": "L4-08",
    "hovercard": "L4-09",
    "下拉菜单": "L4-11",
    "命令面板 / ⌘K": "L4-15",
    "抽屉 / drawer": "L4-16",
    "侧边面板 / side sheet": "L4-17",
    "底部面板 / bottom sheet": "L4-18",
    "图片放大 / lightbox": "L4-20",
    "原生 popover API / showModal": "L4-25",
    "视频 / 音频播放器、树形表格 / 甘特图": DATA,
    "批量操作栏、聊天 / 会话界面": FLOWS,
    "焦点管理 / 键盘": ("L10-01", "L10-02"),
    "焦点困住": "L10-03",
    "Esc 关闭": "L10-05",
    "背景 inert": "L10-08",
}
HOT_ONLY = {
    "瞬时轻量结果 / Toast": "L3-03",
    "模态六条契约 C1–C6": OVERLAY,
    "触控 / 对比度 / 焦点环 / Toast / hover": HARD,
    "反模式总表": "contracts/anti-patterns.md",
    "冲突谁覆盖谁": "contracts/precedence.md",
    "文件预览 / PDF": DATA,
    "树形表格": DATA,
    "甘特图": DATA,
    "二维码 / 水印": DATA,
    "回到顶部 / 悬浮按钮": DATA,
    "Cookie 同意": FLOWS,
    "聊天 / 会话界面": FLOWS,
    "Markdown 编辑器": FLOWS,
}
INTENTS = {
    "就地结果的反馈与可达性": STATUS,
    "瞬时轻量结果": "L3-03",
    "对象级常驻（贴字段/区块）": "L3-01",
    "持续状态 / 系统级": "L3-02",
    "异步可回看": "L3-05",
    "字段级错误": FIELD,
    "区块请求失败": "L3-10",
    "整页连接中断 / 同步状态": ("L3-02", "L3-13"),
    "空结果 / 首次使用": "L3-09",
    "不回应无法安全继续": ("L4-02", "L4-03"),
    "就地调整、即时生效、不提交（列设置 / 筛选）": "L4-06",
    "纯文本短说明": "L4-07",
    "悬停预览且别处可达": ("L4-08", "L4-09"),
    "需与列表 / 图表并排对照": ("L4-16", "L4-18"),
    "超一屏或需 URL": FLOWS,
    "多义词先消歧": "index/glossary.md",
    "校验时机与错误呈现": FIELD,
    "精确数值 vs 相对手感": "L2-04",
    "值可自由输 vs 受限长列表": ("L2-09", "L2-10"),
    "少量比较 vs 中量固定值": ("L2-11", "L2-16"),
    "立即生效 vs 提交后生效": ("L2-17", "L2-15"),
    "长且高风险表单": "L8-13",
    "先数目的地再选导航": ("L5-02", "L5-04"),
    "同处换面 vs 换参数": ("L5-05", "L1-08"),
    "来找 vs 随便逛": ("L5-07", "L5-08"),
    "单值低风险就地改": "L7-03",
    "落地页 / 定价页": ("L8-01", "L8-02"),
    "首次使用引导": "L8-04",
    "结果收窄 / 详情": ("L8-07", "L8-10"),
    "多步表单": "L8-13",
    "页面模式全表": FLOWS,
    "模态 / 焦点 / 键盘 / Esc / inert": OVERLAY,
    "焦点可见与不被遮挡": HARD,
    "拖放替代": "L10-11",
    "一致帮助、冗余输入": HARD,
    "错误恢复": "L10-15",
    "撤销重做": "L3-16",
}


def normalize_label(text):
    return " ".join(text.split()).casefold()


BUSINESS_ENTRY = (
    "先判断用户主要要查找、比较、编辑、批量处理还是追踪，再根据数据的层级、数量和状态，"
    "查阅 `references/topics/data-display-notes.md` 或 `references/topics/page-flows.md`。"
)


def validate_entries(index_dir, package):
    errors = []
    path = index_dir / "entries.md"
    if not path.is_file():
        return ["缺少 entries.md"]
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 6 or not re.fullmatch(r"L\d+-\d+", cells[0]):
            continue
        raw = re.findall(r"`([^`]+)`", cells[-1])
        if not raw:
            errors.append(f"entries: {cells[0]} 缺目标路径")
            continue
        target = posixpath.normpath(posixpath.join("references/index", raw[0]))
        if not (package / target).is_file():
            errors.append(f"entries: {cells[0]} 目标不可达 -> {raw[0]}")
        if posixpath.basename(target) != cells[0] + ".md":
            errors.append(f"entries: {cells[0]} 目标编号应为 {cells[0]}.md")
    return errors


def validate_aliases(index_dir, entries_text):
    names = {}
    for line in entries_text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 6 and re.fullmatch(r"L\d+-\d+", cells[0]):
            names[cells[0]] = (cells[1].casefold(), cells[2].casefold())
    errors = []
    path = index_dir / "aliases.md"
    if not path.is_file():
        return ["缺少 aliases.md"]
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not re.fullmatch(r"L\d+-\d+", cells[1]):
            continue
        name = names.get(cells[1])
        if not name:
            errors.append(f"aliases: {cells[1]} 不在 entries 中")
            continue
        tokens = [part.strip().casefold() for part in re.split(r"[/·、,，]", cells[0]) if len(part.strip()) >= 2]
        if not any(token in name[0] or token in name[1] for token in tokens):
            errors.append(f"aliases: 「{cells[0]}」与目标编号 {cells[1]} 不对应")
    return errors


def expected_paths(destinations):
    if isinstance(destinations, str):
        destinations = (destinations,)
    return tuple(
        f"references/cards/{destination}.md"
        if re.fullmatch(r"L\d+-\d+", destination)
        else f"references/{destination}"
        for destination in destinations
    )


def validate_routes(text, label, parent, expected):
    errors = []
    known = {normalize_label(name): (name, expected_paths(targets)) for name, targets in expected.items()}
    seen = set()
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or not line.endswith("|"):
            continue
        cells = [cell.strip() for cell in re.split(r"(?<!\\)\|", line[1:-1])]
        if not cells or cells[0] in {"说法", "场景"} or re.fullmatch(r":?-+:?", cells[0]):
            continue
        name = normalize_label(cells[0])
        if name in seen:
            errors.append(f"{label}: 场景重复「{cells[0]}」")
            continue
        seen.add(name)
        if name not in known:
            errors.append(f"{label}: 场景「{cells[0]}」未登记预期路由")
            continue

        raw = re.findall(r"`([^`]+)`", cells[1]) if len(cells) == 2 else []
        actual = tuple(posixpath.normpath(posixpath.join(parent, path)) for path in raw)
        _, wanted = known[name]
        if actual != wanted:
            errors.append(f"{label}: 「{cells[0]}」目标应为 {', '.join(wanted)}，实际 {', '.join(actual)}")
    for name, (display, _) in known.items():
        if name not in seen:
            errors.append(f"{label}: 缺少必备场景「{display}」")
    return errors


def validate(package):
    errors = []
    allowed = {"SKILL.md", "references", "scripts", "assets"}
    extra = sorted(path.name for path in package.iterdir() if path.name not in allowed)
    if extra:
        errors.append(f"包根出现非标准文件或目录: {extra}")

    index = package / "references/index"
    for path in sorted(index.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        lines = len(text.splitlines())
        if lines > 100:
            errors.append(f"{path.name}: {lines} 行 > 100")
        if re.search(r"- \[ \]|\b\d+\s*(?:px|ms)\b|https?://", text):
            errors.append(f"{path.name}: 索引含检查项、取值或来源 URL")

    entries_text = (index / "entries.md").read_text(encoding="utf-8")
    errors.extend(validate_entries(index, package))
    errors.extend(validate_aliases(index, entries_text))

    skill = (package / "SKILL.md").read_text(encoding="utf-8")
    if BUSINESS_ENTRY not in skill:
        errors.append("SKILL 业务场景入口指令缺失或被改指")
    section = re.search(r"^## 3 [^\n]*\n(.*?)(?=^## 4 )", skill, re.M | re.S)
    if section is None:
        errors.append("SKILL.md 缺首屏速查表")
    else:
        errors.extend(validate_routes(section[1], "SKILL §3", ".", QUICK_ROUTES))
    for filename, expected in (("hot.md", QUICK_ROUTES | HOT_ONLY), ("intents.md", INTENTS)):
        path = index / filename
        if not path.is_file():
            errors.append(f"缺少 {filename}")
        else:
            errors.extend(validate_routes(path.read_text(encoding="utf-8"), filename, "references/index", expected))

    for path in (package / "references/cards").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "HR-01 触控目标 ≥44×44" in text or "| C1 | 焦点移入" in text:
            errors.append(f"{path.name}: 复制了硬约束或契约全文")
    return errors


if __name__ == "__main__":
    errors = validate(Path(__file__).resolve().parents[1])
    print("layers:", "FAIL" if errors else "PASS")
    for error in errors[:20]:
        print("  -", error)
    sys.exit(bool(errors))
