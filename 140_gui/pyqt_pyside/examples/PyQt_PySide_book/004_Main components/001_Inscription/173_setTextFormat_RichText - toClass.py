from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

window.setWindowTitle("Класс QLabel")
window.resize(300, 80)
label = QtGui.QLabel()
label.setText("<b>Текст в формате HTML</b>")
label.setTextFormat(QtCore.Qt.RichText)
label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
