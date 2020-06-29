from PySide.QtCore ______ *
from PySide.QtGui ______ *

___ getMainWindow():
    app = QApplication.instance()
    ___ widget __ app.topLevelWidgets():
        __ widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget

qnuke = getMainWindow()