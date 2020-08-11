import logging
from logging.handlers import RotatingFileHandler

# Local params
ENABLE_DEBUG = True
INFO_LEVEL = 20
DEBUG_LEVEL = 10
ACTIVITY_LOG = "activity.log"
TRACE_LOG = "trace.log"

# Init logger
logger = logging.getLogger()

# Log format
log_format = logging.Formatter('%(asctime)s | %(name)s |  %(levelname)s: %(message)s')

# Set log level
logger.setLevel(logging.DEBUG)

# Setup handlers
activity_log_handler = RotatingFileHandler(
    filename=ACTIVITY_LOG, 
    maxBytes=1000000
)

activity_log_handler.setFormatter(log_format)
activity_log_handler.setLevel(INFO_LEVEL)

logger.addHandler(activity_log_handler)

if ENABLE_DEBUG:
    trace_log_handler = RotatingFileHandler(
        filename=TRACE_LOG, 
        maxBytes=1000000
    )

    trace_log_handler.setFormatter(log_format)
    trace_log_handler.setLevel(DEBUG_LEVEL)

    logger.addHandler(trace_log_handler)


# Examples
logger.info("TESTING INFO")
logger.warning("TESTING WARNING")
logger.error("TESTING ERROR !!!!!!")

try:
    int("sdfsdfsdfs")
except Exception as error:
    logger.error("Could not convert string to int")
    logger.debug(error)

