from PySide.QtCore import *
from PySide.QtGui import *
import math

import computeArea_UIs as ui


class computerAreaClass(QMainWindow, ui.Ui_computeArea):
    def __init__(self):
        super(computerAreaClass, self).__init__()
        self.setupUi(self)

# rasschjot v real'nom vremeni. Esli rezim live is True, knopka "Compute" prjachetsja.
# y lybogo widgeta est'  fyncija setVisible
        # variable
        self.live = True

        # connects
        self.shape_cbb.currentIndexChanged.connect(self.updateUi)
        self.compute_btn.clicked.connect(self.compute)
        if self.live:
            self.compute_btn.setVisible(0)
            self.square_height_spx.valueChanged.connect(self.compute)
            self.square_width_spx.valueChanged.connect(self.compute)
            self.circle_radius_spx.valueChanged.connect(self.compute)

        # start

        self.updateUi()

    def compute(self):                           # osnovnaja fynkcija bydet vuchisljat' kakyjy formyly nado raschitat'
                                                 # i potom otprovljat' v nyznyjy fynkcijy
        if self.shape_cbb.currentIndex() == 0:
            self.computeSquare()
        elif self.shape_cbb.currentIndex() == 1:
            self.computeCircle()

    def computeSquare(self):
        w = self.square_width_spx.value()        # nado zabrat' znachenie so spinboksov. Method value() zabiraet
                                                 # tekychee znachenie
        h = self.square_height_spx.value()
        area = w * h
        self.showResult(area)                    # otobrazit rezyl'tat v label

    def computeCircle(self):
        r = self.circle_radius_spx.value()
        area = math.pi * (r**2)
        self.showResult(area)

# fynkcija updateUi prjachet nenyznue groupbox
    def updateUi(self):
        self.square_gb.setVisible(self.shape_cbb.currentIndex() == 0)
        self.circle_gb.setVisible(self.shape_cbb.currentIndex() == 1)
        self.compute()

    def showResult(self, result):                # fynkcija otvechaet za otobrazenie rezyl'tata, shto bu ne pisat'
                                                 # v kazdoj fynkcii etot metod
        self.result_lbl.setText('Result: %.3f' % result)

if __name__ == '__main__':
    app = QApplication([])
    w = computerAreaClass()
    w.show()
    app.exec_()
