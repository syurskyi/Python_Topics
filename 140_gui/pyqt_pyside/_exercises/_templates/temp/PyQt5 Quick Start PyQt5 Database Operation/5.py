______ ___
____ ?.?S.. ______ ?SD.., QSqlQuery
____ ?.?C.. ______ *
____ ?.?W.. ______ *

c_ MainWindow(QWidget):
    ___ __init__  parent_None):
        super(MainWindow, self).__init__(parent)
        self.db _ ?SD...aD..("QSQLITE")
        self.db.sDN..("test.db")
        self.db.o..()

    ___ closeEvent  event):
        self.db.close()

__ __name__ == "__main__":
    app _ ?A..(___.argv)
    window _ MainWindow()
    window.s..
    ___.exit(app.exec_())