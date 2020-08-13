______ ?
______ ___

c_ Logger(object):

    LOGGER_NAME _ "Zurbrigg"

    FORMAT_DEFAULT _ "[%(name)s][%(l..)s] %(m..)s"

    LEVEL_DEFAULT _ ?.D..
    PROPAGATE_DEFAULT _ T..

    _logger_obj _ N..


    ??
    ___ logger_obj(cls):

        __ no. cls._logger_obj:
            __ cls.logger_exists():
                cls._logger_obj _ ?.gL..(cls.LOGGER_NAME)
            ____
                cls._logger_obj _ ?.gL..(cls.LOGGER_NAME)

                cls._logger_obj.sL..(cls.LEVEL_DEFAULT)
                cls._logger_obj.propagate _ cls.PROPAGATE_DEFAULT

                fmt _ ?.F..(cls.FORMAT_DEFAULT)

                stream_handler _ ?.StreamHandler(___.stderr)
                stream_handler.sF..(fmt)
                cls._logger_obj.aH..(stream_handler)

        r_ cls._logger_obj

    ??
    ___ logger_exists(cls):
        r_ cls.LOGGER_NAME __ ?.Logger.m__.lD__.k..

    ??
    ___ set_level(cls, level):
        lg _ cls.l..
        lg.sL..(level)
        
    ??
    ___ set_propagate(cls, propagate):
        lg _ cls.l..
        lg.propagate _ propagate

    ??
    ___ d..(cls, msg, @ @@:
        lg _ cls.l..
        lg.d..(msg, @ @@

    ??
    ___ i..(cls, msg, @ @@:
        lg _ cls.l..
        lg.i..(msg, @ @@

    ??
    ___ w..(cls, msg, @ @@:
        lg _ cls.l..
        lg.w..(msg, @ @@

    ??
    ___ e..(cls, msg, @ @@:
        lg _ cls.l..
        lg.e..(msg, @ @@

    ??
    ___ c..(cls, msg, @ @@:
        lg _ cls.l..
        lg.c..(msg, @ @@

    ??
    ___ log(cls, level, msg, @ @@:
        lg _ cls.l..
        lg.log(level, msg, @ @@

    ??
    ___ exception(cls, msg, @ @@:
        lg _ cls.l..
        lg.exception(msg, @ @@

    ??
    ___ write_to_file(cls, path, level_?.WARNING):
        file_handler _ ?.FH..(path)
        file_handler.sL..(level)

        fmt _ ?.F..("[%(a_t_)s][%(l..)s] %(m..)s")
        file_handler.sF..(fmt)

        lg _ cls.l..
        lg.aH..(file_handler)


__  -n __ "__main__":
    
    Logger.set_propagate(F..)

    Logger.d..("d.. m..")
    Logger.i..("i.. m..")
    Logger.w..("warning m..")
    Logger.e..("error m..")
    Logger.c..("c.. m..")







