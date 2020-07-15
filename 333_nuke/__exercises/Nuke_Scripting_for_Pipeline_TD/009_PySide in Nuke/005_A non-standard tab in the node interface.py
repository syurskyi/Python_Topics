from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

def getMainWindow():
    app = QApplication.instance()
    for widget in app.topLevelWindow():
        if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget

qnuke = getMainWindow