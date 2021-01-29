import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_modules.Gbx_demo_ui import *

class DlgMain(QDialog, Ui_DlgMain):
    def __init__(self):
        super(DlgMain, self).__init__()
        self.setupUi(self)

        self.rbtCheckTrue.toggled.connect(self.evt_rbtCheckTrue_toggled)
        self.rbtFlatTrue.toggled.connect(self.evt_rbtFlatTrue_toggled)
        self.rbtLeftAlign.toggled.connect(self.evt_rbtAlignLeft_toggled)
        self.rbtRightAlign.toggled.connect(self.evt_rbtAlignRight_toggled)
        self.rbtCenterAlign.toggled.connect(self.evt_rbtAlignCenter_toggled)

    def evt_rbtCheckTrue_toggled(self, chk):
        self.gbxCheckable.setCheckable(chk)

    def evt_rbtFlatTrue_toggled(self, chk):
        self.gbxFlat.setFlat(chk)

    def evt_rbtAlignLeft_toggled(self, chk):
        if chk:
            self.gbxAlignment.setAlignment(Qt.AlignLeft)
            self.gbxAlignment.setTitle("Left")

    def evt_rbtAlignCenter_toggled(self, chk):
        if chk:
            self.gbxAlignment.setAlignment(Qt.AlignCenter)
            self.gbxAlignment.setTitle("Center")

    def evt_rbtAlignRight_toggled(self, chk):
        if chk:
            self.gbxAlignment.setAlignment(Qt.AlignRight)
            self.gbxAlignment.setTitle("Right")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())

