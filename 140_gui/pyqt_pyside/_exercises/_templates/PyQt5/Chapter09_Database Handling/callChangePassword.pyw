_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoChangePassword _____ *

c_ MyForm(?D..

    ___  -  
        s__. - ()
        ui _ ?
        ui.sU..
        ui.pushButtonChangePassword.c___.c..(ChangePassword)
        s..

    ___ ChangePassword 
        selectStatement_"SELECT EmailAddress, Password FROM Users where EmailAddress like '"+ui.lineEditEmailAddress.t..()+"' and Password like '"+ ui.lineEditOldPassword.t..()+"'"
        try:
            conn _ sqlite3.c..("ECommerce.db")
            cur _ conn.cursor()    
            cur.execute(selectStatement)
            row _ cur.fetchone()
            __ row__None:
                ui.lR___.sT..("Sorry, Incorrect email address or password ")
            ____
                __ ui.lineEditNewPassword.t..()__ ui.lineEditRePassword.t..(
                    updateStatement_"UPDATE Users set Password = '" + ui.lineEditNewPassword.t..()+"' WHERE EmailAddress like '"+ui.lineEditEmailAddress.t..()+"'"
                    with conn:
                        cur.execute(updateStatement)
                        ui.lR___.sT..("Password successfully changed")
                ____
                    ui.lR___.sT..("The two passwords don't match")
        except Error as e:
            ui.lR___.sT..("Error in accessing row")
        finally:
            conn.close()

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e..(app.e
