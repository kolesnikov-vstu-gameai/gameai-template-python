"""Пример эксперимента: замените тело функции run() на свою задачу."""

import random

from gameai.config import ExperimentConfig
from gameai.metrics import save_metrics


def run(cfg: ExperimentConfig) -> dict:
    rng = random.Random(cfg.seed)
    scores = [rng.random() for _ in range(cfg.n_runs)]
    return {"mean_score": sum(scores) / len(scores), "runs": cfg.n_runs}


if __name__ == "__main__":
    cfg = ExperimentConfig(name="baseline")
    metrics = run(cfg)
    path = save_metrics(cfg.name, metrics, cfg.to_dict())
    print(f"Сохранено: {path}\n{metrics}")
