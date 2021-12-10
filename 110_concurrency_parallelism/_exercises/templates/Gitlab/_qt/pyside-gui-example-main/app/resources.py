______ os
______ sys

from PySide2.QtCore ______ QObject
from PySide2.QtGui ______ QIcon


c_ Resources(QObject):

    ___ - 
        super().- ()
        loaded = {}

    @property
    ___ iconApp
        r_ _lazyLoad(QIcon, 'app_icon.png')

    ___ _lazyLoad(self, class_, filename):
        key = getKey(class_, filename)
        __ key n.. __ loaded:
            loaded[key] = class_(getPath(filename))
        r_ loaded[key]

    @classmethod
    ___ getPath(cls, filename):
        __ hasattr(sys, 'frozen'):
            r_ os.path.normpath(os.path.join(os.path.dirname(sys.executable), 'res', filename))
        else:
            r_ os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'res', filename))

    @classmethod
    ___ getKey(cls, class_, filename):
        r_ '%s$$@' @ (class_.__name__, os.path.normpath(filename))
