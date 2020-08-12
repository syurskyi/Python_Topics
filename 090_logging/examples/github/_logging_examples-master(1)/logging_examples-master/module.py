import logging
import logging.config
import submodule


logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def bar():
    logger.warning("Calling bar")


def exc_logging():
    a, b = 5, 0

    try:
        c = a / b
    except ZeroDivisionError:
        logger.critical("Exception occurred", exc_info=True)


if __name__ == '__main__':
    bar()
    submodule.foo()
    exc_logging()
