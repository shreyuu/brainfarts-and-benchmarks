# Hyperframes Composition Brief: brainfarts-and-benchmarks

## Objective
Create a short launch-style brag video for brainfarts-and-benchmarks — a repo of curiosity-driven Python experiments — played as a deadpan research-lab announcement of findings nobody asked for.

## Output
- Composition directory: `brag-output/composition/`
- Rendered video: `brag-output/brag.mp4`
- Format: landscape — 1920x1080, 30fps
- Duration: 23.0 seconds

## Source Material
- Project root: `/Users/shreyu/VSCODE/Projects/brainfarts-and-benchmarks`
- Primary files read: `README.md`, `how-long-until-dice-match/{main.py, explained.md, charts.ipynb, logs/*.txt}`, `why_is_list_multiply_faster/{experiment.py, explained.md, tests/test_main.py}`, `pytest.ini`, `.gitignore`, git remote
- Product name: brainfarts-and-benchmarks 🧠⚡
- Tagline / strongest claim: 257,518 logged dice rolls to check one formula — math predicted 1,296, measured 1,287.6; runs ranged from 2 to 8,738
- Key UI or visual moment to recreate:
  - `main.py` terminal session (`python main.py`, inputs 5 / 200, `>>> Simulation N finished after K iterations`, `--- Simulation Results ---`)
  - the analysis notebook's "Iterations per Simulation" line plot, redrawn with all 200 real values
  - the pytest summary table printed by `tests/test_main.py`
  - real log rows (`[3, 2, 1, 1, 3] [5, 1, 3, 3, 2] …`) from `logs/5die_200sim_26-01-26_17-40-55.txt`
- Copy that must appear verbatim:
  - "How long until five dice match?"
  - "Math says 1,296 rolls."
  - "I checked. 200 times."
  - "Every one logged."
  - "Expected value ≠ typical experience." (dice `explained.md`)
  - "0.105 µs faster."
  - "If something here looks dumb — that's probably the point." (README)
  - "hidden cases passed silently ✔" (pytest output)
  - "Iterations per Simulation" (notebook chart title)
  - "Match achieved with value 6 in 2 iterations." (log line, Sim 98)

## Creative Direction
- Tone preset: yc-parody
- Creative direction: "a serious research lab announcing findings on questions nobody asked"
- Interpretation: hard cuts, one claim per beat, journal-serif statements with mono data, zero jokes in the copy — the corporate-warm bed and lab-report seriousness make the dice statistics funny on their own.
- Angle: Serious science for stupid questions. The comedy is the gap between the question and the rigor (200 simulations, every roll logged, 4.1 MB of dice; 220 tests for a one-line function). Every number on screen is real.
- Hook: five dice tumbling through real Sim 1 rolls, landing on a near miss `[4, 4, 4, 5, 4]` while "How long until five dice match?" holds.
- Outro / punchline: brainfarts-and-benchmarks 🧠⚡ — "If something here looks dumb — that's probably the point." — github.com/shreyuu/brainfarts-and-benchmarks
- Avoid:
  - Generic SaaS language
  - Abstract filler visuals
  - Unrelated visual redesign
  - Invented numbers or claims (every figure comes from the logs, notebook, or test output)

## Visual Identity
- Background: paper `#F7F8FB` (seaborn whitegrid white, tinted toward the data blue), whitegrid lines `#DCE1EA`
- Text: ink `#1E232D` (seaborn ".15" `#262626`, tinted); muted `#5A6272`
- Accent: data blue `#4C72B0` (seaborn deep C0, the notebook's line color); math red `#D62728` (matplotlib tab:red — the notebook's dashed red line, darkened from `#FF0000` to pass WCAG AA as text)
- Terminal cards: `#1E1E1E` / `#D4D4D4` (VS Code dark default; the repo lives in `~/VSCODE/Projects`), pytest green `#55A868` (seaborn deep C2) on dark only
- Display font: STIX Two Text (the scientific-publishing typeface; OFL; embedded locally from the macOS system copy via `@font-face`) — statements, numbers in prose, formula
- Body font: IBM Plex Mono (bundled by Hyperframes) — terminal, logs, data labels, metadata
- Visual references from the project: seaborn whitegrid chart look, red dashed reference line, terminal output of `main.py` and pytest, log row format, README emoji 🧠⚡, pytest `✔`

## Storyboard
Use the storyboard in `brag-output/brag-plan.md` as the creative contract.

