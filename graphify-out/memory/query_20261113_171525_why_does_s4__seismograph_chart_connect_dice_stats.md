---
type: "query"
date: "2026-11-13T17:15:25.571011+00:00"
question: "Why does s4: seismograph chart connect Dice Stats & Lab Design to Brag Video Production, Dice Match Simulation, HyperFrames Timeline Config?"
contributor: "graphify"
outcome: "useful"
source_nodes: ["s4: seismograph chart", "data.js", "5die_200sim_26-01-26_17-40-55.txt", "iterations_to_match()", "Music cue locks (6.34 / 9.50 / 12.65 s)", "Registry catalog search", "Deterministic tl.set frame rows", "Paused GSAP root timeline (main)"]
---

# Q: Why does s4: seismograph chart connect Dice Stats & Lab Design to Brag Video Production, Dice Match Simulation, HyperFrames Timeline Config?

## Answer

Expanded from original query via vocab: [seismograph, chart, dice, lab, design, brag, video, simulation, match, hyperframes, timeline]. Then traversed BFS, explain on s4, and undirected paths. s4 bridges because three layers meet in it. Data (Dice Match Simulation): iterations_to_match() rolls and logs every roll; main.py shares_data_with the 5die_200sim log (brag-plan.md L27); data.js is extracted from that log (index.html L9); s4 plots D.iters, all 200 iteration counts (index.html L985). All EXTRACTED and source-checked. Timing (Brag Video Production): s4 implements the music cue locks; the Sim 155 spike callout is beat-locked at 12.65s (index.html L1108), EXTRACTED. Tooling (HyperFrames Timeline Config): Registry catalog search is rationale_for s4 (INFERRED, composition-brief.md L100) and holds up: mk-line-graph did not fit a 200-point plot, so the chart was hand-built with the count-up tl.set frame-row idiom on the paused GSAP root timeline. Home (Dice Stats & Lab Design): the expected value vs typical experience takeaway (math 1,296, avg 1,287.6, Sim 98 = 2 rolls, Sim 155 = 8,738). The shortest chart-to-code path runs through music timing (cue locks, s3), not data, because the log links to the main.py module rather than iterations_to_match. Gaps: two separate nodes for the same 5die_200sim log (brag-plan vs brag.gif); no direct edge from s4 to the paused root timeline even though its tweens run on it (index.html L1100-1112).

## Outcome

- Signal: useful

## Source Nodes

- s4: seismograph chart
- data.js
- 5die_200sim_26-01-26_17-40-55.txt
- iterations_to_match()
- Music cue locks (6.34 / 9.50 / 12.65 s)
- Registry catalog search
- Deterministic tl.set frame rows
- Paused GSAP root timeline (main)