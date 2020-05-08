from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import editorItem

class editorSceneClass(QGraphicsScene):
    def __init__(self):
        super(editorSceneClass, self).__init__()
        self.setSceneRect(-1000, -100, 2000, 2000)
        self.grid = 30
        self.addNode()

    def drawBackground(self, painter, rect):
        if False:
            painter = QPainter()
        painter.fillRect(rect, QColor(30, 30, 30))
        left = int(rect.left()) - (int(rect.left()) % self.grid)
        top = int(rect.top()) - int(rect.top()) % self.grid
        right = int(rect.right())
        bottom = int(rect.bottom())
        lines = []
        for x in range(left, right, self.grid):
            lines.append(QLine(x, top, x, bottom))
        for y in range(top, bottom, self.grid):
            lines.append(QLine(left, y, right, y))

        painter.setPen(QPen(QColor(100, 100, 100), 1))
        painter.drawLines(lines)

    def addNode(self, pos=False):
        if not pos:
            pos = QPoint(0, 0)
        item = editorItem.editorItemClass(self.grid, len(self.items()) + 1)
        self.addItem(item)
        item.setPos(pos)

    def mouseDoubleClickEvent(self, event):
        self.addNode(event.scenePos())
