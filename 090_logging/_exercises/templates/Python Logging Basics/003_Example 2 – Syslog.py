# The alternative is to send it directly to syslog. This is great for older operating systems that dont have systemd.
# In an ideal world this should be simple, but sadly, Python requires a bit more elaborate configuration to be able
# to send unicode log messages. Here is a sample implementation.
#
______ l____
______ l____.handlers
______ os

class SyslogBOMFormatter(l____.Formatter):
    def format(self, record):
        result = super().format(record)
        return "ufeff" + result

handler = l____.handlers.SysLogHandler('/dev/log')
formatter = SyslogBOMFormatter(l____.BASIC_FORMAT)
handler.setFormatter(formatter)
root = l____.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

try:
    exit(main())
except Exception:
    l____.exception("Exception in main()")
    exit(1)