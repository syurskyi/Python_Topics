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
        # print rec
        painter = QPainter()
        painter.begin(self)
        ###
        painter.end()


if __name__ == '__main__':
    app = QApplication([])
    w = DrawCustomWidget()
    w.show()
    app.exec_()