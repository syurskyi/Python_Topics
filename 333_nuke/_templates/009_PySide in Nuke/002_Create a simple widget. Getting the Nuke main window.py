____ PySide.QtCore ______ *
____ PySide.QtGui ______ *


qnuke = QApplication.activeWindow()
print qnuke
w = ?W..()
w.s__

########################################################################################################################

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *


qnuke = QApplication.activeWindow()
print qnuke
w = ?W..(qnuke, Qt.Tool)
w.s__
w.c__

___ active():
    print QApplication.activeWindow()
QTimer.singleShot(2000, active)

########################################################################################################################

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *

app = QApplication.instance()
___ w __ app.topLevelWidgets():
    print w.windowTitle()

app = QApplication.instance()
___ w __ app.topLevelWidgets():
    print w.metaObject().className()


___ getNukeWindow():
    app = QApplication.instance()
    ___ w __ app.topLevelWidgets():
        __ w.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return w


qnuke = getNukeWindow()
qnuke.sQT..('Nuke')

########################################################################################################################

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *


w = ?W..(getNukeWindow(), Qt.Tool)
w.s__
w.c__

___ active():
    print QApplication.activeWindow()
QTimer.singleShot(2000, active)

########################################################################################################################

____ PySide.QtCore ______ *
____ PySide.QtGui ______ *


w = ?W..(getNukeWindow(), Qt.Tool)
w.s__
w.c__

___ active():
    w = ?W..(getNukeWindow(), Qt.Tool)
    w.s__
QTimer.singleShot(2000, active)