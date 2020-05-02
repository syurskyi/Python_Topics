_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..,QTableWidgetItem
____ sqlite3 _____ Error

____ demoShowRecords _____ *

rowNo=1
sqlStatement="SELECT EmailAddress, Password FROM Users"
conn = sqlite3.c..("ECommerce.db")
cur = conn.cursor()  

c_ MyForm(?D..

    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        cur.execute(sqlStatement)
        ui.pushButtonFirst.clicked.c..(ShowFirstRow)
        ui.pushButtonPrevious.clicked.c..(ShowPreviousRow)
        ui.pushButtonNext.clicked.c..(ShowNextRow)
        ui.pushButtonLast.clicked.c..(ShowLastRow)
        s..

    ___ ShowFirstRow
        try: 
            cur.execute(sqlStatement)
            row=cur.fetchone()
            __ row:
                ui.lineEditEmailAddress.sT..(row[0])
                ui.lineEditPassword.sT..(row[1])
        except Error as e:
            ui.labelResponse.sT..("Error in accessing table")


    ___ ShowPreviousRow
        global rowNo
        rowNo -= 1
        sqlStatement="SELECT EmailAddress, Password FROM Users where rowid="+st.(rowNo)
        cur.execute(sqlStatement)
        row=cur.fetchone()
        __ row:
            ui.labelResponse.sT..("")
            ui.lineEditEmailAddress.sT..(row[0])
            ui.lineEditPassword.sT..(row[1])
        else:
            rowNo += 1
            ui.labelResponse.sT..("This is the first row")
       
            
    ___ ShowNextRow
        global rowNo
        rowNo += 1
        sqlStatement="SELECT EmailAddress, Password FROM Users where rowid="+st.(rowNo)
        cur.execute(sqlStatement)
        row=cur.fetchone()
        __ row:
            ui.labelResponse.sT..("")
            ui.lineEditEmailAddress.sT..(row[0])
            ui.lineEditPassword.sT..(row[1])
        else:
            rowNo -= 1
            ui.labelResponse.sT..("This is the last row")

    ___ ShowLastRow
        cur.execute(sqlStatement)
        for row in cur.fetchall(
            ui.lineEditEmailAddress.sT..(row[0])
            ui.lineEditPassword.sT..(row[1])

        
__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
