# Graph Report - brainfarts-and-benchmarks  (2026-11-14)

## Corpus Check
- 4 files · ~282,609 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 166 nodes · 377 edges · 13 communities (12 shown, 1 thin omitted)
- Extraction: 73% EXTRACTED · 27% INFERRED · 0% AMBIGUOUS · INFERRED: 103 edges (avg confidence: 0.9)
- Token cost: 242,781 input · 0 output

## Community Hubs (Navigation)
- Dice Simulation & s3 Replay
- Dice Statistics & Scenes
- List Multiply Benchmark
- HyperFrames Project Setup
- Brag Video Style & Music
- Repo Philosophy & Outro
- s4 Chart & GSAP Timeline
- Brag GIF Frames
- HyperFrames Config Keys
- Benchmark Test Reporting
- Share Copy & Median Fix
- Multigraph Drawing Script

## God Nodes (most connected - your core abstractions)
1. `Brag video (23 s, 1920×1080)` - 19 edges
2. `s4: seismograph chart` - 17 edges
3. `5die_200sim_26-01-26_17-40-55.txt` - 16 edges
4. `iterations_to_match()` - 15 edges
5. `s3: terminal run + roll counter` - 13 edges
6. `brainfarts-and-benchmarks` - 12 edges
7. `Music cue locks (6.34 / 9.50 / 12.65 s)` - 11 edges
8. `multiply_way()` - 10 edges
9. `Expected iterations 6^(n−1)` - 10 edges
10. `Expected value ≠ typical experience` - 10 edges

## Surprising Connections (you probably didn't know these)
- `How long until five dice match?` --conceptually_related_to--> `iterations_to_match()`  [INFERRED]
  brag-output/brag.jpg → how-long-until-dice-match/main.py
- `Outro card: brainfarts-and-benchmarks README title, tagline, GitHub link, five matching dice` --references--> `iterations_to_match()`  [INFERRED]
  brag-output/brag.gif → how-long-until-dice-match/main.py
- `pytest -q -s visible-case timing table (avg µs per call, 220 passed)` --references--> `teardown_module()`  [INFERRED]
  brag-output/brag.gif → why_is_list_multiply_faster/tests/test_main.py
- `Verbatim on-screen copy` --references--> `teardown_module()`  [INFERRED]
  brag-output/composition-brief.md → why_is_list_multiply_faster/tests/test_main.py
- `python main.py run: 200 sims, 257,518 rolls, 'Every one logged.'` --conceptually_related_to--> `Roll dice until all show the same value. Log rolls in rows of fixed column…`  [INFERRED]
  brag-output/brag.gif → how-long-until-dice-match/main.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Brag video six-scene storyboard** — brag_output_brag_plan_scene_1_the_question, brag_output_brag_plan_scene_2_the_prediction, brag_output_brag_plan_scene_3_the_run, brag_output_brag_plan_scene_4_the_twist, brag_output_brag_plan_scene_5_meanwhile_in_benchmarks, brag_output_brag_plan_scene_6_the_lab [EXTRACTED 1.00]
- **EXP. 01 arc: math prediction, 200-run simulation, Fig. 1 result, takeaway** — brag_output_brag_expected_1296_rolls, brag_output_brag_200_simulation_run, brag_output_brag_fig1_iterations_per_simulation, brag_output_brag_avg_1287_6_rolls, brag_output_brag_expected_value_not_typical_experience [EXTRACTED 1.00]
- **5-dice run data lineage: log to data.js to video scenes** — how_long_until_dice_match_logs_5die_200sim_26_01_26_17_40_55, brag_output_composition_assets_data, brag_output_composition_index_s1_dice_tumble, brag_output_composition_index_s3_terminal_run, brag_output_composition_index_s4_seismograph_chart [EXTRACTED 1.00]
- **Measure-don't-assume takeaways across experiments** — readme_measure_dont_assume, how_long_until_dice_match_explained_expected_value_vs_typical_experience, why_is_list_multiply_faster_explained_same_result_not_same_cost [INFERRED 0.75]
- **EXP. 02 benchmark: plus_way and multiply_way timed by the pytest summary into the 0.105 µs claim** — why_is_list_multiply_faster_experiment_plus_way, why_is_list_multiply_faster_experiment_multiply_way, why_is_list_multiply_faster_tests_test_main_teardown_module, brag_output_brag_pytest_timing_table, brag_output_brag_mul_0_105us_faster_at_n100 [INFERRED 0.85]
- **Real dice simulation data feeding the poster frame** — how_long_until_dice_match_main_main, how_long_until_dice_match_main_iterations_to_match, brag_output_composition_assets_data, brag_output_brag_roll_15_near_miss [INFERRED 0.85]

## Communities (13 total, 1 thin omitted)

### Community 0 - "Dice Simulation & s3 Replay"
Cohesion: 0.17
Nodes (22): python main.py run: 200 sims, 257,518 rolls, 'Every one logged.', EXP. 01 · 5 dice · 200 runs, How long until five dice match?, Launch video poster frame, Scene 3 — The run, Roll 15 near miss [4, 4, 4, 5, 4], no match, s3: terminal run + roll counter, Shortest s4-to-code path runs through music timing, not data (log links to main.py, not iterations_to_match()) (+14 more)

