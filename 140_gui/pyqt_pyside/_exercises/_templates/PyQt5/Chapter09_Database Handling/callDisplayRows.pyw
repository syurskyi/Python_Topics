_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..,QTableWidgetItem
____ sqlite3 _____ Error

____ demoDisplayRowsOfTable _____ *


c_ MyForm(?D..

    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonDisplayRows.clicked.c..(DisplayRows)
        s..

    ___ DisplayRows 
        sqlStatement="SELECT * FROM "+ui.lineEditTableName.text()
        try:
            conn = sqlite3.c..(ui.lineEditDBName.text()+".db")
            cur = conn.cursor()    
            cur.execute(sqlStatement)
            rows = cur.fetchall()
            rowNo=0
            for tuple in rows:
                ui.labelResponse.sT..("")
                colNo=0
                for columns in tuple:
                    oneColumn=QTableWidgetItem(columns)
                    ui.tableWidget.setItem(rowNo, colNo, oneColumn)
                    colNo+=1
                rowNo+=1                  
                
        except Error as e:
            ui.tableWidget.clear()
            ui.labelResponse.sT..("Error in accessing table")
        finally:
            conn.close()

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
