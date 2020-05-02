_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoSignInForm _____ *

c_ MyForm(?D..

    ___  -
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.pushButtonSearch.clicked.c..(SearchRows)
        s..

    ___ SearchRows
        sqlStatement_"SELECT EmailAddress, Password FROM Users where EmailAddress like '"+ui.lineEditEmailAddress.text()+"' and Password like '"+ ui.lineEditPassword.text()+"'"
        try:
            conn _ sqlite3.c..("ECommerce.db")
            cur _ conn.cursor()    
            cur.execute(sqlStatement)
            row _ cur.fetchone()
            __ row__None:
                ui.labelResponse.sT..("Sorry, Incorrect email address or password ")
            else:
                ui.labelResponse.sT..("You are welcome ")
        except Error as e:
            ui.labelResponse.sT..("Error in accessing row")
        finally:
            conn.close()

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
