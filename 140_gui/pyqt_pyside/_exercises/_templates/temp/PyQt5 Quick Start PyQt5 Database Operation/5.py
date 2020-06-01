______ ___
____ ?.?S.. ______ ?SD.., QSqlQuery
____ ?.?C.. ______ *
____ ?.?W.. ______ *

c_ MainWindow(QWidget):
    ___  -   parent_None):
        super(MainWindow, self). - (parent)
        db _ ?SD...aD..("QSQLITE")
        db.sDN..("test.db")
        db.o..()

    ___ closeEvent  event):
        db.close()

__ __name__ == "__main__":
    app _ ?A..(___.a..
    window _ MainWindow()
    window.s..
    ___.e..(app.exec_())