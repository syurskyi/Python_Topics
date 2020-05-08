from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# ne vsegda menjy buvaet statichnoe. Sostav menju zavisit ot kakih to yslovij. Poetomy chasto menu prohoditsja generirovat'
# v moment sozdanija

class MainWindowClass(QMainWindow):
    def __init__(self):
        super(MainWindowClass, self).__init__()
        # widget
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        # menu bar
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)
        # menu
        self.menu = QMenu('File')
        self.menu.setTearOffEnabled(1)                                     # dobavljaet v menu  divide line pri nazatii na kototyjy mozno otsoedinit' menu i ono stanet otdel;num vidgetpm
        self.menu_bar.addMenu(self.menu)
        # actions first version
        self.act1 = QAction('Open', self)    # objazatel'no ykazuvat' parent
        self.act1.setCheckable(1)
        self.act1.triggered.connect(self.action)
        self.menu.addAction(self.act1)

        # actions second version                                            # raznica mezdy pervum i vtorum sposobom
                                                                            # mu ne imeem prjmogo dostypa neposredstvenno k action (self.act1)
                                                                            # potomy shto vo vtorom variante on sozdajotsja dinamicheski
                                                                            # i y nas net peremennoj, kotoraja ssulaetsja na etot objekt

        self.menu.addAction(QAction('Save', self, triggered=self.action))
        # self.menu.actions()[1]

        # submenu
        self.sMenu = QMenu('Sub')
        self.menu.addMenu(self.sMenu)

        for i in range(10):
            self.sMenu.addAction(QAction('Item %s' % i, self))

    def action(self):
        if self.act1.isCheckable():
            print('ACTION')
        else:
            print('STOP')

if __name__ == '__main__':
    app = QApplication([])
    w = MainWindowClass()
    w.show()
    app.exec_()