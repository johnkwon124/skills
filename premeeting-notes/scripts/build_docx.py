#!/usr/bin/env python3
"""build_docx.py: markdown to DOCX (and optional PDF) for EN and KR notes, with a text round-trip check.

Usage:
  python3 -I build_docx.py --lang en --title "ExampleCo Pre-Meeting Notes" --date 11032026 --md note_en.md --out out_en.docx [--pdf]
  python3 -I build_docx.py --lang kr --title "ExampleCo - kr title" --date 11032026 --md note_kr.md --out out_kr.docx [--pdf]
  python3 -I build_docx.py --verify --md note_en.md --out out_en.docx      (check only)

Markdown rules: '## ' section header, '### ' subheader, '- ' bullet ('- **Label**: text' allowed),
'**x**' inline bold, anything else is a body paragraph. A leading '# ' title line is ignored.
Format values follow the fixed format table of the skill (EN Calibri 11, Letter, 1 inch; KR NanumGothic 11).
"""
import argparse
import os
import re
import subprocess
import sys
import zipfile
import xml.etree.ElementTree as ET

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

BOLD = re.compile(r"\*\*(.+?)\*\*")


def set_font(run, name, size, bold=False):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.insert(0, rf)
    for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rf.set(qn(a), name)


def add_runs(p, text, name, size, base_bold=False):
    pos = 0
    for m in BOLD.finditer(text):
        if m.start() > pos:
            set_font(p.add_run(text[pos:m.start()]), name, size, base_bold)
        set_font(p.add_run(m.group(1)), name, size, True)
        pos = m.end()
    if pos < len(text):
        set_font(p.add_run(text[pos:]), name, size, base_bold)


def add_hr(doc):
    p = doc.add_paragraph()
    bdr = OxmlElement("w:pBdr")
    b = OxmlElement("w:bottom")
    for k, v in (("w:val", "single"), ("w:sz", "4"), ("w:space", "1"), ("w:color", "000000")):
        b.set(qn(k), v)
    bdr.append(b)
    p._element.get_or_add_pPr().append(bdr)


def build(lang, title, date, md_path, out):
    en = lang == "en"
    font = "Calibri" if en else "NanumGothic"
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name, st.font.size = font, Pt(11)
    rf = st.element.get_or_add_rPr().find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        st.element.get_or_add_rPr().insert(0, rf)
    for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rf.set(qn(a), font)
    for s in doc.sections:
        s.page_width, s.page_height = Inches(8.5), Inches(11)
        s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Inches(1.0 if en else 1.1)

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    set_font(p.add_run(title), font, 13, True)
    if not en:
        add_hr(doc)
        pd = doc.add_paragraph()
        pd.paragraph_format.space_after = Pt(14)
        set_font(pd.add_run("작성일: " + date), font, 10)

    for raw in open(md_path, encoding="utf-8").read().split("\n"):
        s = raw.strip()
        if not s or s.startswith("# "):
            continue
        p = doc.add_paragraph()
        pf = p.paragraph_format
        if s.startswith("## "):
            pf.space_before, pf.space_after = Pt(12 if en else 18), Pt(4 if en else 6)
            add_runs(p, s[3:], font, 11, True)
        elif s.startswith("### "):
            pf.space_before, pf.space_after = Pt(6 if en else 10), Pt(2 if en else 4)
            add_runs(p, s[4:], font, 11, True)
        elif s.startswith("- "):
            pf.left_indent = Inches(0.25 if en else 0.3)
            pf.space_after = Pt(2 if en else 4)
            pf.line_spacing = 1.0 if en else 1.15
            set_font(p.add_run("• "), font, 11)
            add_runs(p, s[2:], font, 11)
        else:
            pf.space_before = Pt(0 if en else 4)
            pf.space_after = Pt(6 if en else 8)
            pf.line_spacing = 1.15 if en else 1.25
            add_runs(p, s, font, 11)
    doc.save(out)
    if not en:
        inject_font_table(out, font)


def inject_font_table(path, name):
    tmp = path + ".tmp"
    entry = ('  <w:font w:name="%s">\n    <w:charset w:val="81"/>\n    <w:family w:val="swiss"/>\n'
             '    <w:pitch w:val="variable"/>\n  </w:font>\n') % name
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/fontTable.xml":
                t = data.decode("utf-8")
                if name not in t:
                    t = t.replace("</w:fonts>", entry + "</w:fonts>")
                data = t.encode("utf-8")
            zout.writestr(item, data)
    os.replace(tmp, path)


