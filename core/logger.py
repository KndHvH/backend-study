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
        
    def _get_log_format(self):
        return (
            "{time:YYYY-MM-DD HH:mm:ss} | "
            "{level:<8} | "
            "{file:<25}:{line:<4} | "
            "<cyan>{function:<25}</cyan> | "
            "{message}"
        )
        
    def _make_dir(self):
        os.makedirs(self.dir_name, exist_ok=True)
        
    def _configure_logger(self):
        self.logger.remove()

        # Não exibir logs no stdout durante os testes
        if settings.environment != "test":
            self.logger.add(
                sys.stdout,
                level="INFO",
                format=self._get_log_format(),
            )

        self.logger.add(
            f"{self.dir_name}/info.log",
            level="INFO",
            rotation="10 MB",
            retention="7 days",
            compression="zip",
            backtrace=False,
            diagnose=False,
            format=self._get_log_format(),
        )

        if settings.environment == "dev":
            self.logger.add(
                f"{self.dir_name}/debug.log",
                level="DEBUG",
                rotation="10 MB",
                retention="7 days",
                compression="zip",
                backtrace=True,
                diagnose=True,
                format=self._get_log_format(),
            )
            
app_logger = Logger(LOGS_DIR).logger