Scene summary:
1. The question — 3.0s (0.0–3.0) — dice tumble through real rolls, land on `[4, 4, 4, 5, 4]`; headline "How long until five dice match?"
2. The prediction — 3.2s (3.0–6.2) — "Math says 1,296 rolls." + formula *P* = 6 · (1/6)⁵ = 1/1,296; "I checked. 200 times."
3. The run — 4.2s (6.2–10.4) — terminal runs `python main.py`, types 5 and 200, streams all 200 real "finished after K iterations" lines + results block; counter = running sum of real iterations, locks at 257,518; "Every one logged."; log tape of real rows
4. The twist — 5.0s (10.4–15.4) — "Iterations per Simulation" line plot of 200 real runs, dashed red 1,296; measured 1,287.6; callouts Sim 98 = 2 rolls (`[6, 6, 6, 6, 6]`), Sim 155 = 8,738 rolls; headline "Expected value ≠ typical experience."
5. Meanwhile, in benchmarks — 3.4s (15.4–18.8) — `nums * 2` vs `nums + nums`; pytest summary table (explained.md sample) with `mul` winners and n=100 row highlighted; "0.105 µs faster."; "220 passed"
6. The lab — 4.2s (18.8–23.0) — repo name + 🧠⚡, README tagline, GitHub URL, matched dice `[6, 6, 6, 6, 6]` with "Match achieved with value 6 in 2 iterations."

## Audio
- Audio role: warm corporate bed under deadpan data
- Audio arc: dice rattle into the bed → typing and one counter landing carry the experiment → one soft thud lands the 8,738 spike → small crisp accent on 0.105 µs → bell crowns the name as the bed fades out
- Music: `happy-beats-business-moves-vol-11-by-ende-dot-app.mp3`
- Music treatment: starts at 0.0 from track start; bed level ~0.30 via a `data-automation` volume lane (0→0.30 over 0.3s, hold, fade to 0 over 21.8→23.0s); no ducking needed (no voice)
- Music cue guidance: bundled preset `assets/music/cues/happy-beats-business-moves-vol-11-by-ende-dot-app.music-cues.{md,json}` — 114.84 BPM. Hard locks: 6.34s (terminal lands), 9.50s (counter locks), 12.65s (8,738 callout). Soft bias: 1.60s (dice land), 3.70s ("1,296" settles). Beat-grid: pytest rows from 15.81s; `mul` highlights on consecutive beats. "0.105 µs faster." uses natural timing (~17.55s) for a ≥1.2s hold rather than the 17.91s cue.
- Audio-reactive treatment: none — deliberate; stillness sells the deadpan seriousness, and motion comes from the data. Documented here per brag step 3.
- Audio-coupled moments:
  - Scene 1 — dice shake under the tumble, dice throw on the landing
  - Scene 3 — per-character keypresses (thinned) for `python main.py`, `5`, `200`; one dry landing accent when the counter locks
  - Scene 4 — one soft impact on the 8,738 callout
  - Scene 5 — one small crisp accent on "0.105 µs faster."
  - Scene 6 — bell-style logo hit; a quiet dice throw as the matched dice land
- SFX selection guidance: match the gesture — dice for dice, keys for typing, soft impact for the reveal, bell for the payoff; nothing on streamed terminal lines or chart points
- SFX analysis guidance: `skills/brag/assets/sfx/sfx-analysis.md` — impactSoft_medium is the lowest-risk reveal family; casino files skew bright, so dice cues stay isolated and moderate in volume
- Exact SFX choice: chosen in the composition against the implemented animation
- Audio files: music and chosen SFX copied into `brag-output/composition/assets/`

## Hyperframes Instructions
Built with `hyperframes-core`, `hyperframes-animation`, `hyperframes-creative`, `hyperframes-keyframes`, `hyperframes-cli` (plus `hyperframes-audio` for the volume lane and `hyperframes-registry` for the catalog search). /brag is its own workflow: no `hyperframes` entry-point interview, no generic promo workflow.

Requirements:
- Show real UI, copy, and data from the source project (all four source moments above).
- Keep all text readable in the final render (reading-time floors from `step-2-plan.md`).
- Keep the video at 23.0s.
- Include the music bed and SFX layer.
- Music cues are hints; readability wins over cue locks.
- Local assets for audio and fonts.
- `npx hyperframes check` must pass with zero errors before render.

Implementation notes (decided during composition):
- Monolithic `index.html` with one paused GSAP timeline; persistent paper/grid/top-bar layer spans all scenes; six timed scene clips.
- Per-frame text (dice faces, counter digits, terminal stream) uses `tl.set(..., {textContent|attr})` rows — the registry `count-up` pattern — so every seek is deterministic without update callbacks.
- Catalog searched for terminal / line chart / counter / dice: `terminal-simulator`, `mk-line-graph`, `count-up` inspected; none matches the exact repo output or 200-point plot, so these are hand-built (borrowing count-up's frame-row idiom). No dice primitive exists.
