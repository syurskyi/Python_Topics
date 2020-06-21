# The alternative is to send it directly to syslog. This is great for older operating systems that dont have systemd.
# In an ideal world this should be simple, but sadly, Python requires a bit more elaborate configuration to be able
# to send unicode log messages. Here is a sample implementation.
#
import logging
import logging.handlers
import os

class SyslogBOMFormatter(logging.Formatter):
    def format(self, record):
        result = super().format(record)
        return "ufeff" + result

handler = logging.handlers.SysLogHandler('/dev/log')
formatter = SyslogBOMFormatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

try:
    exit(main())
except Exception:
    logging.exception("Exception in main()")
    exit(1)