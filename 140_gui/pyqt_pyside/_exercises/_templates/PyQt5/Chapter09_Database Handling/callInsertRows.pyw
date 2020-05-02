_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoInsertRowsInTable _____ *

c_ MyForm(?D..

    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonInsertRow.clicked.c..(InsertRows)
        s..

    ___ InsertRows
        sqlStatement="INSERT INTO "+ui.lineEditTableName.text()+" VALUES('"+ui.lineEditEmailAddress.text()+"', '"+ui.lineEditPassword.text()+"')"
        try:
            conn = sqlite3.c..(ui.lineEditDBName.text()+".db")
            with conn:
                cur = conn.cursor()
                cur.execute(sqlStatement)
                conn.commit()
            ui.labelResponse.sT..("Row successfully inserted")
        except Error as e:
            ui.labelResponse.sT..("Error in inserting row")
        finally:
            conn.close()

__ __name____"__main__":
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
