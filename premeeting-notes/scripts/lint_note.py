#!/usr/bin/env python3
"""lint_note.py: deterministic text checks for final notes (EN or KR) before delivery.

Usage:
  python3 -I lint_note.py --mode pre  note.md
  python3 -I lint_note.py --mode post note.docx
  python3 -I lint_note.py --mode pre  note.md --allow R14,R15

Modes:
  pre   premeeting-notes: no meeting exists, so any meeting attribution is a defect.
  post  meeting-notes: reporting-style framing of what a speaker said is a defect.

Option --max-words N adds R19 (FAIL when the word count of the markdown exceeds N). Quick mode uses 1200 for the English note.
Exit code 1 if any FAIL is found. WARN lines need a human decision, never an automatic edit.
Rules cover the mechanical part of the feedback only. Judgment checks stay in the checklist.
The file contains no literal em dash; U+2014 is built from an escape.

Two configurable private-watch rules, both inactive until their token file exists next to this
script (one token per line, "#" comments; see the matching .example.txt templates):
  R09 PRIVATE_TOKEN  - lint_private_tokens.txt  : firm names, codenames, affiliations
  R08 INTERNAL_NAME  - lint_internal_names.txt  : internal agent, tool or project names
With no token file the corresponding rule is inactive; the generic R08 markers always apply.
"""
import argparse
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

EM_DASH = chr(0x2014)  # built from a code point so this file holds no literal em dash
BANNED_KR = "".join(chr(c) for c in (0xD14C, 0xC81C))  # Korean transliteration of "thesis"; notes must say "thesis"

