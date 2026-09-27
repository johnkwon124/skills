# Document and PDF generation

This report uses real footnotes and always ships as a document plus a PDF.

## Setup

Use a Word-generation library (the examples use the Node `docx` package). Install it if missing. Use `require('docx')` with the plain package name.

Known pitfalls:
1. Use clear shading, not solid shading, for highlight boxes.
2. Put page breaks inside a paragraph: `new Paragraph({ children: [new PageBreak()] })`.

## Footnotes

Pass a `footnotes` map to the document constructor and reference entries from body text.

```javascript
const footnotes = {
  1: { children: [ new Paragraph({ children: [ new TextRun(
        "Example Agency, 2025. Quarterly incident report. https://example.com/report") ] }) ] },
};

new Paragraph({
  children: [
    new TextRun({ text: "The agency reported a rise in incidents in the first quarter", size: 22 }),
    new FootnoteReferenceRun(1),
    new TextRun({ text: ".", size: 22 }),
  ],
  spacing: { before: 120, after: 120 }, indent: { firstLine: 440 }
});

const doc = new Document({ footnotes, sections: [ /* ... */ ] });
```

Rules: footnote every key figure, contract, and quotation. Each footnote gives source name, year, and URL. For "estimate" and "analysis" items, state the basis.

## Layout

- US Letter, one-inch margins, header with report title and "Confidential", footer with page number.
- Title 26 pt bold dark blue, centered. Subtitle 12 pt gray.
- Heading 1: 16 pt bold with bottom border. Heading 2: 13 pt bold. Body: 11 pt, first-line indent.
- Tables only for comparisons and summaries.

## PDF

```bash
soffice --headless --convert-to pdf --outdir . "<report>.docx"
pdftotext -f 1 -l 1 "<report>.pdf" - | head
```

Check that the page count is not zero and that the first page text renders. If verification changes the document, convert again so both files match.

File name: `<Company>_PreDiligence_Report_v<N>_<YYYY-MM-DD>.docx` and `.pdf`.
