"""
tools/sim_repliche.py

Ripete gli scenari del simulatore con semi diversi e riporta media e
deviazione standard delle frazioni usate nella tabella dei risultati del
simulatore (Capitolo 5).

Per ogni scenario:
  - bersagli: frazione di osservazioni (entita', passo) classificate
    ALERT o ENGAGE  -> TP / (TP + FN)
  - civili: frazione di osservazioni classificate ALERT o ENGAGE
    (falso allarme) -> FP / (FP + TN)

Esperimento 1: solo canale visivo (pesi 1 / 0 / 0).
Esperimento 2: pesi nominali di config.FUSION_WEIGHTS.

Il canale visivo legge R1 e R2 da outputs/metrics/vision_metrics.json,
come --run-sim.

Uso:
    python tools/sim_repliche.py                 # 20 semi (0..19), 150 passi
    python tools/sim_repliche.py --seeds 50 --steps 150
"""

import argparse
import os
import sys

import numpy as np

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _ROOT)
sys.path.insert(0, os.path.join(_ROOT, "src"))

from simulator import LAWSSim  # noqa: E402
from metrics import AttackScenario as S  # noqa: E402

CASI = [
    ("Esp. 1, solo visione, nessun attacco", S.BASELINE, True),
    ("Esp. 1, solo visione, contromisura", S.PATCH_ONLY, True),
    ("Esp. 2, nessun attacco", S.BASELINE, False),
    ("Esp. 2, contromisura", S.PATCH_ONLY, False),
    ("Esp. 2, contaminazione OSINT", S.OSINT_POISONING, False),
    ("Esp. 2, entrambi gli attacchi", S.CASCADING, False),
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", type=int, default=20)
    ap.add_argument("--steps", type=int, default=150)
    args = ap.parse_args()

    print(f"{args.seeds} repliche (semi 0..{args.seeds - 1}), {args.steps} passi\n")
    print(f"{'Scenario':40s} {'bersagli':>16s} {'civili':>16s}")
    for nome, scenario, solo_visione in CASI:
        bers, civ = [], []
        for seed in range(args.seeds):
            sim = LAWSSim(scenario=scenario, steps=args.steps, seed=seed)
            if solo_visione:
                sim.fusion.w = {"vision": 1.0, "osint": 0.0, "behavioral": 0.0}
            m = sim.run()
            bers.append(m.sensitivity)
            civ.append(m.fpr)
        b, c = np.array(bers), np.array(civ)
        print(f"{nome:40s} {b.mean():.3f} ± {b.std():.3f}   {c.mean():.3f} ± {c.std():.3f}")


if __name__ == "__main__":
    main()
