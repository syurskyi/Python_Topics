import sys, time
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.ledTitle = QLineEdit(self.windowTitle(), self)
        self.ledTitle.move(50, 50)
        #self.ledTitle.textChanged.connect(self.evt_ledTitle_textChanged)
        self.btnChange = QPushButton("Update Title", self)
        self.btnChange.move(50, 80)
        self.btnChange.clicked.connect(self.evt_btnChanged_clicked)

        self.ledEdit = QLineEdit("1234567890", self)
        self.ledEdit.move(50, 120)
        self.btnEdit = QPushButton("Start Editing", self)
        self.btnEdit.move(50, 150)
        self.btnEdit.clicked.connect(self.evt_btnEdit_clicked)

    def evt_btnEdit_clicked(self):
        print(self.ledEdit.text())
        print("Move cursor to position 4")
        self.ledEdit.setCursorPosition(4)
        QApplication.processEvents()
        time.sleep(1)
        print("Highlight next 3 characters")
        self.ledEdit.cursorForward(True, 3)
        QApplication.processEvents()
#        QMessageBox.information(self, "Selected", "You selected '{}'".format(self.ledEdit.selectedText()))
        time.sleep(1)
        print("Cut highlighted characters")
        self.ledEdit.cut()
        QApplication.processEvents()
        time.sleep(1)
        print("Move cursor to beginning")
        self.ledEdit.home(False)
        QApplication.processEvents()
        time.sleep(1)
        print("Paste cut text")
        self.ledEdit.paste()
        QApplication.processEvents()
        time.sleep(1)



    def evt_ledTitle_textChanged(self, title):
        print(title)
        self.setWindowTitle(title)

    def evt_btnChanged_clicked(self):
        res = QMessageBox.question(self, "Line Edit", "Are you sure you want to change the window title to '" + self.ledTitle.text() + "'")
        if res == QMessageBox.Yes:
            self.setWindowTitle(self.ledTitle.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
