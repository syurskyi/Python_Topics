# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_link_activated(link):
    print("activated", link)

def on_link_hovered(link):
    print("hovered", link)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QLabel")
window.resize(300, 150)
label = QtGui.QLabel()
label.setText("""<a href="http://google.ru/">Это гиперссылка 1</a>
<a href="http://bhv.ru/">Это гиперссылка 2</a>
""")
label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
label.linkActivated["const QString&"].connect(on_link_activated)
label.linkHovered["const QString&"].connect(on_link_hovered)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())