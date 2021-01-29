import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.chkTwoState = QCheckBox("Two state", self)
        self.chkTwoState.move(50, 50)
        self.chkTwoState.toggled.connect(self.evt_chkHandle)

        self.chkThreeState = QCheckBox("Three state", self)
        self.chkThreeState.move(50, 80)
        self.chkThreeState.setTristate(True)
        self.chkThreeState.setCheckState(1)
        self.chkThreeState.stateChanged.connect(self.evt_chkHandle)

    def evt_chkHandle(self, chkd):
        print(self.chkTwoState.isChecked())
        print(self.chkThreeState.checkState())
        chkBox = self.sender()
        if chkBox.text() == "Two state":
            QMessageBox.information(self, "", "Two state box clicked \nCurrent Status: "+str(chkd))
        else:
            QMessageBox.information(self, "", "Three state box clicked \nCurrent Status: "+str(chkd))
            if self.chkThreeState.checkState() == Qt.PartiallyChecked:
                print("Partially Checked")







if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())