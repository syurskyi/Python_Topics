
###############################################################################

# vsjo shto mu vidim v interfejse nodu eto setka

from PySide.QtCore import *
from PySide.QtGui import *

def getMainWindow():
    app = QApplication.instance()
    for widget in app.topLevelWidgets():
        if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget

qnuke = getMainWindow()
w = qnuke.findChild(QWidget, 'Transform1')
w.setWindowTitle('Transform11')
t = w.findChild(QTabWidget)
t.count()
nw = QWidget()
ly = QVBoxLayout()
nw.setLayout(ly)
for i in range(5):
    ly.addWidget(QPushButton())
t.addTab(nw, 'My Tab')
c = QCalendarWidget()
t.insertTab(0, c, 'Calendar')
t.setCurrentIndex(0)

###############################################

w = qnuke.findChild(QWidget, 'Transform1')
t = w.findChild(QTabWidget)
tw = t.widget(0)
gl = tw.children()[0]
gl.rowCount()
s = QSlider()
s.setOrientation(Qt.Horizontal)
gl.addWidget(s, 12, 1)
lb = QLabel('SYURSKYI')
gl.addWidget(lb, 12, 0, Qt.AlignRight)

###############################################

w = qnuke.findChild(QWidget, 'Transform1')
t = w.findChild(QTabWidget)
tw = t.widget(0)
gl = tw.children()[0]

w2 = QWidget()
w2.setLayout(gl)
ly = QVBoxLayout()
tw.setLayout(ly)
btn = QPushButton('SYURSKYI')
ly.addWidget(btn)
ly.addWidget(w2)
