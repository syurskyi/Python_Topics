from PySide.QtCore import *
from PySide.QtGui import *

def getMainWindow():
    app = QApplication.instance()
    for widget in app.topLevelWidgets():
        if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget

qnuke = getMainWindow()