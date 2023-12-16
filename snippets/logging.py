"""
Python Logging Snippet

Description:
    This snippet provides the `Loggable` class, which can be inherited from to get a `log()` classmethod that returns a
    logger for the parent class. It also provides a `setup()` method that can be used to configure logging to file and
    console.


Dependencies:
    None (standard library only)

References:
    https://docs.python.org/3/library/logging.html
"""
import logging
import sys
from logging import handlers
from pathlib import Path


class Loggable:
    """Inherit from this class to get a `log()` classmethod that returns a logger for the parent class."""

    @staticmethod
    def setup(
            log_path: Path,
            console_log_level: int = logging.INFO,
            file_log_level: int = logging.DEBUG,
    ) -> None:
        """
        Setup logging to file and console.
        Uses a rotating file handler to limit log file size.
        Optionally, configure the logging levels for the console and file handlers.

        :param log_path: Path to log directory
        :param console_log_level: Log level for console logging
        :param file_log_level: log level for file logging

        """
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)

        # setup logging to file
        file_handler = logging.handlers.RotatingFileHandler(
            log_path, maxBytes=1000000, backupCount=5
        )
        file_handler.setLevel(file_log_level)
        root_logger.addHandler(file_handler)

        # setup logging to console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(console_log_level)
        root_logger.addHandler(console_handler)

    @property
    def logger(self) -> logging.Logger:
        """Returns a logger for the parent class."""
        return logging.getLogger(self.__class__.__name__)

    @classmethod
    def log(cls) -> logging.Logger:
        """Returns a logger for the parent class."""
        return logging.getLogger(cls.__name__)
