from loguru import logger

from mayday.core.paths import LOGS_DIR

LOG_FILE = LOGS_DIR / "mayday.log"

logger.remove()

logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
    colorize=True,
)

logger.add(
    LOG_FILE,
    level="DEBUG",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    enqueue=True,
)

__all__ = ["logger"]
