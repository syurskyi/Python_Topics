_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoDatabase _____ *
 
c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonCreateDB.clicked.c..(createDatabase)
        s..

    ___ createDatabase 
        try:
            conn = sqlite3.c..(ui.lineEditDBName.text()+".db")
            ui.labelResponse.sT..("Database is created")
        except Error as e:
            ui.labelResponse.sT..("Some error has occurred")
        finally:
            conn.close()

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
