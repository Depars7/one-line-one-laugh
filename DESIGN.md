# One Line, One Laugh — design notes

Bounty: One Line, One Laugh (u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a, $2, 10 places).
Gate: `/output/entry.txt`, UTF-8, 1–140 characters, not only whitespace.
Judge (pairwise, blind): laugh first, then the turn, the tightness, the
freshness, the clarity. One self-contained line; the punchline lands last.

## Candidates (12, all original, written for this entry)

1. **My Roomba mapped my apartment and left a one-star review.** (57) — PICK
2. My phone's screen-time report just filed for custody of my attention span. (74)
3. I told my plants I'm a botanist now. They've never looked more disappointed in a human. (86)
4. My smart fridge emailed me about my midnight snacking. Even my appliances have started a group chat about me. (109)
5. My calendar invited me to a meeting with myself. I declined — I seemed busy. (76)
6. I bought a self-help book that told me to stop buying self-help books, so now I own two problems. (99)
7. My GPS took the scenic route past my ex's house. Twice. (55)
8. I finally organized my desk. Now I can't find anything, but at least I look productive. (85)
9. My smartwatch congratulated me for standing up. I was already standing — it just believes in me. (95)
10. I went to a silent retreat and came back with strong opinions I refuse to share. (82)
11. My password is so secure even I can't get in. My bank calls it maximum protection. (84)
12. I named my Wi-Fi after the FBI so my neighbours wave at the router now. (73)

## Why #1 wins

- **Laugh / turn:** one image (a vacuum that maps the flat), one twist
  (it behaves like a disappointed guest and rates the place). The
  punchline is the last three words, "one-star review".
- **Tight:** 57 characters, every word earns its place; v1 ("finished
  mapping") was cut to "mapped" with no loss.
- **Fresh:** a collision of two everyday domains — robot-vacuum mapping
  and review culture — not a recycled setup. No AI joke (the field will
  be full of them), no ex joke, no "FBI van" Wi-Fi trope.
- **Clear:** readable in one breath, no explanation needed, no second
  line to make sense.

## Why the others lost

- #2: strong metaphor, but "screen time ate my life" is well-trodden.
- #3: charming, but the second sentence explains the first; slower.
- #4: two beats, 109 characters — flabby for a one-liner.
- #5: "meeting with myself" is a known trope; the turn is mild.
- #6: self-help-book irony is a familiar setup.
- #7: ex jokes are a crowded lane; "Twice." is the only surprise.
- #8: mild observation, no real twist — the judge's criterion 2 fails it.
- #9: sweet, not funny enough; the turn is a shrug.
- #10: clever premise, weak landing — no punchline word.
- #11: "so secure even I can't get in" is a heard-before setup.
- #12: the FBI-van Wi-Fi name is a classic trope, not fresh.

## Program

`main.py` (stdlib only, no network, no randomness) validates the line
against the gate, writes it to `/output/entry.txt` with no trailing
newline, mode 0644, then reads the bytes back and verifies they match
exactly. Two runs are byte-identical by construction.
