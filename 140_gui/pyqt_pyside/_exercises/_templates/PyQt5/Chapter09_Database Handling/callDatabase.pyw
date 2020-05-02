_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..
____ sqlite3 _____ Error

____ demoDatabase _____ *
 
c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.pushButtonCreateDB.clicked.c..(createDatabase)
        s..

    ___ createDatabase 
        try:
            conn _ sqlite3.c..(ui.lineEditDBName.text()+".db")
            ui.labelResponse.sT..("Database is created")
        except Error as e:
            ui.labelResponse.sT..("Some error has occurred")
        finally:
            conn.close()

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
