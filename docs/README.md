# SSNT Documentation Scope Note

This folder contains the **canonical documentation** for  
**Shunyaya Structural Number Theory (SSNT)**.

All documents here describe a **deterministic, observational mathematical framework**
for studying **integer behavior under structural pressure**.

---

## Canonical Reference Run

All empirical claims in the current SSNT documentation correspond to a **single frozen reference run**:

- **Scan range:** `n <= 20000`
- **Run ID:** `SSNT_ALL_RUN_0001`
- **Execution:** deterministic, offline, reproducible
- **Verification:** parameter-explicit, hash-verifiable

When inputs and parameters match, outputs are **identical across machines**.

---

## Note on the Finite Structural Alphabet

Several documents refer to a **finite alphabet of integer transition behavior**.

**Canonical observation:**

- Within the verified reference scan (`n <= 20000`),
  integer transition behavior resolves into **54 distinct structural signatures**.

This value is:

- **empirical**, not assumed
- **deterministic**, not statistical
- **specific to the canonical scan range**

**Important clarification:**

SSNT’s core claim is **not** that `54` is a universal constant.

SSNT’s core claim is that:

> Integer behavior under deterministic structural observation  
> admits a **finite, stabilizing symbolic alphabet**.

Alphabet size beyond the canonical range is an **empirical question**
subject to further deterministic scanning.

Extended scans may:
- preserve the same alphabet, or
- introduce additional signatures slowly

Such outcomes do **not** affect the validity of the SSNT framework.

---

## Interpretation Discipline

SSNT is an **observational mathematical framework**.

- No probabilistic assumptions
- No learning or heuristics
- No prediction claims
- No modification of arithmetic

Terms such as *pressure*, *fracture*, *shock*, and *time*
describe **structural transition regimes**, not physical forces.

Interpretation should remain within mathematics unless explicitly mapped to another domain.

---

## Versioning Note

Current documents reflect **Public Research Release v1.8.1**.

Version `v1.8.1` is a **documentation clarification release** only.
It does **not** introduce new algorithms, parameters, scans, or empirical results.

- The canonical reference run remains **SSNT_ALL_RUN_0001**
- The scan range remains **n <= 20000**
- All reported empirical quantities (including the 54-signature alphabet) are unchanged

This update exists solely to improve:
- interpretive clarity
- scope discipline
- reviewer-facing precision

No empirical claims were modified, extended, or withdrawn.


---

## Summary

- SSNT studies **how integers behave when they move** (`n -> n+1`)
- All results are **deterministic and reproducible**
- The observed `54`-signature alphabet is **canonical-range evidence**, not a fixed constant
- The framework remains valid independent of future scan extensions

For execution, verification, and full empirical outputs,
refer to the project root and the canonical run directory.
