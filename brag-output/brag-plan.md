# Brag Plan: brainfarts-and-benchmarks 🧠⚡

## What is this app?
A public notebook of curiosity-driven Python experiments where tiny, self-admittedly dumb questions get answered with absurd rigor — 257,518 logged dice rolls to check one formula, 220 pytest cases to compare `nums * 2` with `nums + nums`.

## The angle
**Serious science for stupid questions.** Play it completely straight: a sober research-lab launch film reporting findings nobody asked for. The comedy is the gap between the question ("how long until five dice match?") and the rigor (200 simulations, every roll logged, 4.1 MB of dice). Every number on screen is real, pulled from the repo's own logs and test output. No winking copy — the numbers are the jokes.

## Hook (first 2-3 seconds)
Five dice tumbling, faces flickering through real rolls from the log, landing hard on a non-match. The question slams in and holds:
**"How long until five dice match?"**
Everyone instinctively guesses. That guess earns the next 20 seconds.

## Key moments (the middle)
- **The prediction:** "Math says 1,296 rolls." — the formula from `explained.md` (6 × (1/6)⁵ = 1/1,296) as supporting texture. Then the deadpan pivot: "I checked. 200 times."
- **The run (the product in use):** a terminal runs `python main.py`, the inputs `5` and `200` get typed, `>>> Simulation N finished after K iterations` lines stream past with real K values, the real log rows (`[3, 2, 1, 1, 3] [5, 1, 3, 3, 2] …`) scroll behind, and a counter climbs to **257,518 rolls. Every one logged.**
- **The twist (the notebook chart):** the notebook's "Iterations per Simulation" line plot redrawn with all 200 real runs, seismograph-style. The dashed red line at 1,296 is the math; the average lands at **1,287.6 ✔** — the math was right. Then the spread: **Simulation 98: 2 rolls** (`[6, 6, 6, 6, 6]`), **Simulation 155: 8,738 rolls**. Headline, verbatim from the repo: **"Expected value ≠ typical experience."**
- **The bonus benchmark:** `nums * 2` vs `nums + nums`, shown as the repo's real pytest summary table. The `mul` rows win, the n=100 row highlights, stamp: **"0.105 µs faster."** Footer: **220 passed.**

## Outro / punchline
The repo name lands like a lab's logo: **brainfarts-and-benchmarks 🧠⚡**
Tagline, verbatim from the README: **"If something here looks dumb — that's probably the point."**
URL that implies legitimacy: `github.com/shreyuu/brainfarts-and-benchmarks`

## User flow worth showing
1. **Entry:** `$ python main.py` → `Enter number of dice: 5` → `Enter number of simulations to run: 200`
2. **Key action:** simulations churn — `>>> Simulation 1 finished after 769 iterations`, `>>> Simulation 2 finished after 57 iterations`, … — while every roll lands in `logs/5die_200sim_26-01-26_17-40-55.txt` (4.1 MB, 26,243 lines).
3. **Result:** the analysis notebook's chart of all 200 runs: average 1,287.6 vs expected 1,296; min 2 (Sim 98), max 8,738 (Sim 155).

## Tone
- Preset: `yc-parody`
- Creative direction: "a serious research lab announcing findings on questions nobody asked"
- Interpretation: structured hard cuts, one claim per beat, sentence-case headlines with mono data, zero jokes in the copy — the corporate-warm music bed and lab-report seriousness make the dice statistics funny on their own.

## Format: landscape — 1920x1080
## Duration: 23.0s

