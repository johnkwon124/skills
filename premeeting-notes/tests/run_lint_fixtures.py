#!/usr/bin/env python3
"""Run lint_note.py against every fixture and compare with tests/manifest.json.
Usage: python3 -I tests/run_lint_fixtures.py
Two fixtures are built at run time from escapes so that no package file contains the characters they test."""
import json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LINT = os.path.join(HERE, "..", "scripts", "lint_note.py")
# R09 (PRIVATE_TOKEN) reads scripts/lint_private_tokens.txt. Point it at a temp token file so the
# bad_private_token fixture passes on a fresh clone without shipping real private tokens.
TOKEN_FILE = os.path.join(HERE, "..", "scripts", "lint_private_tokens.txt")
NAMES_FILE = os.path.join(HERE, "..", "scripts", "lint_internal_names.txt")
RUNTIME = [
    ("rt_em_dash.txt", "pre", "Seed round \u2014 $8M.\n", ["R01"], []),
    ("rt_banned_term.txt", "pre", "\ud22c\uc790 \ud14c\uc81c\ub294 \ucd94\ud6c4 \uc815\ub9ac\ud568.\n", ["R02"], []),
]

def run(path, mode):
    p = subprocess.run([sys.executable, "-I", LINT, "--mode", mode, path], capture_output=True, text=True)
    fails, warns = set(), set()
    for line in p.stdout.splitlines():
        if line.startswith("[FAIL]"):
            fails.add(line.split()[1])
        elif line.startswith("[WARN]"):
            warns.add(line.split()[1])
    return fails, warns

def main():
    saved = {}
    for path, content in ((TOKEN_FILE, "TestFirm\n"), (NAMES_FILE, "TestAgent\n")):
        saved[path] = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        open(path, "w", encoding="utf-8").write(content)
    try:
        run_all()
    finally:
        for path, prev in saved.items():
            if prev is None:
                os.remove(path)
            else:
                open(path, "w", encoding="utf-8").write(prev)

def run_all():
    manifest = json.load(open(os.path.join(HERE, "manifest.json"), encoding="utf-8"))
    cases = [(os.path.join(HERE, "lint-fixtures", c["file"]), c["file"], c["mode"], c["expect_fail"], c["expect_warn"]) for c in manifest]
    tmp = tempfile.mkdtemp()
    for name, mode, text, ef, ew in RUNTIME:
        path = os.path.join(tmp, name)
        open(path, "w", encoding="utf-8").write(text)
        cases.append((path, name, mode, ef, ew))
    bad = 0
    for path, name, mode, ef, ew in cases:
        fails, warns = run(path, mode)
        ok = fails == set(ef) and set(ew) <= warns
        bad += 0 if ok else 1
        print(("PASS " if ok else "FAIL ") + name + "  got fail=" + str(sorted(fails)) + " warn=" + str(sorted(warns)))
    print("RESULT " + str(len(cases) - bad) + "/" + str(len(cases)) + " fixtures as expected")
    sys.exit(1 if bad else 0)

main()
