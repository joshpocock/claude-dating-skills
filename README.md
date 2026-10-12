# Claude Dating Skills

Nine free Claude skills that make online dating less painful: keep a private log of every match that gets smarter over time, make every draft sound like you, fix your profile, write better first messages, get an honest read on a chat, let a council of Claude agents debate what to text her next, plan the date at real places near her, and spot fake profiles and scams before they cost you anything.

They work on the **free Claude plan** as uploaded skills, and in Claude Code.

**Who it's for:** the defaults and examples are written for guys on the apps, mostly dating women (photo lineups, openers, date plans and the scams that hit men most). Tell Claude who you are and who you're dating and every skill adapts, any gender, any orientation.

> **You're still the one dating.** These skills coach and draft. You edit and send in your own words. Use everything here as a starting point and make it sound like you, so the person you meet is the person they were talking to.

## The skills

| Skill | What it does | Try saying |
|---|---|---|
| **dating-logbook** | A private running log of every match: what she's into, what she responded to, what fell flat, status and next step. Reads it before advising, and spots patterns across matches (which openers get replies, which date ideas land). See [How the log works](#how-the-log-and-voice-profile-are-saved). | "Log this match" / "Where am I with Maya?" / "What's working for me?" |
| **dating-voice-profile** | Learns how you text (tone, length, humour, emoji, words you'd never use) and what you're into from a few of your own messages, and saves a short profile. Every other skill reads it so drafts sound like you. | "Learn how I text" + a few of your messages |
| **dating-profile-glowup** (start here) | One screenshot, your whole profile fixed. Photo order, rewritten bio and prompts in your voice, before/after scores, top 3 changes for today. | "Glow up my Hinge profile" + your profile screenshots |
| **dating-photo-ranker** | Ranks your photos, picks your lead, says what to cut and what to shoot next. Judges the photo, never your looks. | "Which of these should be my first photo?" |
| **dating-bio-rewriter** | Rewrites your bio and prompt answers so they're specific and easy to message. Asks a few questions first, never makes things up. | "Rewrite my Bumble bio" + screenshot |
| **dating-opener** | Reads a match's profile and writes 3 personalized openers (not "hey"), each with a reason, plus a top pick. | "What should I open with?" + their profile |
| **dating-reply-reader** | An honest read of a conversation, with evidence and a confidence level, then a reply council: three advisors (Playful, Direct, Careful) each pitch one reply and a judge picks the best fit for the read, your log and your voice. See [The reply council](#the-reply-council). | "Is she into me? What should I text her?" + the chat |
| **dating-date-planner** | Plans a first date from both your interests, area, budget and vibe, finds real current spots near her when web search is on (never invents a venue), and writes the invite (one day, one activity, one place). | "Plan a first date near her in East Austin, she's vegetarian, $40 budget" |
| **dating-red-flags** | Checks a profile or chat for fake-profile, romance-scam and safety red flags and gives first-date safety tips. | "Is this a scam?" + the chat |

Every skill checks for your voice profile and your log and uses them when they're there. Without them, each skill still works on its own.

Each skill is a folder in [`skills/`](skills) with a `SKILL.md`.

## The reply council

Ask dating-reply-reader "what should I text her?" (or just share the chat, or say "run the council") and, after the honest read, three advisors each propose one reply to her last message and argue for it:

- **Playful:** light, teasing, fun.
- **Direct:** moves things forward, toward a date when the signals support it.
- **Careful:** low-pressure, matches her energy, protects you from over-investing.

Then a judge weighs them against the honest read, your log (what she's into, what landed, what fell flat) and your voice profile, picks one with a one-line reason, and keeps the other two as backups. Every reply is in your voice and only uses interests that are really yours. In **Claude Code** the three advisors run as real parallel subagents and the main agent is the judge; in **Claude.ai** Claude runs the same council in a single reply. It never sends anything: you pick, edit and send.

A fictional example. Her last message: *"ok that's honestly impressive. I'd need proof before I believe it though"* (about his 12-hour ramen):

```
Playful: "proof will be provided. bring your own spoon, sourdough person"
  Why: keeps the mock-serious bit going, and food debates are what she replies to.
Direct:  "come try it then. ramen tasting at the noodle bar near you, saturday?"
  Why: she asked for proof and she's asking questions back. Easy, public, specific.
Careful: "fair. i'll send a photo of the pot on sunday as evidence"
  Why: low effort, keeps it going without asking for anything yet.

Judge's pick: Direct. She's engaged (two questions back, long replies) and she
handed you the reason to meet. Backups: Playful, Careful.
```

Use these as a starting point and make it sound like you.

## Install

### Claude.ai (Free, Pro, Max)

1. Download the zip for the skill you want from [`dist/`](dist) (one zip per skill, e.g. `dating-profile-glowup.zip`).
2. In Claude, go to **Settings > Capabilities** and turn on **Code execution and file creation**.
3. Go to **Customize > Skills**, click **+**, then **+ Create skill**, then **Upload a skill**, and upload the zip.
4. Repeat for each skill you want. Make sure each one is toggled on.
5. Start a new chat and just ask, e.g. "glow up my Tinder profile", with your screenshots attached.
6. For the date planner to find real spots, keep **web search** turned on in the chat (the tools/search toggle under the message box).

Claude.ai takes one skill per zip, so upload them individually. `claude-dating-skills-all.zip` is a convenience bundle of all nine folders (handy for Claude Code). Team and Enterprise plans may need an admin to enable skills first. Steps are from [Claude's help center](https://support.claude.com/en/articles/12512180-using-skills-in-claude) as of October 2026; if the menu has moved, search the help center for "skills".

### Claude Code

Copy the folders into your skills directory:

```bash
git clone https://github.com/joshpocock/claude-dating-skills.git
# all projects:
cp -r claude-dating-skills/skills/* ~/.claude/skills/
# or just one project:
cp -r claude-dating-skills/skills/* your-project/.claude/skills/
```

Then ask Claude Code naturally ("rank my dating photos" with image paths) or call a skill by name.

### Rebuild the zips

```bash
python scripts/build.py   # writes dist/<skill>.zip and dist/claude-dating-skills-all.zip
```

## How the log and voice profile are saved

The logbook and voice profile only help if they're there next time. How that works depends on where you use Claude, and the two are honestly different:

**Claude Code (saves automatically).** The skills keep plain markdown files in a `dating-log/` folder in the project you run Claude Code from:

```
dating-log/
  INDEX.md        one line per match + "patterns so far"
  me.md           your voice profile
  matches/
    maya-hinge.md one short file per match
```

Claude asks before creating the folder the first time, then reads and updates it on every use, across sessions. The files never leave your computer except as context in your Claude conversations. If the folder is inside a git repo, add `dating-log/` to `.gitignore`.

**Claude.ai (you keep the file).** Skills in the Claude app can't save files that last between chats; anything created in a chat's sandbox is gone when the chat ends. So the skills give you the updated log (or voice profile) as a block at the end of each update, and you keep it in one of these:

1. **A Claude Project (best):** make a Project called "Dating", add `dating-log.md` and `me.md` to its files, and do your dating chats inside it. Claude reads Project files in every chat there but can't edit them, so after an update, replace the file with the new version Claude gives you.
2. **Paste it back:** save the block in your notes app and paste it at the start of your next dating chat.
3. **Claude's memory:** if your plan has memory and it's turned on, Claude may remember some details between chats. It's a summary Claude keeps, not an exact log, so use it as a helper, not your only copy. You can view and delete what it saved in Settings.

## Privacy and safety

- **Other people's messages and profiles are private.** Before you share a screenshot, crop out full names, phone numbers, workplaces, and anything else that identifies them. Don't forward someone's messages to other people.
- **Your photos and chats go to Claude** when you upload them. Only share what you're comfortable sharing.
- **The log stores the minimum.** First name or a nickname only. No last names, phone numbers, social handles, workplaces, photos or screenshots, and no copied message transcripts, just short notes. The logbook strips these out if you include them.
- **Keep it yours.** The log lives on your own computer (Claude Code) or in your own Claude account (Project file, notes app, memory). Never share it, post it, or show someone's chats to other people.
- **Delete entries when things end.** The logbook offers to delete an ended match or shrink it to an anonymous lesson ("debate opener got a reply"). In Claude Code, delete the file; in Claude.ai, replace or remove the Project file and clear anything memory saved.
- **It's a memory aid, not a tracker.** The logbook won't log things found by looking someone up off the app.
- **No skill rates anyone's attractiveness.** Photo feedback is about the photo: light, framing, variety.
- **Nothing here is a manipulation playbook.** No negging, no games, no pressure. A no is a no, and the skills will tell you so.
- **dating-red-flags is not a guarantee.** It spots common patterns. If you've sent money or someone is threatening you, contact your bank and local authorities right away.
- These skills are AI suggestions, not professional advice.

## Tests

[`tests/`](tests) has the fictional sample profiles and chats used to test each skill and the outputs Claude produced. Every person in them is made up. Run them yourself with `python scripts/run_tests.py` (requires Claude Code). The logbook and voice profile are also tested in a 4-turn Claude Code session where each turn is a separate session, to check the files really persist.

## License

MIT. See [LICENSE](LICENSE).
