from mayday.core.settings import settings
from mayday.ingestion.kaggle import KaggleDataSource


def test_dataset_name():
    datasource = KaggleDataSource()

    assert datasource.dataset == settings.kaggle.dataset
