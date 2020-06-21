# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(300, 300)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        black = QtCore.Qt.black
        white = QtCore.Qt.white
        red = QtCore.Qt.red
        painter.setPen(QtGui.QPen(black))
        painter.setBrush(QtGui.QBrush(white))
        painter.drawRect(3, 3, 294, 294)

        painter.setPen(QtGui.QPen(red, 1))
        painter.setFont(QtGui.QFont("Tahoma", 12))

        painter.drawRect(QtCore.QRect(20, 40, 260, 200))
        textOption = QtGui.QTextOption(QtCore.Qt.AlignCenter)
        textOption.setFlags(QtGui.QTextOption.ShowTabsAndSpaces)
        painter.drawText(QtCore.QRectF(20., 40., 260., 200.),
                         "Показаны все\tспециальные символы ",
                         option=textOption)

        print(painter.boundingRect(20, 100, 260, 30,
                                   QtCore.Qt.AlignCenter | QtCore.Qt.TextShowMnemonic,
                                   "Строка &1"))

        print(painter.boundingRect(QtCore.QRect(20, 140, 260, 50),
                                   QtCore.Qt.AlignRight | QtCore.Qt.TextSingleLine,
                                   "Строка 2\nвсе специальные символы трактуются как пробелы и текст выводится в одну строку"))

        print(painter.boundingRect(QtCore.QRectF(20., 190., 260., 50.),
                                   QtCore.Qt.AlignRight | QtCore.Qt.TextWordWrap,
                                   "Строка 3 очень длинный текст на двух строках"))

        print(painter.boundingRect(QtCore.QRectF(20., 40., 260., 200.),
                                   "Показаны все\tспециальные символы ",
                                   option=textOption))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPainter")
    window.show()
    sys.exit(app.exec_())