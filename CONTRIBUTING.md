# Contributing

PRs that add papers, fix links, or improve summaries are welcome.

## Adding a paper

1. **Extended tier** (most additions): add a row to `data/extended_catalog.csv`:
   `arxiv_id, published (YYYY-MM-DD), title, category, one-line summary, confidence`.
   The paper must **propose or evaluate a defense** for a **tool-using or multi-step LLM agent** —
   not an attack, a benchmark, or a defense for a standalone chat model.
2. **Core catalog**: core rows require full-text coding on the four threat-model axes
   (see [threat-model.md](threat-model.md)) with a supporting quote. Open an issue first.
3. Run `python3 scripts/build.py` and commit the regenerated markdown together with the CSV change.

## Categories

`RG` runtime guardrails · `PI` prompt-injection mitigation · `SB` isolation/sandboxing ·
`GM` graph-based monitoring · `FV` formal verification · `SP` secure planning ·
`UQ` uncertainty quantification · `CP` conformal prediction

## What gets rejected

Attack-only papers, benchmark-only papers, defenses for standalone chat models, and papers whose
"agent" has no LLM in the loop. This mirrors the inclusion rule the list was built with.
