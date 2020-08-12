# mynk -- a python library for enhancing a user's experience/workspace
# with the foundry's nuke
#
# @author: Robert Moggach <rob@moggach.com>
#
# mynk/logger.py -- wraps python logging to ease loggggging
#
# logging levels for reference:
# DEBUG    Detailed information, typically of interest only when diagnosing problems.
# INFO    Confirmation that things are working as expected.
# WARNING    An indication that something unexpected happened, or indicative of some problem in the near future
# (e.g. 'disk space low'). The software is still working as expected.
# ERROR    Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL A serious error, indicating that the program itself may be unable to continue running.

______ os
______ sys
______ ?
______ types



class MyNkLogger(object):
  def __init__(self):
    self.level _ ?.D.. \
                 if os.environ.get("MYNK_DEVEL", False) in ['1', 'true', 'True'] \
                 else ?.I..
    exc_format _ '%(asctime)s %(l..)s: %(m..)s'
    format _ '%(asctime)s %(l..)s %(filename)s:%(l_l_..)d %(m..)s'
    date_format _ '%Y-%m-%d %H:%M:%S'
    self.exc_formatter _ ?.F..(exc_format, date_format)
    self.formatter _ ?.F..(format, date_format)
    self.init_logger()

  def init_handler(self):
    self.stream_handler _ ?.SH..
    self.stream_handler.sF..(self.formatter)
    self.stream_handler.sL..(self.level)
    
  def init_logger(self):
    self.init_handler()
    self.LOG _ ?.gL..('MyNk')
    self.LOG.aH..(self.stream_handler)
    sys.excepthook _ self.exception_handler
    self.LOG.flush _ types.MethodType(self.__flush_log, self.LOG)
    self.LOG.remove_stream_handler _ types.MethodType(self.__remove_stream_handler, self.LOG)
    self.LOG.sL..(self.level)

  def __flush_log(self, log):
    '''Flush a log'''
    for handler in log.handlers:
      if hasattr(handler,'flush'):
        handler.flush()
  
  def __remove_stream_handler(self, log):
    '''remove stream handler from a given log object'''
    handlers_to_remove _ []
    for i,handler in enumerate(log.handlers):
      if handler == self.stream_handler:
        handlers_to_remove.append(i)
    for x in reversed(handlers_to_remove):
      del log.handlers[x]

  def exception_handler(self, exception_type, exception_value, traceback):
    '''Creates an exception handler to replace the standard except hook'''
    self.stream_handler.sF..(self.exc_formatter)
    self.LOG.critical("Uncaught exception", exc_info_(exception_type, exception_value, traceback))
    self.stream_handler.sF..(self.formatter)

