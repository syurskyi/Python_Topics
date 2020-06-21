import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import *

def createDB():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("test.db")
    if db.open():
        query = QSqlQuery()
        query.exec_("create table person(id int primary key, name varchar(20), address varchar(30))")
        query.exec_("insert into person values(1, 'Bauer', 'beijing')")
        query.exec_("insert into person values(2, 'Jack', 'shanghai')")
        query.exec_("insert into person values(3, 'Alex', 'chengdu')")

        db.close()

if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    createDB()
    sys.exit(app.exec_())