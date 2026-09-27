---
name: skill-packager
description: Checks a skill folder and packages it as a versioned zip, with a single top-level folder, an updated changelog, and its references. Use it once a skill is finished or edited and needs a clean, installable archive, or for a repeatable release routine across a set of skills.
---

# Skill Packager

A skill is a folder with a `SKILL.md` and optional `references/` and `scripts/`. This skill turns such a folder into a release archive you can upload, share, or keep in version control. It validates first, so a broken skill never gets packaged.

## Principles

- Work on a copy. Never edit the original folder while packaging.
- Define success before you change anything, for example: frontmatter parses, description is within the length limit, version bumped, no banned strings.
- Make the smallest change that fixes the problem. Do not reformat unrelated sections.
- If validation fails, stop and report what failed. Do not package anyway.
- After two failed attempts at the same fix, stop and report instead of trying a third.

## Workflow

### 1. Define the change

Write one line: what is changing and why. Pick the new version number. Use a simple scheme, for example patch for wording fixes, minor for new steps or options, major for a changed contract.

### 2. Edit a working copy

1. Copy the skill folder to a scratch location.
2. Edit `SKILL.md` and any references or scripts in the copy.
3. Bump the version wherever the skill states it, and add one changelog line.
4. Remove references that no longer point to anything (deleted files, renamed sections).

### 3. Check the structure

- Exactly one `SKILL.md`, at the root of the skill folder.
- Frontmatter has `name` and `description`. The name is lowercase letters, digits, and single hyphens, at most 64 characters, and matches the folder name.
- The description is at most 1024 characters and has no angle brackets. Count it with code, not by eye.
- Long detail lives in `references/`, not in `SKILL.md`. If `SKILL.md` grows past about 500 lines, split it.
- No file is orphaned: every reference or script is mentioned from `SKILL.md`.

### 4. Run the validator and build the zip

Use `scripts/package_skill.py`:

```bash
python3 scripts/package_skill.py path/to/my-skill out/ \
  --issue "Clarified step 3 and added a failure table" \
  --old-version 1.1 --new-version 1.2
```

It checks the frontmatter and name rules, checks that there is a single `SKILL.md`, and scans for any banned strings you list with `--ban`. On success it writes `my-skill-v1.2-YYYYMMDD.zip`.

### 5. Confirm the archive layout

Every file must sit inside one top-level folder named after the skill. Nothing may sit at the zip root.

```
my-skill/
  SKILL.md
  CHANGELOG.md
  references/
    ...
  scripts/
    ...
```

List the archive contents and confirm this before you hand it over.

### 6. Report

State the skill name, old and new version, the archive path, and anything you found but left alone. Keep the report about the result. Do not narrate drafts or intermediate mistakes.

## Changelog rules

- Keep `CHANGELOG.md` inside the skill folder. Append one dated entry per release, newest last.
- Each entry is one or two lines: the version change and what improved.
- Do not record incident stories or debugging history. State the change.

## Naming the archive

Use `<skill-name>-v<version>-<YYYYMMDD>.zip`. Store archives in one flat folder, or in one subfolder per skill if you release often.

## Checks that catch real problems

- **Conflicts between skills:** two skills give different rules for the same file, tool, or trigger phrase.
- **Version drift:** one skill names another at a specific version that has since changed.
- **Duplicated text:** the same paragraph repeated across skills. Keep it only if each skill must work alone.
- **Unwanted characters or phrases:** any style rule you enforce, such as banning a punctuation mark, goes in the validator's `--ban` list so packaging enforces it.

## Do not

- Do not package a skill that failed validation.
- Do not put anything at the zip root.
- Do not rewrite sections unrelated to the change.
- Do not include secrets, personal data, or absolute local paths in a skill.
