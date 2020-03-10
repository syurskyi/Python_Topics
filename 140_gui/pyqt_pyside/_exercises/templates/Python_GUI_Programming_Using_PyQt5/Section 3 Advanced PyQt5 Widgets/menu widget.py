import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Widget")
        self.setGeometry(350, 150, 600, 600)
        self.ui()

    def ui(self):
        # #########################Main Menu###############
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        code = menubar.addMenu("Code")
        helpMenu = menubar.addMenu("Help")

        # ##########################Sub Menu Items################
        new = QAction("New Project", self)
        new.setShortcut("Ctrl+O")
        file.addAction(new)
        open = QAction("Open", self)
        file.addAction(open)
        exit = QAction("Exit", self)
        exit.setIcon((QIcon("icons/exit.png")))
        exit.triggered.connect(self.exit_func)
        file.addAction(exit)
        # ###############ToolBar###################
        tb = self.addToolBar("My Toolbar")
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        new_tb = QAction(QIcon('icons/folder.png'), "New", self)
        tb.addAction(new_tb)
        open_tb = QAction(QIcon('icons/empty.png'), "Open", self)
        tb.addAction(open_tb)
        save_tb = QAction(QIcon('icons/save.png'), "Save", self)
        tb.addAction(save_tb)
        exit_tb = QAction(QIcon('icons/exit.png'), "Exit", self)
        exit_tb.triggered.connect(self.exit_func)
        tb.addAction(exit_tb)
        tb.actionTriggered.connect(self.btn_func)
        self.combo = QComboBox()
        self.combo.addItems(["Spiderman", "Superman", "Batman"])
        tb.addWidget(self.combo)
        self.show()

    def exit_func(self):
        mbox = QMessageBox.information(self, "Warning", "Are you sure to exit?", QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()

    def btn_func(self, btn):
        if btn.text() == "New":
            print("You clicked new button")
        elif btn.text() =="Open":
            print("You clicked open button")
        else:
            print("You clicked save button")


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
