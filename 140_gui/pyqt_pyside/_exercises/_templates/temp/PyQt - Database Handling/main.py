______ ___
____ ? ______ ?C.., ?G.., ?S.., ?W..
______ sportsconnection


___ initializeModel model
    model.setTable('sportsmen')
    model.setEditStrategy(?S...?STM...OnFieldChange)
    model.select()
    model.setHeaderData(0, ?C...__.Horizontal, "ID")
    model.setHeaderData(1, ?C...__.Horizontal, "First name")
    model.setHeaderData(2, ?C...__.Horizontal, "Last name")


___ createView(title, model):
    view _ ?W...QTableView()
    view.sM..(model)
    view.sWT..(title)
    r_ view


___ addrow
    print
    model.rowCount()
    ret _ model.insertRows(model.rowCount(), 1)
    print
    ret


___ findrow(i):
    delrow _ i.row()


__ ______ __ ______
    app _ ?W...?A..(___.a..
    db _ ?S...?SD...aD..('QSQLITE')
    db.sDN..('sports.db')
    model _ ?S...?STM..()
    delrow _ -1
    initializeModel(model)

    view1 _ createView("Table Model (View 1)", model)
    view1.c__.c..(findrow)

    dlg _ ?W...QDialog()
    layout _ ?W...?VBL..
    layout.aW..(view1)

    button _ ?W...?PB..("Add a row")
    button.c__.c..(addrow)
    layout.aW..(button)

    btn1 _ ?W...?PB..("del a row")
    btn1.c__.c..(lambda: model.removeRow(view1.currentIndex().row()))
    layout.aW..(btn1)

    dlg.sL..(layout)
    dlg.sWT..("Database Demo")
    dlg.s..
    ___.e..(app.exec_())