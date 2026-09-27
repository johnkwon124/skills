---
name: web-transcript-extractor-otter
description: Pulls the full raw transcript of an otter.ai recording using browser automation and saves it as a .txt file in a local scratch folder. Use it when another workflow, such as meeting notes, conference summaries, or research briefs, needs an Otter recording as input. It only extracts text; it does not summarize or format.
---

# Otter Transcript Extractor

A fetch primitive. It finds one recording in Otter, exports the transcript with Otter's native Export feature, and returns the path to the saved text file. The caller owns everything after that: speaker name fixes, fact checks, analysis, formatting, and the final deliverable.

## Contract

**Input:** a search keyword (company or meeting name) and an optional date preference. Default is the most recent match. Otherwise use `YYYY-MM-DD`.

**Output:** the absolute path to `{RecordingName}_otter_ai_transcript.txt` in the local Downloads folder of the machine the browser is running on. The text keeps speaker labels and timestamps and is not truncated.

The file is scratch input. Do not move it into a cloud-synced folder or a notes archive. Only the caller's finished output belongs there.

## Workflow

### 0. Confirm which browser you are driving

Downloads and local paths only make sense on the machine the browser runs on.

1. List the connected browsers.
2. If exactly one is connected, continue.
3. If two or more are connected, do not guess from device names. Ask the user which one to use and continue only after they answer.

### 1. Check browser download settings (only if exports do not land in Downloads)

Two browser settings matter:

- **Download location** must be a plain local folder. A cloud-synced folder can make the browser's temporary-file rename step hang forever, leaving a placeholder file that never completes.
- **"Ask where to save each file"** must be off. If it is on, each export opens a native Save As dialog outside the page, which browser automation cannot see or click.

Browser settings pages are usually blocked for automation. Ask the user to change these once by hand. It is a per-machine setting, not a per-run step.

### 2. Locate the recording

1. Open the browser tab context, creating a tab if needed.
2. Go to `https://otter.ai/home`.
3. Click the search field, type the keyword, and open the first result unless a date was given.

If a login page appears, stop and ask the user to sign in. If there are zero results, stop and report.

### 3. Export

1. Click the Export icon (an up arrow) near the Share button. Do not confuse it with the copy-link icon or the overflow menu next to it.
2. In the export panel, confirm these settings with one screenshot, since Otter can remember settings from an earlier session:
   - Transcript on, file format `txt`
   - Show speaker names on, show timestamps on
   - Combine paragraphs off, remove Otter branding off
   - Highlights and comments off, audio off
3. Click Export and wait about five seconds.

### 4. Verify and read

1. Make sure the Downloads folder is accessible to your file tools. Request access if needed.
2. Find `*{keyword}*.txt`. Otter may append `(1)`, `(2)` when a same-named file exists, so when in doubt pick the most recently modified file.
3. Read the file directly. No clipboard or file manager is needed.

### 5. Return

Return the absolute path. Note any speaker labels that look wrong, but do not correct them here.

## Do not

- Do not use "Copy transcript" as the main path. Automation cannot reliably read the clipboard after a browser click.
- Do not scrape the page text in chunks. Page-reading tools truncate long pages, and Export avoids that entirely.
- Do not point the browser's download location at a cloud-synced folder, and do not wait longer on a stalled download. It will not finish.
- Do not skip the browser check when several browsers are connected.
- Do not summarize, edit, or reformat the transcript.

## Failure handling (two tries, then stop)

| Failure | Retry | Then |
|---|---|---|
| Several browsers, unclear which is real | Always confirm with the user | Report and wait if the prompt times out |
| Zero search results | Try a looser keyword once | Report "no matching recording" |
| Export panel does not open | Reload once and click again | Report "export panel did not load" |
| File not in Downloads after about five seconds | Wait five more seconds, check once | Report and point to the download settings in step 1 |
| File near zero bytes | Export once more | Report "download appears incomplete" |
| Session logged out | Stop | Report "session expired, please sign in" |

After two retries at any stage, stop and report status. Do not continue silently.

## Caller integration

Call this skill first when the source is an Otter recording, then read the returned file as the transcript.
