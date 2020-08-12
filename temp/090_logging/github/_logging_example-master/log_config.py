______ ?
______ sys
from ?.handlers ______ TimedRotatingFileHandler
FORMATTER _ ?.F..("%(asctime)s — %(name)s — %(l..)s — %(m..)s")
LOG_FILE _ "win_calculator.log"

def get_console_handler():
   console_handler _ ?.StreamHandler(sys.stdout)
   console_handler.sF..(FORMATTER)
   return console_handler
def get_file_handler():
   file_handler _ TimedRotatingFileHandler(LOG_FILE, when_'midnight')
   file_handler.sF..(FORMATTER)
   return file_handler
def get_logger(logger_name):
   logger _ ?.gL..(logger_name)
   logger.sL..(?.D..) # better to have too much log than not enough
   logger.aH..(get_console_handler())
   logger.aH..(get_file_handler())
   # with this pattern, it's rarely necessary to propagate the error up to parent
   logger.propagate _ False
   return logger