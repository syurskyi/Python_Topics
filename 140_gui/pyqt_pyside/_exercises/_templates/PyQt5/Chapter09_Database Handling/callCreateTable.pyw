_____ _3, ___
____ ?.?W.. _____ ?D.., ?A..
____ _3 _____ E..

____ demoCreateTable _____ *

tabledefinition_""
c_ MyForm(?D..

    ___  -
        s__. - 
        ui _ ?
        ?.sU..
        ?.pushButtonCreateTable.c___.c..(createTable)
        ?.pushButtonAddColumn.c___.c..(addColumns)
        s..

    ___ addColumns
        g.. tabledefinition
        __ tabledefinition__"":
            tabledefinition_"CREATE TABLE IF NOT EXISTS "+ ?.lineEditTableName.t..+"("+?.lineEditColumnName.t..+" "+?.comboBoxDataType.iT..(?.comboBoxDataType.cI..())
        ____
            tabledefinition+_", "+?.lineEditColumnName.t..+" "+?.comboBoxDataType.iT..(?.comboBoxDataType.cI..())
        ?.lineEditColumnName.sT..("")
        ?.lineEditColumnName.sF..

    ___ createTable
        g.. tabledefinition
        ___
            conn _ _3.c..(?.lineEditDBName.t..+".db")
            ?.lR___.sT..("Database is connected")
            c _ conn.c..
            tabledefinition+_");"
            c.e..(tabledefinition)
            ?.lR___.sT..("Table is successfully created")
        _____ E.. __ e:
            ?.lR___.sT..("Error in creating table")
        f..
            conn.c..

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
