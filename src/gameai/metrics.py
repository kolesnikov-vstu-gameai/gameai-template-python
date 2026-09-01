"""Сохранение метрик в results/ в воспроизводимом формате."""

import json
from datetime import datetime
from pathlib import Path

RESULTS = Path(__file__).resolve().parents[2] / "results"


def save_metrics(experiment: str, metrics: dict, config: dict | None = None) -> Path:
    out_dir = RESULTS / experiment
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = out_dir / f"{stamp}.json"
    path.write_text(
        json.dumps({"experiment": experiment, "config": config or {}, "metrics": metrics},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path
