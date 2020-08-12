from logger ______ Logger


class MayaLogger(Logger):
    
    LOGGER_NAME _ "MayaLogger"
    
    FORMAT_DEFAULT _ "[%(l..)s][%(name)s] %(m..)s"
    
    PROPAGATE_DEFAULT _ False
    
    
if __name__ == "__main__":

    MayaLogger.debug("debug m..")
    MayaLogger.info("info m..")
    MayaLogger.warning("warning m..")
    MayaLogger.error("error m..")
    
    
    
    