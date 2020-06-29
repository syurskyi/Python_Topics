from PySide.QtCore import *
from PySide.QtGui import *

def getMainWindow():
    app = QApplication.instance()
    ___ widget __ app.topLevelWidgets():
        if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget

qnuke = getMainWindow()