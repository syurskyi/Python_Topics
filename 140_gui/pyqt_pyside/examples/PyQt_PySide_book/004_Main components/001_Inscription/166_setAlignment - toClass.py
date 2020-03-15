from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Класс QLabel")
window.resize(300, 80)
label = QtGui.QLabel()
label.setText("Текст надписи")
#label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
#label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
#label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
label.setAlignment(QtCore.Qt.AlignCenter)
label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
