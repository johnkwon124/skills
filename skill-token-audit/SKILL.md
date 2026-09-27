---
name: skill-token-audit
description: Flags token cost and quality problems in a library of skill files (SKILL.md), such as unclear triggers, dead references, duplicated guidance, and over-built agent chains. Use it when skills feel heavy, when trigger descriptions overlap or misfire, or before cleaning up a skill library.
---

# skill-token-audit

## Scope and limits

Two modes. Both are read-only. Suggested edits appear in the report and are applied only after the skill's author approves.

- **Mode T, token cost.** Where does a skill's context cost come from?
- **Mode Q, quality.** Would the skill run cleanly, trigger at the right time, and stay lean?

Chat tools usually do not expose real per-message token counts. Every number in Mode T is a structural estimate. Label it as an estimate in the report and avoid strong conclusions from small differences.

Pick the mode from the request: cost words ("heavy", "slow", "usage") mean T, cleanup words ("review", "dead", "messy") mean Q, both or "full audit" means T+Q. If unclear, ask one short question.

## Mode T: token cost

### Collect

For each skill in scope, record:
- Size of SKILL.md and of each reference file (characters, then divide by 4 for a rough token count).
- What always loads and what loads only on demand.
- Number of explicit tool calls, web searches, and sub-agents.
- Output type and size (inline text, a document, several languages).
- Number of wait or confirmation gates.

For a whole library, list every skill directory and repeat. For a specific past session, read its transcript if your environment provides one.

### Estimate

Cost per run is roughly: fixed system context + the skill text + files it loads + tool results + output. Use these rough rules and replace them with measured values when you have them.

| Driver | Rough estimate |
| --- | --- |
| Skill text | characters / 4 |
| One web search result set | 1,500 to 3,000 tokens |
| Each extra sub-agent | Adds a full context of its own. Two agents cost about twice one, not less. |
| One page of document output | about 800 tokens |
| Same output in two languages | roughly double |
| Chained skills | Each skill in the chain adds its text and carries the prior context forward |

Grade each run: HEAVY above 20,000 tokens, MODERATE 8,000 to 20,000, LEAN below 8,000.

### Ten inefficiency patterns

Structural
1. Over-specification: repeated instructions, duplicate sections.
2. Loading files the task does not need, every time.
3. The same persona or tone guidance copied across skills.
4. Agent structure too large for the task, such as a three-agent chain for a short answer.

Behavioral
5. Retrying failures inside one long accumulated context.
6. Needless skill chaining, where skill A calls B calls C.
7. Starting a heavy skill late in a long session.
8. Excess agent-to-agent Q&A loops.

Output
9. Always producing two languages or formats when one is asked for.
10. A fixed large deliverable regardless of scope.

## Mode Q: quality and trigger review

### Checklist

1. **Dead tool references.** The skill names a tool that does not exist in the environment.
2. **Dead file references.** It loads a file or script that is missing. Verify by listing the path.
3. **Wrong paths.** Hardcoded paths that do not match where the skill actually lives. Prefer paths relative to the skill folder.
4. **Unreachable logic.** A branch whose condition can never hold, or a step that depends on data an earlier failed step never produced.
5. **Redundant instructions.** The same rule stated twice, or the same persona defined in SKILL.md and in a reference file.
6. **Over-built agent chains.** Rule of thumb: inline text needs no agents, a single document needs at most two, and three or more only when three or more independent sections are built in parallel.
7. **Stale capability assumptions.** Old tool names, retired parameters, changed path conventions.
8. **Output mismatch.** The skill promises a format (for example slides) but never says how to produce it.
9. **Conflicting instructions.** "Finish without creating files" versus "save a document and link it", or "ask few questions" versus several confirmation gates.
10. **Context bloat.** Long persona text that two sentences would replace, example tables that no step uses, guidance that duplicates global instructions.
11. **Trigger quality.** Check the frontmatter description, since it decides when the skill loads.
    - It says what the skill does and when to use it, in concrete terms.
    - The trigger phrases are specific enough not to fire on unrelated requests.
    - No two skills claim the same trigger without saying how they differ. List overlapping pairs.
    - It names the "do not use for" cases when a neighbor skill covers them.
    - It is short. A description longer than a few sentences is paid for on every request that scans the library.

### Procedure

1. **Read** the whole SKILL.md and its references.
2. **Inventory** tool names, file paths, agent structure, and conditional branches.
3. **Verify** each referenced file and path exists.
4. **Flag** issues against the checklist with a severity: Critical (would fail or misfire), Warning (wasteful or ambiguous), Note (cosmetic).
5. **Propose** a concrete fix for each: delete, edit, or merge.
6. **Output** using the structure below.

## Output structure

Mode T:

```
# Token Audit: {target} ({date})
1. Summary: scope, overall grade, 2 to 3 key findings, 1 to 2 immediate actions.
2. Load estimate: table of input and output drivers, plus a note that values are estimates.
3. Patterns found: pattern / where / token impact / cause. Or "none detected".
4. Comparison matrix: one row per skill (library audits only).
5. Recommendations by priority: problem / fix / expected savings / effort (quick edit, skill change, redesign).
```

Mode Q:

```
# Skill Quality Audit: {skill} ({date})
1. Summary: issue count, severity split, 2 to 3 key findings.
2. Issues: checklist number / severity / location / description / fix.
3. Simplification proposals: sections that can be cut or merged, with expected line savings.
4. Trade-off warnings: where trimming could reduce quality.
5. Trigger overlap: pairs of skills with competing descriptions (library audits only).
```

## Principles

- State that numbers are estimates. Do not overstate conclusions.
- Something that looks wasteful may be deliberate. Say so when the intent is plausible.
- Any simplification must preserve output quality and the intended workflow. Name the risk when there is one.
- Never edit skill files during an audit. Put proposed changes in the report.
- Finish in the chat as markdown. Do not create files unless asked.
