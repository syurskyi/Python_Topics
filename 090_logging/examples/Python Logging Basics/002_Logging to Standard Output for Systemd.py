# This is the simplest and probably the best option for configuring logging these days. When using systemd to run
# a daemon, applications can just send log messages to stdout or stderr and have systemd forward the messages
# to journald and syslog. As an additional perk, this does not even require catching exceptions, as Python already
# writes those to standard error. That said, follow proper convention and handle your exceptions.
#
# In the case of running Python in containers like Docker, logging to standard output is also often the easiest move
# as this output can be directly and easily managed by the container itself.

import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

# exit(main())
# That is it. The application will now log all messages with level INFO or above to stderr, using a simple format:
#
# ERROR:the.module.name:The log message
#
# The application can even be configured to include DEBUG messages, or maybe only ERROR, by setting the LOGLEVEL
# environment variable.
# The only problem with this solution is that exceptions are logged as multiple lines, which can cause problems
# for later analysis. Sadly, configuring Python to send multi-line exceptions as a single line is not quite as simple,
# but certainly possible. Note the implementation here below, calling logging.exception is shorthand equivalent
# to logging.error(..., exc_info=True).

import logging
import os


class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)

    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace("\n", "")
        return result


handler = logging.StreamHandler()
formatter = OneLineExceptionFormatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

try:
    exit(main())
except Exception:
    logging.exception("Exception in main(): ")
    exit(1)