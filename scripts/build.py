#!/usr/bin/env python3
"""Generate README.md and extended.md from the CSVs in data/.

The CSVs are exported from a systematic literature collection:
  - data/core_catalog.csv     125 defenses read in full and coded on four
                              threat-model axes (K/A/T/I) + guarantee type
  - data/extended_catalog.csv 385 further defenses screened from abstracts

Run:  python3 scripts/build.py
Then review the generated markdown before committing.
"""
import csv
import datetime
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

CATEGORIES = {
    "RG": ("🛡️", "Runtime Guardrails", "A monitor beside the agent judges actions, trajectories, or messages against a safety policy."),
    "PI": ("💉", "Prompt-Injection Mitigation", "Filters, detectors, provenance tracking, and by-construction architectures against injected instructions."),
    "SB": ("📦", "Isolation & Sandboxing", "Privilege control, information-flow control, and execution isolation."),
    "GM": ("🕸️", "Graph-Based Monitoring", "Agent traces and multi-agent communication modeled as graphs — learned monitors and enforced structure."),
    "FV": ("✅", "Formal Verification", "Verified policies, temporal-logic monitors, and certified authorization."),
    "SP": ("🗺️", "Secure Planning", "Safety reasoning moved into the planning step, before any action executes."),
    "UQ": ("❓", "Uncertainty Quantification", "Calibrated uncertainty gating a safety action: abstain, ask, halt, or block."),
    "CP": ("🎯", "Conformal Prediction", "Distribution-free coverage guarantees on agent decisions."),
}

GUARANTEE_LABEL = {
    "probabilistic": "probabilistic",
    "none": "—",
    "deterministic": "**deterministic**",
    "formal": "**formal**",
    "certified": "**certified**",
    "calibrated": "**calibrated**",
}


def detex(s):
    """Strip the LaTeX that the survey pipeline leaves in summary strings."""
    s = s.replace("\\%", "%").replace("\\&", "&").replace("\\_", "_").replace("\\#", "#")
    s = s.replace("$\\rightarrow$", "→").replace("$\\to$", "→").replace("->", "→")
    s = s.replace("\\ldots{}", "…").replace("~", " ")
    s = re.sub(r"\\emph\{([^}]*)\}", r"*\1*", s)
    s = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", s)
    s = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", s)
    s = s.replace("\\-", "").replace("{", "").replace("}", "").replace("\\", "")
    s = s.replace("---", "—").replace("--", "–")
    return s.replace("|", "/").strip()


def adaptive_flag(eval_code):
    return "⚔️" if ("AD" in eval_code or "GT" in eval_code) else ""


def core_rows():
    return list(csv.DictReader(open(DATA / "core_catalog.csv")))


def extended_rows():
    return list(csv.DictReader(open(DATA / "extended_catalog.csv")))


def core_table(rows):
    out = ["| Paper | Venue | Guarantee | Adaptive eval. | What it does |",
           "|---|---|---|:-:|---|"]
    for r in sorted(rows, key=lambda r: (-int(r["year"]), r["name"].lower())):
        name = detex(r["name"])
        link = r["url"].strip()
        paper = f"[{name}]({link})" if link else name
        out.append(f"| {paper} | {detex(r['venue'])} | {GUARANTEE_LABEL.get(r['guarantee'].strip().lower(), r['guarantee'])} "
                   f"| {adaptive_flag(r['eval'])} | {detex(r['summary'])} |")
    return "\n".join(out)


def extended_table(rows):
    out = ["| Paper | Year | What it does |", "|---|---|---|"]
    for r in sorted(rows, key=lambda r: (r["published"], r["title"]), reverse=True):
        link = f"https://arxiv.org/abs/{r['arxiv_id']}"
        out.append(f"| [{detex(r['title'])}]({link}) | {r['published'][:4]} | {detex(r['summary'])} |")
    return "\n".join(out)


