_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoChangePassword _____ *

c_ MyForm(?D..

    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonChangePassword.clicked.c..(ChangePassword)
        s..

    ___ ChangePassword 
        selectStatement="SELECT EmailAddress, Password FROM Users where EmailAddress like '"+ui.lineEditEmailAddress.text()+"' and Password like '"+ ui.lineEditOldPassword.text()+"'"
        try:
            conn = sqlite3.c..("ECommerce.db")
            cur = conn.cursor()    
            cur.execute(selectStatement)
            row = cur.fetchone()
            __ row__None:
                ui.labelResponse.sT..("Sorry, Incorrect email address or password ")
            else:
                __ ui.lineEditNewPassword.text()__ ui.lineEditRePassword.text(
                    updateStatement="UPDATE Users set Password = '" + ui.lineEditNewPassword.text()+"' WHERE EmailAddress like '"+ui.lineEditEmailAddress.text()+"'"
                    with conn:
                        cur.execute(updateStatement)
                        ui.labelResponse.sT..("Password successfully changed")
                else:
                    ui.labelResponse.sT..("The two passwords don't match")
        except Error as e:
            ui.labelResponse.sT..("Error in accessing row")
        finally:
            conn.close()

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
