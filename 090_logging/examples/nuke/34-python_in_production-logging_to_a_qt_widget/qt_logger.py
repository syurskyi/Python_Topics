import logging

from PySide2 import QtCore

from logger import Logger


class QtSignaler(QtCore.QObject):
    message_logged = QtCore.Signal(str)


class QtSignalHandler(logging.Handler):

    def __init__(self, *args, **kwargs):
        super(QtSignalHandler, self).__init__(*args, **kwargs)
        self.emitter = QtSignaler()

    def emit(self, record):
        msg = self.format(record)
        self.emitter.message_logged.emit(msg)


class QtLogger(Logger):

    LOGGER_NAME = "QtZurbrigg"

    _signal_handler = None

    @classmethod
    def logger_obj(cls):
        if not cls.logger_exists():
            fmt = logging.Formatter("[%(levelname)s] %(message)s")

            cls._signal_handler = QtSignalHandler()
            cls._signal_handler.setFormatter(fmt)

            logger_obj = super(QtLogger, cls).logger_obj()
            logger_obj.addHandler(cls._signal_handler)

        return super(QtLogger, cls).logger_obj()

    @classmethod
    def signal_handler(cls):
        cls.logger_obj()
        return cls._signal_handler



if __name__ == "__main__":

    QtLogger.error("error message")
