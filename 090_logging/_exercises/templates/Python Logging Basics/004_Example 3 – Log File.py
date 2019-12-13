# The final option is to log messages directly to a file. This is rarely useful these days, as administrators can
# configure syslog to write certain messages to specific files, or if deploying inside containers,
# this is an anti-pattern. Also if you use centralized logging, having to deal with additional log files is an
# added concern. But it is an option that is still available.
#
# When logging to files, the main thing to be wary of is that log files need to be rotated regularly.
# The application needs to detect the log file being renamed and handle that situation. While Python provides its
# own file rotation handler, it is best to leave log rotation to dedicated tools such as logrotate.
# The WatchedFileHandler will keep track of the log file and reopen it if it is rotated, making it work well with
# logrotate without requiring any specific signals.
#
# Here is a sample implementation.

______ l____
______ l____.handlers
______ os

handler = l____.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", "/var/log/yourapp.log"))
formatter = l____.Formatter(l____.BASIC_FORMAT)
handler.setFormatter(formatter)
root = l____.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

try:
    exit(main())
except Exception:
    l____.exception("Exception in main()")
    exit(1)