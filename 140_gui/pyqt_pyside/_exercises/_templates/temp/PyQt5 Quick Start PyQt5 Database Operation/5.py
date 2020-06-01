______ sys
____ ?.QtSql ______ QSqlDatabase, QSqlQuery
____ ?.?C.. ______ *
____ ?.?W.. ______ *

c_ MainWindow(QWidget):
    ___ __init__  parent_None):
        super(MainWindow, self).__init__(parent)
        self.db _ QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("test.db")
        self.db.o..()

    ___ closeEvent  event):
        self.db.close()

__ __name__ == "__main__":
    app _ ?A..(sys.argv)
    window _ MainWindow()
    window.s..
    sys.exit(app.exec_())