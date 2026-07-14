from pathlib import Path

from mayday.preprocessing.pipeline import PreprocessingPipeline


def test_pipeline_creation() -> None:
    """
    The preprocessing pipeline should be constructible.
    """

    pipeline = PreprocessingPipeline()

    assert pipeline is not None


def test_pipeline_run_returns_output_path() -> None:
    """
    Running the pipeline should return the path
    to the processed dataset.
    """

    pipeline = PreprocessingPipeline()

    output = pipeline.run()

    assert isinstance(output, Path)

    assert output.exists()

    assert output.name.startswith("modeling_dataset_v")

    assert output.suffix == ".csv"
