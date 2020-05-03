_____ _3, ___
____ ?.?W.. _____ ?D.., ?A..
____ _3 _____ E..

____ demoInsertRowsInTable _____ *

c_ MyForm(?D..

    ___  -
        s__. -
        ui _ ?
        ?.sU..
        ?.pushButtonInsertRow.c___.c..(InsertRows)
        s..

    ___ InsertRows
        sqlStatement_"INSERT INTO "+?.lineEditTableName.t..+" VALUES('"+?.lineEditEmailAddress.t..+"', '"+?.lineEditPassword.t..+"')"
        ___
            conn _ _3.c..(?.lineEditDBName.t..+".db")
            w__ conn:
                cur _ conn.c..
                cur.e..(sqlStatement)
                conn.commit
            ?.lR___.sT..("Row successfully inserted")
        _____ E.. __ e:
            ?.lR___.sT..("Error in inserting row")
        f..
            conn.c..

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
