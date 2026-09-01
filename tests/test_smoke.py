from gameai.config import ExperimentConfig


def test_config_defaults():
    cfg = ExperimentConfig()
    assert cfg.seed == 42
    assert cfg.to_dict()["name"] == "baseline"