### Community 1 - "Dice Statistics & Scenes"
Cohesion: 0.16
Nodes (22): logs/5die_200sim_26-01-26_17-40-55.txt (4.1 MB), Scene 1 — The question, Scene 2 — The prediction, Scene 4 — The twist, Verbatim on-screen copy, s2: prediction headline, Gap: two nodes for the same 5die_200sim log (brag-plan vs brag.gif), Home takeaway: expected value ≠ typical experience (math 1,296, avg 1,287.6, Sim 98 = 2, Sim 155 = 8,738) (+14 more)

### Community 2 - "List Multiply Benchmark"
Cohesion: 0.21
Nodes (20): EXP. 02: nums * 2 vs nums + nums (n = 0-100, 5,000 repeats), nums * 2 is 0.105 µs faster per call at n = 100 (0.304 vs 0.409 µs), Crossover: nums + nums wins for n ≤ 5, nums * 2 wins from n = 10, pytest -q -s visible-case timing table (avg µs per call, 220 passed), parametrize, multiply_way(), plus_way(), run_test() (+12 more)

### Community 3 - "HyperFrames Project Setup"
Cohesion: 0.14
Nodes (15): Agent-safe background preview, /hyperframes skill router, Pinned hyperframes CLI version, Timed clip rule (data-start + .clip), /brag workflow, name, private, scripts (+7 more)

### Community 4 - "Brag Video Style & Music"
Cohesion: 0.25
Nodes (14): Brag video (23 s, 1920×1080), STIX Two Text + IBM Plex Mono typography, Motion-matched sparse SFX, Music cue locks (6.34 / 9.50 / 12.65 s), Seaborn whitegrid visual identity, Serious science for stupid questions, yc-parody tone preset, Beat grid and strong cues (114.84 BPM) (+6 more)

### Community 5 - "Repo Philosophy & Outro"
Cohesion: 0.26
Nodes (10): Scene 6 — The lab, s6: lab outro, Adding an experiment, Assert correctness, report speed, brainfarts-and-benchmarks, Measure, don't assume, One question per folder, Playground, not a library (+2 more)

### Community 6 - "s4 Chart & GSAP Timeline"
Cohesion: 0.32
Nodes (12): Deterministic logic only, Paused root timeline on window.__timelines, Registry catalog search, Deterministic tl.set frame rows, GSAP, Paused GSAP root timeline (main), s4: seismograph chart, Data layer: iterations_to_match() → 5die_200sim log → data.js → s4 plots all 200 counts (+4 more)

### Community 7 - "Brag GIF Frames"
Cohesion: 0.29
Nodes (10): Observed average 1,287.6 rolls vs math 1,296 (✓), EXP. 01: How long until five dice match? (5 dice, 200 runs), Math says 1,296 rolls (P = 6 × (1/6)^5 = 1/1,296), Expected value ≠ typical experience, Extremes: 2 rolls (Sim 98) and 8,738 rolls (Sim 155), Fig. 1: Iterations per Simulation (Sim 1 to 200, 5 dice), Lab-notebook visual style (grid paper, repo-path breadcrumb, EXP. tag, serif headlines, monospace data), brag.gif launch video (23 s, 960x540, 12 fps) (+2 more)

### Community 8 - "HyperFrames Config Keys"
Cohesion: 0.22
Nodes (8): media, autoProxy, paths, assets, blocks, components, registry, $schema

### Community 9 - "Benchmark Test Reporting"
Cohesion: 0.39
Nodes (8): 0.105 µs faster at n = 100, Scene 5 — Meanwhile, in benchmarks, s5: pytest summary terminal, Call overhead dominates tiny lists, Visible-case timing summary table, LeetCode-style visible/hidden cases, Print LeetCode-style summary for visible cases only., teardown_module()

### Community 10 - "Share Copy & Median Fix"
Cohesion: 0.47
Nodes (3): share-copy.txt, Median error: true median is 861.5 (middle runs 858 and 865), not 865, Median 861.5 rolls (131/200 under 1,296)

## Knowledge Gaps
- **9 isolated node(s):** `name`, `private`, `type`, `autoProxy`, `assets` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Brag video (23 s, 1920×1080)` connect `Brag Video Style & Music` to `Dice Simulation & s3 Replay`, `Dice Statistics & Scenes`, `HyperFrames Project Setup`, `Repo Philosophy & Outro`, `Benchmark Test Reporting`, `Share Copy & Median Fix`?**
  _High betweenness centrality (0.241) - this node is a cross-community bridge._
- **Why does `s4: seismograph chart` connect `s4 Chart & GSAP Timeline` to `Dice Simulation & s3 Replay`, `Dice Statistics & Scenes`, `Brag Video Style & Music`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Why does `Registry catalog search` connect `s4 Chart & GSAP Timeline` to `HyperFrames Config Keys`, `Dice Simulation & s3 Replay`, `Brag Video Style & Music`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `s4: seismograph chart` (e.g. with `Registry catalog search` and `Paused GSAP root timeline (main)`) actually correct?**
  _`s4: seismograph chart` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `5die_200sim_26-01-26_17-40-55.txt` (e.g. with `logs/5die_200sim_26-01-26_17-40-55.txt (4.1 MB)` and `Dice matching experiment`) actually correct?**
  _`5die_200sim_26-01-26_17-40-55.txt` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `iterations_to_match()` (e.g. with `python main.py run: 200 sims, 257,518 rolls, 'Every one logged.'` and `How long until five dice match?`) actually correct?**
  _`iterations_to_match()` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `s3: terminal run + roll counter` (e.g. with `Registry catalog search` and `iterations_to_match()`) actually correct?**
  _`s3: terminal run + roll counter` has 3 INFERRED edges - model-reasoned connections that need verification._