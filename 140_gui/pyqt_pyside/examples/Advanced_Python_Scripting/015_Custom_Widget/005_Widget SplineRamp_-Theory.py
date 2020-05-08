from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class splineRampWidget(QWidget):
    def __init__(self):
        super(splineRampWidget, self).__init__()
        self.resize(300, 200)

        self.lineWidth = 3
        self.pointSize = 10

        self.point1 = QPointF(0, 0)
        self.point2 = QPointF(300, 200)

        self.factor1 = 0.0
        self.factor2 = 1.0

        self.dragged = None

        self.region1 = QRect()
        self.region2 = QRect()
        self.regionSize = 40
        self.updateRegions()

    def updateRegions(self):
        self.region1 = QRect(0, 0, self.regionSize, self.regionSize)
        self.region1.moveCenter(self.point1.toPoint())

        self.region2 = QRect(0, 0, self.regionSize, self.regionSize)
        self.region2.moveCenter(self.point2.toPoint())

        self.factor1 = self.point1.y() / float(self.size().height())
        self.factor2 = self.point2.y() / float(self.size().height())
        print(self.factor1, self.factor2)

    def paintEvent(self, event):
        rec = event.rect()
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), Qt.black)
        path = QPainterPath()
        path.moveTo(self.point1)
        path.cubicTo(rec.width()/2, self.point1.y(),
                     rec.width()/2, self.point2.y(),
                     rec.width(), self.point2.y())
        painter.setPen(QPen(QBrush(Qt.white), self.lineWidth))
        painter.drawPath(path)
        painter.setBrush(QBrush(Qt.white))

        painter.drawEllipse(self.point1, self.pointSize, self.pointSize)
        painter.drawEllipse(self.point2, self.pointSize, self.pointSize)

        painter.setPen(QPen(QBrush(Qt.white), 1))
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(self.region1)
        painter.drawRect(self.region2)
        painter.end()

    def mousePressEvent(self, event):
        # print self.region1.contains(event.pos())
        if self.region1.contains(event.pos()):
            self.dragged = self.point1
        elif self.region2.contains(event.pos()):
            self.dragged = self.point2
        super(splineRampWidget, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        # print self.dragged
        if not self.dragged is None:
            y = event.pos().y()
            s = self.size()
            self.dragged.setY(min(max(y, 1), s.height()))
            self.update()
        super(splineRampWidget, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.dragged = None
        self.updateRegions()
        self.update()
        super(splineRampWidget, self).mouseReleaseEvent(event)

    def resizeEvent(self, event):

        self.point1.setY(event.size().height() * self.factor1)
        self.point2.setY(event.size().height() * self.factor2)
        self.point2.setX(event.size().width())
        self.updateRegions()
        self.update()
        super(splineRampWidget, self).resizeEvent(event)

if __name__ == '__main__':
    app = QApplication([])
    w = splineRampWidget()
    w.show()
    app.exec_()