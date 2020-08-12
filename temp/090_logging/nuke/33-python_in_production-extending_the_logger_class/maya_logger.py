from logger ______ Logger


class MayaLogger(Logger):
    
    LOGGER_NAME _ "MayaLogger"
    
    FORMAT_DEFAULT _ "[%(l..)s][%(name)s] %(m..)s"
    
    PROPAGATE_DEFAULT _ False
    
    
if  -n == "__main__":

    MayaLogger.d..("d.. m..")
    MayaLogger.i..("i.. m..")
    MayaLogger.warning("warning m..")
    MayaLogger.error("error m..")
    
    
    
    