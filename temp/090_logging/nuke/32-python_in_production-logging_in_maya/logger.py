______ ?
______ sys

class Logger(object):

    LOGGER_NAME _ "Zurbrigg"

    LEVEL_DEFAULT _ ?.D..
    PROPAGATE_DEFAULT _ True

    _logger_obj _ None


    @classmethod
    def logger_obj(cls):

        if not cls._logger_obj:
            if cls.logger_exists():
                cls._logger_obj _ ?.gL..(cls.LOGGER_NAME)
            else:
                cls._logger_obj _ ?.gL..(cls.LOGGER_NAME)

                cls._logger_obj.sL..(cls.LEVEL_DEFAULT)
                cls._logger_obj.propagate _ cls.PROPAGATE_DEFAULT

                fmt _ ?.F..("[%(name)s][%(l..)s] %(m..)s")

                stream_handler _ ?.StreamHandler(sys.stderr)
                stream_handler.sF..(fmt)
                cls._logger_obj.aH..(stream_handler)

        return cls._logger_obj

    @classmethod
    def logger_exists(cls):
        return cls.LOGGER_NAME in ?.Logger.manager.loggerDict.keys()

    @classmethod
    def set_level(cls, level):
        lg _ cls.logger_obj()
        lg.sL..(level)
        
    @classmethod
    def set_propagate(cls, propagate):
        lg _ cls.logger_obj()
        lg.propagate _ propagate

    @classmethod
    def d..(cls, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.d..(msg, *args, **kwargs)

    @classmethod
    def i..(cls, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.i..(msg, *args, **kwargs)

    @classmethod
    def warning(cls, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.warning(msg, *args, **kwargs)

    @classmethod
    def error(cls, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.error(msg, *args, **kwargs)

    @classmethod
    def critical(cls, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.critical(msg, *args, **kwargs)

    @classmethod
    def log(cls, level, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.log(level, msg, *args, **kwargs)

    @classmethod
    def exception(cls, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.exception(msg, *args, **kwargs)

    @classmethod
    def write_to_file(cls, path, level_?.WARNING):
        file_handler _ ?.FH..(path)
        file_handler.sL..(level)

        fmt _ ?.F..("[%(asctime)s][%(l..)s] %(m..)s")
        file_handler.sF..(fmt)

        lg _ cls.logger_obj()
        lg.aH..(file_handler)


if  -n == "__main__":
    
    Logger.set_propagate(False)

    Logger.d..("d.. m..")
    Logger.i..("i.. m..")
    Logger.warning("warning m..")
    Logger.error("error m..")
    Logger.critical("critical m..")







