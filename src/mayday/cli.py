import time

import typer

from mayday.ingestion.pipeline import DataIngestionPipeline
from mayday.ingestion.sources.kaggle import KaggleDataSource
from mayday.ingestion.sources.nasa_power import NasaPowerDataSource
from mayday.ingestion.utils.downloader import Downloader

app = typer.Typer(
    help="MayDay Health Forecast CLI",
    no_args_is_help=True,
)


@app.callback()
def main() -> None:
    """
    MayDay Health Forecast command line interface.
    """
    pass


@app.command()
def ingest() -> None:
    """
    Download and prepare datasets.
    """
    typer.secho(
        "\n=== MayDay Health Forecast ===",
        fg=typer.colors.CYAN,
        bold=True,
    )

    typer.echo("Starting ingestion...\n")

    start = time.perf_counter()

    sources = [
        KaggleDataSource(),
        NasaPowerDataSource(),
    ]

    downloader = Downloader(sources)

    pipeline = DataIngestionPipeline(downloader)

    files = pipeline.run()

    elapsed = time.perf_counter() - start

    typer.secho("Prepared datasets:", fg=typer.colors.GREEN)

    for file in files:
        typer.echo(f"  ✓ {file}")

    typer.echo()

    typer.secho(
        f"Ingestion completed in {elapsed:.2f} seconds.",
        fg=typer.colors.GREEN,
        bold=True,
    )


if __name__ == "__main__":
    app()
