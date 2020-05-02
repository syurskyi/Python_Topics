_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoInsertRowsInTable _____ *

c_ MyForm(?D..

    ___  -
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.pushButtonInsertRow.clicked.c..(InsertRows)
        s..

    ___ InsertRows
        sqlStatement_"INSERT INTO "+ui.lineEditTableName.text()+" VALUES('"+ui.lineEditEmailAddress.text()+"', '"+ui.lineEditPassword.text()+"')"
        try:
            conn _ sqlite3.c..(ui.lineEditDBName.text()+".db")
            with conn:
                cur _ conn.cursor()
                cur.execute(sqlStatement)
                conn.commit()
            ui.labelResponse.sT..("Row successfully inserted")
        except Error as e:
            ui.labelResponse.sT..("Error in inserting row")
        finally:
            conn.close()

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
