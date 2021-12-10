______ os
______ sys

from PySide2.QtCore ______ QObject
from PySide2.QtGui ______ QIcon


class Resources(QObject):

    ___ __init__(self):
        super().__init__()
        self.loaded = {}

    @property
    ___ iconApp(self):
        return self._lazyLoad(QIcon, 'app_icon.png')

    ___ _lazyLoad(self, class_, filename):
        key = self.getKey(class_, filename)
        if key not __ self.loaded:
            self.loaded[key] = class_(self.getPath(filename))
        return self.loaded[key]

    @classmethod
    ___ getPath(cls, filename):
        if hasattr(sys, 'frozen'):
            return os.path.normpath(os.path.join(os.path.dirname(sys.executable), 'res', filename))
        else:
            return os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'res', filename))

    @classmethod
    ___ getKey(cls, class_, filename):
        return '%s$$%s' % (class_.__name__, os.path.normpath(filename))
