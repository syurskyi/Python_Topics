_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoCreateTable _____ *

tabledefinition_""
c_ MyForm(?D..

    ___  -
        s__. - ()
        ui _ ?
        ?.sU..
        ?.pushButtonCreateTable.c___.c..(createTable)
        ?.pushButtonAddColumn.c___.c..(addColumns)
        s..

    ___ addColumns
        global tabledefinition         
        __ tabledefinition__"":
            tabledefinition_"CREATE TABLE IF NOT EXISTS "+ ?.lineEditTableName.t..()+"("+?.lineEditColumnName.t..()+" "+?.comboBoxDataType.iT..(?.comboBoxDataType.cI..())
        ____
            tabledefinition+_", "+?.lineEditColumnName.t..()+" "+?.comboBoxDataType.iT..(?.comboBoxDataType.cI..())
        ?.lineEditColumnName.sT..("")
        ?.lineEditColumnName.sF..

    ___ createTable
        global tabledefinition 
        ___
            conn _ sqlite3.c..(?.lineEditDBName.t..()+".db")
            ?.lR___.sT..("Database is connected")
            c _ conn.cursor()
            tabledefinition+_");"
            c.execute(tabledefinition)
            ?.lR___.sT..("Table is successfully created")
        _____ Error __ e:
            ?.lR___.sT..("Error in creating table")
        f..
            conn.c..

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
