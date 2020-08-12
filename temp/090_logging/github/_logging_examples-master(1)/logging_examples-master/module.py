______ ?
______ ?.config
______ submodule


?.config.fileConfig("logging.ini", disable_existing_loggers_False)
logger _ ?.gL..(__name__)


def bar():
    logger.warning("Calling bar")


def exc_logging():
    a, b _ 5, 0

    try:
        c _ a / b
    except ZeroDivisionError:
        logger.critical("Exception occurred", exc_info_True)


if __name__ == '__main__':
    bar()
    submodule.foo()
    exc_logging()
