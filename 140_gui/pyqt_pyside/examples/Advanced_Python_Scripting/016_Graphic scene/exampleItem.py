from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class exampleItemClass(QGraphicsItem):
    def __init__(self):
        super(exampleItemClass, self).__init__()
        self.x = 0
        self.y = 0
        self.h = 50
        self.w = 170
        self.width = 2
        self.text = 'None'
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

    def boundingRect(self):
        return QRect(self.x, self.y, self.w, self.h)

    def paint(self, painter, options, widget):
        painter.setPen(QPen(Qt.black, self.width))
        if self.isSelected():
            painter.setBrush(Qt.red)
        else:
            painter.setBrush(Qt.lightGray)
        rec = self.boundingRect().adjusted(self.width/2, self.width/2, -self.width/2, -self.width/2)
        painter.drawRect(rec)

        painter.setFont(QFont("Arial", 16))
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self.text)

if __name__ == '__main__':
    app = QApplication([])
    w = exampleItemClass()
    w.show()
    app.exec_()