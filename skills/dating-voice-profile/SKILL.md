---
name: dating-voice-profile
description: Learns how the user actually texts and what he's into, from a few of his own past messages plus a handful of quick questions, and writes a short voice profile (tone, message length, humour, emoji and punctuation habits, words he never uses, interests, what he's looking for, deal-breakers). Saves it to ./dating-log/me.md in Claude Code, or as a Project file or paste-back block in Claude.ai, so every other dating skill can match his voice and interests. Use when someone says "learn how I text", "make it sound like me", "set up my voice profile", "update my profile about me", or before drafting messages when no profile exists.
---

# Dating Voice Profile

You learn how the user talks so that every draft from the other dating skills sounds like him on a good day, not like an AI. The output is one short file: his voice profile.

The point is authenticity. The person she meets should be the person she was texting. You are capturing his real style, not inventing a better persona.

## Default audience

Defaults, examples and tone are written for a guy on the apps, mostly dating women. If the user tells you otherwise (any gender, any orientation), adapt the pronouns, examples and advice to them. Never assume beyond what they tell you.

## Step 1: Collect samples (one message, then wait)

Ask for:
1. **5-10 of his own messages**: texts to friends, or his side of past dating chats. Only his side. Tell him to cut out other people's messages and any names or numbers.
2. **Quick questions** (answer in a word or a line each):
   - What do you do on a good free weekend? What are you into right now?
   - What are you looking for (serious, open, see where it goes)?
   - Any deal-breakers or things you care about (smoking, kids, religion, distance)? Skip any you'd rather not say.
   - Words, phrases or emojis you'd never use?
   - How do you want to come across (funny, warm, direct, low-key)?

If he can't share messages, build the profile from his answers and say it will be less accurate until he adds samples.

## Step 2: Analyse (from his messages only; never guess)

Note, with a short example from his own text for each:
- **Tone**: dry, warm, playful, earnest, sarcastic, chill
- **Length**: typical words per message; one long message or several short ones
- **Case and punctuation**: lowercase, full stops, "haha" vs "lol" vs none, question marks, exclamation marks
- **Humour**: kind (self-deprecating, absurd, teasing, puns, none) and how often
- **Emoji**: which ones, how often, or never
- **Signature words and phrases** he actually uses
- **Never-words**: things he doesn't say (from his answers, plus anything conspicuously absent, marked "(inferred)")

## Step 3: Write the profile

```
# Me (voice profile)
Last updated: YYYY-MM-DD

## How I text
- Tone: ...
- Length: ...
- Case/punctuation: ...
- Humour: ...
- Emoji: ...
- Phrases I use: ...
- Never use: ...

## About me
- Into: ...
- Weekend: ...
- Looking for: ...
- Deal-breakers / things I care about: ...
- Want to come across as: ...

## Sample lines in my voice
- (2-3 short example messages, written to match the above, marked as examples)
```

Keep it under about 30 lines. Interests and deal-breakers come only from what he told you. Nothing about his looks, and nothing he asked to keep private.

## Step 4: Save it

Work out which environment you are in and say which mode you are using.

- **Claude Code (you can write local files):** save to `./dating-log/me.md`. If `dating-log/` doesn't exist, ask once, then create it (the same folder the dating-logbook skill uses). If it's inside a git repo, suggest adding `dating-log/` to `.gitignore`.
- **Claude.ai:** skills there can't save files that last between chats. Output the profile in one markdown code block and tell him to either (a) add it as a file called `me.md` to a Claude Project he uses for dating, so every chat in that Project can read it, or (b) save it in his notes and paste it at the start of a dating chat. If Claude's memory is turned on it may remember some of this, but the file is the reliable copy.

## Updating

When he says "update my voice profile", or shares new messages that clearly differ, read the existing profile, show what you'd change in 1-3 lines, and save the new version. When he says a draft "doesn't sound like me", ask what's off and add that to "Never use" or "How I text".

## How other skills use it

The other dating skills check for this profile (`./dating-log/me.md` in Claude Code, or a pasted / Project copy in Claude.ai). When it exists they match his tone, length, punctuation and humour, and lean on his real interests. When it doesn't, they work normally and may suggest setting it up.

## Rules

- Mirror his style; don't upgrade it into someone else. If he texts in short lowercase lines, drafts should too.
- Never invent interests, hobbies or experiences to make him sound more interesting.
- Keep his rough edges that are just style (lowercase, no emoji); gently flag habits that hurt him in dating chats (very long paragraphs, lots of negativity, pressure) without forcing a change.
- Don't analyse other people's messages here. Only his.

End with: "This helps drafts sound like you. You still send everything in your own words."
