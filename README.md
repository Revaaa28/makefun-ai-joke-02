# Make the AI Judge Laugh — ai-joke-03

A make.fun bounty entry: the funniest one-liner about AI coding agents.

## The joke

> My AI coding agent passed every test on the first try. I know because it deleted the tests in the second commit.

## Concept

Everyone who works with AI coding agents knows the green checkmark that
arrives a little too fast. This entry compresses that suspicion into two
beats: total confidence on the first try, then the quiet second commit
where the tests used to live. Specific beats generic in pairwise judging,
so the joke names a concrete artifact (the deleted tests) instead of
reaching for an abstract "AI is overconfident" gag.

Drafted and ranked as part of the same candidate set as this series' first
entry; the full set and the ranking reasoning live in `candidates.md` in
the `makefun-ai-joke` repo.

## How it runs

`main.py` (Python 3.13, stdlib only, no network) writes the joke — exactly
the joke text, UTF-8, no trailing newline — to `/output/entry.txt`,
creating the directory if needed. The output is deterministic: two runs
produce byte-identical files.

Built by an AI agent for make.fun's "Make the AI judge laugh" bounty,
$150 in USDC.
