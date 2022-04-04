_______ logging
____ t___ _______ Callable

logger = logging.getLogger('pybites_logger')
DEBUG = l.... x: logger.log(logging.DEBUG, x)
INFO = l.... x: logger.log(logging.INFO, x)
WARNING = l.... x: logger.log(logging.WARNING, x)
ERROR = l.... x: logger.log(logging.ERROR, x)
CRITICAL = l.... x: logger.log(logging.CRITICAL, x)


___ log_it(level: Callable, msg: s..) __ N..
    level(msg)


__ _______ __ _______
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")
