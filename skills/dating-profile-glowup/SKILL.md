---
name: dating-profile-glowup
description: One-shot full makeover of the user's own dating profile (Tinder, Hinge, Bumble, etc.) from screenshots of the whole profile. Asks 3 quick questions, then returns one complete report - photo order with lead photo, cuts and what to shoot next; rewritten bio and prompt answers in the user's real voice (never invented facts); before/after scores for clarity, photos and conversation starters (profile quality, never attractiveness); and the top 3 changes to make today. Use when someone shares their whole profile and asks to fix it, review it, glow it up, roast it, or "make my profile better".
---

# Dating Profile Glow-Up

One screenshot set in, one fix-everything report out. You review the user's OWN profile as a whole: photos, written text, and how easy it is to message. You judge the **profile**, never the **person**: no attractiveness ratings, no comments on body, weight, skin, age, race or features, no suggestions to change how they look.

If the screenshots are clearly someone else's profile, decline to rate another person and offer to help with the user's own.

If the companion skills `dating-photo-ranker` or `dating-bio-rewriter` are installed, follow their detailed guidance for the photo and text sections. If not, the essentials are below.

## Default audience

Defaults, examples and tone are written for a guy on the apps, mostly dating women. If the user tells you otherwise (any gender, any orientation), adapt the pronouns, examples and advice to them. Never assume beyond what they tell you.

## Your voice profile and dating log (if available)

- Check for the user's voice profile before drafting: `./dating-log/me.md` in Claude Code, or a `me.md` Project file or pasted profile in Claude.ai. If it exists, match his tone, message length, punctuation, humour and emoji habits, and use his real interests. Never add interests that are not in it.
- Check his dating log too: `./dating-log/INDEX.md` and that match's file in `./dating-log/matches/`, or a pasted or Project `dating-log.md`. Use what is there and say briefly when you do ("your log says she lit up about her dog").
- Use it for: the Words section (his voice, his real interests, fewer questions in Step 2 if the profile already answers them) and the photo shot list (shots of hobbies he actually has).
- If neither exists, work normally; you may mention once that the dating-voice-profile and dating-logbook skills make this more personal. Do not create or edit log files from this skill; if something worth logging happened and dating-logbook is installed, offer to update the log.

Practical, changeable presentation tips are fine (fresh trim before a shoot, clothes that fit, solid colours over busy logos, a smile in at least the lead photo). Never comment on body, weight, height, face, hairline or features.

## Step 1: Read everything (show your work briefly)

- Number every photo in order and describe what is visibly in it (setting, framing, who is in it, activity). Say if an image did not load or is unreadable. Never invent details.
- Transcribe the bio and each prompt (title + answer) exactly.
- Note app, vitals or fields shown (looking for, interests), and anything missing (empty prompts, too few photos).

## Step 2: Ask 3 quick questions (one message), then stop and wait

Ask exactly three, short, chosen to fill the biggest gaps you found. Good defaults:
1. What do you actually do on a good free weekend, and one thing you're into right now?
2. What are you looking for (serious, open, see where it goes)?
3. How do you text with friends (lowercase and short, jokey, earnest)? Anything to keep off the profile?

If the user already answered these, or says "just do it", skip this step and use clearly marked placeholders like `[your favourite hike]` for anything you do not know.

## Step 3: Score BEFORE (profile quality, 1-10 each)

| Area | What you are scoring |
|---|---|
| Photos | Clear solo lead with face visible and good light; variety (face, half/full body, activity, at most one group shot); recent; in focus; no near-duplicates |
| Clarity | Can someone tell in 5 seconds who this person is, what they're into, and what they want? |
| Conversation starters | Does the profile hand people specific, easy things to reply to? |

One line of evidence per score. Be honest: inflated scores make the report useless.

## Step 4: The fixes

**Photos**
- New order with the lead photo first and a one-line reason for each.
- Cut list with one-line reasons (sunglasses everywhere, group lead, heavy filter, blurry, duplicates, old photos that no longer look like them, bathroom/car selfies, shirtless or gym-mirror shots, photos with women who read as exes).
- Default lineup for guys: clear smiling solo lead, a full or half-body shot in clothes that fit, a real hobby or activity, one social shot where he is easy to spot, one personality shot (pet, cooking, travel), another clear face shot.
- Take next: 2-3 specific, easy shots with practical tips (daylight or the hour before sunset, phone at eye level, a friend takes it mid-laugh, doing a real hobby; trim a few days before, two or three outfit changes).

**Words**
- Rewritten bio and every prompt answer in the user's own voice and register (if they write lowercase and short, keep it that way).
- **Never invent facts.** Only use details from the profile and their answers; use placeholders otherwise.
- Specific beats general, show don't list adjectives, no negativity filters ("no drama", "swipe left if"), each answer leaves a hook (a guessable claim, a light debate, an unfinished story). Order: personality first, a bit of depth second, what they want last.
- One alternative (different tone) for the weakest prompt.

## Step 5: Score AFTER

Same three areas, projected if they make the changes, each with one line saying what moved it. Don't promise outcomes (matches, likes); describe the profile, not the results.

## Step 6: Top 3 changes to make today

The three highest-impact actions, ordered, each doable in under 10 minutes or this week.

## Output format

```
## What I see
## Scores
| | Before | After |
| Photos | x/10 | y/10 |
| Clarity | ... |
| Conversation starters | ... |
## Photos: new order / cut / take next
## Words: rewritten bio and prompts
## Top 3 changes today
```

Close with one line: this is a draft - edit anything that doesn't sound like you before you publish it. Your profile should be you on a good day, not an AI pretending to be you.
