# -*- coding: utf-8 -*-
from PySide import QtGui
import sys

class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Class QLineEdit")
        self.resize(300, 50)
        self.line_edit = QtGui.QLineEdit()
        self.line_edit.setPlaceholderText("Enter login")
        self.line_edit2 = QtGui.QLineEdit()
        self.line_edit2.setPlaceholderText("Enter password")
        self.line_edit2.setEchoMode(QtGui.QLineEdit.Password)
        button = QtGui.QPushButton("OK")
        button.clicked.connect(self.on_clicked)
        box = QtGui.QVBoxLayout()
        box.addWidget(self.line_edit)
        box.addWidget(self.line_edit2)
        box.addWidget(button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        print(self.line_edit(), self.line_edit2())


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