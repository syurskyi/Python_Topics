# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget(flags=QtCore.Qt.Dialog)
window.setWindowTitle("Tooltips")
window.resize(300, 70)
button = QtGui.QPushButton("Close Window", window)
button.setFixedSize(150, 30)
button.move(75, 20)
button.setToolTip("This is a tooltip for the button.")
window.setToolTip("This is a tooltip for a window.")
button.setWhatsThis("This is the help for the button.")
window.setWhatsThis("This is the help for the window.")
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"),
                       QtGui.qApp, QtCore.SLOT("quit()"))
window.show()
sys.exit(app.exec_())