from logger ______ Logger


c_ MayaLogger(Logger):
    
    LOGGER_NAME _ "MayaLogger"
    
    FORMAT_DEFAULT _ "[%(l..)s][%(name)s] %(m..)s"
    
    PROPAGATE_DEFAULT _ False
    
    
__  -n == "__main__":

    MayaLogger.d..("d.. m..")
    MayaLogger.i..("i.. m..")
    MayaLogger.warning("warning m..")
    MayaLogger.error("error m..")
    
    
    
    