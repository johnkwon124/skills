---
name: web-transcript-extractor-soniox
description: Pulls the full raw transcript of a Soniox recording, from either the Smart Scribe (standard) or Translator (bilingual, live-translated) list, via the Soniox web or desktop app, and saves it as a .txt file in the local Downloads folder. Use it when another workflow needs a Soniox transcript as input. It only extracts text; it does not summarize.
---

# Soniox Transcript Extractor

A fetch primitive with the same contract as the Otter extractor, for a different source app. It finds one recording, exports it with the app's native download feature, and returns the file path. The caller owns speaker name fixes, analysis, formatting, and the final deliverable.

Soniox (`soniox.com`) is a different company from Sonix.ai (`sonix.ai`). Check the domain before trusting export instructions found online.

## Contract

**Input:** a search keyword (company or meeting name) and an optional date preference. Default is the most recent match. Otherwise use `YYYY-MM-DD`.

**Output:** the absolute path to `{Recording Title}.txt` in the local Downloads folder of the machine being driven. Speaker labels and timestamps are kept, with no truncation. Soniox adds no vendor suffix to the filename.

The file is scratch input. Do not move it into a cloud-synced folder or a notes archive.

## Workflow

### 0. Choose the surface: web app (default) or desktop app

Both surfaces share one account, list the same recordings, and export identical text.

Use the **web app** (`app.soniox.com`) whenever a browser is reachable. A download button there triggers an ordinary browser download into the Downloads folder with no dialog.

The **desktop app** opens a native Save As dialog on every download, and that dialog often does not default to Downloads. It sits outside any browser page, so only full desktop control can drive it. Use the desktop app only if the user asks for it, no browser is reachable, or the web session is broken while the desktop app is signed in.

Identity check, every time:

- **Web route:** list the connected browsers. If two or more are connected, do not guess from device names. Ask the user which one to use.
- **Desktop route:** confirm the target device, make sure the app is accessible to your desktop-control tool, then open it.

If a login screen appears on either surface, stop and ask the user to sign in.

### 0.5. Smart Scribe or Translator?

Soniox keeps two recording lists under one account, and they are not cross-listed.

- **Smart Scribe:** standard single-language recordings. Start here.
- **Translator:** live-translated, bilingual recordings. Check here if Smart Scribe finds nothing, if the user describes the meeting as bilingual, or if the user says so.

If Smart Scribe returns zero results, check Translator before reporting no match.

### 1. Locate the recording

1. In the left navigation, open Smart Scribe (or Translator).
2. Click the search field, type the keyword, and wait for the list to filter. Results are grouped by date, newest first.
3. Click the recording title to open its detail page.

If there are zero results, try a looser keyword once and check the organization switcher in case the recording sits under another organization. Then try the other list. If both lists come up empty, report "no matching recording (checked Smart Scribe and Translator)".

On the desktop app the layout is the same. Read click coordinates from a screenshot.

### 2. Export

1. On the detail page, click **Download**. On a narrow window it may sit under an overflow menu.
2. In the download dialog, under **Include**, keep speaker names on and turn timestamps on. Leave language labels off unless the user asked for them.
3. **Translator recordings only:** choose the **Source only** content option to get the original-language transcript. Export a translation or a bilingual file only if the caller asked for it.
4. Under **Download as**, click **Plain text (.txt)**. On the web app the download starts immediately. Wait about two seconds.

**Desktop only:** a native Save As dialog opens. Do not accept its default folder. Click the file name field, select all, and type the full destination path, for example `<your Downloads folder>/{Recording Title}.txt`. Then click Save. The dialog asks before overwriting a same-named file, so add a suffix yourself if the old file should be kept. If the options differ from the above, say so in your report rather than guessing.

### 3. Verify and read

1. Make sure the Downloads folder is accessible to your file tools.
2. Find `{Recording Title}.txt`, or the most recently modified file if the title is uncertain.
3. Read it. The format is:

```
{Recording Title}

[MM:SS] Speaker 1:
utterance text

[MM:SS] Speaker 2:
next utterance
```

### 4. Return

Return the absolute path and say which list (Smart Scribe or Translator) the recording came from.

## Do not

- Do not confuse Soniox with Sonix.ai.
- Do not trust the desktop Save As dialog's default folder. Always type the full path.
- Do not use browser automation on the desktop Save As dialog. It cannot see it.
- Do not skip the browser identity check when several browsers are connected.
- Do not summarize, edit, or reformat the transcript.

## Failure handling (two tries, then stop)

| Failure | Retry | Then |
|---|---|---|
| Several browsers, unclear which is real | Always confirm with the user | Report and wait |
| Zero results in Smart Scribe | Looser keyword once, check organization switcher, then check Translator | Report "no matching recording" |
| Zero results in Translator too | Looser keyword once more | Report "no matching recording" |
| Download dialog does not open | Reload once, click Download again | Report "download panel did not load" |
| Desktop Save As opens at the wrong folder | Retype the full path once | Report the quirk |
| File not in Downloads after about five seconds | Wait five more seconds, check once | Report; on desktop, confirm the typed path |
| File near zero bytes | Export once more | Report "download appears incomplete" |
| Session logged out | Stop | Report "session expired, please sign in" |

After two retries at any stage, stop and report status.

## Caller integration

Call this skill first when the source is a Soniox recording, then read the returned file as the transcript. Callers do not need to know in advance which list holds the recording.
