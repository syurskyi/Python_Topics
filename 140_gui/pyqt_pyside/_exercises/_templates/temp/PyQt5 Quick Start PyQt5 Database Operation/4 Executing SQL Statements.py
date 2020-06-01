______ sys
____ ?.QtSql ______ QSqlDatabase, QSqlQuery
____ ?.?C.. ______ *

___ createDB
    db _ QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("test.db")
    __ db.o..
        query _ QSqlQuery()
        query.exec_("create table person(id int primary key, name varchar(20), address varchar(30))")
        query.exec_("insert into person values(1, 'Bauer', 'beijing')")
        query.exec_("insert into person values(2, 'Jack', 'shanghai')")
        query.exec_("insert into person values(3, 'Alex', 'chengdu')")

        db.close()

__ __name__ == "__main__":
    app _ QCoreApplication(sys.argv)
    createDB()
    sys.exit(app.exec_())