#!/usr/bin/env python3
"""Zip each skill for upload to Claude.ai (Settings > Capabilities > Skills).

    python scripts/package_skills.py      # writes dist/<skill>.zip
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)

for skill in sorted(p for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").exists()):
    out = DIST / f"{skill.name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill.rglob("*")):
            if f.is_file():
                z.write(f, Path(skill.name) / f.relative_to(skill))
    print(f"dist/{out.name}")
