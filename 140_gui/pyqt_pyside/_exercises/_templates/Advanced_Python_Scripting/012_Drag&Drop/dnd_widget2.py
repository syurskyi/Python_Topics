import sys
import os
from PySide.QtCore import *
from PySide.QtGui import *

class listWidgetClass(QListWidget):
    def __init__(self):
        super(listWidgetClass, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setDragDropMode(QAbstractItemView.DropOnly)

    def dropEvent(self, event):
        print 'DROP', type(event)  # type event est' QDropEvent i samoe glavnoe shto on delaet on vozvrachaet mimedata
        mimedata = event.mimeData()
        print mimedata
        if mimedata.hasUrls():
            print mimedata.urls()

    def dragEnterEvent(self, event):
        event.accept()
        # print 'ENTER', type(event)

    def dragMoveEvent(self, event):
        # print 'MOVE', type(event)
        pass

if __name__ == '__main__':
    app = QApplication([])
    w = listWidgetClass()
    w.show()
    app.exec_()