from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import editorScene


class editorViewClass(QGraphicsView):
    def __init__(self):
        super(editorViewClass, self).__init__()
        self.s = editorScene.editorSceneClass()
        self.setScene(self.s)