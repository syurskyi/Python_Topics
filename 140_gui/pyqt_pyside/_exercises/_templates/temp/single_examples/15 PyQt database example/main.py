____ os.path ______ exists
____ ?.QtWidgets ______ *
____ ?.QtSql ______ *

______ ___

__ not exists("projects.db"):
    print("File projects.db does not exist. Please run initdb.py.")
    ___.exit()

app _ ?A..([])
db _ QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("projects.db")
db.open()
model _ QSqlTableModel(None, db)
model.setTable("projects")
model.select()
view _ QTableView()
view.sM..(model)
view.s..
app.exec_()