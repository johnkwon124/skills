---
name: sourcing-summary-email
description: Compiles meeting notes on recently sourced startups into a five-bullet-per-company summary email draft for a team. Use it whenever a list of company names needs a short, analytical write-up for circulation.
---

# Sourcing Summary Email

Produce an email draft that summarizes recently sourced companies in five analytical bullets each. Output is a draft only. Nothing is sent and no files are saved.

## Workflow

### 1. Parse the company list
Extract every company name. One company is fine. Tag each as `[New]` or `[Follow up]`, inferring from context and asking only if it is unclear.

### 2. Find the notes
For each company, search your notes store for a meeting note or meeting summary. Prefer these over one-pagers and raw transcripts. If notes exist in more than one language, use the one you are writing in. If no note exists, write the bullets from public research and add "(based on public information only)" in the footer.

### 3. Extract content
Read the matched note. In long documents, focus on the overview, the technical differentiation, funding, competitive position, and open questions or risks.

### 4. Write five bullets per company
Use this order. If a section has no material, substitute another.

1. Market context and problem: the specific gap the company addresses, and why existing alternatives fall short. Add your own analysis rather than repeating the company's pitch.
2. Solution and differentiation: the core technology or operating model and the concrete differentiator. Mark unverified figures ("company figures, not independently verified"). Add one line on how credible the moat looks.
3. Business traction: funding round, lead investor, total raised, pilots or paying customers. Note when figures come only from the company, and say what the traction signals about commercial validation.
4. Competitive positioning: where the company sits relative to incumbents and other startups, and your preliminary view of whitespace or overlap.
5. Key investment considerations: two or three specific assumptions behind the bull case and what would have to be true. Name the assumption, not a generic risk label. End with the next diligence step.

Style rules:
- Two or three sentences per bullet, most important fact first.
- Do not start with "The company".
- Each bullet needs an observation and a "so what" inference.
- Use numbers only if verified or clearly attributed.
- Objective and analytical. No promotional adjectives. Present company claims as claims and add an independent read.
- No em dashes.

### 5. Optional second-language section
If the readers need one, add a short section in that language under each company. Rewrite from the meaning rather than translating sentence by sentence. Keep technical terms (Series B, capex) in English, keep caveats, and keep the length equal to the English section.

### 6. Subject line
- One company: `[New] - Company Name` or `[Follow up] - Company Name`
- Several: `[New] - Company A / [Follow up] - Company B`

### 7. Create the draft
Use your email tool's draft function with an HTML body only. Leave the recipient for the user to fill unless they name one. Use this layout.

```html
<div style="font-family:Arial,Helvetica,sans-serif;font-size:13px;color:#222;line-height:1.65;">
<p>Team,</p>
<p>Brief on [Company Name(s)] from a recent intro call.</p>
<hr style="border:none;border-top:1px solid #ddd;margin:16px 0;"/>

<!-- Repeat per company -->
<h3 style="color:#1F4E79;font-size:14px;margin-bottom:2px;">[COMPANY NAME]
  <span style="font-size:11px;color:#888;font-weight:normal;">&nbsp;|&nbsp;[Sector]</span></h3>
<p style="font-size:11px;color:#555;font-style:italic;">Summary</p>
<ul style="margin:4px 0 12px 20px;padding:0;">
  <li style="margin-bottom:6px;">[Bullet 1]</li>
  <li style="margin-bottom:6px;">[Bullet 2]</li>
  <li style="margin-bottom:6px;">[Bullet 3]</li>
  <li style="margin-bottom:6px;">[Bullet 4]</li>
  <li style="margin-bottom:6px;">[Bullet 5]</li>
</ul>
<!-- optional second-language block here, same structure -->
<hr style="border:none;border-top:1px solid #eee;margin:16px 0;"/>

<!-- Only if a note was missing: -->
<!-- <p style="font-size:11px;color:#aaa;">* [Company]: based on public information only.</p> -->
<p>Happy to discuss further. Notes are available on request.</p>
</div>
```

Replace every placeholder with real names. No dates in the body and no signature.

### 8. Report
Tell the user the draft was created, with its subject, list the note files used, and remind them that attachments must be added by hand if they want any.
