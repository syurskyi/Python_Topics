# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.btnСut = QtWidgets.QPushButton("Копировать из файла")
        self.btnPaste = QtWidgets.QPushButton("Вставить")
        self.label = QtWidgets.QLabel("")
        self.label.setAutoFillBackground(True)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnСut)
        self.vbox.addWidget(self.btnPaste)
        self.setLayout(self.vbox)
        self.btnСut.clicked.connect(self.on_copy)
        self.btnPaste.clicked.connect(self.on_paste)
        QtWidgets.qApp.clipboard().dataChanged.connect(
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
        QtWidgets.qApp.clipboard().setMimeData(data)

    def on_paste(self):
        mime = QtWidgets.qApp.clipboard().mimeData()
        if mime.hasFormat("image/png"):
            pixmap = QtGui.QPixmap()
            if pixmap.loadFromData(mime.data("image/png"), "PNG"):
                self.label.setPixmap(pixmap)

    def on_change_clipboard(self):
        print("Данные в буфере обмена изменены")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Работа с буфером обмена")
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec_())