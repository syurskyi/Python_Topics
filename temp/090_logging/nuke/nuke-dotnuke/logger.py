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
# E.    Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL A serious error, indicating that the program itself may be unable to continue running.

______ __
______ ___
______ ?
______ types



c_ MyNkLogger(object):
  ___  -
    level _ ?.D.. \
                 __ __.environ.get("MYNK_DEVEL", F..) __ ['1', 'true', 'True'] \
                 else ?.I..
    exc_format _ '%(a_t_)s %(l..)s: %(m..)s'
    f.. _ '%(a_t_)s %(l..)s %(filename)s:%(l_l_..)d %(m..)s'
    date_format _ '%Y-%m-%d %H:%M:%S'
    exc_formatter _ ?.F..(exc_format, date_format)
    formatter _ ?.F..(f.., date_format)
    init_logger()

  ___ init_handler
    stream_handler _ ?.SH..
    stream_handler.sF..(formatter)
    stream_handler.sL..(level)
    
  ___ init_logger
    init_handler()
    LOG _ ?.gL..('MyNk')
    LOG.aH..(stream_handler)
    ___.excepthook _ exception_handler
    LOG.flush _ types.MethodType(__flush_log, LOG)
    LOG.remove_stream_handler _ types.MethodType(__remove_stream_handler, LOG)
    LOG.sL..(level)

  ___ __flush_log(, log):
    '''Flush a log'''
    ___ handler __ log.handlers:
      __ hasattr(handler,'flush'):
        handler.flush()
  
  ___ __remove_stream_handler(, log):
    '''remove stream handler from a given log object'''
    handlers_to_remove _ []
    ___ i,handler __ enumerate(log.handlers):
      __ handler __ stream_handler:
        handlers_to_remove.ap..(i)
    ___ x __ reversed(handlers_to_remove):
      del log.handlers[x]

  ___ exception_handler(, exception_type, exception_value, traceback):
    '''Creates an exception handler to replace the standard except hook'''
    stream_handler.sF..(exc_formatter)
    LOG.c..("Uncaught exception", exc_info_(exception_type, exception_value, traceback))
    stream_handler.sF..(formatter)

