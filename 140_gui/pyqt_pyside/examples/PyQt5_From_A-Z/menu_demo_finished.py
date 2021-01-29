import sys,os
from PyQt5.QtWidgets import *
from ui_modules.menu_demo_ui import *
import treewidget_finished


class MenuMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MenuMain, self).__init__()
        self.setupUi(self)

        self.lytMain = QHBoxLayout()
        self.centralwidget.setLayout(self.lytMain)
        self.lytMain.addWidget(self.splitter)

        self.btn = QPushButton("Push Me")
        self.statusbar.addPermanentWidget(self.btn)

        self.prg = QProgressBar()
        self.prg.setValue(50)
        self.prg.setStyle(QStyleFactory.create("Windows"))
        self.statusbar.addPermanentWidget(self.prg)

        self.listWidget.addItems(os.listdir("ui/"))

        self.actionOpen.triggered.connect(self.evt_open_triggered)
        self.actionQuit.triggered.connect(self.evt_quit_triggered)
        self.actionHelp.triggered.connect(self.evt_help_triggered)
        self.listWidget.itemDoubleClicked.connect(self.evt_lst_dbl)

    def evt_help_triggered(self):
        dlgTrw = treewidget_finished.DlgMain()
        dlgTrw.show()
        dlgTrw.exec_()

    def evt_lst_dbl(self, lwi):
        #QMessageBox.information(self, "File", "You selected {}".format(lwi.text()))
        f = open("ui/"+lwi.text())
        self.plainTextEdit.setPlainText(f.read())

    def evt_open_triggered(self):
        sFile, sFilter = QFileDialog.getOpenFileName(self, "Open File", "ui/", "Any Text File (*.*)")
        if sFile:
            f = open(sFile)
            self.plainTextEdit.setPlainText(f.read())
        else:
            print("CANCELED BY USER!!!!")

    def evt_quit_triggered(self):
        sys.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mnuMain = MenuMain()
    mnuMain.show()
    sys.exit(app.exec_())
