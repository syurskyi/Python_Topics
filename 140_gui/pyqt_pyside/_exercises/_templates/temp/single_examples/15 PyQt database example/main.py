____ os.path ______ exists
____ ?.QtWidgets ______ *
____ ?.QtSql ______ *

______ ___

if not exists("projects.db"):
    print("File projects.db does not exist. Please run initdb.py.")
    ___.exit()

app = ?A..([])
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("projects.db")
db.open()
model = QSqlTableModel(None, db)
model.setTable("projects")
model.select()
view = QTableView()
view.sM..(model)
view.s..
app.exec_()