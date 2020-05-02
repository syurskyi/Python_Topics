_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoCreateTable _____ *

tabledefinition_""
c_ MyForm(?D..

    ___  -
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        ui.pushButtonCreateTable.c___.c..(createTable)
        ui.pushButtonAddColumn.c___.c..(addColumns)
        s..

    ___ addColumns
        global tabledefinition         
        __ tabledefinition__"":
            tabledefinition_"CREATE TABLE IF NOT EXISTS "+ ui.lineEditTableName.t..()+"("+ui.lineEditColumnName.t..()+" "+ui.comboBoxDataType.iT..(ui.comboBoxDataType.cI..())
        ____
            tabledefinition+_", "+ui.lineEditColumnName.t..()+" "+ui.comboBoxDataType.iT..(ui.comboBoxDataType.cI..())
        ui.lineEditColumnName.sT..("")
        ui.lineEditColumnName.sF..

    ___ createTable
        global tabledefinition 
        try:
            conn _ sqlite3.c..(ui.lineEditDBName.t..()+".db")
            ui.lR___.sT..("Database is connected")
            c _ conn.cursor()
            tabledefinition+_");"
            c.execute(tabledefinition)
            ui.lR___.sT..("Table is successfully created")
        except Error as e:
            ui.lR___.sT..("Error in creating table")
        finally:
            conn.close()

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ ?
    w.s..
    ___.e..(app.e
