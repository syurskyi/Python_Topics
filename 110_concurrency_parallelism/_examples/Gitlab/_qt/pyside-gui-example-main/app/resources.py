import os
import sys

from PySide2.QtCore import QObject
from PySide2.QtGui import QIcon


class Resources(QObject):

    def __init__(self):
        super().__init__()
        self.loaded = {}

    @property
    def iconApp(self):
        return self._lazyLoad(QIcon, 'app_icon.png')

    def _lazyLoad(self, class_, filename):
        key = self.getKey(class_, filename)
        if key not in self.loaded:
            self.loaded[key] = class_(self.getPath(filename))
        return self.loaded[key]

    @classmethod
    def getPath(cls, filename):
        if hasattr(sys, 'frozen'):
            return os.path.normpath(os.path.join(os.path.dirname(sys.executable), 'res', filename))
        else:
            return os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'res', filename))

    @classmethod
    def getKey(cls, class_, filename):
        return '%s$$%s' % (class_.__name__, os.path.normpath(filename))
