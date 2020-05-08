from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sceneWidget

class exampleViewClass(QGraphicsView):
    def __init__(self):
        super(exampleViewClass, self).__init__()
        # self.s = QGraphicsScene()
        self.s = sceneWidget.exampleSceneClass()
        self.setScene(self.s)


if __name__ == '__main__':
    app = QApplication([])
    w = exampleViewClass()
    w.show()
    app.exec_()