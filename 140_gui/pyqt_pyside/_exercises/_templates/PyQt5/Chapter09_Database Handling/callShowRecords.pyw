_____ _3, ___
____ ?.?W.. _____ ?D.., ?A..,?TWI..
____ _3 _____ E..

____ demoShowRecords _____ *

rowNo_1
sqlStatement_"SELECT EmailAddress, Password FROM Users"
conn _ _3.c..("ECommerce.db")
cur _ conn.c..

c_ MyForm(?D..

    ___  -
        s__. -
        ui _ ?
        ?.sU..
        cur.e..(sqlStatement)
        ?.pushButtonFirst.c___.c..(ShowFirstRow)
        ?.pushButtonPrevious.c___.c..(ShowPreviousRow)
        ?.pushButtonNext.c___.c..(ShowNextRow)
        ?.pushButtonLast.c___.c..(ShowLastRow)
        s..

    ___ ShowFirstRow
        ___
            cur.e..(sqlStatement)
            row_cur.f..
            __ row:
                ?.lineEditEmailAddress.sT..(row[0])
                ?.lineEditPassword.sT..(row[1])
        _____ E.. __ e:
            ?.lR___.sT..("Error in accessing table")


    ___ ShowPreviousRow
        g.. rowNo
        rowNo -_ 1
        sqlStatement_"SELECT EmailAddress, Password FROM Users where rowid="+st.(rowNo)
        cur.e..(sqlStatement)
        row_cur.f..
        __ row:
            ?.lR___.sT..("")
            ?.lineEditEmailAddress.sT..(row[0])
            ?.lineEditPassword.sT..(row[1])
        ____
            rowNo +_ 1
            ?.lR___.sT..("This is the first row")
       
            
    ___ ShowNextRow
        g.. rowNo
        rowNo +_ 1
        sqlStatement_"SELECT EmailAddress, Password FROM Users where rowid="+st.(rowNo)
        cur.e..(sqlStatement)
        row_cur.f..
        __ row:
            ?.lR___.sT..("")
            ?.lineEditEmailAddress.sT..(row[0])
            ?.lineEditPassword.sT..(row[1])
        ____
            rowNo -_ 1
            ?.lR___.sT..("This is the last row")

    ___ ShowLastRow
        cur.e..(sqlStatement)
        ___ row in cur.fetchall(
            ?.lineEditEmailAddress.sT..(row[0])
            ?.lineEditPassword.sT..(row[1])

        
__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
