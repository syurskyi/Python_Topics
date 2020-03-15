# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

def show_modal_window():
    global modalWindow
    modalWindow = QtGui.QWidget(window1, QtCore.Qt.Window)
    modalWindow.setWindowTitle("Modal Window")
    modalWindow.resize(200, 50)
    modalWindow.setWindowModality(QtCore.Qt.WindowModal)
    modalWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    modalWindow.move(window1.geometry().center() -
         modalWindow.rect().center() - QtCore.QPoint(4, 30))
    modalWindow.show()

app = QtGui.QApplication(sys.argv)
window1 = QtGui.QWidget()
window1.setWindowTitle("Usual Window")
window1.resize(300, 100)
button = QtGui.QPushButton("Open modal window")
QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"),
                       show_modal_window)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(button)
window1.setLayout(vbox)
window1.show()

window2 = QtGui.QWidget()
window2.setWindowTitle("This window will not be blocked when WindowModal")
window2.resize(500, 100)
window2.show()

sys.exit(app.exec_())