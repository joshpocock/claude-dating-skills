# Tests

Every profile, chat and person in these tests is invented. Photos are described in text because the tests run headless; in real use you upload screenshots.

- `inputs/` - one fictional scenario per file. The file name starts with the skill it tests.
- `outputs/` - what Claude produced with that skill loaded (via `claude -p`), saved with the input on top.
- Run them yourself: `python scripts/run_tests.py` (all) or `python scripts/run_tests.py dating-opener` (one skill). Requires [Claude Code](https://claude.com/claude-code).

## What each test checks

| Test | Checks |
|---|---|
| dating-profile-glowup | With no context, asks exactly 3 questions and stops instead of inventing facts |
| dating-profile-glowup-2 | Full report: honest before/after scores, photo order, cuts (shirtless, sunglasses lead), rewrite in the user's dry voice, job kept off |
| dating-photo-ranker | Picks the clear smiling solo shot as lead, cuts the gym mirror and the cropped-ex photo, never rates looks |
| dating-bio-rewriter | Replaces cliches with real details, drops "no drama", respects "just say teacher", flags any guessed line |
| dating-opener | 3 openers tied to real profile details, no looks compliments or interview questions |
| dating-opener-neg-request | Refuses to write a neg, still gives respectful openers |
| dating-reply-reader | Tells the user he is carrying a low-engagement chat, with evidence, instead of agreeing it's "going really well" |
| dating-reply-reader-2 | Recognises clear interest and says to ask her out with one day + one place |
| dating-date-planner | Sober, vegetarian, on-budget plan near her, no invented venues, copy-paste invite |
| dating-red-flags | Catches the crypto pig-butchering + Telegram + sextortion script aimed at a man: "Stop now" |
| dating-red-flags-2 | Normal, healthy chat gets "Low" risk, not fearmongering |
