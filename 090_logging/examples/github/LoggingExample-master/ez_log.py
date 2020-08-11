import argparse
import logging
import sys


def parse_log_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    default_level = "INFO"
    parser.add_argument(
        "-l", "--loglevel",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default=default_level,
        help=f"Set the logging level (default: {default_level})")

    parser.add_argument(
        "-f", "--logfile",
        help="File for logging")
    
    parser.add_argument(
        "-ns", "--no_stdout", action="store_true",
        help="Whether to display logging on stdout")

    return parser


def conf_logging(logger: logging.Logger, loglevel: str,
                 no_stdout: bool, path=None) -> logging.Logger:

    if loglevel.upper() not in ("CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"):
        raise ValueError("Invalid logging level")

    if path is None and no_stdout:
        raise ValueError("No file output and no console?")

    if not no_stdout:
        console_formatter = logging.Formatter("[%(levelname)s] %(message)s")
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(console_formatter)
        logger.addHandler(handler)

    if path is not None:
        open(path, "w").close()

        file_formatter = logging.Formatter(
            ("%(asctime)s [%(levelname)s] %(name)s.%(funcName)s"
             "@ L%(lineno)d\n  %(message)s"))
        handler = logging.FileHandler(path, encoding="utf-8")
        handler.setFormatter(file_formatter)

    l_name = logging.getLevelName(loglevel)
    handler.setLevel(l_name)
    logger.setLevel(l_name)

    logger.addHandler(handler)

    return logger
