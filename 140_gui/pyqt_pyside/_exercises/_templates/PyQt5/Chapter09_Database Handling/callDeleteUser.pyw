_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoDeleteUser _____ *

c_ MyForm(?D..

    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonDelete.clicked.c..(DeleteUser)
        ui.pushButtonYes.clicked.c..(ConfirmDelete)
        ui.labelSure.hide()
        ui.pushButtonYes.hide()
        ui.pushButtonNo.hide()       
        s..

    ___ DeleteUser 
        selectStatement="SELECT * FROM Users where EmailAddress like '"+ui.lineEditEmailAddress.text()+"' and Password like '"+ ui.lineEditPassword.text()+"'"
        try:
            conn = sqlite3.c..("ECommerce.db")
            cur = conn.cursor()    
            cur.execute(selectStatement)
            row = cur.fetchone()
            __ row__None:
                ui.labelSure.hide()
                ui.pushButtonYes.hide()
                ui.pushButtonNo.hide()   
                ui.labelResponse.sT..("Sorry, Incorrect email address or password ")
            else:
                ui.labelSure.s..
                ui.pushButtonYes.s..
                ui.pushButtonNo.s..
                ui.labelResponse.sT..("")
        except Error as e:
            ui.labelResponse.sT..("Error in accessing user account")
        finally:
            conn.close()

    ___ ConfirmDelete 
        deleteStatement="DELETE FROM Users where EmailAddress like '"+ui.lineEditEmailAddress.text()+"' and Password like '"+ ui.lineEditPassword.text()+"'"      
        try:
            conn = sqlite3.c..("ECommerce.db")
            cur = conn.cursor()  
            with conn:
                cur.execute(deleteStatement)
                ui.labelResponse.sT..("User successfully deleted")
        except Error as e:
            ui.labelResponse.sT..("Error in deleting user account")
        finally:
            conn.close()

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
