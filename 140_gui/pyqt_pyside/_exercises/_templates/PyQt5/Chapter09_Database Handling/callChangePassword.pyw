_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoChangePassword _____ *

c_ MyForm(?D..

    ___  -  
        s__. - 
        ui _ ?
        ?.sU..
        ?.pushButtonChangePassword.c___.c..(ChangePassword)
        s..

    ___ ChangePassword 
        selectStatement_"SELECT EmailAddress, Password FROM Users where EmailAddress like '"+?.lineEditEmailAddress.t..+"' and Password like '"+ ?.lineEditOldPassword.t..+"'"
        ___
            conn _ sqlite3.c..("ECommerce.db")
            cur _ conn.cursor    
            cur.execute(selectStatement)
            row _ cur.fetchone
            __ row__None:
                ?.lR___.sT..("Sorry, Incorrect email address or password ")
            ____
                __ ?.lineEditNewPassword.t..__ ?.lineEditRePassword.t..(
                    updateStatement_"UPDATE Users set Password = '" + ?.lineEditNewPassword.t..+"' WHERE EmailAddress like '"+?.lineEditEmailAddress.t..+"'"
                    w__ conn:
                        cur.execute(updateStatement)
                        ?.lR___.sT..("Password successfully changed")
                ____
                    ?.lR___.sT..("The two passwords don't match")
        _____ Error __ e:
            ?.lR___.sT..("Error in accessing row")
        f..
            conn.c..

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
