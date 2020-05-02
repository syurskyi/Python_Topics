_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoInsertRowsInTable _____ *

c_ MyForm(?D..

    ___  -
        s__. - ()
        ui _ ?
        ui.sU..
        ui.pushButtonInsertRow.c___.c..(InsertRows)
        s..

    ___ InsertRows
        sqlStatement_"INSERT INTO "+ui.lineEditTableName.t..()+" VALUES('"+ui.lineEditEmailAddress.t..()+"', '"+ui.lineEditPassword.t..()+"')"
        try:
            conn _ sqlite3.c..(ui.lineEditDBName.t..()+".db")
            with conn:
                cur _ conn.cursor()
                cur.execute(sqlStatement)
                conn.commit()
            ui.lR___.sT..("Row successfully inserted")
        except Error as e:
            ui.lR___.sT..("Error in inserting row")
        finally:
            conn.close()

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e..(app.e
