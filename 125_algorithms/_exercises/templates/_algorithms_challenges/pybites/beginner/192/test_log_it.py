_______ logging

_______ p__

____ log_it _______ CRITICAL, DEBUG, ERROR, INFO, WARNING, log_it

LOG_LEVEL = {
    "debug": DEBUG,
    "info": INFO,
    "warning": WARNING,
    "error": ERROR,
    "critical": CRITICAL,
}


___ test_callable_log_levels
    ___ level __ LOG_LEVEL:
        ... callable(LOG_LEVEL[level])

 
?p__.m__.p.(
    "msg, level",
    [
        ("This is a debug message", "debug"),
        ("This is an info message", "info"),
        ("This is a warning message", "warning"),
        ("This is an error message", "error"),
        ("This is a critical message", "critical"),
    ],
)
___ test_log_it(msg, level, caplog):
    caplog.set_level(logging.DEBUG)
    log_it(LOG_LEVEL[level], msg)
    ... l..(caplog.records) __ 1
    ___ record __ caplog.records:
        ... record.levelname __ level.u..
        ... record.message __ msg
        ... record.name __ "pybites_logger"


___ test_wrong_log_level(caplog):
    msg = "This is a warning message"
    caplog.set_level(logging.ERROR)
    log_it(WARNING, msg)
    ... l..(caplog.records) __ 0

    caplog.set_level(logging.ERROR)
    msg = "This is an error message"
    log_it(ERROR, msg)
    ... l..(caplog.records) __ 1
    ___ record __ caplog.records:
        ... record.levelname __ "ERROR"
        ... record.message __ msg
        ... record.name __ "pybites_logger"