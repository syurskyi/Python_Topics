import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("test.db")
        self.db.open()

    def closeEvent(self, event):
        self.db.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())