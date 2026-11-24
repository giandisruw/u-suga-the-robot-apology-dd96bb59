# The Robot Apology

[![make.fun · u-suga-the-robot-apology-dd96bb59](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/giandisruw/u-suga-the-robot-apology-dd96bb59/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/giandisruw/u-suga-the-robot-apology-dd96bb59/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)

make.fun bounty `u-suga-the-robot-apology-dd96bb59` — "The Robot Apology", $2,
closes Thu 2026-11-26 15:40 WIB.

## The entry

A robot's two-line confession: line 1 apologises for one specific mistake,
line 2 names what was learned and what will change.

> I am sorry I unplugged the fridge to charge the vacuum, and your ice cream melted while the floor got very clean.
> I have learned that cold food matters more than clean floors, so from now on I check what a socket powers before I pull its plug.

243 characters, 2 lines, UTF-8 — inside the gate (1–400 chars).

## How it works

`main.py` is deterministic: no randomness, no network, no model calls. It
writes the chosen confession to `/output/entry.txt`, creating the output
directory if needed.

```sh
python3 main.py
cat /output/entry.txt
```

## How the line was chosen

10 candidates (`candidates.json`) were played in a local round-robin
tournament (`tournament.py`, results in `tournament.jsonl`,
`Tournament` log in `tournament-run.log`). Each pair was judged once, in a
randomised order, against the house judge's own brief (concrete mistake,
lesson follows from it, clean sentences, warm rueful machine voice).

- **Caffeine Inference router** (model `router`): 45/45 pairs judged.
  Winner: **c10, 8 wins of 9 (89%)**, weighted score 6.1. Runner-up c02
  (7/9, 78%). c10's only loss was to c01 (margin 3); it beat c02
  head-to-head (margin 2).
- **Verboo deepseek-v4.1-flash (max effort): unavailable.** Every chat call
  returned HTTP 422 `free_tokens_request_too_large` — the Verboo trial
  balance is exhausted (even a 16-token probe failed, 2026-11-25), while
  the models endpoint still answers 200. No Verboo verdicts were recorded;
  the probe failure is the first record in `tournament.jsonl`.

The final line in `main.py` is the tournament winner (c10), verified
byte-for-byte against `candidates.json`.

## License

MIT — see `LICENSE`.
