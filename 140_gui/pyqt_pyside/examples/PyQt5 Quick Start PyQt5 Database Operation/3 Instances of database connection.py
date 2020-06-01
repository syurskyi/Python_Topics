import sys
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtCore import *

if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("test.db")
    if db.open():
        print("open DB success.")
    sys.exit(app.exec_())