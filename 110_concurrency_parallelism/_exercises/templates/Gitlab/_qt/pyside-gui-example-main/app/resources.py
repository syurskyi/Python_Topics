______ os
______ sys

____ PySide2.QtCore ______ QObject
____ PySide2.QtGui ______ QIcon


c_ Resources(QObject):

    ___ - 
        s__().- ()
        loaded    # dict

    @property
    ___ iconApp
        r_ _lazyLoad(QIcon, 'app_icon.png')

    ___ _lazyLoad class_, filename):
        key = getKey(class_, filename)
        __ key n.. __ loaded:
            loaded[key] = class_(getPath(filename))
        r_ loaded[key]

    @classmethod
    ___ getPath(cls, filename):
        __ hasattr(sys, 'frozen'):
            r_ os.path.normpath(os.path.join(os.path.dirname(sys.executable), 'res', filename))
        ____
            r_ os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'res', filename))

    @classmethod
    ___ getKey(cls, class_, filename):
        r_ '%s$$@' @ (class_.__name__, os.path.normpath(filename))