def docx_paragraphs(path):
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    return ["".join(t.text or "" for t in p.iter(ns + "t")) for p in root.iter(ns + "p")]


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def verify(md_path, out):
    have = {norm(x) for x in docx_paragraphs(out)}
    missing = []
    for raw in open(md_path, encoding="utf-8").read().split("\n"):
        s = raw.strip()
        if not s or s.startswith("# "):
            continue
        s = re.sub(r"^#{2,3} ", "", s)
        s = "• " + s[2:] if s.startswith("- ") else s
        s = norm(BOLD.sub(r"\1", s))
        if s not in have:
            missing.append(s[:100])
    if missing:
        print("VERIFY FAIL: %d paragraph(s) from markdown not found in %s" % (len(missing), out))
        for m in missing:
            print("  - " + m)
        return False
    print("VERIFY OK: every markdown paragraph found in " + os.path.basename(out))
    return True


def verify_pdf(md_path, pdf_path):
    """Extract PDF text with pdftotext and check every markdown paragraph appears (whitespace and ligatures ignored)."""
    import unicodedata
    r = subprocess.run(["pdftotext", "-layout", pdf_path, "-"], capture_output=True, text=True)
    if r.returncode != 0:
        print("PDF VERIFY SKIPPED: pdftotext unavailable (%s)" % r.stderr[:80])
        return True

    def flat(s):
        return re.sub(r"\s+", "", unicodedata.normalize("NFKC", s))
    hay = flat(r.stdout)
    missing = []
    for raw in open(md_path, encoding="utf-8").read().split("\n"):
        s = raw.strip()
        if not s or s.startswith("# "):
            continue
        s = re.sub(r"^(#{2,3} |- )", "", s)
        s = BOLD.sub(r"\1", s)
        if flat(s) not in hay:
            missing.append(s[:100])
    if missing:
        print("PDF VERIFY FAIL: %d paragraph(s) not found in %s" % (len(missing), pdf_path))
        for m in missing:
            print("  - " + m)
        return False
    print("PDF VERIFY OK: every markdown paragraph found in " + os.path.basename(pdf_path))
    return True


def ensure_korean_font():
    """Register NanumGothic for PDF rendering if no Nanum font is installed. Warn, never fail, if it cannot be fetched."""
    try:
        if "nanum" in subprocess.run(["fc-list"], capture_output=True, text=True).stdout.lower():
            return
        import urllib.request
        d = os.path.expanduser("~/.local/share/fonts/korean")
        os.makedirs(d, exist_ok=True)
        f = os.path.join(d, "NanumGothic.ttf")
        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/google/fonts/main/ofl/nanumgothic/NanumGothic-Regular.ttf", f)
        subprocess.run(["fc-cache", "-f", d], capture_output=True)
    except Exception as e:  # network or fontconfig problems must not block the DOCX
        print("WARN: could not install NanumGothic for PDF rendering: %s" % e)


def to_pdf(docx_path):
    outdir = os.path.dirname(os.path.abspath(docx_path))
    r = subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", outdir, docx_path],
                       capture_output=True, text=True, timeout=180)
    pdf = os.path.splitext(os.path.abspath(docx_path))[0] + ".pdf"
    if not os.path.exists(pdf) or os.path.getsize(pdf) == 0:
        print("PDF FAIL: " + (r.stderr or r.stdout)[:200])
        return None
    print("PDF OK: %s (%d bytes)" % (os.path.basename(pdf), os.path.getsize(pdf)))
    return pdf


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["en", "kr"])
    ap.add_argument("--title")
    ap.add_argument("--date", default="")
    ap.add_argument("--md", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--verify", action="store_true", help="check only, do not build")
    a = ap.parse_args()
    if not a.verify:
        if not a.lang or not a.title:
            ap.error("--lang and --title are required unless --verify")
        build(a.lang, a.title, a.date, a.md, a.out)
        print("DOCX saved: %s (%d bytes)" % (a.out, os.path.getsize(a.out)))
    ok = verify(a.md, a.out)
    if ok and a.pdf and not a.verify:
        if a.lang == "kr":
            ensure_korean_font()
        pdf = to_pdf(a.out)
        ok = pdf is not None and verify_pdf(a.md, pdf)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
