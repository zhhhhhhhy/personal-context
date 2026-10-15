#!/usr/bin/env python3
"""Deterministic sanity checks for a contract-field patent material package."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED = (
    "步骤.md",
    "材料盘点与来源.md",
    "证据摘录.md",
    "发明点与证据边界.md",
    "权利要求书.md",
    "说明书.md",
    "说明书摘要.md",
    "说明书附图.md",
    "验收报告.md",
)
PLACEHOLDER_RE = re.compile(r"TODO|TBD|PLACEHOLDER|<待填写>|\[待填写\]", re.I)


def read_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def claim_numbers(text: str) -> list[int]:
    # Accept the compact Markdown form used by this workflow and common variants.
    values = []
    for line in text.splitlines():
        match = re.match(r"^#{1,4}\s*(?:权利要求\s*)?(\d+)\s*$", line.strip())
        if match:
            values.append(int(match.group(1)))
    return values


def abstract_body(text: str) -> str:
    lines = [line for line in text.splitlines() if not line.lstrip().startswith("#")]
    return re.sub(r"\s+", "", "\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path, help="directory containing the patent materials")
    parser.add_argument("--json", dest="json_path", type=Path, help="optional result JSON path")
    args = parser.parse_args()
    root = args.package

    missing = [name for name in REQUIRED if not (root / name).is_file()]
    claims_text = read_utf8(root / "权利要求书.md") if not missing or (root / "权利要求书.md").is_file() else ""
    abstract_text = read_utf8(root / "说明书摘要.md") if (root / "说明书摘要.md").is_file() else ""
    numbers = claim_numbers(claims_text)
    expected = list(range(1, len(numbers) + 1)) if numbers else []
    placeholders = []
    stale_path_mentions = []
    for path in root.rglob("*.md"):
        text = read_utf8(path)
        # The acceptance report names the tokens it checked; that mention is
        # evidence, not an unfinished placeholder.
        if path.name != "验收报告.md" and PLACEHOLDER_RE.search(text):
            placeholders.append(str(path.relative_to(root)))
        if "第三章.pdf" in text and "排除" not in text:
            stale_path_mentions.append(str(path.relative_to(root)))

    result = {
        "required_files_present": not missing,
        "missing_files": missing,
        "claim_numbers": numbers,
        "claims_contiguous": bool(numbers) and numbers == expected,
        "abstract_body_chars_without_whitespace": len(abstract_body(abstract_text)),
        "abstract_under_300_chars": len(abstract_body(abstract_text)) < 300,
        "placeholder_files": placeholders,
        "unexpected_stale_source_mentions": stale_path_mentions,
    }
    result["pass"] = bool(
        result["required_files_present"]
        and result["claims_contiguous"]
        and result["abstract_under_300_chars"]
        and not placeholders
        and not stale_path_mentions
    )

    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    print(rendered)
    if args.json_path:
        args.json_path.write_text(rendered + "\n", encoding="utf-8")
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
