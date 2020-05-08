from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

textArray = 'Click', 'Press', 'Enter'


class WidgetMenuClass(QWidget):
    def __init__(self):
        super(WidgetMenuClass, self).__init__()
        ly = QVBoxLayout(self)
        self.btn = QPushButton('Click')
        ly.addWidget(self.btn)
        self.line = QLineEdit()
        ly.addWidget(self.line)

        self.btn.setContextMenuPolicy(Qt.CustomContextMenu)        # shto bu contekstnoe menu pojavilos', nado etoj knopke skazat' shto bu ona reagirovala na etot signal
        self.btn.customContextMenuRequested.connect(self.openMenu) # etot signal generitsja kogda mu zaprashuvaem
                                                                   #  konteksnoe menu a eto y nas nazatie pravoj knopkoj mushi

    def openMenu(self, pos):
        pos = self.btn.mapToGlobal(pos)                           # y lybogo widgeta est' metodu kotorue delajyt remap koordinat
        menu = QMenu()                                            # esli net pozicii gde bul proizvedjon klik mozno ykazat' koordinatu kyrsora

        for i in textArray:
            menu.addAction(QAction(i, self))
        # menu.exec_(pos)                                         # lokalnue koordinatu klika na preobrazovat' v global'nue koordinatu ekrana
        a = menu.exec_(QCursor().pos())                           # funkcija obrachaetsja k tekychemy kyrsory i vozvrachaet ego global'nue koordinatu
        # print a                                                 # menu.exec_ vozvrachaet nam action, kotoruj bul vubran i mu mozem ego zabrat'
        # print a.text()
        if a:
            self.btn.setText(a.text())


if __name__ == '__main__':
    app = QApplication([])
    w = WidgetMenuClass()
    w.show()
    app.exec_()