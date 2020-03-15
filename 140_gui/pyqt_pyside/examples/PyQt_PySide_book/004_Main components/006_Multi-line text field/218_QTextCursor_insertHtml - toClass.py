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
        self.textEdit.setHtml("<p>Block 1</p><p>Block 2</p>")
        button = QtGui.QPushButton("Insert text")
        button.clicked.connect(self.on_clicked)
        box = QtGui.QVBoxLayout()
        box.addWidget(self.textEdit)
        box.addWidget(button)
        self.setLayout(box)
        self.show()
        sys.exit(app.exec_())

    def on_clicked(self):
        self.textEdit.setFocus()
        cur = self.textEdit.textCursor()
        cur.beginEditBlock()              # Начало блока
        cur.insertHtml("<b>inserted fragment 1</b>")
        cur.insertHtml("""<span style="color: red;">inserted fragment 2</span>""")
        cur.endEditBlock()                # Конец блока
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