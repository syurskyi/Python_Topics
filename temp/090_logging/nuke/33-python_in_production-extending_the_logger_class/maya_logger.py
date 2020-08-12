____ logger ______ Logger


c_ MayaLogger(Logger):
    
    LOGGER_NAME _ "MayaLogger"
    
    FORMAT_DEFAULT _ "[%(l..)s][%(name)s] %(m..)s"
    
    PROPAGATE_DEFAULT _ F..
    
    
__  -n __ "__main__":

    MayaLogger.d..("d.. m..")
    MayaLogger.i..("i.. m..")
    MayaLogger.w..("warning m..")
    MayaLogger.e..("error m..")
    
    
    
    