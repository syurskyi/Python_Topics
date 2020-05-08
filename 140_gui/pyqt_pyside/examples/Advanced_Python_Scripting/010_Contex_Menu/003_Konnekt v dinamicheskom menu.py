from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

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
        self.menu.setTearOffEnabled(1)
        self.menu_bar.addMenu(self.menu)
        # actions
        self.act1 = QAction('Open', self)
        self.act1.setCheckable(1)
        self.act1.triggered.connect(self.action)
        self.menu.addAction(self.act1)

        self.menu.addAction(QAction('Save', self, triggered=self.action))
        # self.menu.actions()[1]

        # submenu
        self.sMenu = QMenu('Sub')
        self.menu.addMenu(self.sMenu)

        for i in range(10):
            # self.sMenu.addAction(QAction('Item %s' % i, self, triggered=self.action)) # mu ne mozem zapisat' self.acrion(i)
                                                                                      # potomy shto eto bydet vuzov fynkcii a ne connect na imja funkcii
                                                                                      # poetomy zdes' nyzno ispol'zovat' lambda

            # self.sMenu.addAction(QAction('Item %s' % i, self,
            #                              triggered=lambda: self.action(i))) # v etoj versii mu vsegda bydem polychat' 9
                                                                            # eto proishodit potomyshto v processe cukla kazdaja lambda
                                                                            # connectjas' na 'i', konektitsja na odno i toze znachenie
                                                                            # 'i' iteriryetsja, nabiraja kazduj raz edinicy i pod konec cykla, stanovitsja ravno 9
                                                                            # I vse lambda fyhkcii shto y nas sozdalis', oni zakonektenu y nas na odno i toze znachenie
                                                                            #
            self.sMenu.addAction(QAction('Item %s' % i, self,
                                         triggered=lambda x=i: self.action(x)))
                                                                            # x=i, mu zastovljaem lambda prinimat' argyment, no pri etom triggered nam ego ne otpravljaet
                                                                            # i mu pishem znachenie po ymolchanijy x=i, kotoroe ravno nashemy i, to est' nomery iteracii
                                                                            # i v nytri mu ispol'zyem etot x
                                                                            # KAzduj raz vnytri lambda fynkcii sozdajotsja x, kotoruj javljaetsja lokal'noj peremenoj dlja etoj fynkcuu
                                                                            # i on yze ne izmenjaetsja, prosto znachenie dlja etogo x berjotsja  is peremennoj 'i', kotoraja
                                                                            # v konkretnoj iteracii ravna konkretnomy znachenijy

    def action(self, i):
        print(i)


if __name__ == '__main__':
    app = QApplication([])
    w = MainWindowClass()
    w.show()
    app.exec_()