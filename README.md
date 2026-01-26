# ⭐ Shunyaya Structural Number Theory (SSNT)

**Redefining Integers as Behavioral Structure, Not Just Classification**

![STARS](https://img.shields.io/badge/SSNT-STARS-green) ![Deterministic](https://img.shields.io/badge/Deterministic-Yes-green) ![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green)

**Deterministic • Integer Behavior • Structural Time • Fractures • Belts • Finite Alphabet • Observation-Only**

---

## 🔎 What Is SSNT?

Shunyaya Structural Number Theory (SSNT) is a deterministic framework that studies **how integers behave under structural pressure**, rather than only classifying them as prime, composite, or factorable.

Classical number theory answers:

- What divides `n`?
- Is `n` prime?
- How are primes distributed?

SSNT answers:

- How does `n` yield under closure pressure?
- How does the transition `n -> n+1` behave structurally?
- Where do fractures occur, and why do they cluster?
- Does the integer line contain belts (regional structure), not uniform randomness?
- Can integer behavior be expressed as a finite symbolic alphabet?

SSNT does not modify arithmetic or definitions.  
It introduces **structural observables** (time-like and event-like) that make integer transitions legible, compressible, and reproducible.

There are:

- no probabilistic assumptions  
- no training  
- no heuristics  
- no hidden state  

Everything is **deterministic**, **offline**, and **audit-friendly**.

---

## ✅ Minimal Public Release Layout (Review-Grade)

A clean SSNT public release contains exactly:

```

/SSNT
  ssnt_run_all.py
  SSNT_ALL_RUN_0001/
  docs/
    Quickstart.md
    FAQ.md

```

### Notes

- `ssnt_run_all.py` is the **single executable entry point**.
- `SSNT_ALL_RUN_0001/` is the **frozen, hash-verified canonical reference run**.
- All results described in the documentation correspond exactly to this run.
- Intermediate scripts and legacy run folders are intentionally excluded to prevent reviewer ambiguity.

---

## 🔗 Quick Links

### **Docs**
- [Concept Flyer (PDF)](docs/Concept-Flyer_SSNT_v1.8.pdf)
- [Full Specification (PDF)](docs/SSNT_ver1.8.pdf)
- [Documentation Scope & Canonical Range](docs/README.md)
- [Quickstart Guide](docs/Quickstart.md)
- [FAQ](docs/FAQ.md)

### **Core Entry Point**
- [`scripts/ssnt_run_all.py`](scripts/ssnt_run_all.py) — single deterministic master runner that reproduces the full SSNT pipeline

### **Canonical Reference Run**
- [`SSNT_ALL_RUN_0001/`](SSNT_ALL_RUN_0001/) — frozen, hash-verified empirical ground truth  
  (all documentation, claims, and figures correspond exactly to this run)

### **Empirical Outputs (Structured)**
- [`SSNT_ALL_RUN_0001/alphabet/`](SSNT_ALL_RUN_0001/alphabet/) — SSNT signature alphabet evolution
- [`SSNT_ALL_RUN_0001/belts/`](SSNT_ALL_RUN_0001/belts/) — structural belt detection
- [`SSNT_ALL_RUN_0001/epochs/`](SSNT_ALL_RUN_0001/epochs/) — corridor epochs & fracture clusters
- [`SSNT_ALL_RUN_0001/signature/`](SSNT_ALL_RUN_0001/signature/) — finite structural signature encoding
- [`SSNT_ALL_RUN_0001/ssnttfp/`](SSNT_ALL_RUN_0001/ssnttfp/) — rows, transitions, fractures, manifests

### **Manifests & Audit Records**
- [`SSNT_ALL_RUN_0001/SSNT_ALL_MANIFEST.csv`](SSNT_ALL_RUN_0001/SSNT_ALL_MANIFEST.csv) — master output manifest
- [`SSNT_ALL_RUN_0001/SSNT_ALL_META.json`](SSNT_ALL_RUN_0001/SSNT_ALL_META.json) — run metadata & parameter receipt

> All outputs are deterministic, offline, reproducible, and identical across machines when inputs match.

---

## 🎯 Problem Statement — Why Classical Views Miss Behavior

Classical number theory is extraordinarily powerful at proving facts and discovering distributions.

But it usually treats the integer line as:

- discrete  
- static  
- classification-driven  

It rarely asks whether integers exhibit **behavioral geography**, such as:

- calm corridors  
- clustered shock regimes  
- sparse fracture events  
- regional belts of structural turbulence  
- repeatable oscillatory signatures  

SSNT introduces a new observational layer:

**the behavior of transitions**, not only the identity of numbers.

---

## ⏱️ Structural Time on Integers (Core Idea)

For a given integer `n` (non-prime case), SSNT forms a structural time-like observable from the minimal closure depth:

- `d_min(n)` = smallest divisor `d >= 2` such that `d | n`
- `L(n) = floor(sqrt(n))`

Define (when `d_min(n)` is defined):

- `t_hat(n) = (d_min(n) - 2) / (L(n) - 1)`

Scaled integer form:

- `t_hat_1e6(n) = floor(t_hat(n) * 10^6)`

This produces a deterministic **structural-time coordinate** on the integer line.

---

## 🔁 Transitions, Corridors, and SHOCK

SSNT is transition-centric:

- `Delta_t_hat_1e6(n) = t_hat_1e6(n+1) - t_hat_1e6(n)`

Each transition is assigned a corridor label:

- **CALM**
- **NORMAL**
- **SHOCK**
- **UNDEFINED** (prime-involved or missing structural time)

Corridors are not narrative — they are **deterministic regimes** defined by explicit thresholds.

---

## 💥 Fractures (Event Structure)

A fracture is a transition where structural time changes sharply:

- `abs_delta = abs(Delta_t_hat_1e6(n))`

With run-explicit thresholds:

- `F_hat` (fracture threshold)
- `F_strong`
- `F_extreme`

Fracture classes are threshold-transparent and reproducible.

**Key behavioral finding:** fractures are sparse and structured — not uniform.

---

## 🧭 Belts & Epochs (Structural Geography)

SSNT introduces regional objects on the integer line.

**Belts**  
Persistent stretches of elevated fracture activity.  
Computed deterministically from fracture-density conditions within windows.

**Epochs**  
Temporal-like segmentation of the integer line, including:

- SHOCK_FREE epochs
- corridor epochs (CALM / NORMAL / SHOCK / UNDEFINED)
- FRACTURE_CLUSTER epochs

Integers do not vary only pointwise — they exhibit **regional and temporal structure**.

---

## 🧬 The SSNT Signature (Finite Behavioral Alphabet)

Each transition is compressed into a canonical signature:

- `SSNT_SIG(n) = <U, C, F, O, B>`

Where:

- `U` = undefined flag (prime-involved)
- `C` = corridor code
- `F` = fracture class
- `O` = oscillation flag (paired fracture behavior)
- `B` = belt-membership bitmask

This yields a **finite symbolic alphabet** of integer behavior.

---

## 🔐 A Finite Alphabet Hidden Inside Infinite Integers

SSNT reveals a strict and surprising compression of integer transition behavior.

Within the canonical SSNT reference run (`n <= 20000`), all observed integer transitions
collapse into exactly `54` distinct structural signatures.

This result is:
- deterministic
- executable
- reproducible across machines
- free of probability, heuristics, or learning

Signature discovery stabilizes rapidly in the canonical run:
- `n = 2000`  -> `14` signatures
- `n = 5000`  -> `27` signatures
- `n = 10000` -> `32` signatures
- `n = 15000` -> `53` signatures
- `n = 20000` -> `54` signatures

The integer line is infinite.
Its transition behavior is compressible.

SSNT’s core claim is not that `54` is universal,
but that integer behavior admits a finite, stabilizing structural alphabet
under deterministic observation.
The observed value `54` is a measured property of the canonical run.

Alphabet growth beyond the canonical range is an empirical question,
subject to further deterministic scanning.

---

## 🔍 Alphabet Evolution (Convergence)

SSNT measures how many distinct signatures appear as `n` grows.

Observed pattern:
- rapid signature discovery at small `n`
- long plateaus
- occasional late discoveries under extended ranges

This indicates that integer behavior under SSNT is compressible and bounded,
and that alphabet completion should be treated as an empirical convergence question
that depends on scan range, not as an assumed constant.

---

## ✅ Cross-Validation (Lens Robustness)

SSNT includes robustness checks using residue slicing:

- slice the integer line by `n mod m`
- compare fracture counts, corridor coherence, belt coverage
- verify invariants survive slicing

A strong lens example:

- `mod = 210 (2*3*5*7)`

Survival under strong lenses supports the conclusion that structure is **intrinsic**, not a scanning artifact.

---

## ▶️ Running SSNT (One Command)

From the project root:

`python ssnt_run_all.py --run-id RUN_0001 --n-max 20000`

This produces a single canonical run root containing:

- `ssnttfp/` (rows, transitions, fractures, top fractures, manifest)
- `epochs/` (corridor epochs + fracture cluster epochs)
- `belts/`
- `signature/`
- `alphabet/`
- master manifest + meta receipts

When parameters and inputs match, outputs match the frozen reference run `SSNT_ALL_RUN_0001/` exactly.

---

## ❄️ Determinism & Freeze Contract

For identical inputs and parameters:

- identical rows
- identical transitions
- identical fractures
- identical belts
- identical signatures
- identical alphabet evolution outputs

No randomness.  
No machine dependence.  
No hidden state.

SSNT behavior is frozen by **structure**, not by version number.

---

## 🚫 What SSNT Is Not

SSNT is not:

- a replacement for prime theory
- a conjecture engine
- a probabilistic model
- a learning system
- a numerology framework
- a heuristic pattern miner

It does not predict primes.  
It does not change arithmetic.

It **observes transition behavior**.

---

## 🧱 Structural Stability vs Structural Instability (Insight)

SSNT reveals a distinction that classical number theory usually leaves implicit:

**not all integer constructions are structurally compatible**.

In SSNT terms:

Some integers yield, transition, and resist closure in similar ways.  
Others — even when numerically close — occupy very different structural regimes.

As a result:

An integer construction `(a, b, c, d)` may be structurally stable.  
Replacing one element `(c -> c1)` can silently introduce instability — not because arithmetic fails, but because behavioral regimes mismatch.

This distinction is **observational**, not prescriptive.

SSNT does not claim how integers should be used.  
It reveals when substitutions preserve structural coherence — and when they do not.

This insight applies wherever integers act as **structural carriers**, not just values:
geometry, discrete design, encodings, and other deterministic systems.

---

## 🔍 Interpretation Boundaries

SSNT is an **observational mathematical framework**.

Terms such as *pressure*, *fracture*, and *shock* describe structural transition regimes, not physical forces.

Results are reproducible.  
Interpretation should remain within mathematics unless explicitly mapped to another domain.

---

## 📄 License & Attribution

**CC BY 4.0 — Public Research Release**

Attribution:  
**Shunyaya Structural Number Theory (SSNT)**  

Built within the broader **Shunyaya ecosystem**.

No Warranty.  
Provided “as is”, without warranty of any kind, express or implied.

---

## 🔗 Related Structural Mathematics (Optional Reference)

Shunyaya Structural Number Theory (SSNT) is a **standalone, executable framework**.

For readers interested in the broader context of **Structural Mathematics**, including symbolic foundations, universal structural observatories, and related domains, see:

- [Shunyaya Symbolic Mathematics — Master Documentation](https://github.com/OMPSHUNYAYA/Shunyaya-Symbolic-Mathematics-Master-Docs)

This reference is **not required** to understand, run, or validate SSNT.

---

## 🏷️ Topics

SSNT, Structural-Number-Theory, Integer-Behavior, Structural-Time, Fractures, Belts, Epochs, Modular-Cross-Validation, Deterministic-Mathematics, Finite-Alphabet, Shunyaya

