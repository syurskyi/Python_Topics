from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import button

textArray = 'Click', 'Press', 'Enter'


class WidgetMenuClass(QWidget):
    def __init__(self):
        super(WidgetMenuClass, self).__init__()
        ly = QVBoxLayout(self)
        self.btn = button.MyButtonClass('Click')     # Custom button i ves' fynkcional ja mogy perenesti tyda
        ly.addWidget(self.btn)
        self.line = QLineEdit()
        ly.addWidget(self.line)

        # self.btn.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.btn.customContextMenuRequested.connect(self.openMenu)

        self.line.setContextMenuPolicy(Qt.CustomContextMenu)
        self.line.customContextMenuRequested.connect(self.openMenu) # Kogda y nas srabatuvet kakoj to signal, to v klasse generitsja
                                                                    # special'naja peremenaja, kotoraja nazuvaetsja sender - otpravitel' signala

    def openMenu(self, pos):
        pos = self.sender().mapToGlobal(pos)
        try:
            menu = self.sender().createStandardContextMenu()
        except:
            menu = QMenu()
        for i in textArray:
            menu.addAction(QAction(i, self))
        a = menu.exec_(QCursor().pos())
        if a:
            self.sender().setText(a.text())


if __name__ == '__main__':
    app = QApplication([])
    w = WidgetMenuClass()
    w.show()
    app.exec_()