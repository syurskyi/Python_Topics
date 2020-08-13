______ ?
______ ___

c_ Logger(object):

    LOGGER_NAME _ "Zurbrigg"

    LEVEL_DEFAULT _ ?.D..
    PROPAGATE_DEFAULT _ T..

    _logger_obj _ None


    @classmethod
    ___ logger_obj(cls):

        __ no. cls._logger_obj:
            __ cls.logger_exists():
                cls._logger_obj _ ?.gL..(cls.LOGGER_NAME)
            ____
                cls._logger_obj _ ?.gL..(cls.LOGGER_NAME)

                cls._logger_obj.sL..(cls.LEVEL_DEFAULT)
                cls._logger_obj.propagate _ cls.PROPAGATE_DEFAULT

                fmt _ ?.F..("[%(name)s][%(l..)s] %(m..)s")

                stream_handler _ ?.StreamHandler(___.stderr)
                stream_handler.sF..(fmt)
                cls._logger_obj.aH..(stream_handler)

        r_ cls._logger_obj

    @classmethod
    ___ logger_exists(cls):
        r_ cls.LOGGER_NAME __ ?.Logger.manager.loggerDict.keys()

    @classmethod
    ___ set_level(cls, level):
        lg _ cls.logger_obj()
        lg.sL..(level)
        
    @classmethod
    ___ set_propagate(cls, propagate):
        lg _ cls.logger_obj()
        lg.propagate _ propagate

    @classmethod
    ___ d..(cls, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.d..(msg, *args, **kwargs)

    @classmethod
    ___ i..(cls, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.i..(msg, *args, **kwargs)

    @classmethod
    ___ w..(cls, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.w..(msg, *args, **kwargs)

    @classmethod
    ___ e..(cls, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.e..(msg, *args, **kwargs)

    @classmethod
    ___ c..(cls, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.c..(msg, *args, **kwargs)

    @classmethod
    ___ log(cls, level, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.log(level, msg, *args, **kwargs)

    @classmethod
    ___ exception(cls, msg, *args, **kwargs):
        lg _ cls.logger_obj()
        lg.exception(msg, *args, **kwargs)

    @classmethod
    ___ write_to_file(cls, path, level_?.WARNING):
        file_handler _ ?.FH..(path)
        file_handler.sL..(level)

        fmt _ ?.F..("[%(a_t_)s][%(l..)s] %(m..)s")
        file_handler.sF..(fmt)

        lg _ cls.logger_obj()
        lg.aH..(file_handler)


__  -n __ "__main__":
    
    Logger.set_propagate(F..)

    Logger.d..("d.. m..")
    Logger.i..("i.. m..")
    Logger.w..("warning m..")
    Logger.e..("error m..")
    Logger.c..("c.. m..")







