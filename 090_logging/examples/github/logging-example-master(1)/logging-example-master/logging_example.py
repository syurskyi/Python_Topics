import logging
import os
import datetime


normalLogger = logging.getLogger('normalLogger')

def SetupLogger(loggerName, filename):
    path = 'C:\\my_project\\logs'
    if not os.path.exists(path):
        os.makedirs(path)

    logger = logging.getLogger(loggerName)

    logfilename = datetime.datetime.now().strftime(filename)
    logfilename = os.path.join(path, logfilename)
    
    logformatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
    fileHandler = logging.FileHandler(logfilename, 'a', 'utf-8')
    fileHandler.setFormatter(logformatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(logformatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)



def some_function():
    normalLogger.debug('this is somethimg want to record')
    

if __name__ == '__main__':
    SetupLogger('normalLogger', "%Y-%m-%d.log")
    some_function()
    
