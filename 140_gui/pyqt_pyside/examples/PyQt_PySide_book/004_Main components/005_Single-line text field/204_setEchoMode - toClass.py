# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Class QLineEdit")
        self.resize(300, 150)
        lineEdit1 = QtGui.QLineEdit()
        lineEdit2 = QtGui.QLineEdit()
        lineEdit3 = QtGui.QLineEdit()
        lineEdit4 = QtGui.QLineEdit()
        lineEdit1.setEchoMode(QtGui.QLineEdit.Normal)
        lineEdit2.setEchoMode(QtGui.QLineEdit.NoEcho)
        lineEdit3.setEchoMode(QtGui.QLineEdit.Password)
        lineEdit4.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        form = QtGui.QFormLayout()
        form.addRow("&Normal:", lineEdit1)
        form.addRow("No&Echo:", lineEdit2)
        form.addRow("&Password:", lineEdit3)
        form.addRow("PasswordEchoOn&Edit:", lineEdit4)
        self.setLayout(form)
        self.show()

if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QtGui.QApplication(sys.argv)
    main = SampleWindow()
    main.show()

    if app is not None:
        app.exec_()