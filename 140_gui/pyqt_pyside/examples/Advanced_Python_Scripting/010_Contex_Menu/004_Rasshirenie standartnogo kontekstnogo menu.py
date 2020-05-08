from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

textArray = 'Click', 'Press', 'Enter'

# Y nas est' dva varianta rabotu s kontekstnum menu, zamenit menu ili dopolnit'

class WidgetMenuClass(QWidget):
    def __init__(self):
        super(WidgetMenuClass, self).__init__()
        ly = QVBoxLayout(self)
        self.btn = QPushButton('Click')
        ly.addWidget(self.btn)
        self.line = QLineEdit()
        ly.addWidget(self.line)

        self.btn.setContextMenuPolicy(Qt.CustomContextMenu)
        self.btn.customContextMenuRequested.connect(self.openMenu)

        self.line.setContextMenuPolicy(Qt.CustomContextMenu)
        self.line.customContextMenuRequested.connect(self.openMenu2) # Kogda y nas srabatuvet kakoj to signal, to v klasse generitsja
                                                                     # special'naja peremenaja, kotoraja nazuvaetsja sender - otpravitel' signala
                                                                     #

    def openMenu(self, pos):
        pos = self.btn.mapToGlobal(pos)
        menu = QMenu()
        for i in textArray:
            menu.addAction(QAction(i, self))
        a = menu.exec_(QCursor().pos())
        if a:
            self.btn.setText(a.text())

    def openMenu2(self, pos):                                        # Shto bu nam ne zamenjat menu a doplnit' ili rasshiret'
        pos = self.line.mapToGlobal(pos)                             # Nam nyzno sozdavat' ego ne novoe, a vzjat' standartnoe menu
        menu = self.line.createStandardContextMenu()                 # y lineEdit
        menu.addSeparator()
        for i in textArray:
            menu.addAction(QAction(i, self))
        a = menu.exec_(QCursor().pos())
        if a:
            self.line.setText(a.text())


if __name__ == '__main__':
    app = QApplication([])
    w = WidgetMenuClass()
    w.show()
    app.exec_()