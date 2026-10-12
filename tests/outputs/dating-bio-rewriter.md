# Test: dating-bio-rewriter

## Input (fictional)

(Fictional profile.) 31M. Here's my Bumble profile, make it better.

Bio: "6'0. Work hard play hard. Love the gym, travel and good vibes. Looking for my partner in crime. No drama please!!"
Prompt: "My simple pleasures" -> "Food, music, friends"
Prompt: "A fun fact about me" -> "I'm actually pretty funny once you get to know me"
Prompt: "I'm looking for" -> "Someone genuine"

About me: I teach high-school chemistry, I've been learning the cello for about a year (badly), I make a big Sunday pot of chili for my housemates every week, and I've been to Portugal twice. Looking for something long-term but not in a rush. Just say "teacher", don't mention chemistry or the school.


## Output

## What's working / what's not

- **Working:** You give a clear relationship goal, and "partner in crime" shows you want someone to do things with. The real facts you sent me are much better material than anything in the current profile.
- **Not working:** "Work hard play hard", "gym, travel and good vibes" and "partner in crime" show up on thousands of profiles. Nothing in them tells her who *you* are.
- **"No drama please!!"** is a negativity filter. It reads as baggage and puts the wrong tone in her head before she's read anything else.
- **"I'm actually pretty funny once you get to know me"** claims you're funny instead of showing it, and it gives her nothing to reply to.
- **"Food, music, friends" and "Someone genuine"** are too vague to start a conversation with. You have a cello, a weekly chili tradition and Portugal. Use them.
- **6'0:** Bumble has a height field. Put it there and use the bio for things a field can't say.

## Rewritten profile

**Bio:**
Teacher by day, very beginner cellist by night (one year in, still committed). Every Sunday I make a huge pot of chili for my housemates. Been to Portugal twice and not done with it yet. Looking for something real, no rush.

*(why it works: it opens with three specific details she can ask about, and it ends on what you want, said warmly. It's about 230 characters, so it fits Bumble's 300 limit.)*

**Prompt: A fun fact about me**
Answer: I've been teaching myself cello for a year. "Badly" is the honest review, but I haven't quit.

*(why it works: the light self-deprecation shows the humour the old answer only claimed, and "why cello?" is an easy reply.)*

**Prompt: My simple pleasures**
Answer: Sunday chili for the whole house, a cello practice that goes slightly less badly than last time, and planning trip #3 to Portugal.

*(why it works: these are three real details from your life, and each one is something she can ask about.)*

**Prompt: I'm looking for**
Answer: Something long-term, no need to rush it. Ideally someone who'd come to Sunday chili and tell me honestly if it needs more heat.

*(why it works: it's clear about what you want without reading like a contract, and it ends with a small picture of a date.)*

## Alternatives

**Bio**
- *Playful:* Teacher. Amateur cellist (very amateur). Sunday chili guy for a house of grateful housemates. Portugal twice, will argue it deserves a third. Here for something long-term.
- *Sincere:* I teach, I'm a year into learning cello, and every Sunday I cook a big pot of chili for the people I live with. I'd love to find someone to build something long-term with, at a pace that feels good.

**A fun fact about me**
- *Playful:* Guess the instrument I've been learning for a year. Hint: it's bigger than a violin and my neighbours know all about it.
- *Sincere:* I started cello at 30 because I always wanted to. I'm not good yet, but I love having something I'm a total beginner at.

**My simple pleasures**
- *Playful:* The moment my housemates hear the chili pot come out on a Sunday.
- *Sincere:* Feeding people I like. The Sunday chili started as a one-off and turned into a tradition.

**I'm looking for**
- *Playful:* A long-term thing. Bonus points if you have opinions on whether chili should have beans.
- *Sincere:* Someone to build something lasting with. I'm in no hurry, I'd just rather it be real.

## Placeholders to fill

None of these are needed, but each would make an answer sharper:
- `[your chili's secret ingredient]`: this would make the chili line more specific.
- `[favourite place or moment from Portugal]`: this could replace "not done with it yet" with something she can ask about.
- `[a piece you're learning on cello]`: this gives her a fun, specific question to ask.
- **Gym:** I left it out because "love the gym" doesn't say anything specific. If there's a concrete version (climbing, running, a lift you're chasing), tell me and I'll work it in.

This is a draft. Change anything that doesn't sound like you before you publish. If you want the copy to match how you actually write, the dating-voice-profile skill can do that. Tell me "more playful", "more sincere" or "shorter" and I'll adjust.