def load_tokens(filename):
    """Private-watch tokens, one per line in the given file next to this script; "#" comments."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    try:
        with open(path, encoding="utf-8") as f:
            return [ln.strip() for ln in f if ln.strip() and not ln.strip().startswith("#")]
    except OSError:
        return []

MONEY = re.compile(r"\$\s?\d[\d,.]*\s?(?:[MBK]\b|million|billion|thousand)?", re.I)
CONTRAST = re.compile(
    r"\b(differs?|differ from|differing|versus|vs\.?|whereas|while|instead|compared (?:to|with)|than|however|but)\b"
    r"|다르|대비|반면|차이|그러나",  # 다르, 대비, 반면, 차이, 그러나
    re.I,
)
CONTRAST_STRICT = re.compile(
    r"\b(differs?|differ from|differing|versus|vs\.?|whereas|compared (?:to|with)|than)\b|다르|대비|차이", re.I)
VALUATION = re.compile(
    r"\b(post|pre)-?\s?money\b|\bvaluation\b|밸류에이션|포스트머니|프리머니",
    re.I,
)
RAISE = re.compile(
    r"\b(announced|raise[ds]?|round|financing|investment|funding)\b|발표|조달|라운드|투자금",
    re.I,
)

ROMAN_PREV = {"phase", "type", "series", "stage", "tier", "class", "part", "level", "group", "chapter", "gen", "generation"}


def read_text(path):
    if path.lower().endswith(".docx"):
        with zipfile.ZipFile(path) as z:
            root = ET.fromstring(z.read("word/document.xml"))
        ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
        paras = []
        for p in root.iter(ns + "p"):
            paras.append("".join(t.text or "" for t in p.iter(ns + "t")))
        return "\n".join(paras)
    with open(path, encoding="utf-8") as f:
        return f.read()


def word_count(text):
    """Words in the note body: markdown markers and bullets are not counted."""
    n = 0
    for line in text.split("\n"):
        line = re.sub(r"^\s*(#+|[-*])\s+", "", line).replace("**", "")
        n += sum(1 for t in line.split() if re.search(r"[A-Za-z0-9가-힣]", t))
    return n


def sentences(text):
    out = []
    for ln, line in enumerate(text.split("\n"), 1):
        for s in re.split(r"(?<=[.!?])\s+", line):
            if s.strip():
                out.append((ln, s.strip()))
    return out


def line_rules(mode):
    rules = [
        ("R01", "EM_DASH", "FAIL", re.compile(EM_DASH)),
        ("R02", "BANNED_TERM", "FAIL", re.compile(BANNED_KR)),
        ("R03", "VENDOR_OR_DB_LABEL", "FAIL", re.compile(
            r"pitchbook|"
            r"\b(?:deal|funding|commercial|paid|private|investor|startup) databases?\b|"
            r"\bdatabase (?:lists?|shows?|records?|indicates?|data)\b", re.I)),
        ("R06", "SELF_NARRATION", "FAIL", re.compile(
            r"\boriginally\b|\bon re-?check(?:ing)?\b|\bin this revision\b|\bwhile reviewing\b|\bpreviously (?:stated|wrote|listed)\b|"
            r"\bcorrected from\b|\bearlier draft\b|처음에는|수정 전|재확인 결과|이번 개정", re.I)),
        ("R08", "INTERNAL_MARKER", "FAIL", re.compile(
            r"\bMODE\s?[A-DR]\b|\[UNVERIFIED\]|\[f/u\]|\[footnote\]|"
            r"\[VC insight\]|\[Analysis\]|\[Action Item\]|\bTrack [AB]\b|\bSource (?:Mode|Record)\b|\bclaims? ledger\b", re.I)),
        ("R10", "AI_TELL_WORD", "FAIL", re.compile(
            r"\b(notably|importantly|significantly|furthermore|moreover|cutting-edge|revolutionary|highly innovative)\b", re.I)),
        ("R11", "AI_TELL_SOFT", "WARN", re.compile(
            r"\b(leverag\w+|utili[sz]\w+|facilitat\w+|industry-leading|raises? the question of)\b", re.I)),
        ("R12", "UNDISCLOSED_AS_ZERO", "WARN", re.compile(
            r"\b(?:has|have|had) no (?:grants?|debt|customers?|revenue|pilots?|lois?)\b(?!\s+(?:disclosed|found|identified|confirmed))|"
            r"\bzero (?:grants?|customers?|revenue|debt)\b|(?:그랜트|부채|매출)\s?없음", re.I)),
        ("R14", "RELATIVE_DATE", "WARN", re.compile(
            r"\b(recently|currently|last year|this year|next year|so far|nowadays)\b|최근|올해|작년", re.I)),
        ("R15", "OBVIOUS_ABSENCE", "WARN", re.compile(
            r"\b(?:absent|missing) from the [^.]{0,40}(?:announcement|release|round)\b|"
            r"\bdid not appear in the [^.]{0,40}(?:announcement|release|round)\b", re.I)),
        ("R16", "TAG_AS_TRACTION", "WARN", re.compile(
            r"(?:listed|tagged|classified) as (?:revenue[- ]generating|generating revenue)|\bgenerating revenue\b", re.I)),
        ("R17", "SELF_GRADING", "WARN", re.compile(r"\b(most accurate|most reliable|best available)\b|가장 정확", re.I)),
    ]
    names = load_tokens("lint_internal_names.txt")
    if names:
        rules.append(("R08", "INTERNAL_NAME", "FAIL",
                      re.compile("|".join(re.escape(t) for t in names), re.I)))
    toks = load_tokens("lint_private_tokens.txt")
    if toks:
        rules.append(("R09", "PRIVATE_TOKEN", "FAIL",
                      re.compile("|".join(re.escape(t) for t in toks), re.I)))
    if mode == "pre":
        rules.append(("R13", "MEETING_ATTRIBUTION_IN_PRE", "FAIL", re.compile(
            r"\b(?:the )?(?:founder|ceo|cto|cofounder|co-founder) (?:said|told|explained|mentioned)\b|"
            r"\b(?:told|said to) us\b|\bwe met\b|\bin our (?:meeting|call)\b", re.I)))
        rules.append(("R18", "MEETING_VENUE_REFERENCE", "WARN", re.compile(
            r"\b(?:during|in) the (?:meeting|call)\b|미팅(?:에서|중)", re.I)))
    else:
        rules.append(("R13", "REPORTING_FRAME", "FAIL", re.compile(
            r"\b(?:the )?(?:founder|ceo|cto|speaker|presenter|team|management) "
            r"(?:said|described|positioned|expects?|estimated|claimed|argued|stated|noted)\b|"
            r"(?:라고|이라고)\s*(?:밝|설명|주장|추정|언급)(?:힘|혔|했|함|하)", re.I)))
    return rules


def check(text, mode, allow):
    findings = []
    for ln, line in enumerate(text.split("\n"), 1):
        for rid, name, level, rx in line_rules(mode):
            if rid in allow:
                continue
            m = rx.search(line)
            if m:
                findings.append((level, rid, name, ln, line.strip()[:140]))
        if "R07" not in allow:
            for m in re.finditer(r"\b(I|we|We|my|My|our|Our)\b|\bus\b", line):
                if m.group(0) == "I":
                    prev = re.findall(r"[A-Za-z]+", line[: m.start()])
                    if prev and prev[-1].lower() in ROMAN_PREV:
                        continue
                findings.append(("FAIL", "R07", "FIRST_PERSON", ln, line.strip()[:140]))
                break
            if re.search(r"(?<![가-힣])(저희|나는|내가|저는|제가)(?![가-힣])|"
                         r"(?<![가-힣])우리(?:는|가|의|를|도)?(?![가-힣])", line):
                findings.append(("FAIL", "R07", "FIRST_PERSON_KR", ln, line.strip()[:140]))
    for ln, s in sentences(text):
        if "R04" not in allow and VALUATION.search(s) and RAISE.search(s) and CONTRAST_STRICT.search(s):
            findings.append(("FAIL", "R04", "UNLIKE_METRIC_COMPARISON", ln, s[:140]))
        if "R05" not in allow:
            figs = {re.sub(r"\s", "", m.group(0).lower()) for m in MONEY.finditer(s)}
            if (len(figs) >= 2 and CONTRAST.search(s)) or re.search(
                r"\bsources? (?:disagree|differ|conflict)\b|\bdiscrepanc|\bconflicting (?:figures|reports|numbers)\b|"
                r"소스(?:마다|에 따라)[^.]{0,12}(?:다르|상이)", s, re.I):
                findings.append(("WARN", "R05", "COMPETING_FIGURES_IN_PROSE", ln, s[:140]))
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--mode", choices=["pre", "post"], required=True)
    ap.add_argument("--allow", default="", help="comma separated rule ids to skip")
    ap.add_argument("--max-words", type=int, default=0, help="FAIL (R19) when the word count exceeds this value")
    a = ap.parse_args()
    allow = {x.strip() for x in a.allow.split(",") if x.strip()}
    text = read_text(a.file)
    findings = check(text, a.mode, allow)
    words = word_count(text)
    if a.max_words and words > a.max_words and "R19" not in allow:
        findings.append(("FAIL", "R19", "WORD_LIMIT", 0, f"{words} words > {a.max_words}"))
    seen = set()
    for level, rid, name, ln, snippet in findings:
        key = (rid, ln)
        if key in seen:
            continue
        seen.add(key)
        print(f"[{level}] {rid} {name} line {ln}: {snippet}")
    fails = sum(1 for f in findings if f[0] == "FAIL")
    warns = sum(1 for f in findings if f[0] == "WARN")
    print(f"SUMMARY fail={fails} warn={warns} mode={a.mode} words={words}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
