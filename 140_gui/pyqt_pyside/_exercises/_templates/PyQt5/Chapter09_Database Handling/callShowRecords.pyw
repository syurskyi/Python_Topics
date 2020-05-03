_____ sqlite3, ___
____ ?.?W.. _____ ?D.., ?A..,?TWI..
____ sqlite3 _____ Error

____ demoShowRecords _____ *

rowNo_1
sqlStatement_"SELECT EmailAddress, Password FROM Users"
conn _ sqlite3.c..("ECommerce.db")
cur _ conn.cursor()

c_ MyForm(?D..

    ___  -
        s__. - ()
        ui _ ?
        ?.sU..
        cur.execute(sqlStatement)
        ?.pushButtonFirst.c___.c..(ShowFirstRow)
        ?.pushButtonPrevious.c___.c..(ShowPreviousRow)
        ?.pushButtonNext.c___.c..(ShowNextRow)
        ?.pushButtonLast.c___.c..(ShowLastRow)
        s..

    ___ ShowFirstRow
        ___
            cur.execute(sqlStatement)
            row_cur.fetchone()
            __ row:
                ?.lineEditEmailAddress.sT..(row[0])
                ?.lineEditPassword.sT..(row[1])
        _____ Error __ e:
            ?.lR___.sT..("Error in accessing table")


    ___ ShowPreviousRow
        global rowNo
        rowNo -_ 1
        sqlStatement_"SELECT EmailAddress, Password FROM Users where rowid="+st.(rowNo)
        cur.execute(sqlStatement)
        row_cur.fetchone()
        __ row:
            ?.lR___.sT..("")
            ?.lineEditEmailAddress.sT..(row[0])
            ?.lineEditPassword.sT..(row[1])
        ____
            rowNo +_ 1
            ?.lR___.sT..("This is the first row")
       
            
    ___ ShowNextRow
        global rowNo
        rowNo +_ 1
        sqlStatement_"SELECT EmailAddress, Password FROM Users where rowid="+st.(rowNo)
        cur.execute(sqlStatement)
        row_cur.fetchone()
        __ row:
            ?.lR___.sT..("")
            ?.lineEditEmailAddress.sT..(row[0])
            ?.lineEditPassword.sT..(row[1])
        ____
            rowNo -_ 1
            ?.lR___.sT..("This is the last row")

    ___ ShowLastRow
        cur.execute(sqlStatement)
        ___ row in cur.fetchall(
            ?.lineEditEmailAddress.sT..(row[0])
            ?.lineEditPassword.sT..(row[1])

        
__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
