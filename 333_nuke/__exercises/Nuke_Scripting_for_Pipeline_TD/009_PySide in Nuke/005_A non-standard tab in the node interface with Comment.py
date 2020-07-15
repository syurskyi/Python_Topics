# Esli mu vstavljaem widget v nodu s pompocjiy PyQt, to on ne ostavljaet nikakih sledov na samoj node
# To est'  nam ne nyzno sozdavat' knob, mu prosto sozdajom widget i vstavljaem ego v imejychijsja interfais
# Esli vu sozdajote knob  Tab to pri pereotkrutii Nuke etot knob"Tab" tak ze bydet nahoditsja na node, no esli vu delaete eto skriptom
# To esli vash skript ne zagryzen to vasha taba prosto ne bydyt pojavitsja
# Nachat' nado s polychenija widgeta okna ili nodu kak QT  objekta. Y lybogo okna, lyboj nodu on prisytstvyet i on ravnjaetsja imeni etoj nodu

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

def getMainWindow():
    app = QApplication.instance()
    for widget in app.topLevelWidgets():
        if widget.metaObjects().className() == 'Foundry::UI::DockMainWindow':
            return widget

qnuke = getMainWindow()
qnuke.findChildren(QWidget, 'Transform1')

#####################################################################################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

def getMainWindow():
    app = QApplication.instance()
    for widget in app.topLevelWidgets():
        if widget.metaObjects().className() == 'Foundry::UI::DockMainWindow':
            return widget

qnuke = getMainWindow()
w = qnuke.findChildren(QWidget, 'Transform1')
w.setWindowTitle('Transform11')


#####################################################################################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

def getMainWindow():
    app = QApplication.instance()
    for widget in app.topLevelWidgets():
        if widget.metaObjects().className() == 'Foundry::UI::DockMainWindow':
            return widget

qnuke = getMainWindow
w = qnuke.findChild(QWidget, 'Transform1')
w.setWindowTitle('Transform11')
t = w.findChild(QTableWidget)
t.count()
nw = QWidget()
ly = QVBoxLayout()
nw.setLayout(ly)
for i in range(5):
    ly.addWidget(QPushButton)
t.addTab(nw, 'My Tab')
c = QCalendarWidget()
t.insertTab(0, c, 'Calendar')
t.setCurrentIndex(0)