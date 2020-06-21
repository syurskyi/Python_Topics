# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Class QLineEdit")
        self.resize(300, 50)
        self.lineEdit = QtGui.QLineEdit()
        self.lineEdit.setInputMask("Date: 99.B9.9999;#")
        button = QtGui.QPushButton("Get Value")
        button.clicked.connect(self.on_clicked)
        box = QtGui.QVBoxLayout()
        box.addWidget(self.lineEdit)
        box.addWidget(button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        if self.lineEdit.hasAcceptableInput():
            print(self.lineEdit.text())
        else:
            print("The value does not match the mask")

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