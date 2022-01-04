_______ logging
____ typing _______ Callable



logger = logging.getLogger("pybites_logger")
DEBUG = logger.debug
INFO = logger.info
WARNING = logger.warning
ERROR = logger.error
CRITICAL = logger.critical


___ log_it(level: Callable, msg: s..) __ N..

       
    level(msg)




__ __name__ __ "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")
