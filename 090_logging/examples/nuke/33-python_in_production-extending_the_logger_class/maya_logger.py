from logger import Logger


class MayaLogger(Logger):
    
    LOGGER_NAME = "MayaLogger"
    
    FORMAT_DEFAULT = "[%(levelname)s][%(name)s] %(message)s"
    
    PROPAGATE_DEFAULT = False
    
    
if __name__ == "__main__":

    MayaLogger.debug("debug message")
    MayaLogger.info("info message")
    MayaLogger.warning("warning message")
    MayaLogger.error("error message")
    
    
    
    