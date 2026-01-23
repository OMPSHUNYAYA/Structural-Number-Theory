#!/usr/bin/env python3

import argparse
import csv
import hashlib
import json
import subprocess
from pathlib import Path
from datetime import datetime, timezone


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def run(cmd):
    print("RUN:", " ".join(cmd))
    subprocess.check_call(cmd)


def write_manifest(manifest_path, rows):
    with open(manifest_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["artifact", "path", "sha256"])
        for r in rows:
            w.writerow(r)


def pick_latest_tfp_run_dir(tfp_root: Path) -> Path:
    # SSNTTFP writes nested run dirs like: tfp_root/SSNTTFP_RUN_0001/...
    candidates = [p for p in tfp_root.iterdir() if p.is_dir() and p.name.startswith("SSNTTFP_RUN_")]
    if not candidates:
        raise SystemExit(f"No SSNTTFP_RUN_* directory found under: {tfp_root}")
    # deterministically pick highest by name
    candidates.sort(key=lambda p: p.name)
    return candidates[-1]


def find_single(pattern: str, base: Path) -> Path:
    matches = list(base.glob(pattern))
    if len(matches) != 1:
        raise SystemExit(f"Expected exactly 1 match for pattern '{pattern}' under {base}, found {len(matches)}")
    return matches[0]


def main():
    ap = argparse.ArgumentParser(description="SSNT Master Runner (deterministic)")
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--n-max", type=int, default=20000)
    args = ap.parse_args()

    run_id = args.run_id
    n_max = args.n_max

    root = Path.cwd()
    run_root = root / f"SSNT_ALL_{run_id}"
    run_root.mkdir(exist_ok=True)

    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")

    # ---- 1) SSNTTFP RUN ----
    tfp_root = run_root / "ssnttfp"
    tfp_root.mkdir(exist_ok=True)

    run([
        "python", "ssnt_structural_time_fp.py",
        "--n-max", str(n_max),
        "--out-dir", str(tfp_root)
    ])

    tfp_dir = pick_latest_tfp_run_dir(tfp_root)

    rows_csv = find_single("*__rows.csv", tfp_dir)
    transitions_csv = find_single("*__transitions.csv", tfp_dir)

    # ---- 2) EPOCHS ----
    epochs_dir = run_root / "epochs"
    epochs_dir.mkdir(exist_ok=True)

    run([
        "python", "ssnt_corridor_epochs.py",
        "--transitions", str(transitions_csv),
        "--out", str(epochs_dir)
    ])

    # ---- 3) BELTS ----
    belts_dir = run_root / "belts"
    belts_dir.mkdir(exist_ok=True)

    run([
        "python", "ssnt_belts_v1.py",
        "--rows", str(rows_csv),
        "--transitions", str(transitions_csv),
        "--out", str(belts_dir)
    ])

    belts_csv = belts_dir / "belts.csv"

    # ---- 4) SIGNATURE ----
    sig_dir = run_root / "signature"
    sig_dir.mkdir(exist_ok=True)

    run([
        "python", "ssnt_signature.py",
        "--transitions", str(transitions_csv),
        "--belts", str(belts_csv),
        "--out-dir", str(sig_dir),
        "--fracture-hat", "200000",
        "--fracture-extreme", "800000"
    ])

    sig_csv = sig_dir / "ssnt_signature.csv"

    # ---- 5) ALPHABET EVOLUTION ----
    alpha_dir = run_root / "alphabet"
    alpha_dir.mkdir(exist_ok=True)

    run([
        "python", "ssnt_alphabet_evolution.py",
        "--signature", str(sig_csv),
        "--cutoffs", "2000,5000,10000,15000,20000",
        "--out-dir", str(alpha_dir),
        "--top-k", "10"
    ])

    # ---- 6) MASTER MANIFEST ----
    manifest_rows = []
    artifacts = [
        rows_csv,
        transitions_csv,
        epochs_dir / "corridor_epochs.csv",
        epochs_dir / "fracture_cluster_epochs.csv",
        belts_csv,
        sig_csv,
        sig_dir / "ssnt_signature_manifest.json",
        alpha_dir / "ssnt_alphabet_evolution.csv",
        alpha_dir / "ssnt_alphabet_topk_by_cutoff.csv",
        alpha_dir / "ssnt_alphabet_evolution_manifest.json",
    ]

    for p in artifacts:
        manifest_rows.append([p.name, str(p.relative_to(run_root)), sha256_file(p)])

    write_manifest(run_root / "SSNT_ALL_MANIFEST.csv", manifest_rows)

    meta = {
        "run_id": run_id,
        "n_max": n_max,
        "timestamp_utc": ts,
        "ssnttfp_run_dir": str(tfp_dir.relative_to(run_root)),
    }

    with open(run_root / "SSNT_ALL_META.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    print("SSNT MASTER RUN COMPLETE")
    print("run_root =", run_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
