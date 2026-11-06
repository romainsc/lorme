"""Tests for batch size config."""

from lorme.config import LormeConfig
from lorme.ingest import get_batch_size


class TestBatchSizeConfig:
    def test_default(self):
        assert get_batch_size() == 32

    def test_from_config(self):
        cfg = LormeConfig(embedding_batch_size=32)
        assert get_batch_size(cfg) == 32

    def test_from_config_small(self):
        cfg = LormeConfig(embedding_batch_size=1)
        assert get_batch_size(cfg) == 1
