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
        lineEdit = QtGui.QLineEdit("Initial value")
        lineEdit.setText("New text")
        box = QtGui.QVBoxLayout()
        box.addWidget(lineEdit)
        self.setLayout(box)
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