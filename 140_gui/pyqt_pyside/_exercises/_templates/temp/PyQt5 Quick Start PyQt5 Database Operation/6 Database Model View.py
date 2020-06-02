______ ___
____ ?.?S.. ______ ?SD.., QSqlQuery, ?STM..
____ ?.?C.. ______ *
____ ?.?W.. ______ *

c_ MainWindow(?W..):
    ___  -   parent_None):
        super(MainWindow, self). - (parent)
        db _ ?SD...aD..("QSQLITE")
        db.sDN..("test.db")
        db.o..()
        model _ ?STM..()
        initializedModel()

        tableView _ ?TV..
        tableView.sM..(model)

        layout _ ?VBL..
        addButton _ ?PB..("add")
        deleteButton _ ?PB..("delete")
        hLayout _ QHBoxLayout()
        hLayout.aW..(addButton)
        hLayout.aW..(deleteButton)
        layout.aW..(tableView)
        layout.aL..(hLayout)
        sL..(layout)
        r..(600, 400)

        addButton.c__.c..(onAddRow)
        deleteButton.c__.c..(onDeleteRow)

    ___ initializedModel
        model.setTable("person")
        model.setEditStrategy(?STM...OnFieldChange)
        model.select()
        model.setHeaderData(0, __.H.., "ID")
        model.setHeaderData(1, __.H.., "Name")
        model.setHeaderData(2, __.H.., "Address")

    ___ onAddRow
        model.insertRows(model.rowCount(), 1)
        model.submit()

    ___ onDeleteRow
        model.removeRow(tableView.currentIndex().row())
        model.submit()
        model.select()

    ___ closeEvent  event):
        db.c..

__ __name__ __ "__main__":
    app _ ?A..(___.a..
    window _ MainWindow()
    window.s..
    ___.e.. ?.e..