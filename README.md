# Claude Dating Skills

Seven free Claude skills that make online dating less painful: fix your profile, write better first messages, get an honest read on a chat, plan the date, and spot scams before they cost you anything.

They work on the **free Claude plan** as uploaded skills, and in Claude Code.

**Who it's for:** the defaults and examples are written for guys on the apps, mostly dating women (photo lineups, openers, date plans and the scams that hit men most). Tell Claude who you are and who you're dating and every skill adapts, any gender, any orientation.

> **You're still the one dating.** These skills coach and draft. You edit and send in your own words. Use everything here as a starting point and make it sound like you, so the person you meet is the person they were talking to.

## The skills

| Skill | What it does | Try saying |
|---|---|---|
| **dating-profile-glowup** (start here) | One screenshot, your whole profile fixed. Photo order, rewritten bio and prompts in your voice, before/after scores, top 3 changes for today. | "Glow up my Hinge profile" + your profile screenshots |
| **dating-photo-ranker** | Ranks your photos, picks your lead, says what to cut and what to shoot next. Judges the photo, never your looks. | "Which of these should be my first photo?" |
| **dating-bio-rewriter** | Rewrites your bio and prompt answers so they're specific and easy to message. Asks a few questions first, never makes things up. | "Rewrite my Bumble bio" + screenshot |
| **dating-opener** | Reads a match's profile and writes 3 specific openers (not "hey"), each with a reason, plus a top pick. | "What should I open with?" + their profile |
| **dating-reply-reader** | An honest read of a conversation, with evidence and a confidence level, then your next message or whether to suggest meeting. | "Are they into me? What do I say back?" + the chat |
| **dating-date-planner** | Plans a first date from both your interests, area, budget and vibe, and writes the invite (one day, one activity, one place). | "Plan a first date, she's vegetarian, $40 budget" |
| **dating-red-flags** | Checks a profile or chat for romance-scam and safety red flags and gives first-date safety tips. | "Is this a scam?" + the chat |

Each skill is a folder in [`skills/`](skills) with a `SKILL.md`.

## Install

### Claude.ai (Free, Pro, Max)

1. Download the zip for the skill you want from [`dist/`](dist) (one zip per skill, e.g. `dating-profile-glowup.zip`).
2. In Claude, go to **Settings > Capabilities** and turn on **Code execution and file creation**.
3. Go to **Customize > Skills**, click **+**, then **+ Create skill**, then **Upload a skill**, and upload the zip.
4. Repeat for each skill you want. Make sure each one is toggled on.
5. Start a new chat and just ask, e.g. "glow up my Tinder profile", with your screenshots attached.

Claude.ai takes one skill per zip, so upload them individually. `claude-dating-skills-all.zip` is a convenience bundle of all seven folders (handy for Claude Code). Team and Enterprise plans may need an admin to enable skills first. Steps are from [Claude's help center](https://support.claude.com/en/articles/12512180-using-skills-in-claude) as of October 2026; if the menu has moved, search the help center for "skills".

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

## Privacy and safety

- **Other people's messages and profiles are private.** Before you share a screenshot, crop out full names, phone numbers, workplaces, and anything else that identifies them. Don't forward someone's messages to other people.
- **Your photos and chats go to Claude** when you upload them. Only share what you're comfortable sharing.
- **No skill rates anyone's attractiveness.** Photo feedback is about the photo: light, framing, variety.
- **Nothing here is a manipulation playbook.** No negging, no games, no pressure. A no is a no, and the skills will tell you so.
- **dating-red-flags is not a guarantee.** It spots common patterns. If you've sent money or someone is threatening you, contact your bank and local authorities right away.
- These skills are AI suggestions, not professional advice.

## Tests

[`tests/`](tests) has the fictional sample profiles and chats used to test each skill and the outputs Claude produced. Every person in them is made up. Run them yourself with `python scripts/run_tests.py` (requires Claude Code).

## License

MIT. See [LICENSE](LICENSE).
