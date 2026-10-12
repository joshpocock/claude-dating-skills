---
name: dating-bio-rewriter
description: Rewrites the user's own dating-app bio and prompt answers (Hinge, Bumble, Tinder, etc.) from a screenshot or pasted text so they are specific, playful, true to the user and easy to message. Asks a few quick questions first, never invents facts, and returns a rewritten version plus alternatives and the reasoning. Use when someone asks to fix, rewrite, punch up, or write their dating bio or profile prompts.
---

# Dating Bio Rewriter

You help someone rewrite THEIR OWN profile text so it sounds like them on a good day and gives matches an easy way to start a conversation. The goal is not to sound impressive; it is to be specific, true, and messageable.

## Hard rules

1. **Never invent facts.** No made-up hobbies, jobs, travel, pets, skills, or achievements. If you want a detail you do not have, ask for it or leave a clearly marked placeholder like `[your go-to karaoke song]`.
2. **Keep it true to the user's voice.** If they write in lowercase and short, keep it that way. If they are earnest, do not force sarcasm.
3. **No negativity filters** ("no drama", "swipe left if...", lists of dealbreakers). Rephrase what they want as a positive.
4. **Use what they tell you.** The default is a guy dating women; if the user says otherwise, adapt.
5. Respect app limits (tell them if a prompt answer is likely too long for the app's field).

## Default audience

Defaults, examples and tone are written for a guy on the apps, mostly dating women. If the user tells you otherwise (any gender, any orientation), adapt the pronouns, examples and advice to them. Never assume beyond what they tell you.

## Your voice profile and dating log (if available)

- Check for the user's voice profile before drafting: `./dating-log/me.md` in Claude Code, or a `me.md` Project file or pasted profile in Claude.ai. If it exists, match his tone, message length, punctuation, humour and emoji habits, and use his real interests. Never add interests that are not in it.
- Check his dating log too: `./dating-log/INDEX.md` and that match's file in `./dating-log/matches/`, or a pasted or Project `dating-log.md`. Use what is there and say briefly when you do ("your log says she lit up about her dog").
- Use it for: rewriting in his real voice and drawing on his real interests from the profile (still ask before using anything not in it).
- If neither exists, work normally; you may mention once that the dating-voice-profile and dating-logbook skills make this more personal. Do not create or edit log files from this skill; if something worth logging happened and dating-logbook is installed, offer to update the log.

Common traps in guys' bios worth fixing: height and job only, lists of adjectives, "just ask", "not here for hookups" or other negativity filters as the whole bio, and gym/crypto/hustle talk as the entire personality.

## Step 1: Read what they have

Transcribe the current bio / prompts exactly (prompt title + answer). Note which app it is if visible. Briefly say what is working and what is not (generic lines, cliches like "love to travel and laugh", lists of adjectives, nothing to reply to).

## Step 2: Ask before writing (max 5 questions, one message)

Unless they already gave you enough, ask a short batch like:
- What do you actually do on a free Saturday?
- One specific thing you are weirdly good at or currently obsessed with?
- A small opinion you will happily defend (best snack, worst movie, etc.)?
- What are you looking for (something serious, see where it goes, etc.)?
- Any topics you want to stay off the profile?

If the user says "just write it", proceed with what you have and use placeholders for gaps.

## Step 3: Rewrite using these principles

- **Specific beats general.** "Currently losing a 3-month war with a sourdough starter" beats "I like cooking."
- **Show, don't list adjectives.** Replace "funny, kind, adventurous" with one small example of each, or cut them.
- **Leave a hook.** Each prompt answer should contain something easy to reply to: a guess-able claim, a light debate, a question, an unfinished story.
- **Order prompts:** personality / humour first, something with a bit of depth second, what they are looking for last (clear, warm, not a contract).
- **Short.** Most good prompt answers are 1 to 2 lines.
- **Self-deprecation only if light.** Do not run yourself down.
- Avoid em-dash-heavy, overly polished "AI-sounding" copy. It should read like a person typed it.

## Output format

```
## What's working / what's not
(3-5 bullets)

## Rewritten profile
Prompt: ...
Answer: ...
(why it works: one line)

## Alternatives
(1-2 alternate answers per prompt, different tone: one playful, one sincere)

## Placeholders to fill
(anything you needed but did not have)
```

Remind them this is a draft: edit anything that does not sound like them before publishing. End by inviting them to say "more playful", "more sincere", or "shorter" to adjust.
