______ ?

____ PySide2 ______ QtCore

____ logger ______ Logger


c_ QtSignaler(QtCore.QObject):
    message_logged _ QtCore.Signal(str)


c_ QtSignalHandler(?.Handler):

    ___  - (, @ @@:
        s___(QtSignalHandler, ). - (@ @@
        emitter _ QtSignaler()

    ___ emit(, record):
        msg _ f..(record)
        emitter.message_logged.emit(msg)


c_ QtLogger(Logger):

    LOGGER_NAME _ "QtZurbrigg"

    _signal_handler _ N..

    ??
    ___ logger_obj(___):
        __ no. ___.l_e..
            fmt _ ?.F..("[%(l..)s] %(m..)s")

            ___._signal_handler _ QtSignalHandler()
            ___._signal_handler.sF..(fmt)

            logger_obj _ s___(QtLogger, ___).l..
            logger_obj.aH..(___._signal_handler)

        r_ s___(QtLogger, ___).l..

    ??
    ___ signal_handler(___):
        ___.l..
        r_ ___._signal_handler



__  -n __ "__main__":

    QtLogger.e..("error m..")
