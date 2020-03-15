# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.btnСut = QtGui.QPushButton("Copy from file")
        self.btnPaste = QtGui.QPushButton("Paste")
        self.label = QtGui.QLabel("")
        self.label.setAutoFillBackground(True)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnСut)
        self.vbox.addWidget(self.btnPaste)
        self.setLayout(self.vbox)
        self.btnСut.clicked.connect(self.on_copy)
        self.btnPaste.clicked.connect(self.on_paste)
        self.connect(QtGui.qApp.clipboard(), QtCore.SIGNAL("dataChanged()"),
                     self.on_change_clipboard)

    def on_copy(self):
        img = QtGui.QImage("pixmap.png")
        byteArray = QtCore.QByteArray()
        buffer = QtCore.QBuffer(byteArray)
        buffer.open(QtCore.QIODevice.WriteOnly)
        img.save(buffer, "PNG")
        buffer.close()
        data = QtCore.QMimeData()
        data.setData("image/png", byteArray)
        QtGui.qApp.clipboard().setMimeData(data)

    def on_paste(self):
        mime = QtGui.qApp.clipboard().mimeData()
        if mime.hasFormat("image/png"):
            pixmap = QtGui.QPixmap()
            if pixmap.loadFromData(mime.data("image/png"), "PNG"):
                self.label.setPixmap(pixmap)

    def on_change_clipboard(self):
        print("Data in the clipboard changed")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Working with the clipboard")
    window.resize(300, 150)
    window.show()

    sys.exit(app.exec_())