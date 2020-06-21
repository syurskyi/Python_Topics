from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class DrawCustomWidget(QWidget):
    def __init__(self):
        super(DrawCustomWidget, self).__init__()
        self.resize(300, 200)
        self.setWindowTitle('Custom Widget')

    def paintEvent(self, event):
        rec = event.rect()
        if False:
            rec = QRect()
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        ###
        painter.fillRect(rec, Qt.black)
        painter.setPen(QPen(QBrush(Qt.red), 3))
        painter.setBrush(QBrush(Qt.black))
        painter.drawRect(30, 30, rec.width() - 60, rec.height() - 60)

        painter.setPen(QPen(QBrush(Qt.green), 8))
        painter.drawLine(100, 0, 150, rec.height())

        painter.end()


if __name__ == '__main__':
    app = QApplication([])
    w = DrawCustomWidget()
    w.show()
    app.exec_()