## Visual identity (from the project)
No CSS in this repo — the identity comes from the project's real artifacts: the seaborn `whitegrid` notebook charts and the terminal where `main.py` and pytest run.
- Background: `#F7F8FB` paper (seaborn whitegrid white `#FFFFFF`, tinted toward the data blue so it isn't dead white), with whitegrid lines (seaborn grid `#CCCCCC`, softened to `#DCE1EA` for video)
- Accent (data): `#4C72B0` (seaborn default "deep" blue — the notebook's line color)
- Accent (math / expected line): `#D62728` matplotlib `tab:red`, dashed — the notebook's cap line is `#FF0000`, which fails WCAG AA as text on paper (~4.0:1); tab:red keeps the matplotlib identity at ~4.9:1
- Text: `#1E232D` (seaborn ".15" ink `#262626`, tinted toward the blue)
- Terminal cards: `#1E1E1E` background, `#D4D4D4` text (inferred: VS Code dark default — the repo lives in `~/VSCODE/Projects`), pass marks in `#55A868` (seaborn green, dark cards only)
- Display font: STIX Two Text — the typeface scientific journals are set in (OFL; embedded from the macOS system copy). Headlines read like a paper's title; the "research lab" register made literal. (Revised from IBM Plex Sans during composition: Plex Sans isn't bundled, and sans + mono is a weaker register switch than journal serif + instrument mono.)
- Body / data font: IBM Plex Mono (bundled; Courier-adjacent for data points, logs, terminal)
- Strongest visual element: the "Iterations per Simulation" chart with the 8,738 spike towering over the dashed 1,296 line
- Brand marks: 🧠⚡ from the README title; `✔` from pytest's "hidden cases passed silently ✔"

## Share copy (draft)
I rolled five dice until they matched — 257,518 times — to check one formula; the math held (1,296 predicted, 1,287.6 measured), and the dice still took anywhere from 2 to 8,738 rolls.

## Audio direction
- Role: warm corporate bed under deadpan data — the "launch film" gloss is part of the joke
- Music: `happy-beats-business-moves-vol-11-by-ende-dot-app.mp3` ("warm and business-y", yc-parody fit)
- Music treatment: start at 0.0s from track start; bed volume ~0.28–0.32; quick 0.3s fade-in; ~1.2s fade-out ending at 23.0s
- Music cue guidance: preset read (`assets/music/cues/happy-beats-business-moves-vol-11-by-ende-dot-app.music-cues.md`), 114.84 BPM, beat ≈ 0.52s. Strong-cue locks (max 3 hard locks, others are soft bias):
  - **6.34s** → terminal cuts in (scene 3 start)
  - **9.50s** → counter locks at 257,518
  - **12.65s** → "8,738 rolls" callout on the spike (biggest comic beat)
  - Soft bias only: 1.60s (dice land), 3.70s ("1,296" settles), 17.91s ("0.105 µs faster" stamp — only if it still leaves ≥0.9s hold)
  - Beat-grid windows for sequential reveals: pytest rows 15.81–16.86s (rows are texture, the full table holds after); typing 6.34–7.38s.
  - Restraint: yc-parody — cues bias timing, never drive visible pulsing.
- Audio-reactive treatment: none. Stillness sells the seriousness; motion comes from the data, not the music.
- SFX posture: sparse-to-moderate, strictly motion-matched, ≤7 distinct cue moments. The dice sounds are the most project-specific sound possible — use them.
- Audio-coupled moments: dice rattle → throw/land in the hook; keypresses on `python main.py` and the typed `5` / `200`; one dry landing accent when the counter locks; one soft impact on the 8,738 callout; a small crisp accent on "0.105 µs faster"; one bell-style payoff on the repo name.
- Restraint rule: no SFX under readable headlines unless the headline itself is the motion; no sound on every streamed terminal line or every chart point; nothing louder than the music bed except the hook dice and the logo hit.

## Storyboard

### Scene 1 — The question — 3.0s (0.0–3.0)
Five large dice (paper-white with ink pips, slight shadow) tumble center-frame on the whitegrid paper, faces flickering through real rolls from Simulation 1 of the log (`[3, 2, 1, 1, 3]`, `[5, 1, 3, 3, 2]`, `[3, 5, 6, 1, 1]` …) and landing hard on a non-match. A tiny mono roll counter ticks in a corner (texture only). Headline slams in by ~0.45s and holds the rest of the scene (≥1.8s settled): **"How long until five dice match?"**
Sequential/interaction: yes — dice rattle, then land (aim the landing near 1.60s)
Audio intent: tactile, immediate, a little tense
Audio-coupled idea: dice rattle under the tumble, dice throw/land on the stop
Music: bed starts, warm and businesslike
Transition mood: hard cut → Scene 2

### Scene 2 — The prediction — 3.2s (3.0–6.2)
Clean paper. Big sentence-case headline settles by ~3.7s and holds: **"Math says 1,296 rolls."** Under it, small mono texture from `explained.md`: `P(all match) = 6 × (1/6)⁵ = 1/1,296`. At ~4.5s the second line lands (holds ≥1.2s): **"I checked. 200 times."**
Sequential/interaction: two lines, one after the other; the first stays on screen
Audio intent: dry, matter-of-fact; let the music beat carry the "1,296"
Audio-coupled idea: none (or one very dry accent on "200 times")
Transition mood: hard cut on the 6.34s cue → Scene 3

### Scene 3 — The run — 4.2s (6.2–10.4)
A dark terminal card fills most of the frame. `$ python main.py` types out; then `Enter number of dice: 5` and `Enter number of simulations to run: 200` (the values typed). Output streams fast (texture): `>>> Simulation 1 finished after 769 iterations`, `2 … 57`, `3 … 724`, `4 … 3368`, `5 … 20`, `6 … 1163`, `7 … 1093`, `8 … 183` … Behind/beside it, a ghosted wall of real log rows scrolls. A big counter climbs 0 → **257,518** and locks at 9.50s; its label is visible during the climb: **"rolls. Every one logged."** Small detail after the lock: `logs/5die_200sim_26-01-26_17-40-55.txt · 4.1 MB`.
Sequential/interaction: yes — simulated typing of the command and both inputs; counter climbs and locks
Audio intent: momentum, machinery working
Audio-coupled idea: per-character keypresses (thinned), one dry landing accent when the counter locks
Transition mood: hard cut (or 0.2s crossfade) → Scene 4

### Scene 4 — The twist — 5.0s (10.4–15.4)
Recreate the notebook's **"Iterations per Simulation"** line plot (seaborn whitegrid look: blue line with small dot markers, light grid, Arial-ish axis labels) using all 200 real iteration counts on a **linear** y-axis. The line draws left→right like a seismograph (~1.2s). Dashed red line at 1,296 labeled **"math: 1,296"**. Then, one by one (each holds through scene end):
1. **"avg 1,287.6 ✔"** lands beside the line (~11.7s)
2. **"Sim 98: 2 rolls"** callout at the near-zero dip, with a tiny `[6, 6, 6, 6, 6]` (~12.1s)
3. **"Sim 155: 8,738 rolls"** callout on the towering spike — at the 12.65s cue
Then the headline (verbatim from `explained.md`), settled by ~13.3s and held ≥1.8s: **"Expected value ≠ typical experience."**
Sequential/interaction: yes — chart draws; three labels arrive one by one, then the headline
Audio intent: the "wait, what?" beat — the spike is the laugh
Audio-coupled idea: soft impact on the 8,738 callout; nothing on the line draw
Transition mood: hard cut → Scene 5

### Scene 5 — Meanwhile, in benchmarks — 3.4s (15.4–18.8)
Mono title: **`nums * 2`  vs  `nums + nums`**. A terminal card shows the repo's real pytest summary (from `explained.md`), rows arriving quickly (texture) then holding as a full table:
```
n    plus_us     mul_us   winner
0        0.040     0.050   plus
1        0.050     0.062   plus
2        0.057     0.069   plus
5        0.072     0.075   plus
10       0.086     0.082   mul
50       0.256     0.213   mul
100      0.409     0.304   mul
hidden cases passed silently ✔
220 passed
```
The `mul` winners light up seaborn-blue; the n=100 row gets emphasis; a stamp lands near it and holds ≥0.9s: **"0.105 µs faster."**
Sequential/interaction: yes — rows reveal one by one quickly, then the full table holds; one stamp
Audio intent: tiny, dry triumph — the smallness is the joke
Audio-coupled idea: light ticks on the first and last row only; one crisp small accent on the stamp
Transition mood: hard cut → Scene 6

### Scene 6 — The lab — 4.2s (18.8–23.0)
Paper background, big mono name lands like a lab logo: **brainfarts-and-benchmarks 🧠⚡**. Tagline (verbatim from the README) settles by ~19.9s and holds ≥3.0s: **"If something here looks dumb — that's probably the point."** Small URL below: `github.com/shreyuu/brainfarts-and-benchmarks`. Long, confident hold; music fades out.
Sequential/interaction: name, then tagline, then URL
Audio intent: earnest corporate sign-off on a brainfart
Audio-coupled idea: one bell-style logo hit when the name lands
Transition mood: end on hold, music fade

Total: 3.0 + 3.2 + 4.2 + 5.0 + 3.4 + 4.2 = **23.0s**

**Music mood for this video:** parody — warm corporate launch bed played completely straight
**Audio summary:** dice rattle into a warm business-y bed, typing and one counter landing carry the experiment, a single soft thud lands the 8,738 spike, and a bell crowns the repo name as the music fades.

## Source material & real numbers (all verified from the repo)
- Run: `how-long-until-dice-match/logs/5die_200sim_26-01-26_17-40-55.txt` — 200 simulations, 5 dice, 26,243 lines, 4.1 MB
- Total rolls: 257,518 (1,287,590 individual dice); average 1,287.59; median 865; 131/200 runs finished under 1,296
- Sim 1: first roll `[3, 2, 1, 1, 3]`, matched `[1, 1, 1, 1, 1]` after 769
- Sim 98: `[5, 6, 1, 4, 2]` → `[6, 6, 6, 6, 6]` — 2 rolls (min)
- Sim 155: 8,738 rolls, ended `[2, 2, 2, 2, 2]` (max)
- First 8 iteration counts: 769, 57, 724, 3368, 20, 1163, 1093, 183
- Expected: 6⁴ = 1,296 (`explained.md` probability table)
- Benchmark table: verbatim sample output in `why_is_list_multiply_faster/explained.md`; suite = 220 tests (re-run today on Python 3.14.6: 220 passed, same winner pattern)
- Copy used verbatim: "Expected value ≠ typical experience." (dice `explained.md`), "If something here looks dumb — that's probably the point." (README), "hidden cases passed silently ✔" (pytest output), "Iterations per Simulation" (notebook chart title)
