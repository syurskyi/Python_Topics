import sys
import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

icon = os.path.join(os.path.dirname(__file__), 'drag.png')

class listWidgetClass(QListWidget):
    def __init__(self):
        super(listWidgetClass, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)  # vjlychaet vozmoznost' vudeljat' neskol'ko fajlov
        self.files = []

    def dropEvent(self, event):
        # print 'DROP', type(event)
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

    def startDrag(self, dropAction):     # pereopredeljaem method kotoruj otvechaet za to shto proishodit kogda mu nachinaem shto to peretaskivat'
                                         # dropAction odin iz rezimov peretaskivanija
        drag = QDrag(self)               # nyzno sozdat' klass kotoruj otvechaet za peretaskivanie dannuh i eto ne mimedata a klass QDrag. QDrag dolzen znat' komy on prenadlezit
        mimedata = QMimeData()           # i sootvestvenno mimedata kotorue bydyt tam lezat'
        url = []                         # potom nado sobrat' danue kotorue mu hotim pomestit' v ety mimedata a eto y nas pyti k fajlam iz vudelenuh fajlov
        for i in self.selectedItems():   # dlja vudelenuh elementov mu zabiraem pyt' i kladjom v url
            url.append(i.data(Qt.UserRole))
        print(url)
        mimedata.setUrls([QUrl.fromLocalFile(x) for x in url])  # kogda mu polychili pyti nam nado ih polozit' v mimedata. preobrazovuvaem strochky v klass QUrls
                                                                # kazduj pyt' kotoruj est' v spiske preobrazovuvaetsja v QUrl. Generator vernjot nam spisok etih klassov
        drag.setMimeData(mimedata)                              # polychennue dannue mu lozim v objekt draga, toest' v etot kontejner dlja peretaskivanija
        pix = QPixmap(icon)
        drag.setPixmap(pix)
        r = drag.exec_()                                        # exec_ kak iv dialogah vozvrachaet kakoj to rezyl'tat
        print(r)
        if r == Qt.DropAction.MoveAction:                       # esli y nas yspesho proizvedeno peretaskivanie to mu ydaljaem nashi vudelenue items
            self.deleteSelected()                               # metod deleteSelected

    def addFile(self, path):
        if not path in self.files:
            item = QListWidgetItem(self)
            item.setText(os.path.basename(path))
            item.setData(Qt.UserRole, path)
            self.files.append(path)

    def deleteSelected(self):
        for s in self.selectedItems():                          # perebiraem vse vudelenue elementu
            self.files.remove(s.data(32))                       # zabirajy pyt' kotoruj lezit v data i ydaljay iz svoego byfera
            self.takeItem(self.indexFromItem(s).row())          # posle chego ydaljay sam item

if __name__ == '__main__':
    app = QApplication([])
    w = listWidgetClass()
    w.show()
    app.exec_()