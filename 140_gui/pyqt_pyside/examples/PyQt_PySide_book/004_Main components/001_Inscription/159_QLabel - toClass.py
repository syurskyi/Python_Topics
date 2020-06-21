from PySide import QtCore, QtGui
import sys


class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

label = QtGui.QLabel("Текст надписи", flags=QtCore.Qt.Window)
label.setWindowTitle("Класс QLabel")
label.resize(300, 50)
label.show()
sys.exit(app.exec_())