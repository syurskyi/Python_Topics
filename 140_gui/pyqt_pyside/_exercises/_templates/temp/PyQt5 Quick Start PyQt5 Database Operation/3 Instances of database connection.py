______ sys
____ ?.QtSql ______ QSqlDatabase
____ ?.?C.. ______ *

__ __name__ == "__main__":
    app _ QCoreApplication(sys.argv)
    db _ QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("test.db")
    __ db.o..
        print("open DB success.")
    sys.exit(app.exec_())