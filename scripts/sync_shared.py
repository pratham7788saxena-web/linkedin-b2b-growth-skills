#!/usr/bin/env python3
"""Copy shared files into every skill so each skill folder is self-contained.

Claude loads each skill folder on its own, so shared references are copied in.
Edit the originals (shared/, templates/), then run:

    python scripts/sync_shared.py          # write copies
    python scripts/sync_shared.py --check  # exit 1 if any copy is out of date (used in CI)
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

# (source, destination relative to each skill, or to one skill)
EVERY_SKILL = [(ROOT / "shared" / "ground-rules.md", Path("references/ground-rules.md"))]
ONE_SKILL = [
    (ROOT / "templates" / "workspace", SKILLS / "workspace-setup" / "assets" / "workspace"),
    (ROOT / "templates" / "CLAUDE.md.example", SKILLS / "workspace-setup" / "assets" / "CLAUDE.md.example"),
]


def pairs():
    for skill in sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").exists()):
        for src, rel in EVERY_SKILL:
            yield src, skill / rel
    for src, dst in ONE_SKILL:
        if src.is_dir():
            for f in sorted(src.rglob("*")):
                if f.is_file():
                    yield f, dst / f.relative_to(src)
        else:
            yield src, dst


def main():
    check = "--check" in sys.argv
    stale = []
    for src, dst in pairs():
        if dst.exists() and dst.read_bytes() == src.read_bytes():
            continue
        stale.append(dst.relative_to(ROOT))
        if not check:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
    if check and stale:
        print("Out of date (run scripts/sync_shared.py):")
        print("\n".join(f"  {p}" for p in stale))
        sys.exit(1)
    print(f"{'Checked' if check else 'Synced'}: {len(stale)} file(s) {'stale' if check else 'updated'}.")


if __name__ == "__main__":
    main()
