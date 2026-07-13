from pathlib import Path

from mayday.preprocessing.environmental import EnvironmentalPreprocessor
from mayday.preprocessing.epidemiology import EpidemiologyPreprocessor
from mayday.preprocessing.io import (
    load_environmental,
    load_epidemiology,
    save_processed,
)
from mayday.preprocessing.merge import DatasetMerger
from mayday.preprocessing.temporal import TemporalAggregator


class PreprocessingPipeline:
    """
    Executes the complete preprocessing workflow.

    Workflow
    --------
    1. Load raw datasets.
    2. Clean epidemiological data.
    3. Clean environmental data.
    4. Aggregate environmental data to epidemiological weeks.
    5. Merge datasets.
    6. Save the processed dataset.
    """

    def run(self) -> Path:
        epidemiology = load_epidemiology()
        environmental = load_environmental()

        epidemiology = EpidemiologyPreprocessor().clean(
            epidemiology,
        )

        environmental = EnvironmentalPreprocessor().clean(
            environmental,
        )

        environmental = TemporalAggregator().aggregate(
            environmental,
        )

        merged = DatasetMerger().merge(
            epidemiology,
            environmental,
        )

        return save_processed(
            merged,
            "model_dataset.csv",
        )
