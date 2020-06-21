from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class editorItemClass(QGraphicsItem):
    def __init__(self, height, num):
        super(editorItemClass, self).__init__()
        self.x = 0
        self.y = 0
        self.w = 150
        self.h = height
        self.num = num
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

    def boundingRect(self):
        return QRectF(self.x, self.y, self.w, self.h)

    def paint(self, painter, opt, w):
        rec = self.boundingRect()
        if False:
            painter = QPainter()
        painter.fillRect(rec, Qt.black)
        painter.fillRect(rec.adjusted(1, 1, -1, -1), Qt.white)
        painter.fillRect(rec.adjusted(3, 3, -3, -3), Qt.gray)

        painter.setFont(QFont('Arial', 10))
        painter.setPen(QPen(Qt.black))
        painter.drawText(rec, Qt.AlignCenter, 'Node %s' % self.num)
