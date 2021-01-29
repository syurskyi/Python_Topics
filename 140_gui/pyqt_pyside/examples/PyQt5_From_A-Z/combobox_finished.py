import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.cmbStates = QComboBox(self)
        self.cmbStates.move(50,50)

        #self.cmbStates.addItems(["AL", "AR", "MA", "MO", "MI"])
        self.cmbStates.addItem("Alabama", {"ab":"AL", "pop":4000000})
        self.cmbStates.addItem("Alaska", {"ab":"AK", "pop":500000})
        self.cmbStates.addItem("Arizona", {"ab":"AZ", "pop":7000000})
        self.cmbStates.addItem("Arkansas", {"ab":"AR", "pop":3000000})
        self.cmbStates.addItem("Mississippi", {"ab":"MS", "pop":5000000})
        self.cmbStates.addItem("Missouri", {"ab":"MO", "pop":5000000})
        self.cmbStates.addItem("Minnesota", {"ab":"MN", "pop":6000000})
        self.cmbStates.addItem("Michigan", {"ab":"MI", "pop":10000000})
        self.cmbStates.currentIndexChanged.connect(self.evt_cmbStates_changed)
        self.cmbStates.highlighted.connect(self.evt_cmbStates_highlighted)

        self.lblPop = QLabel("Population: 4000000", self)
        self.lblPop.move(180, 55)

        self.cmbPlants = QComboBox(self)
        self.cmbPlants.move(50, 80)
        self.cmbPlants.resize(200, 20)
        self.cmbPlants.setEditable(True)
        self.cmbPlants.setDuplicatesEnabled(False)
        self.cmbPlants.addItem("Thalictrum occidentalis", "THOC")
        self.cmbPlants.addItem("Bouteloua gracilis", "BOGR")
        self.cmbPlants.addItem("Bromus tectus", "BRTE")
        self.cmbPlants.addItem("Picea englemanii", "PIEN")
        self.cmbPlants.currentIndexChanged.connect(self.evt_cmbPlants_changed)

    def evt_cmbStates_changed(self, idx):
        data = self.cmbStates.itemData(idx)
        QMessageBox.information(self, "ComboBox", "You selected {}\nwhich has a population of: {}".format(data["ab"], data["pop"]))

    def evt_cmbStates_highlighted(self, idx):
        self.lblPop.setText("Population: {}".format(self.cmbStates.itemData(idx)["pop"]))

    def evt_cmbPlants_changed(self, idx):
        if not self.cmbPlants.itemData(idx):
            sStr, bOk = QInputDialog.getText(self, "Add Species Code", "Add a species code for '{}'".format(self.cmbPlants.itemText(idx)))
            if bOk:
                self.cmbPlants.setItemData(idx, sStr)
        QMessageBox.information(self, "Plants", "You selected '{}'".format(self.cmbPlants.itemData(idx)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
