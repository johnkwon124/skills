#!/usr/bin/env python3
"""check_drift.py: compare the English and Korean note for numbers and proper nouns.

Usage: python3 -I check_drift.py --en note_en.md --kr note_kr.md

FAIL (exit 1): a number in the English note is missing from the Korean note, or the Korean note has a number the English note lacks.
WARN: a Latin-script name in the Korean note does not appear in the English note (misspelling or invented name).
--strict-names also warns for capitalized names in the English note that are absent from the Korean note (noisy: place names are usually translated).
English number words from ten to twenty are read as digits (for example "Eleven" equals 11).
Integers up to --ignore-small (default 9) are skipped; section numbers and spelled-out quantities are outside this check.
"""
import argparse
import re
import sys

NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")
CAP = re.compile(r"\b[A-Z][A-Za-z&\-]{2,}\b")
STOP = set("""The This That These Those There Their They Its And But For With From Into Over Under After Before While When Where
Which What Who Why How Not Nor Per Via Our Out Are Was Were Has Have Had Can May Might Will Would Should Could One Two Three Four
Five Six Seven Eight Nine Ten Some Any All Each Both Most More Less Also Than Then Thus Yet Only Still Just Even Such Many Much
Company Team Product Funding Valuation History Revenue Licensing Capacity Testing Hardware Core Pricing Series January February
March April May June July August September October November December Open Stage Why Now What Founded Not Disclosed""".split())


WORDS = {"ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
         "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20}


def norm(t):
    t = t.replace(",", "").rstrip(".")
    if "." in t:
        a, b = t.split(".", 1)
        b = b.rstrip("0")
        return str(int(a or 0)) + ("." + b if b else "")
    return str(int(t))


def nums(text, small):
    out = set()
    for w, v in WORDS.items():
        if re.search(r"\b" + w + r"\b", text, re.I):
            out.add(str(v))
    for line in text.split("\n"):
        if line.startswith("#"):
            continue
        for m in NUM.finditer(line):
            t = norm(m.group(0))
            if re.fullmatch(r"\d+", t) and int(t) <= small:
                continue
            out.add(t)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--en", required=True)
    ap.add_argument("--kr", required=True)
    ap.add_argument("--ignore-small", type=int, default=9)
    ap.add_argument("--strict-names", action="store_true")
    a = ap.parse_args()
    en = open(a.en, encoding="utf-8").read()
    kr = open(a.kr, encoding="utf-8").read()
    ne, nk = nums(en, a.ignore_small), nums(kr, a.ignore_small)
    fail = 0
    for t in sorted(ne - nk, key=float):
        print(f"[FAIL] number in EN missing in KR: {t}")
        fail += 1
    for t in sorted(nk - ne, key=float):
        print(f"[FAIL] number in KR missing in EN: {t}")
        fail += 1
    warn = 0
    krnames = {m.group(0) for m in CAP.finditer(kr)} - STOP
    for n in sorted(krnames):
        if n not in en:
            print(f"[WARN] name in KR not found in EN: {n}")
            warn += 1
    if a.strict_names:
        for n in sorted({m.group(0) for m in CAP.finditer(en)} - STOP):
            if n not in kr:
                print(f"[WARN] name in EN not found in KR: {n}")
                warn += 1
    print(f"SUMMARY fail={fail} warn={warn}")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
