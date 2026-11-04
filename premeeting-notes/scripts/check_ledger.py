#!/usr/bin/env python3
"""check_ledger.py: every number in the note must exist in the claims ledger.

Usage:
  python3 -I check_ledger.py --note note_en.md --ledger SourceRecord_X_MMDDYYYY.md
  python3 -I check_ledger.py --note note_en.md --ledger ledger.md --whole-file   (no claims table; use all numbers in the file)

The ledger is the markdown table under a heading that contains "Claims ledger".
Cells that are URLs are ignored, so ids inside links cannot mask an unsourced number.
Integers up to --ignore-small (default 9) are not checked (words like "three phases", "2 to 3 times").
Exit code 1 when a number in the note has no match in the ledger (unless --warn-only).
This catches numbers that were never sourced. It does not prove a number is attached to the right claim.
"""
import argparse
import re
import sys

NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")


def norm(tok):
    tok = tok.replace(",", "")
    if "." in tok:
        a, b = tok.split(".", 1)
        return str(int(a or 0)) + "." + b.rstrip("0") if b.rstrip("0") else str(int(a or 0))
    return str(int(tok))


def tokens(text):
    out = []
    for m in NUM.finditer(text):
        t = m.group(0).rstrip(",")
        if t:
            out.append((norm(t), m.start()))
    return out


def ledger_text(path, whole):
    raw = open(path, encoding="utf-8").read()
    if whole:
        return raw
    lines, on, found = [], False, False
    for ln in raw.split("\n"):
        if re.match(r"^#+\s.*claims ledger", ln, re.I):
            on, found = True, True
            continue
        if on and re.match(r"^#+\s", ln):
            on = False
        if on and ln.strip().startswith("|") and not re.match(r"^\|\s*-", ln.strip()):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            lines.append(" ".join(c for c in cells if not c.lower().startswith("http")))
    if not found:
        sys.exit("ERROR: no heading containing 'Claims ledger' found; use --whole-file or fix the ledger")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--note", required=True)
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--whole-file", action="store_true")
    ap.add_argument("--ignore-small", type=int, default=9)
    ap.add_argument("--warn-only", action="store_true")
    a = ap.parse_args()
    known = {t for t, _ in tokens(ledger_text(a.ledger, a.whole_file))}
    missing = []
    for ln, line in enumerate(open(a.note, encoding="utf-8").read().split("\n"), 1):
        if line.startswith("#"):
            continue
        for t, pos in tokens(line):
            if re.fullmatch(r"\d+", t) and int(t) <= a.ignore_small:
                continue
            if t not in known:
                missing.append((ln, t, line.strip()[:110]))
    seen = set()
    for ln, t, ctx in missing:
        if (ln, t) in seen:
            continue
        seen.add((ln, t))
        print(f"[UNSOURCED] line {ln}: {t} | {ctx}")
    print(f"SUMMARY unsourced={len(seen)}")
    sys.exit(0 if (a.warn_only or not seen) else 1)


if __name__ == "__main__":
    main()
