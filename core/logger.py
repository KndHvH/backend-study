import os
import sys

from loguru import logger

from core.settings import settings

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)    

class Logger:
    def __init__(self, dir_name: str):
        self.logger = logger
        self.dir_name = dir_name
        self._make_dir()
        self._configure_logger()
        
    def _make_dir(self):
        os.makedirs(self.dir_name, exist_ok=True)
        
    def _configure_logger(self):
        self.logger.remove()

        self.logger.add(
            sys.stdout,
            level="INFO",
        )

        self.logger.add(
            f"{self.dir_name}/info.log",
            level="INFO",
            rotation="1 MB",
            retention="7 days",
            compression="zip",
            backtrace=False,
            diagnose=False,
        )

        if settings.environment == "dev":
            self.logger.add(
                f"{self.dir_name}/debug.log",
                level="DEBUG",
                rotation="1 MB",
                retention="5 days",
                compression="zip",
                backtrace=True,
                diagnose=True,
            )
            
app_logger = Logger(LOGS_DIR).logger