_____ _3, ___
____ ?.?W.. _____ ?D.., ?A..,?TWI..
____ _3 _____ E..

____ demoDisplayRowsOfTable _____ *


c_ MyForm(?D..

    ___  -  
        s__. - 
        ui _ ?
        ?.sU..
        ?.pushButtonDisplayRows.c___.c..(DisplayRows)
        s..

    ___ DisplayRows 
        sqlStatement_"SELECT * FROM "+?.lineEditTableName.t..
        ___
            conn _ _3.c..(?.lineEditDBName.t..+".db")
            cur _ conn.c..
            cur.e..(sqlStatement)
            rows _ cur.fetchall
            rowNo_0
            ___ tuple __ rows:
                ?.lR___.sT..("")
                colNo_0
                ___ columns __ tuple:
                    oneColumn_QTableWidgetItem(columns)
                    ?.tableWidget.sI..(rowNo, colNo, oneColumn)
                    colNo+_1
                rowNo+_1                  
                
        _____ E.. __ e:
            ?.tableWidget.c..
            ?.lR___.sT..("Error in accessing table")
        f..
            conn.c..

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
