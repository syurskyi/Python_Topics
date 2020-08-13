______ ?
______ ___

c_ Logger(object):

    LOGGER_NAME _ "Zurbrigg"

    FORMAT_DEFAULT _ "[%(name)s][%(l..)s] %(m..)s"

    LEVEL_DEFAULT _ ?.D..
    PROPAGATE_DEFAULT _ T..

    _logger_obj _ N..


    ??
    ___ logger_obj(___):

        __ no. ___.?:
            __ ___.l_e..
                ___.? _ ?.gL..(___._N..)
            ____
                ___.? _ ?.gL..(___._N..)

                ___.?.sL..(___.L..)
                ___.?.propagate _ ___.P..

                fmt _ ?.F..(___.F..)

                stream_handler _ ?.SH..(___.s_e..)
                stream_handler.sF..(fmt)
                ___.?.aH..(stream_handler)

        r_ ___.?

    ??
    ___ logger_exists(___):
        r_ ___._N.. __ ?.Logger.m__.lD__.k..

    ??
    ___ set_level(___, level):
        lg _ ___.l..
        lg.sL..(level)
        
    ??
    ___ set_propagate(___, propagate):
        lg _ ___.l..
        lg.propagate _ propagate

    ??
    ___ d..(___, msg, @ @@:
        lg _ ___.l..
        lg.d..(msg, @ @@

    ??
    ___ i..(___, msg, @ @@:
        lg _ ___.l..
        lg.i..(msg, @ @@

    ??
    ___ w..(___, msg, @ @@:
        lg _ ___.l..
        lg.w..(msg, @ @@

    ??
    ___ e..(___, msg, @ @@:
        lg _ ___.l..
        lg.e..(msg, @ @@

    ??
    ___ c..(___, msg, @ @@:
        lg _ ___.l..
        lg.c..(msg, @ @@

    ??
    ___ log(___, level, msg, @ @@:
        lg _ ___.l..
        lg.log(level, msg, @ @@

    ??
    ___ exception(___, msg, @ @@:
        lg _ ___.l..
        lg.exception(msg, @ @@

    ??
    ___ write_to_file(___, path, level_?.WARNING):
        file_handler _ ?.FH..(path)
        file_handler.sL..(level)

        fmt _ ?.F..("[%(a_t_)s][%(l..)s] %(m..)s")
        file_handler.sF..(fmt)

        lg _ ___.l..
        lg.aH..(file_handler)


__  -n __ "__main__":
    
    Logger.set_propagate(F..)

    Logger.d..("d.. m..")
    Logger.i..("i.. m..")
    Logger.w..("warning m..")
    Logger.e..("error m..")
    Logger.c..("c.. m..")







