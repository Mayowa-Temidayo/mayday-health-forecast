from mayday.core.logger import logger


def test_logger_import():
    logger.info("Logger initialized successfully.")
    assert logger is not None
