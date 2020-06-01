____ ? ______ QtSql, ?G.., ?W..


___ createDB
    db _ QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('sports.db')

    __ no. db.o..
        ?G...?MB...critical(N.., ?G...qApp.tr("Cannot open database"),
                                   ?G...qApp.tr("Unable to establish a database connection.\n"
                                                 "This example needs SQLite support. Please read "
                                                 "the Qt SQL driver documentation for information "
                                                 "how to build it.\n\n" "Click Cancel to exit."),
                                   ?G...?MB...Cancel)

        r_ False

    query _ QtSql.QSqlQuery()

    query.exec_("create table sportsmen(id int primary key, "
                "firstname varchar(20), lastname varchar(20))")

    query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
    query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
    query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
    query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
    query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
    r_ True


__ __name__ == '__main__':
    ______ sys

    app _ ?W...?A..(sys.argv)
    createDB()