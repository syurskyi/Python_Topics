from PySide2.QtWidgets import QApplication


class g(object):

    log = None
    r = None

    @classmethod
    def init(cls, log, r):
        cls.log = log
        cls.r = r

    @classmethod
    def app(cls):
        return QApplication.instance()
