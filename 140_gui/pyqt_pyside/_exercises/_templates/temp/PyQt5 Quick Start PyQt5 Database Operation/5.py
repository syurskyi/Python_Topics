______ sys
____ ?.QtSql ______ QSqlDatabase, QSqlQuery
____ ?.QtCore ______ *
____ ?.?W.. ______ *

class MainWindow(QWidget):
    ___ __init__(self, parent_None):
        super(MainWindow, self).__init__(parent)
        self.db _ QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("test.db")
        self.db.open()

    ___ closeEvent(self, event):
        self.db.close()

if __name__ == "__main__":
    app _ ?A..(sys.argv)
    window _ MainWindow()
    window.s..
    sys.exit(app.exec_())