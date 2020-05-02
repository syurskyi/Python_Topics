_____ sqlite3, ___
____ PyQt5.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoSearchRows _____ *

c_ MyForm(?D..

    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonSearch.clicked.c..(SearchRows)
        s..

    ___ SearchRows
        sqlStatement="SELECT Password FROM "+ui.lineEditTableName.text()+" where EmailAddress like '"+ui.lineEditEmailAddress.text()+"'"
        try:
            conn = sqlite3.c..(ui.lineEditDBName.text()+".db")
            cur = conn.cursor()    
            cur.execute(sqlStatement)
            row = cur.fetchone()
            __ row__None:
                ui.labelResponse.sT..("Sorry, No User found with this email address")
                ui.lineEditPassword.sT..("")
            else:
                ui.labelResponse.sT..("Email Address Found, Password of this User is :")
                ui.lineEditPassword.sT..(row[0])
        except Error as e:
            ui.labelResponse.sT..("Error in accessing row")
        finally:
            conn.close()

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
