#!/usr/bin/env python3
"""Validate a skill folder and package it as a versioned zip.

Usage:
    python3 package_skill.py <skill_dir> [output_dir] \
        --issue "one-line description of the change" \
        --new-version 1.2 [--old-version 1.1] [--ban STRING ...]

Every file in the archive is placed inside a single top-level folder named
after the skill. The original folder is only read, never modified.
Requires PyYAML (pip install pyyaml).
"""

import argparse
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
SKIP_DIRS = {"__pycache__", "node_modules", ".git"}
SKIP_FILES = {".DS_Store"}


def fail(msg):
    print(f"FAIL: {msg}")
    sys.exit(1)


def load_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.DOTALL)
    if not m:
        fail(f"{path}: no YAML frontmatter block")
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        fail(f"{path}: invalid YAML frontmatter: {e}")
    if not isinstance(fm, dict):
        fail(f"{path}: frontmatter must be a mapping")
    return fm, text


def validate(skill_dir, banned):
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        fail(f"{skill_dir}: SKILL.md not found")

    found = [p for p in skill_dir.rglob("SKILL.md")
             if not any(part in SKIP_DIRS for part in p.relative_to(skill_dir).parts[:-1])]
    if len(found) != 1:
        fail(f"{skill_dir}: expected exactly one SKILL.md, found {len(found)}")

    fm, text = load_frontmatter(skill_md)
    extra = set(fm) - ALLOWED_KEYS
    if extra:
        fail(f"unexpected frontmatter keys: {', '.join(sorted(extra))}")

    name = str(fm.get("name", "")).strip()
    if not name:
        fail("missing 'name'")
    if not re.match(r"^[a-z0-9-]+$", name) or name.startswith("-") or name.endswith("-") or "--" in name:
        fail(f"name '{name}' must be lowercase letters, digits, and single hyphens")
    if len(name) > 64:
        fail(f"name is {len(name)} characters, max 64")
    if name != skill_dir.name:
        fail(f"name '{name}' does not match folder name '{skill_dir.name}'")

    desc = str(fm.get("description", "")).strip()
    if not desc:
        fail("missing 'description'")
    if "<" in desc or ">" in desc:
        fail("description cannot contain angle brackets")
    if len(desc) > 1024:
        fail(f"description is {len(desc)} characters, max 1024")

    for s in banned:
        for p in skill_dir.rglob("*"):
            if p.is_file() and p.suffix in {".md", ".txt", ".py", ".json", ".yaml", ".yml"}:
                if p.name == "package_skill.py":
                    continue
                if s in p.read_text(encoding="utf-8", errors="ignore"):
                    fail(f"banned string {s!r} found in {p.relative_to(skill_dir)}")
    return name


def build_zip(skill_dir, out_dir, new_version, old_version, issue):
    out_dir.mkdir(parents=True, exist_ok=True)
    name = skill_dir.name
    now = datetime.now(timezone.utc)
    zip_path = out_dir / f"{name}-v{new_version}-{now.strftime('%Y%m%d')}.zip"

    changelog = skill_dir / "CHANGELOG.md"
    prior = changelog.read_text(encoding="utf-8").rstrip("\n") if changelog.exists() else f"# {name} changelog"
    label = f"v{old_version} -> v{new_version}" if old_version else f"v{new_version}"
    entry = f"\n\n## {label} ({now.strftime('%Y-%m-%d')})\n- {issue}\n"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(skill_dir.rglob("*")):
            if not p.is_file():
                continue
            rel = p.relative_to(skill_dir)
            if any(part in SKIP_DIRS for part in rel.parts[:-1]) or rel.name in SKIP_FILES:
                continue
            if rel.name == "CHANGELOG.md" and len(rel.parts) == 1:
                continue
            zf.write(p, f"{name}/{rel.as_posix()}")
        zf.writestr(f"{name}/CHANGELOG.md", prior + entry)

    with zipfile.ZipFile(zip_path) as zf:
        tops = {n.split("/")[0] for n in zf.namelist()}
        if tops != {name}:
            fail(f"archive layout wrong, top-level entries: {sorted(tops)}")
    return zip_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("skill_dir")
    ap.add_argument("output_dir", nargs="?", default="out")
    ap.add_argument("--issue", required=True)
    ap.add_argument("--new-version", required=True)
    ap.add_argument("--old-version")
    ap.add_argument("--ban", action="append", default=[], help="string that must not appear (repeatable)")
    a = ap.parse_args()

    skill_dir = Path(a.skill_dir).resolve()
    if not skill_dir.is_dir():
        fail(f"{skill_dir} is not a directory")
    name = validate(skill_dir, a.ban)
    zip_path = build_zip(skill_dir, Path(a.output_dir), a.new_version, a.old_version, a.issue)
    print(f"OK: {name} validated and packaged -> {zip_path}")


if __name__ == "__main__":
    main()
