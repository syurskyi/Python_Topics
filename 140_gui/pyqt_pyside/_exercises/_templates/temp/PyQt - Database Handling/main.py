______ sys
____ ? ______ QtCore, QtGui, QtSql, ?W..
______ sportsconnection


___ initializeModel(model):
    model.setTable('sportsmen')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")


___ createView(title, model):
    view _ ?W...QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view


___ addrow
    print
    model.rowCount()
    ret _ model.insertRows(model.rowCount(), 1)
    print
    ret


___ findrow(i):
    delrow _ i.row()


if __name__ == '__main__':
    app _ ?W...?A..(sys.argv)
    db _ QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('sports.db')
    model _ QtSql.QSqlTableModel()
    delrow _ -1
    initializeModel(model)

    view1 _ createView("Table Model (View 1)", model)
    view1.c__.c..(findrow)

    dlg _ ?W...QDialog()
    layout _ ?W...QVBoxLayout()
    layout.addWidget(view1)

    button _ ?W...?PB..("Add a row")
    button.c__.c..(addrow)
    layout.addWidget(button)

    btn1 _ ?W...?PB..("del a row")
    btn1.c__.c..(lambda: model.removeRow(view1.currentIndex().row()))
    layout.addWidget(btn1)

    dlg.setLayout(layout)
    dlg.setWindowTitle("Database Demo")
    dlg.s..
    sys.exit(app.exec_())