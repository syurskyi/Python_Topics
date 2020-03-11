from PySide.QtCore import *
from PySide.QtGui import *
import editorScene


class editorViewClass(QGraphicsView):
    def __init__(self):
        super(editorViewClass, self).__init__()
        self.s = editorScene.editorSceneClass()
        self.setScene(self.s)