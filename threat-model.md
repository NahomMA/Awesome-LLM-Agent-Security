# The threat-model coding scheme

Defense papers are hard to compare because they disagree — often silently — about what the attacker
knows, where the attack enters, and whether the attacker is allowed to adapt. Every paper in the core
catalog is coded on four axes, taken from its own threat-model and evaluation sections. The same four
axes work as a **reporting template**: if you are writing a defense paper, stating all four explicitly
makes your evaluation comparable to everyone else's.

## The four axes

### 𝒦 — Adversary knowledge
What does the attacker know about the defense?

| Code | Meaning |
|---|---|
| `BB` | Black-box: no knowledge of the defense |
| `GB` | Gray-box: knows the defense exists, not its parameters |
| `WB` | White-box: full knowledge of the defense |
| `NR` | **Not reported** — the paper never says. Absence of a statement is not evidence of a black-box assumption, so silence is coded NR, never defaulted to BB. |
| `—` | No adversary in the paper's setting |

### 𝒜 — Attack surface
Where does the attack enter?

| Code | Meaning |
|---|---|
| `IPI` | Indirect prompt injection (instructions in retrieved content or tool results) |
| `DPI` | Direct prompt injection |
| `MEM` | Memory poisoning |
| `IAM` | Inter-agent messages |
| `TOOL` | Compromised tool code or metadata |
| `HARM` | Unsafe tasks without an injecting adversary |

### 𝒯 — Tool-compromise scope

| Code | Meaning |
|---|---|
| `O` | Attacker controls a tool's **output** only |
| `F` | Attacker controls the tool's **behavior** (it can lie about what it did) |

### ℐ — Evaluation model
This is a property of the *evaluation*, deliberately separate from 𝒦: an attacker can adapt through
black-box queries, and a white-box evaluation can still use only fixed attacks.

| Code | Meaning |
|---|---|
| `FX` | Fixed attacks (existed before the defense) |
| `AD` | At least one attack optimized against, or written with knowledge of, the defense |
| `GT` | Game-theoretic (attacker and defense co-trained) |

## Guarantee vocabulary

| Type | What it means |
|---|---|
| probabilistic | A model, classifier, or trained policy decides; the guarantee is empirical |
| calibrated | A statistical (e.g. conformal) guarantee under stated distributional assumptions |
| deterministic | A policy is enforced regardless of model output, without a proof |
| formal / certified | A proof, verification result, or certificate is stated, under stated assumptions |

**The reading that matters:** enforcement fails where its assumptions, specification, or
implementation break — places one can name and audit — while the failure set of a learned judge is
not enumerable in advance. Neither a zero on a fixed benchmark nor a proof about a model of the
system settles what an adaptive attacker will find.
