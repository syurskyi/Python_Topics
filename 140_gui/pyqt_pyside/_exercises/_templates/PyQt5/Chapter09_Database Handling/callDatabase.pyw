_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoDatabase _____ *
 
c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.pushButtonCreateDB.c___.c..(createDatabase)
        s..

    ___ createDatabase 
        try:
            conn _ sqlite3.c..(ui.lineEditDBName.t..()+".db")
            ui.lR___.sT..("Database is created")
        except Error as e:
            ui.lR___.sT..("Some error has occurred")
        finally:
            conn.close()

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
