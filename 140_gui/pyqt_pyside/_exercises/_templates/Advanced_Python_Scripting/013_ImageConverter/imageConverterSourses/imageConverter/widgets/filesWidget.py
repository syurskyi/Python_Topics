from PySide.QtCore import *
from PySide.QtGui import *
import os

icon = os.path.join(os.path.dirname(__file__), 'drag.png')


class listWidgetClass(QListWidget):
    def __init__(self):
        super(listWidgetClass, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setDragDropMode(QAbstractItemView.DropOnly)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.files = []

    def dropEvent(self, event):
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            for f in mimedata.urls():
                self.addFile(f.toLocalFile())

    def dragEnterEvent(self, event):
        if event.source() is self:
            event.ignore()
        else:
            mimedata = event.mimeData()
            if mimedata.hasUrls():
                event.accept()
            else:
                event.ignore()

    def dragMoveEvent(self, event):
        if event.source() is self:
            event.ignore()
        else:
            mimedata = event.mimeData()
            if mimedata.hasUrls():
                event.accept()
            else:
                event.ignore()

    def addFile(self, path):
        if not path in self.files:
            item = QListWidgetItem(self)
            item.setText(os.path.basename(path))
            item.setData(Qt.UserRole, path)
            self.files.append(path)

    def deleteSelected(self):
        for s in self.selectedItems():
            self.files.remove(s.data(32))
            self.takeItem(self.indexFromItem(s).row())


    def getAllFiles(self):
        return self.files

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.deleteSelected()
