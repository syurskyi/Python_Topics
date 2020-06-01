____ os.path ______ exists
____ ?.?W.. ______ *
____ ?.QtSql ______ *

______ sys

if not exists("projects.db"):
    print("File projects.db does not exist. Please run initdb.py.")
    sys.exit()

app _ ?
db _ QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("projects.db")
db.open()
model _ QSqlTableModel(None, db)
model.setTable("projects")
model.select()
view _ QTableView()
view.setModel(model)
view.s..
app.e..