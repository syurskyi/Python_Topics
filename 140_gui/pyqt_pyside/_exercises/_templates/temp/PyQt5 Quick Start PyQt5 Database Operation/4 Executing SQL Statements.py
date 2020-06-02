______ ___
____ ?.?S.. ______ ?SD.., QSqlQuery
____ ?.?C.. ______ *

___ createDB
    db _ ?SD...aD..("QSQLITE")
    db.sDN..("test.db")
    __ db.o..
        query _ QSqlQuery()
        query.exec_("create table person(id int primary key, name varchar(20), address varchar(30))")
        query.exec_("insert into person values(1, 'Bauer', 'beijing')")
        query.exec_("insert into person values(2, 'Jack', 'shanghai')")
        query.exec_("insert into person values(3, 'Alex', 'chengdu')")

        db.c..

__ __name__ __ "__main__":
    app _  ?CA..(___.a..
    createDB()
    ___.e.. ?.e..