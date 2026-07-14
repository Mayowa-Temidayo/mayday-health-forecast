import time

import typer

from mayday.core.paths import PROCESSED_DATA_DIR
from mayday.datasets.io import DatasetIO
from mayday.features.builder import FeatureBuilder
from mayday.ingestion.pipeline import DataIngestionPipeline
from mayday.ingestion.sources.kaggle import KaggleDataSource
from mayday.ingestion.sources.nasa_power import NasaPowerDataSource
from mayday.ingestion.utils.downloader import Downloader
from mayday.preprocessing.pipeline import PreprocessingPipeline

app = typer.Typer(
    help="MayDay Health Forecast CLI",
    no_args_is_help=True,
)


@app.callback()
def main() -> None:
    """
    MayDay Health Forecast command line interface.
    """


def _header(title: str) -> float:
    """
    Display a command header and start a timer.
    """
    typer.secho(
        f"\n=== {title} ===",
        fg=typer.colors.CYAN,
        bold=True,
    )

    return time.perf_counter()


def _footer(
    elapsed: float,
) -> None:
    """
    Display completion information.
    """
    typer.echo()

    typer.secho(
        f"Completed in {elapsed:.2f} seconds.",
        fg=typer.colors.GREEN,
        bold=True,
    )


@app.command()
def ingest() -> None:
    """
    Download and prepare raw datasets.
    """

    start = _header("MayDay Health Forecast")

    sources = [
        KaggleDataSource(),
        NasaPowerDataSource(),
    ]

    downloader = Downloader(
        sources,
    )

    pipeline = DataIngestionPipeline(
        downloader,
    )

    files = pipeline.run()

    elapsed = time.perf_counter() - start

    typer.echo()

    typer.secho(
        "Prepared datasets:",
        fg=typer.colors.GREEN,
    )

    for file in files:
        typer.echo(f"  ✓ {file}")

    _footer(elapsed)


@app.command()
def preprocess() -> None:
    """
    Execute the preprocessing pipeline.
    """

    start = _header("Data Preprocessing")

    pipeline = PreprocessingPipeline()

    output = pipeline.run()

    elapsed = time.perf_counter() - start

    typer.echo()

    typer.secho(
        "Generated dataset:",
        fg=typer.colors.GREEN,
    )

    typer.echo(f"  ✓ {output}")

    _footer(elapsed)


@app.command()
def features() -> None:
    """
    Generate engineered features.
    """

    start = _header("Feature Engineering")

    dataset = DatasetIO.load(
        PROCESSED_DATA_DIR / "modeling_dataset_latest.csv",
    )

    pipeline = FeatureBuilder.build()

    engineered = pipeline.run(
        dataset,
    )

    output = PROCESSED_DATA_DIR / "feature_dataset_latest.csv"

    DatasetIO.save(
        dataframe=engineered,
        path=output,
    )

    elapsed = time.perf_counter() - start

    typer.echo()

    typer.secho(
        "Generated feature dataset:",
        fg=typer.colors.GREEN,
    )

    typer.echo(f"  ✓ {output}")

    _footer(elapsed)


if __name__ == "__main__":
    app()
