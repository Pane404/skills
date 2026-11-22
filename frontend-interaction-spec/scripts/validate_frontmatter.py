#!/usr/bin/env python3
"""Validate the package entry point and its project metadata."""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("frontmatter: FAIL 需要 PyYAML（pip install PyYAML）")


class UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        mapping = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str) or key in mapping:
                raise yaml.constructor.ConstructorError(
                    None, None, f"字段名必须是唯一字符串：{key!r}", key_node.start_mark
                )
            mapping[key] = self.construct_object(value_node, deep=deep)
        return mapping


def validate(package):
    lines = (package / "SKILL.md").read_text(encoding="utf-8-sig").splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        return ["缺完整的 YAML frontmatter"]

    end = lines.index("---", 1)
    try:
        fields = yaml.load("\n".join(lines[1:end]), Loader=UniqueKeyLoader)
    except yaml.YAMLError as error:
        return [f"YAML 无法解析：{error}"]
    if not isinstance(fields, dict):
        return ["frontmatter 必须是 YAML 映射"]

    errors = []
    name = fields.get("name")
    if not isinstance(name, str) or len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("name 必须是 1–64 字符的 hyphen-case 字符串")
    elif name != package.name:
        errors.append(f"name({name}) 与目录名({package.name}) 不一致")

    description = fields.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        errors.append("description 必须是非空且不超过 1024 字符的字符串")
    elif "<" in description or ">" in description:
        errors.append("description 含尖括号")

    if fields.get("agent_created") is not True:
        errors.append("agent_created 必须为布尔值 true")
    version = fields.get("version")
    if not isinstance(version, str) or not version.strip():
        errors.append("version 必须是非空字符串")
    if len(lines) > 180:
        errors.append(f"SKILL.md {len(lines)} 行 > 180")
    return errors


if __name__ == "__main__":
    errors = validate(Path(__file__).resolve().parents[1])
    print("frontmatter:", "FAIL" if errors else "PASS")
    for error in errors:
        print("  -", error)
    sys.exit(bool(errors))
