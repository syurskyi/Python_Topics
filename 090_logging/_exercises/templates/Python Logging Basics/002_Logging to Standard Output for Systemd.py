# This is the simplest and probably the best option for configuring logging these days. When using systemd to run
# a daemon, applications can just send log messages to stdout or stderr and have systemd forward the messages
# to journald and syslog. As an additional perk, this does not even require catching exceptions, as Python already
# writes those to standard error. That said, follow proper convention and handle your exceptions.
#
# In the case of running Python in containers like Docker, logging to standard output is also often the easiest move
# as this output can be directly and easily managed by the container itself.

______ l____
______ os

l____.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

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

______ l____
______ os


class OneLineExceptionFormatter(l____.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)

    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace("\n", "")
        return result


handler = l____.StreamHandler()
formatter = OneLineExceptionFormatter(l____.BASIC_FORMAT)
handler.setFormatter(formatter)
root = l____.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

try:
    exit(main())
except Exception:
    l____.exception("Exception in main(): ")
    exit(1)