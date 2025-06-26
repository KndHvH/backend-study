import os
import sys

from loguru import logger

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    backtrace=True,
    diagnose=False,
    colorize=True,
)

logger.add(
    f"{LOGS_DIR}/info.log",
    level="INFO",
    rotation="1 MB",
    retention="7 days",
    compression="zip"
)

logger.add(
    f"{LOGS_DIR}/debug.log",
    level="DEBUG",
    rotation="1 MB",
    retention="5 days",
    compression="zip",
    backtrace=True,
    diagnose=True,
)
