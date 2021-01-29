import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.lytMain = QHBoxLayout()

        self.gbxCheckable = QGroupBox("Checkable")
        self.rbtCheckTrue = QRadioButton("True")
        self.rbtCheckFalse = QRadioButton("False")
        self.lytCheckable = QVBoxLayout()
        self.lytCheckable.addWidget(self.rbtCheckTrue)
        self.lytCheckable.addWidget(self.rbtCheckFalse)
        self.gbxCheckable.setLayout(self.lytCheckable)
        self.lytMain.addWidget(self.gbxCheckable)
        self.rbtCheckTrue.toggled.connect(self.evt_rbtCheck_toggled)

        self.gbxFlat = QGroupBox("Flat")
        self.rbtFlatTrue = QRadioButton("True")
        self.rbtFlatFalse = QRadioButton("False")
        self.lytFlat = QVBoxLayout()
        self.lytFlat.addWidget(self.rbtFlatTrue)
        self.lytFlat.addWidget(self.rbtFlatFalse)
        self.gbxFlat.setLayout(self.lytFlat)
        self.rbtFlatTrue.toggled.connect(self.evt_rbtFlat_toggled)
        self.lytMain.addWidget(self.gbxFlat)

        self.gbxAlign = QGroupBox("Alignment")
        self.rbtAlignLeft = QRadioButton("Alignment Left")
        self.rbtAlignCenter = QRadioButton("Alignment Center")
        self.rbtAlignRight = QRadioButton("Alignment Right")
        self.lytAlign = QVBoxLayout()
        self.lytAlign.addWidget(self.rbtAlignLeft)
        self.lytAlign.addWidget(self.rbtAlignCenter)
        self.lytAlign.addWidget(self.rbtAlignRight)
        self.gbxAlign.setLayout(self.lytAlign)
        self.rbtAlignLeft.toggled.connect(self.evt_rbtAlignLeft_toggled)
        self.rbtAlignCenter.toggled.connect(self.evt_rbtAlignCenter_toggled)
        self.rbtAlignRight.toggled.connect(self.evt_rbtAlignRight_toggled)
        self.lytMain.addWidget(self.gbxAlign)

        self.setLayout(self.lytMain)

    def evt_rbtCheck_toggled(self, chk):
        self.gbxCheckable.setCheckable(chk)

    def evt_rbtFlat_toggled(self, chk):
        self.gbxFlat.setFlat(chk)

    def evt_rbtAlignLeft_toggled(self, chk):
        if chk:
            self.gbxAlign.setAlignment(Qt.AlignLeft)
            self.gbxAlign.setTitle("Left Alignment")

    def evt_rbtAlignRight_toggled(self, chk):
        if chk:
            self.gbxAlign.setAlignment(Qt.AlignRight)
            self.gbxAlign.setTitle("Right Alignment")

    def evt_rbtAlignCenter_toggled(self, chk):
        if chk:
            self.gbxAlign.setAlignment(Qt.AlignCenter)
            self.gbxAlign.setTitle("Center Alignment")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
