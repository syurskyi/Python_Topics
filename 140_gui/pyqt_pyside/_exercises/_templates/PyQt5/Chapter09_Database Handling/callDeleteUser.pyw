_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoDeleteUser _____ *

c_ MyForm(?D..

    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        ui.pushButtonDelete.c___.c..(DeleteUser)
        ui.pushButtonYes.c___.c..(ConfirmDelete)
        ui.labelSure.hide()
        ui.pushButtonYes.hide()
        ui.pushButtonNo.hide()       
        s..

    ___ DeleteUser 
        selectStatement_"SELECT * FROM Users where EmailAddress like '"+ui.lineEditEmailAddress.t..()+"' and Password like '"+ ui.lineEditPassword.t..()+"'"
        try:
            conn _ sqlite3.c..("ECommerce.db")
            cur _ conn.cursor()
            cur.execute(selectStatement)
            row _ cur.fetchone()
            __ row__None:
                ui.labelSure.hide()
                ui.pushButtonYes.hide()
                ui.pushButtonNo.hide()   
                ui.lR___.sT..("Sorry, Incorrect email address or password ")
            ____
                ui.labelSure.s..
                ui.pushButtonYes.s..
                ui.pushButtonNo.s..
                ui.lR___.sT..("")
        except Error as e:
            ui.lR___.sT..("Error in accessing user account")
        finally:
            conn.close()

    ___ ConfirmDelete 
        deleteStatement_"DELETE FROM Users where EmailAddress like '"+ui.lineEditEmailAddress.t..()+"' and Password like '"+ ui.lineEditPassword.t..()+"'"
        try:
            conn _ sqlite3.c..("ECommerce.db")
            cur _ conn.cursor()
            with conn:
                cur.execute(deleteStatement)
                ui.lR___.sT..("User successfully deleted")
        except Error as e:
            ui.lR___.sT..("Error in deleting user account")
        finally:
            conn.close()

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e
