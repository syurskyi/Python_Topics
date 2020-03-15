# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Class QTextCursor")
        self.resize(500, 250)
        edit = QtGui.QTextEdit()
        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setPlainText("Block 1\nBlock 2\nBlock 3\nBlock 4\nBlock 5 jjkh hkjhkjh khk hkh khk jhkh hkh khk hk hkh hkj hk hkhk k kjh kh jh kh khk hkh khk hkjh kh kh kjh kjhkj h kh kh kjh khk hk kh kh k")
        button = QtGui.QPushButton("Select the fragment before the beginning of the document")
        button.clicked.connect(self.on_clicked)
        box = QtGui.QVBoxLayout()
        box.addWidget(self.textEdit)
        box.addWidget(button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        self.textEdit.setFocus()
        cur = self.textEdit.textCursor()
        cur.setPosition(0, mode=QtGui.QTextCursor.KeepAnchor)
        self.textEdit.setTextCursor(cur)

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
