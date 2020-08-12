from maya_logger import MayaLogger


class PlayblastLogger(MayaLogger):
    
    LOGGER_NAME = "Playblast"
    
    
    
if __name__ == "__main__":

    PlayblastLogger.error("debug message")