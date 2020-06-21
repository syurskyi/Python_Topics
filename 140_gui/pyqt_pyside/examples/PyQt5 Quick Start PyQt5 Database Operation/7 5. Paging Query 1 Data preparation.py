db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("/home/user/test.db")
if not db.open():
    return False
query = QSqlQuery()
query.exec_("create table student(id int primary key, name varchar(20), sex varchar(8), age int);")

query.exec_("insert into student values(1, 'Bauer', 'Man', 25)")
query.exec_("insert into student values(2, 'Alex', 'Man', 24)")
query.exec_("insert into student values(3, 'Mary', 'Female', 23)")
query.exec_("insert into student values(4, 'Jack', 'Man', 25)")
query.exec_("insert into student values(5, 'xiaoming', 'Man', 24)")
query.exec_("insert into student values(6, 'xiaohong', 'Female', 23)")
query.exec_("insert into student values(7, 'xiaowang', 'Man', 25)")
query.exec_("insert into student values(8, 'xiaozhang', 'Man', 25)")
query.exec_("insert into student values(9, 'xiaoli', 'Man', 25)")
query.exec_("insert into student values(10, 'xiaohan', 'Man', 25)")