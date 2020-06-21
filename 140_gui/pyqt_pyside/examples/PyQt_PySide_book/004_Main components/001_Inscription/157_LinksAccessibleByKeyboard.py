# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def on_link_activated(link):
    print(link)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Class QLabel")
window.resize(300, 150)
label = QtGui.QLabel()
label.setText("""<a href="http://google.ru/">Это гиперссылка 1</a>
<a href="http://bhv.ru/">Это гиперссылка 2</a>
""")
label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard)
label.linkActivated["const QString&"].connect(on_link_activated)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())