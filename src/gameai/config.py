"""Единая точка конфигурации экспериментов."""

from dataclasses import asdict, dataclass


@dataclass
class ExperimentConfig:
    name: str = "baseline"
    seed: int = 42
    n_runs: int = 5

    def to_dict(self) -> dict:
        return asdict(self)
