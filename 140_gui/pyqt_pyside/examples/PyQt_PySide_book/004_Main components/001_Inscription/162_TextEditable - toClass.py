from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Class QLabel")
window.resize(300, 150)
label = QtGui.QLabel()
label.setText("This text possible to edit")
label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse |
                              QtCore.Qt.TextEditable)

vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)

