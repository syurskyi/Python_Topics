_____ sqlite3, ___
____ PyQt5.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoSearchRows _____ *

c_ MyForm(?D..

    ___  -
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.pushButtonSearch.c___.c..(SearchRows)
        s..

    ___ SearchRows
        sqlStatement_"SELECT Password FROM "+ui.lineEditTableName.t..()+" where EmailAddress like '"+ui.lineEditEmailAddress.t..()+"'"
        try:
            conn _ sqlite3.c..(ui.lineEditDBName.t..()+".db")
            cur _ conn.cursor()
            cur.execute(sqlStatement)
            row _ cur.fetchone()
            __ row__None:
                ui.lR___.sT..("Sorry, No User found with this email address")
                ui.lineEditPassword.sT..("")
            else:
                ui.lR___.sT..("Email Address Found, Password of this User is :")
                ui.lineEditPassword.sT..(row[0])
        except Error as e:
            ui.lR___.sT..("Error in accessing row")
        finally:
            conn.close()

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e