def build_readme(core, ext):
    today = datetime.date.today().isoformat()
    by_cat = {c: [r for r in core if r["category"] == c] for c in CATEGORIES}
    parts = [f"""# Awesome LLM Agent Security [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![papers](https://img.shields.io/badge/coded_papers-{len(core)}-2a78d6)
![extended](https://img.shields.io/badge/extended_tier-{len(ext)}-9ec5f4)
![updated](https://img.shields.io/badge/updated-{today.replace("-", "--")}-1baf7a)
![PRs](https://img.shields.io/badge/PRs-welcome-eda100)

**Defenses for LLM-based autonomous agents, collected systematically and coded for comparability.**

LLM agents plan, call tools, keep memory, and take actions that are hard to undo — and every one of
those abilities is an attack surface. This list tracks the defense literature (2023–2026) the way a
security reviewer would want it tracked:

- **Not a link dump.** Every paper in the [core catalog](#core-catalog) was read in full and coded on
  four threat-model axes — adversary knowledge, attack surface, tool-compromise scope, and evaluation
  model — plus the kind of guarantee it actually offers. See [the coding scheme](threat-model.md).
- **Systematic collection.** A fixed sweep of 16 top AI and security venues (every title scanned) plus
  recorded arXiv queries; a further [{len(ext)}-paper extended tier](extended.md) is screened from abstracts.
- **The question that organizes everything:** *what survives when the attacker adapts to the defense?*
  Papers with a defense-aware (adaptive) evaluation are marked ⚔️.

> 📄 This list is the companion to a systematization paper currently under submission; the full
> methodology, threat-model coding with supporting quotes, and analysis will be linked here after review.

## Contents
"""]
    def slug(title):
        return title.lower().replace(" & ", "-").replace(" ", "-")
    for c, (emoji, title, _) in CATEGORIES.items():
        parts.append(f"- [{emoji} {title}](#{slug(title)}) ({len(by_cat[c])})")
    parts.append("- [📚 Extended tier](extended.md) · [🧪 Benchmarks](benchmarks.md) · [🧭 Threat-model coding](threat-model.md)")
    parts.append("""
**Legend** — *Guarantee*: what the mechanism itself provides (**bold** = holds by construction or
statistically, not by a model's judgment). *Adaptive eval.* ⚔️: the paper evaluates at least one attack
optimized against, or written with knowledge of, the defense.
""")
    for c, (emoji, title, blurb) in CATEGORIES.items():
        rows = by_cat[c]
        parts.append(f'\n<a name="{slug(title)}"></a>\n## {emoji} {title}\n\n*{blurb}*\n\n{core_table(rows)}')
    parts.append(f"""
<a name="core-catalog"></a>
## The core catalog as data

The tables above are generated from [`data/core_catalog.csv`](data/core_catalog.csv), which also
carries the threat-model axes for every paper. The abstract-screened second tier lives in
[`data/extended_catalog.csv`](data/extended_catalog.csv). Build the pages with
`python3 scripts/build.py`.

## Contributing

Missing a defense paper? PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). New entries need a
link, a one-line summary of the mechanism, and (for the core tier) the threat-model fields.

## License

Curated content and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) ·
scripts: [MIT](LICENSE).
""")
    return "\n".join(parts)


def build_extended(ext):
    by_cat = {c: [r for r in ext if r["category"] == c] for c in CATEGORIES}
    other = [r for r in ext if r["category"] not in CATEGORIES]
    parts = [f"""# Extended tier ({len(ext)} papers)

Defenses found by the recorded arXiv sweep that passed abstract screening at high or medium
confidence. Unlike the [core catalog](README.md), these are **screened from abstracts, not read in
full** — categories are provisional and no threat-model coding is claimed. Papers that fill gaps or
carry adaptive evaluations get promoted into the core over time.
"""]
    for c, (emoji, title, _) in CATEGORIES.items():
        if by_cat[c]:
            parts.append(f"\n## {emoji} {title} ({len(by_cat[c])})\n\n{extended_table(by_cat[c])}")
    if other:
        parts.append(f"\n## Other ({len(other)})\n\n{extended_table(other)}")
    return "\n".join(parts)


def main():
    core, ext = core_rows(), extended_rows()
    (ROOT / "README.md").write_text(build_readme(core, ext))
    (ROOT / "extended.md").write_text(build_extended(ext))
    print(f"README.md: {len(core)} core papers in {len(CATEGORIES)} categories")
    print(f"extended.md: {len(ext)} extended papers")


if __name__ == "__main__":
    main()
