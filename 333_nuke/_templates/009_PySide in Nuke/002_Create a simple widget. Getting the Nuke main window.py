from PySide.QtCore import *
from PySide.QtGui import *


qnuke = QApplication.activeWindow()
print qnuke
w = QWidget()
w.show()

########################################################################################################################

from PySide.QtCore import *
from PySide.QtGui import *


qnuke = QApplication.activeWindow()
print qnuke
w = QWidget(qnuke, Qt.Tool)
w.show()
w.close()

def active():
    print QApplication.activeWindow()
QTimer.singleShot(2000, active)

########################################################################################################################

from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication.instance()
___ w __ app.topLevelWidgets():
    print w.windowTitle()

app = QApplication.instance()
___ w __ app.topLevelWidgets():
    print w.metaObject().className()


def getNukeWindow():
    app = QApplication.instance()
    ___ w __ app.topLevelWidgets():
        if w.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return w


qnuke = getNukeWindow()
qnuke.setWindowTitle('Nuke')

########################################################################################################################

from PySide.QtCore import *
from PySide.QtGui import *


w = QWidget(getNukeWindow(), Qt.Tool)
w.show()
w.close()

def active():
    print QApplication.activeWindow()
QTimer.singleShot(2000, active)

########################################################################################################################

from PySide.QtCore import *
from PySide.QtGui import *


w = QWidget(getNukeWindow(), Qt.Tool)
w.show()
w.close()

def active():
    w = QWidget(getNukeWindow(), Qt.Tool)
    w.show()
QTimer.singleShot(2000, active)