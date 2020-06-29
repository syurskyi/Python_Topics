from PySide.QtCore ______ *
from PySide.QtGui ______ *


qnuke = QApplication.activeWindow()
print qnuke
w = QWidget()
w.show()

########################################################################################################################

from PySide.QtCore ______ *
from PySide.QtGui ______ *


qnuke = QApplication.activeWindow()
print qnuke
w = QWidget(qnuke, Qt.Tool)
w.show()
w.close()

___ active():
    print QApplication.activeWindow()
QTimer.singleShot(2000, active)

########################################################################################################################

from PySide.QtCore ______ *
from PySide.QtGui ______ *

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
qnuke.setWindowTitle('Nuke')

########################################################################################################################

from PySide.QtCore ______ *
from PySide.QtGui ______ *


w = QWidget(getNukeWindow(), Qt.Tool)
w.show()
w.close()

___ active():
    print QApplication.activeWindow()
QTimer.singleShot(2000, active)

########################################################################################################################

from PySide.QtCore ______ *
from PySide.QtGui ______ *


w = QWidget(getNukeWindow(), Qt.Tool)
w.show()
w.close()

___ active():
    w = QWidget(getNukeWindow(), Qt.Tool)
    w.show()
QTimer.singleShot(2000, active)