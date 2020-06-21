import sys
import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class listWidgetClass(QListWidget):
    def __init__(self):
        super(listWidgetClass, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setDragDropMode(QAbstractItemView.DropOnly)

    def dropEvent(self, event):
        # print 'DROP', type(event)
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            for f in mimedata.urls():
                print(f.toLocalFile())

    def dragEnterEvent(self, event):
        event.accept()
        # print 'ENTER', type(event)

    def dragMoveEvent(self, event):
        # print 'MOVE'
        pass

if __name__ == '__main__':
    app = QApplication([])
    w = listWidgetClass()
    w.show()
    app.exec_()