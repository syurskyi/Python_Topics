_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..,QTableWidgetItem
____ sqlite3 _____ Error

____ demoDisplayRowsOfTable _____ *


c_ MyForm(?D..

    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        ui.pushButtonDisplayRows.c___.c..(DisplayRows)
        s..

    ___ DisplayRows 
        sqlStatement_"SELECT * FROM "+ui.lineEditTableName.t..()
        try:
            conn _ sqlite3.c..(ui.lineEditDBName.t..()+".db")
            cur _ conn.cursor()    
            cur.execute(sqlStatement)
            rows _ cur.fetchall()
            rowNo_0
            ___ tuple __ rows:
                ui.lR___.sT..("")
                colNo_0
                ___ columns __ tuple:
                    oneColumn_QTableWidgetItem(columns)
                    ui.tableWidget.setItem(rowNo, colNo, oneColumn)
                    colNo+_1
                rowNo+_1                  
                
        except Error as e:
            ui.tableWidget.c..
            ui.lR___.sT..("Error in accessing table")
        finally:
            conn.close()

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e
