_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoInsertRowsInTable _____ *

c_ MyForm(?D..

    ___  -
        s__. - ()
        ui _ ?
        ?.sU..
        ?.pushButtonInsertRow.c___.c..(InsertRows)
        s..

    ___ InsertRows
        sqlStatement_"INSERT INTO "+?.lineEditTableName.t..()+" VALUES('"+?.lineEditEmailAddress.t..()+"', '"+?.lineEditPassword.t..()+"')"
        ___
            conn _ sqlite3.c..(?.lineEditDBName.t..()+".db")
            w__ conn:
                cur _ conn.cursor()
                cur.execute(sqlStatement)
                conn.commit()
            ?.lR___.sT..("Row successfully inserted")
        _____ Error __ e:
            ?.lR___.sT..("Error in inserting row")
        f..
            conn.c..

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
