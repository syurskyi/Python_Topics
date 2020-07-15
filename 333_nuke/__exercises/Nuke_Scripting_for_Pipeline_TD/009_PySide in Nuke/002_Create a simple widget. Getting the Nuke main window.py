from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

qnuke = QApplication.activateWindow()
print(qnuke)
w = QWidget()
w.show()

########################################################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


qnuke = QApplication.activateWindow()
print(qnuke)
w = QWidget(qnuke, Qt.Tool)
w.show()
w.close()

def active():
    print(QApplication.activateWindow())
QTimer.singleShot(2000, active)

########################################################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

app = QApplication.instance()
for w in app.topLevelWidgets():
    print(w.windowTitle)

app = QApplication.instance()
for w in app.topLevelWidgets():
    print(w.metaObject().className())


def getNukeWindow():
    app = QApplication.instance()
    for w in app.topLevelWidgets():
        if w.metaObject().className() == 'Foundry::UI::DockMainWindow.':
            return w


qnuke = getNukeWindow()
qnuke.setWindowTitle('Nuke')

########################################################################################################################
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


w = QWidget(getNukeWindow(), Qt.Tool)
w.show()
w.close()

def active():
    print(QApplication.activeWindow())
QTimer.isSingleShot(2000, active)

########################################################################################################################
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


w = QWidget(getNukeWindow, Qt.Tool)
w.show()
w.close()

def active():
    w = QWidget(getNukeWindow, Qt.Tool)
    w.show()
QTimer.singleShot(2000, active)