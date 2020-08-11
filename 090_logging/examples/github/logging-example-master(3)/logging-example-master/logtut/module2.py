import logging

logger = logging.getLogger(__name__)


def fn():
    logger.info("Running fn in module2.py")
    return 1
