______ sys
____ ?.QtSql ______ QSqlDatabase
____ ?.QtCore ______ *

if __name__ == "__main__":
    app _ QCoreApplication(sys.argv)
    db _ QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("test.db")
    if db.open
        print("open DB success.")
    sys.exit(app.exec_())