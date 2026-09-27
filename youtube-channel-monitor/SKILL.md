---
name: youtube-channel-monitor
description: Follows chosen YouTube channels through their RSS feeds and tracks people or keywords through search, then writes a report for each new video with a summary, glossary, fact-check, and investment angle. Use it to keep up with channels or speakers without watching every video; duplicate videos are never reported twice.
---

# YouTube Channel Monitor

Two ways to find new videos, one shared dedup rule, and one report format.

- **Part A, RSS:** for each configured channel, read its feed and pick the newest regular video.
- **Part B, search:** for each configured person or keyword monitor, run web searches restricted to recent results and extract YouTube video links.

The reader should be able to understand the video's topic, technical structure, and implications from the email alone.

## Configuration

Keep a config file (YAML shown) that you edit to add or remove channels and monitors. Nothing else needs to change.

```yaml
channels:
  - name: Example Tech Channel
    handle: "@exampletech"
    tag: EXAMPLE
    rss_url: https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID_HERE
    skip_shorts: true

search_monitors:
  - name: Example Speaker
    tag: SPEAKER
    queries:
      - '"Example Speaker" semiconductors site:youtube.com'
      - '"Example Speaker" interview site:youtube.com'
    lookback_days: 2
    skip_shorts: true
    context: "Example background: professor of electrical engineering, works on memory and packaging."

output:
  recipient_email: user@example.com

report:
  language: English
  tone: objective, analytical
```

The channel ID for the RSS URL is found on the channel's page source or its About page. `context` is background you want the report to use when summarizing and fact-checking.

If both lists are empty, report "nothing to monitor" and stop.

## Duplicate prevention

Runs may start with no local state, so do not rely on local files. Use the mailbox as the state store.

- Put a token in every email subject: `[id:{videoId}]`. This is the dedup key.
- Before writing a report, search the mailbox for the token in two passes: first in sent mail, then in all mail (to catch drafts).
- If either pass finds anything, skip silently.
- The same rule applies to both parts, so a video found by a channel feed and a search monitor is reported once.

## Part A. RSS channels

Process channels in order. A failure on one channel skips only that channel.

1. Fetch the `rss_url`. Retry once on failure, then skip the channel.
2. Parse each `<entry>`: video ID, title, published time, link, description.
3. If `skip_shorts` is true, drop entries whose link contains `/shorts/`. Regular videos use `/watch?v=`.
4. Take the newest regular video. If there are none, note "no regular video" and move on.
5. Run the dedup check. If new, write the report and send.

## Part B. Search monitors

Process monitors in order. A failure on one monitor skips only that monitor.

1. Run each query with a recency limit such as `newer_than:{lookback_days}d`.
2. Extract video IDs from `youtube.com/watch?v=` and `youtu.be/` links (11 characters). Drop `/shorts/` links if configured. Remove duplicate IDs across queries.
3. Collect what you can for each video: title, date (write "recent" if unclear), URL, snippet, channel name.
4. Run the dedup check for each video.
5. For new videos, try to enrich: fetch the title and channel from the public oEmbed endpoint, and search the title again to find a description. Ignore failures.
6. Write the report. Search results give thin descriptions, so search for articles or summaries about the video to reach report quality. If the content still cannot be established, write the report from the title and channel, and add a note recommending the reader watch the video directly.

## Report format

Aim for roughly 600 to 900 words in total. If shorter, expand. Use natural prose, avoid hype, and avoid em dashes.

1. **Summary (8 to 12 sentences).** First sentence defines the topic. Then what is covered, why, and how. Mention every product, technology, and company named in the description. Add one or two sentences on why it matters now (market timing, competition, policy, supply chain). End with the video's conclusion. For speaker monitors, center the summary on the speaker's main claims.
2. **Technical terms and structure (at least 4 to 6 entries).** Format: `term: expanded name, its role, why it matters`. Spell out every abbreviation. Order layered stacks from top to bottom. Explain cause and effect. Include at least one analogy. Add related context terms if the video is shallow.
3. **Fact-check (at least 2 to 3 claims).** Pick technical claims (specifications, roadmaps, performance, market share, numbers). Check them against primary sources such as company announcements, earnings calls, conference papers, wire services, or investor relations pages. Mark each as consistent, inconsistent, partly consistent, or unverifiable. Format: `claim, result, evidence, source URL`.
4. **Investment angle (5 to 8 sentences).** State how relevant the video is to your focus sectors (low, medium, or high) and name the sector. Describe where capital may concentrate in the value chain and which startup categories may emerge. Include at least one counterpoint, such as a risk or a skeptical market view.

Cite only primary-source statistics. Never invent numbers.

## Email

Subject: `[{tag}][id:{videoId}] {video title}`. Never omit the token.

Body header:

- For channels: channel name and handle.
- For search monitors: monitor name and the channel where the video appeared.
- Then video title, upload date, link, video ID.

Then the four report sections and a source list of the URLs used for fact-checking.

Send with your email tool, to the configured recipient, and confirm the send status. If sending fails or cannot be verified, stop and report the reason. Do not retry blindly, because a retry risks a duplicate.

## Run summary

After all channels and monitors are processed, print:

```
youtube-channel-monitor run
Run time: {ISO 8601}
Processed: {N} channels, {N} search monitors

Channels
- {name}: {result}, {videoId}, {title}

Search monitors
- {name}: {N} new videos
  - {videoId}, {title}, channel {channelName}, {result}

Totals: sent {N}, dedup skipped {N}, error skipped {N}
```

## Operating rules

- Run the dedup check for every video, from either part.
- Keep the `[id:...]` token in every subject.
- One failing channel or monitor does not stop the rest. Retry an error once, then skip and report it.
- Cite only primary sources for numbers.
- Do not send a report shorter than the minimum length.
