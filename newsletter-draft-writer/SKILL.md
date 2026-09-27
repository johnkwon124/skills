---
name: newsletter-draft-writer
description: Moves a finished markdown post into a newsletter platform's web editor and saves it as a draft, never published. Use it once a post has been written and reviewed and only needs to be entered, updated, or listed.
---

# Newsletter Draft Writer

A channel skill. It only operates the editor: it copies a finished post into a draft. Content, quality and fact checks belong to whoever wrote the post. Do not rewrite, shorten or add to the text.

## Hard rules

1. Never publish. Do not click Publish, Send, Continue to publish settings, Schedule, or any "send to everyone" control. The post always stays a draft. The author decides when to publish.
2. Never log in for the user. If the browser is logged out, stop and report. The user signs in themselves.
3. Confirm the target publication before typing anything. The caller must name it on every request. If it is missing, ask. If the name shown in the editor does not match, stop and report. Do not guess a default.
4. Never delete existing drafts or published posts. When updating, replace only the body of the named draft.
5. Do not click an image upload button, because it opens a native file dialog that automation cannot control. Find the page's hidden file input and upload to it directly.
6. If a step fails, try up to two workarounds, then stop and report where it stopped.

## Setup
1. Open a browser tab on the platform's home page and check the login state with a screenshot.
2. Go to the dashboard of the target publication and read its name on screen. Compare it to the requested name.
3. If several browsers or profiles are connected and none is selected, ask the user which to use. In an unattended run, do not ask. Fall back to the file output described below.

## Create a draft
Input: target publication, title, subtitle, body in markdown (including the pre-publish checklist block), optional images with captions and positions.

1. Open a new text post.
2. Enter the title and subtitle.
3. Enter the body paragraph by paragraph, not in one paste, to avoid losing text. The editor converts markdown shortcuts (`## ` for a heading, `**bold**`, `- ` for a list). Check formatting with a screenshot after each group of paragraphs. Write tables as plain paragraphs if they do not convert.
4. For each image, place the cursor, upload through the file input, confirm the upload, then type the caption exactly as given. Handle images one at a time.
5. Add the checklist block at the end, exactly as provided.
6. Confirm the editor shows the draft as saved, then open the drafts list and confirm the new title is there. Do not report success before this check.
7. Report the draft title, the number of images inserted, and the result of the drafts list check.

## Update a draft
Input: target publication, the draft's title, and the new body.
1. Find the draft in the drafts list. If there are zero or several matches, stop and ask.
2. Select the body only (check the selection with a screenshot, since select-all may include the title), delete it, and enter the new body as above.
3. Confirm the save as above. Tell the user before replacing the body, since the old text cannot be restored.
Do not update unattended.

## List posts
Input: target publication. Read the titles from the published list and from the drafts list (the latest 30 is enough). Return both lists. The caller decides what counts as a duplicate.

## Unattended fallback
If a run cannot continue (no browser, logged out, publication mismatch, unclear interface), return the markdown and any images as files. Say at which step and why it stopped, and name the draft if it was left partly entered.

## Maintenance
If the editor interface changes and the steps stop working, work around it, report the steps that worked, and suggest updating this skill.
