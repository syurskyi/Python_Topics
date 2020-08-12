______ sys
______ ?


___ create_logger():
    logger _ ?.gL..('The Silo')
    logger.handlers _ []

    handler _ ?.StreamHandler(stream_sys.stderr)
    formatter _ ?.F..(fmt_'%(name)s: %(asctime)s: '
                                      '%(l..)s: %(m..)s',
                                  datefmt_'%d/%m/%Y %I:%M:%S')
    handler.sF..(formatter)
    logger.aH..(handler)

    logger.sL..(?.I..)
    logger.propagate _ False
    return logger


logger _ create_logger()
