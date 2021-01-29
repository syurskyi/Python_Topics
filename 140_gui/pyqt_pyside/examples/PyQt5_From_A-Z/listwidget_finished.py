import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        ########  Create Widgets
        self.lbxLanguages = QListWidget()
        self.lbxLanguages.addItems(
            ["C", "C++", "C#", "JavaScript", "Python", "PHP", "Java", "COBOL", "FORTRAN", "Ruby", "Visual Basic",
             "Rust", "Julia", "Go"])
        self.lbxLanguages.sortItems()
        self.lbxLanguages.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lbxLanguages.itemSelectionChanged.connect(self.evt_lbxLanguages_selection)

        self.lbxLanguagesIKnow = QListWidget()
        self.lbxLanguagesIKnow.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lbxLanguagesIKnow.itemSelectionChanged.connect(self.evt_lbxLanguagesIKnow_selection)

        self.btnAddLanguage = QPushButton("-->")
        self.btnAddLanguage.clicked.connect(self.evt_btnAdd_clicked)

        self.btnRemoveLanguage = QPushButton("<--")
        self.btnRemoveLanguage.clicked.connect(self.evt_btnRemove_clicked)

        self.btnDoSomething = QPushButton("Do Something")
        self.btnDoSomething.clicked.connect(self.evt_btnDoSomething_clicked)

        self.setupLayout()

    def setupLayout(self):
        self.lytMain = QVBoxLayout()
        self.lytLists = QHBoxLayout()
        self.lytButtons = QVBoxLayout()

        ###### Add widgets to lytLists
        self.lytLists.addWidget(self.lbxLanguages)
        self.lytLists.addLayout(self.lytButtons)
        self.lytLists.addWidget(self.lbxLanguagesIKnow)

        ###### Add widgets to lytMain
        self.lytMain.addLayout(self.lytLists)
        self.lytMain.addWidget(self.btnDoSomething)

        ##### Add widgets to lytButtons
        self.lytButtons.addStretch()
        self.lytButtons.addWidget(self.btnAddLanguage)
        self.lytButtons.addWidget(self.btnRemoveLanguage)
        self.lytButtons.addStretch()

        self.setLayout(self.lytMain)

    #######   Event Handlers
    def evt_btnAdd_clicked(self):
        lstItems = self.lbxLanguages.selectedItems()
        for itm in lstItems:
            QLWI = self.lbxLanguages.takeItem(self.lbxLanguages.row(itm))
            self.lbxLanguagesIKnow.addItem(QLWI)
        self.lbxLanguagesIKnow.sortItems()
        self.btnDoSomething.setDefault(True)
        self.repaint()
        self.lbxLanguagesIKnow.repaint()

    def evt_btnRemove_clicked(self):
        lstItems = self.lbxLanguagesIKnow.selectedItems()
        for itm in lstItems:
            QLWI = self.lbxLanguagesIKnow.takeItem(self.lbxLanguagesIKnow.row(itm))
            self.lbxLanguages.addItem(QLWI)
        self.lbxLanguages.sortItems()
        self.btnDoSomething.setDefault(True)
        self.repaint()
        self.lbxLanguages.repaint()

    def evt_lbxLanguages_selection(self):
        self.btnAddLanguage.setDefault(True)
        self.repaint()

    def evt_lbxLanguagesIKnow_selection(self):
        self.btnRemoveLanguage.setDefault(True)
        self.repaint()

    def evt_btnDoSomething_clicked(self):
        if self.lbxLanguagesIKnow.count() == 0:
            QMessageBox.information(self, "Languages", "Wow you don't know any languages!!!")
        else:
            sLanguages = ""
            for row in range(self.lbxLanguagesIKnow.count()):
                sLanguages += self.lbxLanguages.item(row).text() + "\n"
            QMessageBox.information(self, "Languages", "Wow, you know {} languages!!!\n\n{}".format(self.lbxLanguagesIKnow.count(), sLanguages))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
