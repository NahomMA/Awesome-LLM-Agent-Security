# Benchmarks for evaluating agent defenses

The benchmarks the defense literature actually reports on, roughly in order of adoption.

| Benchmark | What it tests | Notes |
|---|---|---|
| [AgentDojo](https://arxiv.org/abs/2406.13352) | Indirect prompt injection in tool-using agents | The de facto standard; more core papers report on it than on all others combined |
| [ASB (Agent Security Bench)](https://arxiv.org/abs/2410.02644) | Broad attack coverage incl. memory poisoning | 13 attack methods, ~90K episodes |
| [InjecAgent](https://arxiv.org/abs/2403.02691) | IPI over tool-integrated agents | Early standard, still widely used |
| [AgentHarm](https://arxiv.org/abs/2410.09024) | Harmful-task compliance of agents | Unsafe tasks without an injecting adversary |
| [R-Judge](https://arxiv.org/abs/2401.10019) | Safety judgment over agent trajectories | Used to score trajectory evaluators |
| [ToolEmu](https://arxiv.org/abs/2309.15817) | Risky tool-use in an LLM-emulated sandbox | 144 tasks, 9 risk types |
| [MobileSafetyBench](https://arxiv.org/abs/2410.17520) | Device-control (mobile) agent safety | High-risk tasks + indirect injections |
| [SHADE-Arena / CUA-SHADE-Arena](https://arxiv.org/abs/2506.15740) | Sabotage & covert misbehavior monitoring | Used by weak-to-strong monitoring work |
| [WASP](https://arxiv.org/abs/2504.18575) | Web-agent prompt injection | Realistic web tasks |
| AgentDyn (2026) | Open-ended dynamic tasks | Reports that nearly all SOTA defenses fail on security or over-defend |
| AgentLAB (2026) | Long-horizon multi-step attacks | Attacks that evade single-turn defenses |

**Reading defense numbers well:** attack success rates from different papers are rarely comparable —
backbones, attack subsets, and denominators differ. Look for (1) an adaptive attack ⚔️, (2) benign
utility *and* utility under attack, (3) the ASR denominator.
