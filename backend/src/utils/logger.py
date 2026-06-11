"""
Logging configuration for the DQ Validation Framework.
"""

import sys
from loguru import logger as loguru_logger
from src.config import settings


def setup_logger():
    """Configure logging for the application."""
    # Remove default handler
    loguru_logger.remove()

    # Add console handler
    loguru_logger.add(
        sys.stdout,
        level=settings.LOG_LEVEL,
        format="<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
        colorize=True,
    )

    # Add file handler
    loguru_logger.add(
        "logs/app.log",
        level=settings.LOG_LEVEL,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function} - {message}",
        rotation="500 MB",
        retention="7 days",
    )

    return loguru_logger


logger = setup_logger()