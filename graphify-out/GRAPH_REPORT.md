# Graph Report - brainfarts-and-benchmarks  (2026-11-13)

## Corpus Check
- 24 files · ~281,891 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 150 nodes · 315 edges · 9 communities (8 shown, 1 thin omitted)
- Extraction: 68% EXTRACTED · 32% INFERRED · 0% AMBIGUOUS · INFERRED: 100 edges (avg confidence: 0.9)
- Token cost: 713,003 input · 0 output

## Community Hubs (Navigation)
- Brag Video Production
- Dice Stats & Lab Design
- List Multiply Benchmark
- Dice Match Simulation
- HyperFrames Timeline Config
- Benchmark Test Conventions
- Brag GIF Frames
- Multigraph Drawing Script

## God Nodes (most connected - your core abstractions)
1. `Brag video (23 s, 1920×1080)` - 19 edges
2. `brainfarts-and-benchmarks` - 12 edges
3. `iterations_to_match()` - 11 edges
4. `5die_200sim_26-01-26_17-40-55.txt` - 11 edges
5. `multiply_way()` - 10 edges
6. `s4: seismograph chart` - 10 edges
7. `Dice matching experiment` - 9 edges
8. `Expected iterations 6^(n−1)` - 9 edges
9. `Expected value ≠ typical experience` - 9 edges
10. `test_same_output_for_sizes_0_to_100()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `How long until five dice match?` --conceptually_related_to--> `iterations_to_match()`  [INFERRED]
  brag-output/brag.jpg → how-long-until-dice-match/main.py
- `Outro card: brainfarts-and-benchmarks README title, tagline, GitHub link, five matching dice` --references--> `iterations_to_match()`  [INFERRED]
  brag-output/brag.gif → how-long-until-dice-match/main.py
- `python main.py run: 200 sims, 257,518 rolls, 'Every one logged.'` --conceptually_related_to--> `Roll dice until all show the same value. Log rolls in rows of fixed column…`  [INFERRED]
  brag-output/brag.gif → how-long-until-dice-match/main.py
- `pytest -q -s visible-case timing table (avg µs per call, 220 passed)` --references--> `teardown_module()`  [INFERRED]
  brag-output/brag.gif → why_is_list_multiply_faster/tests/test_main.py
- `Verbatim on-screen copy` --references--> `teardown_module()`  [INFERRED]
  brag-output/composition-brief.md → why_is_list_multiply_faster/tests/test_main.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Brag video six-scene storyboard** — brag_output_brag_plan_scene_1_the_question, brag_output_brag_plan_scene_2_the_prediction, brag_output_brag_plan_scene_3_the_run, brag_output_brag_plan_scene_4_the_twist, brag_output_brag_plan_scene_5_meanwhile_in_benchmarks, brag_output_brag_plan_scene_6_the_lab [EXTRACTED 1.00]
- **5-dice run data lineage: log to data.js to video scenes** — how_long_until_dice_match_logs_5die_200sim_26_01_26_17_40_55, brag_output_composition_assets_data, brag_output_composition_index_s1_dice_tumble, brag_output_composition_index_s3_terminal_run, brag_output_composition_index_s4_seismograph_chart [EXTRACTED 1.00]
- **Measure-don't-assume takeaways across experiments** — readme_measure_dont_assume, how_long_until_dice_match_explained_expected_value_vs_typical_experience, why_is_list_multiply_faster_explained_same_result_not_same_cost [INFERRED 0.75]
- **EXP. 01 arc: math prediction, 200-run simulation, Fig. 1 result, takeaway** — brag_output_brag_expected_1296_rolls, brag_output_brag_200_simulation_run, brag_output_brag_fig1_iterations_per_simulation, brag_output_brag_avg_1287_6_rolls, brag_output_brag_expected_value_not_typical_experience [EXTRACTED 1.00]
- **EXP. 02 benchmark: plus_way and multiply_way timed by the pytest summary into the 0.105 µs claim** — why_is_list_multiply_faster_experiment_plus_way, why_is_list_multiply_faster_experiment_multiply_way, why_is_list_multiply_faster_tests_test_main_teardown_module, brag_output_brag_pytest_timing_table, brag_output_brag_mul_0_105us_faster_at_n100 [INFERRED 0.85]
- **Real dice simulation data feeding the poster frame** — how_long_until_dice_match_main_main, how_long_until_dice_match_main_iterations_to_match, brag_output_composition_assets_data, brag_output_brag_roll_15_near_miss [INFERRED 0.85]

## Communities (9 total, 1 thin omitted)

### Community 0 - "Brag Video Production"
Cohesion: 0.10
Nodes (27): Brag video (23 s, 1920×1080), Motion-matched sparse SFX, Music cue locks (6.34 / 9.50 / 12.65 s), Serious science for stupid questions, yc-parody tone preset, Agent-safe background preview, /hyperframes skill router, Pinned hyperframes CLI version (+19 more)

### Community 1 - "Dice Stats & Lab Design"
Cohesion: 0.12
Nodes (27): STIX Two Text + IBM Plex Mono typography, Scene 2 — The prediction, Scene 4 — The twist, Scene 6 — The lab, Seaborn whitegrid visual identity, Verbatim on-screen copy, Lab-paper design tokens, s2: prediction headline (+19 more)

### Community 2 - "List Multiply Benchmark"
Cohesion: 0.21
Nodes (20): EXP. 02: nums * 2 vs nums + nums (n = 0-100, 5,000 repeats), nums * 2 is 0.105 µs faster per call at n = 100 (0.304 vs 0.409 µs), Crossover: nums + nums wins for n ≤ 5, nums * 2 wins from n = 10, pytest -q -s visible-case timing table (avg µs per call, 220 passed), parametrize, multiply_way(), plus_way(), run_test() (+12 more)

### Community 3 - "Dice Match Simulation"
Cohesion: 0.20
Nodes (18): python main.py run: 200 sims, 257,518 rolls, 'Every one logged.', EXP. 01 · 5 dice · 200 runs, How long until five dice match?, Launch video poster frame, logs/5die_200sim_26-01-26_17-40-55.txt (4.1 MB), Scene 1 — The question, Scene 3 — The run, Roll 15 near miss [4, 4, 4, 5, 4], no match (+10 more)

### Community 4 - "HyperFrames Timeline Config"
Cohesion: 0.15
Nodes (14): Deterministic logic only, Paused root timeline on window.__timelines, Registry catalog search, Deterministic tl.set frame rows, media, autoProxy, paths, assets (+6 more)

### Community 5 - "Benchmark Test Conventions"
Cohesion: 0.21
Nodes (12): 0.105 µs faster at n = 100, Scene 5 — Meanwhile, in benchmarks, s5: pytest summary terminal, Adding an experiment, Assert correctness, report speed, One question per folder, Averaged timing (5,000 repeats), Call overhead dominates tiny lists (+4 more)

### Community 6 - "Brag GIF Frames"
Cohesion: 0.29
Nodes (10): Observed average 1,287.6 rolls vs math 1,296 (✓), EXP. 01: How long until five dice match? (5 dice, 200 runs), Math says 1,296 rolls (P = 6 × (1/6)^5 = 1/1,296), Expected value ≠ typical experience, Extremes: 2 rolls (Sim 98) and 8,738 rolls (Sim 155), Fig. 1: Iterations per Simulation (Sim 1 to 200, 5 dice), Lab-notebook visual style (grid paper, repo-path breadcrumb, EXP. tag, serif headlines, monospace data), brag.gif launch video (23 s, 960x540, 12 fps) (+2 more)

## Knowledge Gaps
- **9 isolated node(s):** `$schema`, `blocks`, `components`, `assets`, `autoProxy` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Brag video (23 s, 1920×1080)` connect `Brag Video Production` to `Dice Stats & Lab Design`, `Dice Match Simulation`, `Benchmark Test Conventions`?**
  _High betweenness centrality (0.279) - this node is a cross-community bridge._
- **Why does `Registry catalog search` connect `HyperFrames Timeline Config` to `Brag Video Production`, `Dice Stats & Lab Design`, `Dice Match Simulation`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Why does `s4: seismograph chart` connect `Dice Stats & Lab Design` to `Brag Video Production`, `Dice Match Simulation`, `HyperFrames Timeline Config`?**
  _High betweenness centrality (0.107) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `iterations_to_match()` (e.g. with `python main.py run: 200 sims, 257,518 rolls, 'Every one logged.'` and `How long until five dice match?`) actually correct?**
  _`iterations_to_match()` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `5die_200sim_26-01-26_17-40-55.txt` (e.g. with `Dice matching experiment` and `Per-run log file format`) actually correct?**
  _`5die_200sim_26-01-26_17-40-55.txt` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `multiply_way()` (e.g. with `EXP. 02: nums * 2 vs nums + nums (n = 0-100, 5,000 repeats)` and `run_test()`) actually correct?**
  _`multiply_way()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `$schema`, `blocks`, `components` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._