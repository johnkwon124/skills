#!/usr/bin/env python3
"""Tests for lint --max-words (R19), check_ledger.py and check_drift.py.
Usage: python3 -I tests/run_script_tests.py
Fixtures are written to a temp directory at run time."""
import os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(HERE, "..", "scripts")
TMP = tempfile.mkdtemp()


def w(name, text):
    p = os.path.join(TMP, name)
    open(p, "w", encoding="utf-8").write(text)
    return p


def run(script, *args):
    p = subprocess.run([sys.executable, "-I", os.path.join(S, script), *args], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


LEDGER = """# Source Record

## 3. Claims ledger
| ID | Claim | Value | As-of | Source URL | Snippet | Mat | Class |
|---|---|---|---|---|---|---|---|
| C01 | Series B amount | $60M | 2024-07-31 | https://example.com/p/12345 | "raised $60 million" | H | public |
| C02 | Headcount | 48 | 2026-09 | https://example.com/team | "48 employees" | N | company |

## 4. Canonical values
Other number 777 appears here only.
"""

cases = []

# R19
short = w("short.md", "## At a Glance\n- **What**: Maker of cables.\n")
cases.append(("R19 passes under cap", lambda: run("lint_note.py", "--mode", "pre", short, "--max-words", "50"), lambda rc, o: "R19" not in o))
long_ = w("long.md", "## At a Glance\n" + "\n".join(f"- **Item{i}**: word word word word word word word word word word" for i in range(20)) + "\n")
cases.append(("R19 fails over cap", lambda: run("lint_note.py", "--mode", "pre", long_, "--max-words", "50"), lambda rc, o: "R19" in o and "WORD_LIMIT" in o))
cases.append(("R19 off by default", lambda: run("lint_note.py", "--mode", "pre", long_), lambda rc, o: "R19" not in o))

# check_ledger
ledger = w("ledger.md", LEDGER)
ok_note = w("ok_note.md", "The company raised $60 million in July 2024 and has 48 employees as of 2026.\n")
cases.append(("ledger: sourced numbers pass", lambda: run("check_ledger.py", "--note", ok_note, "--ledger", ledger), lambda rc, o: rc == 0 and "unsourced=0" in o))
bad_note = w("bad_note.md", "The company raised $60 million and has 52 employees.\n")
cases.append(("ledger: unsourced number fails", lambda: run("check_ledger.py", "--note", bad_note, "--ledger", ledger), lambda rc, o: rc == 1 and "52" in o and "UNSOURCED" in o))
outside_note = w("outside_note.md", "The company raised $60 million, reference 777.\n")
cases.append(("ledger: number only outside the table fails", lambda: run("check_ledger.py", "--note", outside_note, "--ledger", ledger), lambda rc, o: rc == 1 and "777" in o))
url_note = w("url_note.md", "Reference id 12345 appears in the note.\n")
cases.append(("ledger: number inside a URL cell does not count", lambda: run("check_ledger.py", "--note", url_note, "--ledger", ledger), lambda rc, o: rc == 1 and "12345" in o))
small_note = w("small_note.md", "Three phases and 2 to 3 times faster, raised $60 million.\n")
cases.append(("ledger: small integers ignored", lambda: run("check_ledger.py", "--note", small_note, "--ledger", ledger), lambda rc, o: rc == 0))
nohead = w("nohead.md", "| a | b |\n|---|---|\n| 1 | 2 |\n")
cases.append(("ledger: missing heading errors", lambda: run("check_ledger.py", "--note", ok_note, "--ledger", nohead), lambda rc, o: rc != 0 and "Claims ledger" in o))

# check_drift
en = w("en.md", "Raised $60M in July 2024. Eleven employees as of 2026. Partner: Acme.\n")
kr_ok = w("kr_ok.md", "2024년 7월 $60M 조달. 2026년 기준 11명. 파트너: Acme.\n")
cases.append(("drift: matching numbers pass", lambda: run("check_drift.py", "--en", en, "--kr", kr_ok), lambda rc, o: rc == 0))
kr_bad = w("kr_bad.md", "2024년 7월 $65M 조달. 2026년 기준 11명.\n")
cases.append(("drift: changed number fails", lambda: run("check_drift.py", "--en", en, "--kr", kr_bad), lambda rc, o: rc == 1 and ("65" in o or "60" in o)))
kr_name = w("kr_name.md", "2024년 7월 $60M 조달. 2026년 기준 11명. 파트너: Zenith.\n")
cases.append(("drift: new Latin name in KR only warns", lambda: run("check_drift.py", "--en", en, "--kr", kr_name), lambda rc, o: rc == 0 and "Zenith" in o))

bad = 0
for name, fn, check in cases:
    rc, out = fn()
    ok = bool(check(rc, out))
    bad += 0 if ok else 1
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        print("  rc=%s out=%s" % (rc, out.strip()[:300]))
print("RESULT %d/%d script tests as expected" % (len(cases) - bad, len(cases)))
sys.exit(1 if bad else 0)
