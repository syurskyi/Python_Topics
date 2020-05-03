_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoSearchRows _____ *

c_ MyForm(?D..

    ___  -
        s__. -
        ui _ ?
        ?.sU..
        ?.pushButtonSearch.c___.c..(SearchRows)
        s..

    ___ SearchRows
        sqlStatement_"SELECT Password FROM "+?.lineEditTableName.t..+" where EmailAddress like '"+?.lineEditEmailAddress.t..+"'"
        ___
            conn _ sqlite3.c..(?.lineEditDBName.t..+".db")
            cur _ conn.cursor
            cur.execute(sqlStatement)
            row _ cur.fetchone
            __ row__None:
                ?.lR___.sT..("Sorry, No User found with this email address")
                ?.lineEditPassword.sT..("")
            ____
                ?.lR___.sT..("Email Address Found, Password of this User is :")
                ?.lineEditPassword.sT..(row[0])
        _____ Error __ e:
            ?.lR___.sT..("Error in accessing row")
        f..
            conn.c..

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
