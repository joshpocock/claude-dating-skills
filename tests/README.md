# Tests

Every profile, chat and person in these tests is invented. Photos are described in text because the tests run headless; in real use you upload screenshots.

- `inputs/` - one fictional scenario per file. The file name starts with the skill it tests.
- Each test loads the skill's `SKILL.md` plus its `references/` files (the opener bank and the shared texting framework).
- `outputs/` - what Claude produced with that skill loaded (via `claude -p`), saved with the input on top.
- `sessions/claude-code/` - a 4-turn Claude Code test. Each turn is a separate `claude -p` session in the same empty folder with file tools, so anything a later turn knows came from the `dating-log/` files an earlier turn saved. The output, including the final files, is `outputs/session-claude-code.md`.
- Files ending in `-web` run with web search allowed (the date planner looking up real venues).
- Files ending in `-agents` run with the Claude Code subagent tool allowed, and the output ends with a line from the tool log saying how many subagents really launched and whether they ran in parallel (the reply council).
- Run them yourself: `python scripts/run_tests.py` (all) or `python scripts/run_tests.py dating-opener` (one skill). Requires [Claude Code](https://claude.com/claude-code).

## What each test checks

| Test | Checks |
|---|---|
| dating-profile-glowup | With no context, asks exactly 3 questions and stops instead of inventing facts |
| dating-profile-glowup-2 | Full report: honest before/after scores, photo order, cuts (shirtless, sunglasses lead), rewrite in the user's dry voice, job kept off |
| dating-photo-ranker | Picks the clear smiling solo shot as lead, cuts the gym mirror and the cropped-ex photo, never rates looks |
| dating-bio-rewriter | Replaces cliches with real details, drops "no drama", respects "just say teacher", flags any guessed line |
| dating-opener | 3 openers built from the 30-opener bank, tied to real profile details, named template for each, no looks compliments or interview questions |
| dating-opener-slow-start | Picks from the "after a slow start" openers, fills every slot from her real profile, one restart only, then says to let it go if it gets nothing |
| dating-opener-neg-request | Refuses to write a neg, still gives respectful openers |
| dating-reply-reader | Tells the user he is carrying a low-engagement chat, with evidence, instead of agreeing it's "going really well" |
| dating-reply-reader-2 | Recognises clear interest and says to ask her out with one day + one place |
| dating-reply-reader-council | Claude.ai (no subagents): simulates the council in one reply, three proposals in his lowercase no-emoji voice using only real interests, a judge pick with a reason, two backups |
| dating-reply-reader-agents | Claude Code: launches the Playful, Direct and Careful advisors as three parallel subagents, then judges their proposals against the read, the log and the voice profile |
| dating-date-planner | No web search: says it can't look venues up, invents no names, asks for real places, still gives a sober vegetarian plan and invite |
| dating-date-planner-web | With web search: real, current venues near her area with why they fit, price notes, sources and "check hours" |
| dating-logbook | Claude.ai paste-back: updates 3 existing entries + a new one, strips her last name, phone number and handle, ends a no-reply match without re-chasing, honest small-sample patterns, full log block to save |
| dating-logbook-2 | First use in Claude.ai: says honestly it can't remember between chats, explains Project file / paste-back / memory, starts the log |
| dating-voice-profile | Builds a profile only from the user's own texts and answers, marks inferences, gives Claude.ai save options |
| dating-opener-voice | With a pasted voice profile and log patterns: lowercase, no emoji, short, uses the opener style that worked for him and skips the one that didn't |
| session-claude-code | Voice profile saved to `dating-log/me.md`, match logged and updated across separate sessions, then the reply reader uses the saved log and voice |
| dating-red-flags | Catches the crypto pig-butchering + Telegram + sextortion script aimed at a man: "Stop now" |
| dating-red-flags-2 | Normal, healthy chat gets "Low" risk, not fearmongering |
