#!/usr/bin/env python3
"""Validate every skill: frontmatter, naming, size, links between skills and leaks.

    python scripts/validate_skills.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REQUIRED_SECTIONS = ["## When to use it", "## Common mistakes to avoid"]
# Words that should never ship in a generic repo (add your own company or client names here).
BLOCKLIST = [w.strip().lower() for w in
             (ROOT / "scripts" / "blocklist.txt").read_text().splitlines()
             if w.strip() and not w.startswith("#")] if (ROOT / "scripts" / "blocklist.txt").exists() else []

errors, warnings = [], []


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip().strip('"')
    return data


skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
names = {p.name for p in skill_dirs}

for d in skill_dirs:
    md = d / "SKILL.md"
    if not md.exists():
        errors.append(f"{d.name}: missing SKILL.md")
        continue
    text = md.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if not fm:
        errors.append(f"{d.name}: missing YAML frontmatter")
        continue
    name, desc = fm.get("name", ""), fm.get("description", "")
    if name != d.name:
        errors.append(f"{d.name}: frontmatter name '{name}' must match folder name")
    if not NAME_RE.match(name) or len(name) > 64:
        errors.append(f"{d.name}: name must be kebab-case, <= 64 chars")
    if not desc or len(desc) > 1024:
        errors.append(f"{d.name}: description must be 1-1024 chars (has {len(desc)})")
    if "<" in desc or ">" in desc:
        errors.append(f"{d.name}: description must not contain angle brackets")
    if len(text.splitlines()) > 500:
        warnings.append(f"{d.name}: SKILL.md over 500 lines; consider moving detail to references/")
    if not (d / "references" / "ground-rules.md").exists():
        errors.append(f"{d.name}: references/ground-rules.md missing (run scripts/sync_shared.py)")
    for section in REQUIRED_SECTIONS:
        if d.name != "brand-creative-design" and section not in text:
            warnings.append(f"{d.name}: no '{section}' section")
    for ref in set(re.findall(r"`([a-z]+(?:-[a-z]+)+)`", text)):
        if ref.endswith(".md") or ref in names:
            continue
        if ref.startswith(("linkedin-", "lead-", "content-", "company-", "topic-", "weekly-")) and ref not in names \
                and ref not in {"linkedin-workspace", "lead-tracker-template", "company-profile", "content-log", "campaign-log"}:
            errors.append(f"{d.name}: references unknown skill `{ref}`")
    low = text.lower()
    for word in BLOCKLIST:
        if word in low:
            errors.append(f"{d.name}: contains blocked term '{word}'")

for f in [ROOT / ".claude-plugin" / "plugin.json", ROOT / ".claude-plugin" / "marketplace.json"]:
    try:
        json.loads(f.read_text())
    except Exception as e:  # noqa: BLE001
        errors.append(f"{f.relative_to(ROOT)}: invalid JSON ({e})")

for w in warnings:
    print(f"WARN  {w}")
for e in errors:
    print(f"ERROR {e}")
print(f"\n{len(skill_dirs)} skills checked: {len(errors)} error(s), {len(warnings)} warning(s).")
sys.exit(1 if errors else 0)
