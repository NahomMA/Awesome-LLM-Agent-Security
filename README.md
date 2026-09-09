# Awesome LLM Agent Security [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![papers](https://img.shields.io/badge/coded_papers-125-2a78d6)
![extended](https://img.shields.io/badge/extended_tier-385-9ec5f4)
![updated](https://img.shields.io/badge/updated-2026--09--09-1baf7a)
![PRs](https://img.shields.io/badge/PRs-welcome-eda100)

**Defenses for LLM-based autonomous agents, collected systematically and coded for comparability.**

LLM agents plan, call tools, keep memory, and take actions that are hard to undo — and every one of
those abilities is an attack surface. This list tracks the defense literature (2023–2026) the way a
security reviewer would want it tracked:

- **Not a link dump.** Every paper in the [core catalog](#core-catalog) was read in full and coded on
  four threat-model axes — adversary knowledge, attack surface, tool-compromise scope, and evaluation
  model — plus the kind of guarantee it actually offers. See [the coding scheme](threat-model.md).
- **Systematic collection.** A fixed sweep of 16 top AI and security venues (every title scanned) plus
  recorded arXiv queries; a further [385-paper extended tier](extended.md) is screened from abstracts.
- **The question that organizes everything:** *what survives when the attacker adapts to the defense?*
  Papers with a defense-aware (adaptive) evaluation are marked ⚔️.

> 📄 This list is the companion to a systematization paper currently under submission; the full
> methodology, threat-model coding with supporting quotes, and analysis will be linked here after review.

## Contents

- [🛡️ Runtime Guardrails](#runtime-guardrails) (38)
- [💉 Prompt-Injection Mitigation](#prompt-injection-mitigation) (31)
- [📦 Isolation & Sandboxing](#isolation-sandboxing) (15)
- [🕸️ Graph-Based Monitoring](#graph-based-monitoring) (9)
- [✅ Formal Verification](#formal-verification) (11)
- [🗺️ Secure Planning](#secure-planning) (13)
- [❓ Uncertainty Quantification](#uncertainty-quantification) (4)
- [🎯 Conformal Prediction](#conformal-prediction) (4)
- [📚 Extended tier](extended.md) · [🧪 Benchmarks](benchmarks.md) · [🧭 Threat-model coding](threat-model.md)

**Legend** — *Guarantee*: what the mechanism itself provides (**bold** = holds by construction or
statistically, not by a model's judgment). *Adaptive eval.* ⚔️: the paper evaluates at least one attack
optimized against, or written with knowledge of, the defense.


<a name="runtime-guardrails"></a>
## 🛡️ Runtime Guardrails

*A monitor beside the agent judges actions, trajectories, or messages against a safety policy.*

| Paper | Venue | Guarantee | Adaptive eval. | What it does |
|---|---|---|:-:|---|
| [Adversarial Intent](https://arxiv.org/pdf/2602.21447) | Preprint '26 | probabilistic |  | Bayesian belief state via structured reasoning for trust. |
| [AgentChain](https://doi.org/10.1109/TDSC.2026.3685256 (abstract via OpenAlex; full text paywalled)) | TDSC '26 | probabilistic |  | Blockchain Proof-of-Content-Quality consensus and stake penalties replace centralized multi-agent QA orchestration; poisoning impact under 3%, backdoor/jailbreak success under 4% (eight datasets). |
| [AgentDoG](https://arxiv.org/pdf/2601.18491) | Preprint '26 | probabilistic |  | Fine-grained contextual monitoring, SOTA on R-Judge. |
| [AgentSpec](https://arxiv.org/abs/2503.18666) | ICSE '26 | **deterministic** |  | First DSL for customizable runtime enforcement, millisecond overhead. |
| [CognitiveGuard](https://aclanthology.org/2026.acl-long.954.pdf) | ACL '26 | probabilistic | ⚔️ | Diffusion purification of uploaded images at memory-write time plus counterfactual reasoning verifier at query time; goal-hit rate 85.1% to 9.7% on ShopBench-Agent. |
| [InfrastructureSentinel](https://ojs.aaai.org/index.php/AAAI/article/view/41468) | AAAI '26 | probabilistic |  | Guardian LLM enforces natural-language policies at input, tool-selection, execution-gating and audit layers for MCP agents; attack detection >85% with FPR under 10%. |
| [MATE](https://www.usenix.org/conference/usenixsecurity26/presentation/jiang-changyue) | USENIX Sec '26 | probabilistic |  | Policy-conditioned 0.5-3B auditor trained on 140K synthesized trajectories flags mobile-agent policy violations; over 95% accuracy on MATEBench at sub-100ms latency. |
| [MCP-Guard](https://aclanthology.org/2026.findings-acl.240.pdf) | ACL Find. '26 | probabilistic |  | Static scanner, fine-tuned E5 classifier (96.01% accuracy) and conditional LLM arbitrator cascade over MCP tool traffic; F1 95.4% on MCP-AttackBench. |
| [MemSAD](https://arxiv.org/abs/2605.03482) | Preprint '26 | **certified** | ⚔️ | Calibrated anomaly threshold with a certified detection radius rejects poisoned memory writes at ingestion; composite ASR 0 against three published memory attacks. |
| [MRT hybrid monitor](https://iclr.cc/virtual/2026/poster/10009049) | ICLR '26 | probabilistic | ⚔️ | Hybrid hierarchical-sequential trajectory monitoring lets weak LLMs catch stronger sabotaging agents; AUC above 0.85 with weak monitors on SHADE-Arena. |
| [OntoGuard](https://aclanthology.org/2026.findings-acl.1051.pdf) | ACL Find. '26 | **deterministic** |  | Admissibility rules mined offline from oracle demonstrations and LLM commonsense; graph constraint checker rejects invalid actions; ScienceWorld score 89.56 vs DGAP 85.91. |
| [OS-Sentinel](https://aclanthology.org/2026.acl-long.431/) | ACL '26 | probabilistic |  | Rule-based formal verifier over Android system-state traces plus VLM contextual judge flag unsafe GUI-agent steps; trajectory accuracy 57.1→73.0% on MobileRisk (Claude-4.5). |
| [Praetor](https://arxiv.org/pdf/2604.26274) | Preprint '26 | **deterministic** | ⚔️ | Compiles benign tool-call telemetry into a parameterized DFA enforced by an O(1) gateway; macro ASR 5.6% on Agent Security Bench. |
| [SafeMCP](https://aclanthology.org/2026.acl-long.522/) | ACL '26 | probabilistic |  | Server-side MCP plugin predicts next states with a learned world model and removes tools leading to unsafe states; ToolEmu safety 0.42→0.99 (GPT-4o). |
| [Safety Sidecar](https://aclanthology.org/2026.findings-acl.1542.pdf) | ACL Find. '26 | **deterministic** |  | Self-check router, reflective-memory repair exemplars and CodeQL/compilation verifier gate each artifact before release; secure-solution rate +2.9 to +11.2 points across eight CWEs. |
| [SentinelMem](https://aclanthology.org/2026.findings-acl.320.pdf) | ACL Find. '26 | probabilistic |  | Risk-aware self-evolving memory with reasoning-based extraction, dual-track profiling and state-machine updates; personalized safety rate +23.8% over best memory framework on PerMemSafe. |
| [ToolSafe](https://arxiv.org/pdf/2601.10156) | ACL Find. '26 | probabilistic |  | Per-step tool invocation monitoring. |
| [Trajectory Guard](https://arxiv.org/abs/2601.00516) | Preprint '26 | probabilistic |  | Siamese Recurrent Autoencoder for real-time trajectory validation. |
| [URLGuard](https://aclanthology.org/2026.findings-acl.716.pdf) | ACL Find. '26 | probabilistic |  | QLoRA-fine-tuned Llama-2-7B pre-detection module rejects disguised malicious URLs before the web agent visits them; cuts attack success 30-99% on MalURLBench. |
| [A-MemGuard](https://arxiv.org/pdf/2510.02373) | Preprint '25 | probabilistic |  | Consensus validation and dual memory against memory poisoning. |
| [AgentAuditor](https://arxiv.org/abs/2506.00641) | NeurIPS '25 | probabilistic | ⚔️ | Memory-augmented LLM judge retrieves past reasoning traces to label agent trajectories; 96.1% accuracy on R-Judge, matching human annotators on ASSEBench. |
| [AgentSentinel](https://arxiv.org/pdf/2509.07764) | CCS '25 | probabilistic | ⚔️ | Instrumented computer-use agent suspends sensitive system operations until an LLM auditor correlates task context with system traces; 79.6% defense success on BadComputerUse. |
| [AGrail](https://arxiv.org/abs/2502.11448) | ACL '25 | probabilistic |  | Lifelong adaptive guardrail with two cooperative LLMs; 0% ASR on Safe-OS but 17% average EIA. |
| [ALRPHFS](https://aclanthology.org/2025.findings-emnlp.1066.pdf) | EMNLP Find. '25 | probabilistic |  | Offline red-blue self-learning builds a risk-pattern library; online fast/slow reasoning screens queries and actions; 83.1% accuracy on ASB, 80% average across benchmarks. |
| [CONSECA](https://arxiv.org/abs/2501.17070) | HotOS '25 | probabilistic |  | Just-in-time contextual security policies enforced deterministically. |
| [DRIFT](https://arxiv.org/abs/2506.12104) | NeurIPS '25 | probabilistic | ⚔️ | Secure Planner + Dynamic Validator + Injection Isolator reduce ASR from 30.7% to 1.4%. |
| [GuardAgent](https://arxiv.org/abs/2406.09187) | ICML '25 | probabilistic |  | First LLM agent as guardrail, generating executable guardrail code with 98%+ accuracy. |
| [LlamaFirewall](https://arxiv.org/abs/2505.03574) | Preprint '25 | probabilistic |  | Multi-layer open-source guardrail (PromptGuard2 + AlignmentCheck + CodeShield). |
| [MASTER](https://aclanthology.org/2025.findings-emnlp.917.pdf) | EMNLP Find. '25 | probabilistic |  | Prompt-leakage detection, criticality-weighted hierarchical monitoring, and scenario-aware preemptive prompts for LLM multi-agent systems; ASR 77.1% to 6.5-9.0% at turn 8. |
| [MCIP](https://aclanthology.org/2025.emnlp-main.62.pdf) | EMNLP '25 | probabilistic |  | Fine-tuned guard model classifies MCP function-call trajectories against an 11-class risk taxonomy; risk identification 13.4% to 54.2% on MCIP-bench. |
| [Policy-as-Prompt](https://arxiv.org/pdf/2509.23994) | NeurIPS WS '25 | probabilistic |  | Policy documents to prompt-based classifiers. |
| [PSG-Agent](https://arxiv.org/pdf/2509.23614) | Preprint '25 | probabilistic |  | Personalized guardrails from user interaction history. |
| [RSP-Monitor](https://arxiv.org/pdf/2512.14448) | Preprint '25 | probabilistic |  | Reasoning-style derivative tracking, 0.94 AUROC. |
| [SafeInstructTool](https://aclanthology.org/2025.findings-emnlp.958.pdf) | EMNLP Find. '25 | probabilistic |  | SafeInstructTool scores tool-call risk across nine user-instruction, tool, and joint dimensions before execution; GPT-4o flags 83% of 1,200 risky SafeToolBench instructions. |
| [Safiron + AuraGen](https://arxiv.org/pdf/2510.09781) | Preprint '25 | probabilistic |  | Pre-execution guardrail trained on synthetic risky trajectories. |
| [ShieldAgent](https://arxiv.org/abs/2503.22738) | ICML '25 | probabilistic |  | Probabilistic rule circuits from policy documents for trajectory verification. |
| [PsySafe](https://arxiv.org/abs/2401.11880) | ACL '24 | probabilistic | ⚔️ | Doctor agent rewrites system prompts of agents failing a psychological test; police agent critiques outputs; joint danger rate 50→0% (AutoGen ablation). |
| [TrustAgent](https://arxiv.org/pdf/2402.01586) | EMNLP Find. '24 | probabilistic |  | Three-stage Agent Constitution for safe planning. |

<a name="prompt-injection-mitigation"></a>
## 💉 Prompt-Injection Mitigation

*Filters, detectors, provenance tracking, and by-construction architectures against injected instructions.*

| Paper | Venue | Guarantee | Adaptive eval. | What it does |
|---|---|---|:-:|---|
| [Adv-IMBIA](https://arxiv.org/abs/2511.18467) | AAAI '26 | probabilistic |  | Adversarial safety prompts in agent profiles or the user interface counter implicit malicious-behavior injection; ASR 93/45/71% cut by 73/40/49 on ChatDev/MetaGPT/AgentVerse. |
| [Agentic firewalls](https://arxiv.org/pdf/2502.01822) | TMLR '26 | **deterministic** |  | Inbound agent messages converted to a verified closed protocol, outbound data abstracted to task granularity; GPT-5 security ASR 60% to 3% (ConVerse). |
| [AttriGuard](https://www.usenix.org/conference/usenixsecurity26/presentation/he-yu) | USENIX Sec '26 | probabilistic | ⚔️ | Teacher-forced shadow replay under attenuated observations gates tool calls; 0% static and 6.6% adaptive ASR on AgentDojo (Gemini-2.5). |
| [ICON](https://arxiv.org/abs/2602.20708) | Preprint '26 | probabilistic | ⚔️ | Detects attention collapse from injection, performs targeted intervention. |
| [PACT](https://arxiv.org/pdf/2605.11039) | Preprint '26 | **deterministic** | ⚔️ | Runtime monitor binds role-specific trust contracts to tool arguments via cross-step provenance; 100% security on AgentDojo with 8-16pp more utility than CaMeL. |
| [RAP-ID](https://aclanthology.org/2026.findings-acl.738.pdf) | ACL Find. '26 | probabilistic |  | Train-free fusion of directive likeness, counterfactual attention gain and policy-conflict signals from one pre-fill pass; BIPIA TPR 98.62% at 1.35% Alpaca FPR. |
| [SPA](https://arxiv.org/abs/2608.27234) | Preprint '26 | **deterministic** |  | Plans once per query in a declarative DSL with dual-lattice information-flow control over labeled persistent artifacts; tool-knowledge attack success zero on AgentDojo. |
| [Tool Result Parsing](https://arxiv.org/abs/2601.04795) | Preprint '26 | probabilistic |  | Sanitizes tool outputs to essential data, lowest ASR on AgentDojo. |
| [Tool-Guard](https://arxiv.org/abs/2606.20922) | Preprint '26 | probabilistic | ⚔️ | Isolated planning quarantines tools whose invocations look misaligned, cutting cross-tool description-poisoning influence; ASR below 1.6% on AgentDojo with utility preserved. |
| [TraceGrant](https://arxiv.org/abs/2608.21126) | Preprint '26 | **deterministic** | ⚔️ | Compiles a task-effect contract from trusted request, authorizing effects and verifying completion; no attack successes across 949 AgentDojo and 400 ASB cases. |
| [VIGIL](https://aclanthology.org/2026.acl-long.443/) | ACL '26 | probabilistic |  | Speculative hypothesis trajectories are verified against user-intent constraints before any tool call commits; tool-stream ASR 73.8→8.1% on SIREN (Qwen3-max). |
| [BIPIA](https://arxiv.org/pdf/2312.14197) | KDD '25 | probabilistic |  | Comprehensive IPI benchmark with defense baselines. |
| [CaMeL](https://arxiv.org/abs/2503.18813) | Preprint '25 | **formal** |  | Capability-based access control with provable IPI security, 77% task completion. |
| [DataFilter](https://arxiv.org/pdf/2510.19207) | Preprint '25 | probabilistic |  | Model-agnostic fine-tuned filter strips injected instructions from data. |
| [DataSentinel](https://arxiv.org/pdf/2504.11358) | S&P '25 | — | ⚔️ | Game-theoretic minimax for robust injection detection. |
| [DefensiveTokens](https://arxiv.org/pdf/2507.07974) | AISec '25 | — | ⚔️ | Optimized token embeddings for security without weight changes. |
| [Design Patterns](https://arxiv.org/pdf/2506.08837) | Preprint '25 | **deterministic** |  | Six principled patterns for provable PI resistance. |
| [Firewall (Bhagwatkar)](https://arxiv.org/abs/2510.05244) | Preprint '25 | probabilistic | ⚔️ | Input Minimizer + Output Sanitizer achieves 0% ASR across four benchmarks. |
| [InstructDetector](https://arxiv.org/abs/2505.06311) | EMNLP Find. '25 | probabilistic |  | Hidden-state and gradient analysis for injection detection. |
| [IntentGuard](https://arxiv.org/abs/2512.00966) | Preprint '25 | probabilistic | ⚔️ | Thinking intervention on reasoning models reduces ASR from 100% to 8.5%. |
| [MELON](https://arxiv.org/abs/2502.05174) | ICML '25 | probabilistic |  | Masked re-execution compares tool calls with and without the user prompt to detect IPI. |
| [Memory vaccines](https://arxiv.org/abs/2502.19145) | AAAI '25 | probabilistic |  | Forged memories of safely refusing a malicious message and safety instructions curb multi-hop jailbreak spread; robustness 76.7→90.0% across five GPT models. |
| [Meta SecAlign](https://arxiv.org/pdf/2507.02735) | Preprint '25 | — | ⚔️ | First open-source LLM with built-in PI defense. |
| [PromptArmor](https://arxiv.org/abs/2507.15219) | Preprint '25 | probabilistic | ⚔️ | Guardrail LLM screening tool outputs with $<$1% FPR/FNR. |
| [SecAlign](https://arxiv.org/pdf/2410.05451) | CCS '25 | — | ⚔️ | DPO-based training for secure output preference. |
| [StruQ](https://arxiv.org/pdf/2402.06363) | USENIX '25 | — | ⚔️ | Structured queries separating prompts and data, ASR $<$2%. |
| [Task Shield](https://arxiv.org/pdf/2412.16682) | ACL '25 | probabilistic |  | Task-alignment checking of instructions and tool calls, 2.07% ASR on AgentDojo. |
| [TaskTracker](https://arxiv.org/pdf/2406.00799) | SaTML '25 | probabilistic | ⚔️ | Activation-delta probe detects task drift from injected data. |
| [Formalizing PI (Liu)](https://arxiv.org/pdf/2310.12815) | USENIX '24 | — |  | First systematic formalization of prompt injection + Open-Prompt-Injection benchmark. |
| [Instruction Hierarchy](https://arxiv.org/pdf/2404.13208) | Preprint '24 | probabilistic |  | Priority levels: system $>$ user $>$ data. |
| [Spotlighting](https://arxiv.org/abs/2403.14720) | CAMLIS '24 | — |  | Prompt engineering techniques reducing ASR from $>$50% to $<$2%. |

<a name="isolation-sandboxing"></a>
## 📦 Isolation & Sandboxing

*Privilege control, information-flow control, and execution isolation.*

| Paper | Venue | Guarantee | Adaptive eval. | What it does |
|---|---|---|:-:|---|
| [CaMeL-NOVA](https://arxiv.org/abs/2601.09923) | Preprint '26 | **deterministic** | ⚔️ | Trusted planner emits a complete branching plan before any untrusted observation, giving computer-use agents control-flow integrity; retains up to 57% of OSWorld utility. |
| [PCAS](https://arxiv.org/pdf/2602.16708) | Preprint '26 | **formal** |  | Policy compiler for policy-compliant-by-construction systems. |
| [Permission assistant](https://arxiv.org/pdf/2511.17959) | S&P '26 | probabilistic |  | Hybrid collaborative-filtering and in-context-learning model predicts users' data-access permission decisions for agent tools; 85.1% accuracy overall, 94.4% on high-confidence predictions (205-participant study). |
| [SAGA](https://www.ndss-symposium.org/wp-content/uploads/2026-s869-paper.pdf) | NDSS '26 | **formal** | ⚔️ | Provider-registered agents enforce user-defined contact policies via one-time keys and derived access tokens; ProVerif-verified, 0.165 s overhead on three agentic tasks. |
| [SEAgent](https://arxiv.org/abs/2601.11893) | Preprint '26 | **deterministic** |  | Mandatory access control against privilege escalation. |
| [SecureClaw](https://arxiv.org/abs/2606.09549) | Preprint '26 | **deterministic** | ⚔️ | Effect-sink PREVIEW-COMMIT authorization by trusted executor plus opaque-handle plaintext confinement at reads; 0% ASR on ASB, 0.64% on AgentDojo. |
| [ceLLMate](https://arxiv.org/abs/2512.12594) | Preprint '25 | **deterministic** |  | Browser-level sandbox with HTTP-layer interception. |
| [Fault-Tolerant Sandbox](https://arxiv.org/abs/2512.12806) | Preprint '25 | **deterministic** |  | Transactional filesystem snapshots with 100% rollback success. |
| [Fides](https://arxiv.org/abs/2505.23643) | Preprint '25 | **formal** |  | Formal IFC model with dynamic taint-tracking for agents. |
| [IsolateGPT](https://arxiv.org/abs/2403.04960) | NDSS '25 | **deterministic** |  | Hub-and-spoke architecture with dedicated LLM instances per app. |
| [Progent](https://arxiv.org/abs/2504.11703) | Preprint '25 | **deterministic** | ⚔️ | First privilege control DSL for LLM agents; ASR 39.9%→1.0% on AgentDojo. |
| [Prompt Flow Integrity](https://arxiv.org/pdf/2503.15547) | Preprint '25 | **deterministic** |  | Component isolation and privilege-escalation guardrails. |
| [RTBAS](https://arxiv.org/pdf/2502.08966) | Preprint '25 | **deterministic** |  | Information-flow control with dependency screeners for tool-based agents. |
| [AirGapAgent](https://arxiv.org/pdf/2405.05175) | CCS '24 | probabilistic |  | Minimizer LLM releases only task-necessary user data to the conversational agent; context-hijacking privacy 45% to 97% on Gemini Ultra at 89% utility. |
| [f-secure LLM](https://arxiv.org/pdf/2409.19091) | Preprint '24 | **formal** |  | Disaggregated pipeline with formal IFC guarantees. |

<a name="graph-based-monitoring"></a>
## 🕸️ Graph-Based Monitoring

*Agent traces and multi-agent communication modeled as graphs — learned monitors and enforced structure.*

| Paper | Venue | Guarantee | Adaptive eval. | What it does |
|---|---|---|:-:|---|
| [BlindGuard](https://arxiv.org/abs/2508.08127) | ACL '26 | probabilistic |  | Unsupervised GNN with corruption-guided contrastive detection. |
| [ControlValve](https://arxiv.org/pdf/2510.17276) | ICLR '26 | **deterministic** |  | CFG-based permitted control-flow for MAS. |
| [XG-Guard](https://arxiv.org/abs/2512.18733) | ACL '26 | probabilistic |  | Bi-level GNN with token-level attribution for explainable detection. |
| [AgentArmor](https://arxiv.org/abs/2508.01249) | Preprint '25 | **deterministic** |  | Agent traces as programs, PDGs with type system for security. |
| [G-Safeguard](https://arxiv.org/abs/2502.11127) | ACL '25 | probabilistic |  | First GNN defense for MAS using edge-featured utterance graphs. |
| [GUARDIAN](https://arxiv.org/abs/2505.19234) | NeurIPS '25 | probabilistic |  | Temporal attributed graph with Information Bottleneck for MAS. |
| [IPIGuard](https://arxiv.org/pdf/2508.15310) | EMNLP '25 | **deterministic** |  | Tool Dependency DAG decoupling planning from data. |
| [SentinelAgent](https://arxiv.org/abs/2505.24201) | Preprint '25 | probabilistic |  | Dynamic execution graphs with LLM-powered anomaly detection. |
| [TraceAegis](https://arxiv.org/abs/2510.11203) | Preprint '25 | probabilistic |  | Provenance-based hierarchical trace analysis. |

<a name="formal-verification"></a>
## ✅ Formal Verification

*Verified policies, temporal-logic monitors, and certified authorization.*

| Paper | Venue | Guarantee | Adaptive eval. | What it does |
|---|---|---|:-:|---|
| [CAGE](https://arxiv.org/abs/2607.29190) | Preprint '26 | **formal** | ⚔️ | Certifies tool-action authorization over a typed-return uncertainty neighborhood; certified false-allow 0.000, with an adaptive gate-aware attacker tested. |
| [FormalJudge](https://arxiv.org/pdf/2602.11136) | Preprint '26 | **formal** |  | Dafny+Z3 neuro-symbolic oversight; detects 72B-agent deception at over 90% accuracy. |
| [ProbGuard (Pro2Guard)](https://arxiv.org/abs/2508.00500) | ASE '26 | **certified** |  | PCTL model checking predicts unsafe states 38+ seconds ahead. |
| [ToolGate](https://aclanthology.org/2026.findings-acl.470.pdf) | ACL Find. '26 | **formal** |  | Hoare-style pre/postcondition contracts gate each tool call over a typed symbolic state; ToolBench G1 pass rate 85.5% with GPT-5.2, above ToolChain*. |
| [FM+LLM Roadmap](https://arxiv.org/pdf/2412.06512) | ICML Pos. '25 | — |  | Bidirectional roadmap for LLM-FM integration. |
| [Make Agent Defeat Agent](https://www.usenix.org/system/files/usenixsecurity25-liu-fengyu.pdf) | USENIX '25 | — |  | Automatic taint-style vulnerability detection in agents. |
| [Plan Verification](https://arxiv.org/pdf/2510.03469) | Preprint '25 | **formal** |  | NL plans to Kripke structures + LTL for model checking. |
| [Randomized Smoothing MAS](https://arxiv.org/pdf/2507.04105) | CJA '25 | **certified** |  | Probabilistic robustness certification for MAS consensus. |
| [VeriGuard](https://arxiv.org/pdf/2510.05156) | Preprint '25 | **formal** |  | Offline Nagini/Viper verification + runtime monitoring. |
| [VeriSafe Agent](https://arxiv.org/pdf/2503.18492) | MobiCom '25 | **deterministic** |  | Autoformalization to DSL with deterministic verification. |
| [Formal Security (Balunovi'c)](https://invariantlabs.ai/theme/research/ai_agents_with_formal_security.pdf) | ICML WS '24 | **formal** |  | Hard DSL-based constraints on actions before tool execution. |

<a name="secure-planning"></a>
## 🗺️ Secure Planning

*Safety reasoning moved into the planning step, before any action executes.*

| Paper | Venue | Guarantee | Adaptive eval. | What it does |
|---|---|---|:-:|---|
| [LCO](https://aclanthology.org/2026.findings-acl.1390.pdf) | ACL Find. '26 | probabilistic |  | Self-generated safety constraints plus LLM crossover/mutation over candidate actions curb in-context reward hacking; ToolEmu ICRH occurrence 31.69% to 6.99% (GPT-3.5). |
| [Preemptive hardening](https://arxiv.org/abs/2607.18847) | Preprint '26 | **deterministic** | ⚔️ | Pre-deployment pipeline scans and patches agent code with allowlists and schema tightening; 100% leakage reduction on basic attacks, 91% under stress. |
| [Prudentia](https://iclr.cc/virtual/2026/poster/10008186) | ICLR '26 | **deterministic** |  | IFC-aware planner atop FIDES treats policy compliance as planning objective; 0 ASR on WASP and 1.9x lower HITL load. |
| [SafeAgent](https://aclanthology.org/2026.acl-long.1501.pdf) | ACL '26 | probabilistic |  | Fine-tunes agents on simulator-generated risk scenarios (instruction, context, action sources) with reflective safe actions; +45.4% average sec@k on ToolEmu/SEDA. |
| [Safety-guided CoT](https://arxiv.org/abs/2410.17520) | AAAI '26 | probabilistic |  | Safety-guided chain-of-thought prompt makes device-control agents weigh risks before acting; refusal 6→36% on high-risk tasks, but only 3/50 injections resisted. |
| [SMALL](https://arxiv.org/pdf/2405.20018) | AAAI '26 | — |  | NL safety constraints as embeddings for multi-agent RL. |
| [Agent Safety via RL](https://arxiv.org/pdf/2507.08270) | Preprint '25 | probabilistic |  | RL training against adversary prompts and malicious outputs. |
| [CIP](https://aclanthology.org/2025.findings-acl.784/) | ACL Find. '25 | probabilistic |  | Agent builds a causal influence diagram from the task and refines it while acting; refusal +54% vs SCoT on MobileSafetyBench (GPT-4o). |
| [Self-reflection backdoor defense](https://aclanthology.org/2025.findings-emnlp.411.pdf) | EMNLP Find. '25 | probabilistic |  | DPO-based action-aware self-reflection fine-tuning against AgentGhost composite-trigger backdoors in mobile GUI agents; attack AMR 100% to 22.1% on AITZ, clean AMR 71.4%. |
| [SELP](https://arxiv.org/pdf/2409.19471) | ICRA '25 | **deterministic** |  | B"uchi automata constraining token generation. |
| [ToolSafety](https://aclanthology.org/2025.emnlp-main.714.pdf) | EMNLP '25 | probabilistic |  | Safety fine-tuning on 14,290 direct, indirect, and multi-step tool-use samples; LLaMA3.1-8B refusal 0.93 on indirect harm (ToolSword) with  45% BFCL helpfulness. |
| [Safety Chip](https://arxiv.org/abs/2309.09919) | ICRA '24 | **formal** |  | LTL automaton monitors LLM decisions, prunes unsafe actions. |
| [Formally Specifying (Crouse)](https://arxiv.org/abs/2310.08535) | Preprint '23 | **deterministic** |  | LTL-based constrained decoding for behavioral specifications. |

<a name="uncertainty-quantification"></a>
## ❓ Uncertainty Quantification

*Calibrated uncertainty gating a safety action: abstain, ask, halt, or block.*

| Paper | Venue | Guarantee | Adaptive eval. | What it does |
|---|---|---|:-:|---|
| [DreamPhase](https://iclr.cc/virtual/2026/poster/10011238) | ICLR '26 | probabilistic |  | Latent world-model imagination with uncertainty-aware value and safety gate;  5x fewer executed irreversible actions and 4x fewer API calls on WebShop. |
| [NEXUS](https://arxiv.org/abs/2607.19356) | Preprint '26 | probabilistic |  | Calibrated risk score over structured plan features gates allow, confirm, or block for tool-using agents; 0% ASR on its injection split at 99% benign allow. |
| [CURE](https://arxiv.org/abs/2510.08044) | NeurIPS '25 | probabilistic |  | Splits LLM plan uncertainty into task clarity, familiarity (random network distillation) and expected success; Spearman 0.454/0.635 with outcomes on kitchen/tabletop tasks. |
| [Selectively Quitting](https://arxiv.org/abs/2510.16492) | NeurIPS WS '25 | — |  | Agents withdraw when uncertain, +0.40 safety improvement. |

<a name="conformal-prediction"></a>
## 🎯 Conformal Prediction

*Distribution-free coverage guarantees on agent decisions.*

| Paper | Venue | Guarantee | Adaptive eval. | What it does |
|---|---|---|:-:|---|
| [CORA](https://arxiv.org/abs/2604.09155) | Preprint '26 | **calibrated** |  | Conformal risk control calibrates a mobile GUI agent's execute/abstain gate to a user-set harm budget; executed harm 2.4% against a 5% budget. |
| [Role-stratified CRC](https://arxiv.org/abs/2607.24343) | Preprint '26 | **calibrated** | ⚔️ | Per-field conformal risk control with a separate threshold and budget per argument role; 100% empirical budget compliance across shifted conditions on AgentDojo/InjecAgent. |
| [IntroPlan](https://arxiv.org/pdf/2402.06529) | NeurIPS '24 | **calibrated** |  | Introspective conformal planning with guaranteed act-or-ask probability. |
| [KnowNo](https://arxiv.org/pdf/2307.01928) | CoRL '23 | **calibrated** |  | Conformal prediction sets tell an LLM planner when to ask for help. |

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
