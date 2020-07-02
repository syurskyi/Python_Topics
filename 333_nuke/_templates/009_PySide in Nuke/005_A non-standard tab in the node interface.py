____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

___ getMainWindow():
    app = QApplication.instance()
    ___ widget __ app.topLevelWidgets():
        __ widget.metaObject().className() __ 'Foundry::UI::DockMainWindow':
            r_ widget

qnuke = getMainWindow()