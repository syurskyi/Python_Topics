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
        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setPlainText("Block 1\nBlock 2\nBlock 3\nBlock 4\nBlock 5 jjkh hkjhkjh khk hkh khk jhkh hkh khk hk hkh hkj hk hkhk k kjh kh jh kh khk hkh khk hkjh kh kh kjh kjhkj h kh kh kjh khk hk kh kh k")
        button = QtGui.QPushButton("Move the cursor 10 characters ahead")
        button.clicked.connect(self.on_clicked)
        box = QtGui.QVBoxLayout()
        box.addWidget(self.textEdit)
        box.addWidget(button)
        self.setLayout(box)
        self.show()


    def on_clicked(self):
        self.textEdit.setFocus()
        cur = self.textEdit.textCursor()
        print(cur.movePosition(QtGui.QTextCursor.NextCharacter,
                               mode=QtGui.QTextCursor.MoveAnchor, n=10))
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