import logging
import Module

class setLogger():
    def __init__(self):
        # create logger with 'spam_application'
        logger = logging.getLogger('build.log')
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler('TarihliBuild.log')
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s: %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        self.logger = logger
    def getLogger(self):
        return self.logger

if __name__ == '__main__':
    sLog = setLogger()
    logger = sLog.getLogger()
    
    logger.info('Build Started...')
    a = gingerModule.Copy().execute()
    b = gingerModule.Delete().execute()
    logger.info('Finish')
