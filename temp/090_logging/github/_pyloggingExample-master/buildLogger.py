______ ?
______ Module

class setLogger():
    ___ __init__(self):
        # create logger with 'spam_application'
        logger _ ?.gL..('build.log')
        logger.sL..(?.D..)
        # create file handler which logs even d.. messages
        fh _ ?.FH..('TarihliBuild.log')
        fh.sL..(?.D..)
        # create console handler with a higher log level
        ch _ ?.SH..
        ch.sL..(?.ERROR)
        # create formatter and add it to the handlers
        formatter _ ?.F..('%(asctime)s - %(name)s - %(l..)s - %(funcName)s: %(m..)s')
        fh.sF..(formatter)
        ch.sF..(formatter)
        # add the handlers to the logger
        logger.aH..(fh)
        logger.aH..(ch)
        self.logger _ logger
    ___ gL..(self):
        return self.logger

if  -n == '__main__':
    sLog _ setLogger()
    logger _ sLog.gL..()
    
    logger.i..('Build Started...')
    a _ gingerModule.Copy().execute()
    b _ gingerModule.Delete().execute()
    logger.i..('Finish')
