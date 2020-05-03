_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoDeleteUser _____ *

c_ MyForm(?D..

    ___  -  
        s__. - ()
        ui _ ?
        ?.sU..
        ?.pushButtonDelete.c___.c..(DeleteUser)
        ?.pushButtonYes.c___.c..(ConfirmDelete)
        ?.labelSure.hide()
        ?.pushButtonYes.hide()
        ?.pushButtonNo.hide()
        s..

    ___ DeleteUser 
        selectStatement_"SELECT * FROM Users where EmailAddress like '"+?.lineEditEmailAddress.t..()+"' and Password like '"+ ?.lineEditPassword.t..()+"'"
        ___
            conn _ sqlite3.c..("ECommerce.db")
            cur _ conn.cursor()
            cur.execute(selectStatement)
            row _ cur.fetchone()
            __ row__None:
                ?.labelSure.hide()
                ?.pushButtonYes.hide()
                ?.pushButtonNo.hide()
                ?.lR___.sT..("Sorry, Incorrect email address or password ")
            ____
                ?.labelSure.s..
                ?.pushButtonYes.s..
                ?.pushButtonNo.s..
                ?.lR___.sT..("")
        _____ Error __ e:
            ?.lR___.sT..("Error in accessing user account")
        f..
            conn.c..

    ___ ConfirmDelete 
        deleteStatement_"DELETE FROM Users where EmailAddress like '"+?.lineEditEmailAddress.t..()+"' and Password like '"+ ?.lineEditPassword.t..()+"'"
        ___
            conn _ sqlite3.c..("ECommerce.db")
            cur _ conn.cursor()
            w__ conn:
                cur.execute(deleteStatement)
                ?.lR___.sT..("User successfully deleted")
        _____ Error __ e:
            ?.lR___.sT..("Error in deleting user account")
        f..
            conn.c..

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
