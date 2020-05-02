_____ ___

____ ?.?W.. _____ ?D.., ?A.., QInputDialog, QListWidgetItem

____ demoListWidgetOp _____ _

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        ui.listWidget.aI..('Ice Cream')
        ui.listWidget.aI..('Soda')
        ui.listWidget.aI..('Coffee')
        ui.listWidget.aI..('Chocolate')
        ui.pushButtonAdd.c___.c..(addlist)
        ui.pushButtonEdit.c___.c..(editlist)
        ui.pushButtonDelete.c___.c..(delitem)
        ui.pushButtonDeleteAll.c___.c..(delallitems)
        s..

    ___ addlist 
        ui.listWidget.aI..(ui.lineEdit.t..())
        ui.lineEdit.sT..('')
        ui.lineEdit.setFocus()
        
    ___ editlist 
        row_ui.listWidget.currentRow()
        newtext, ok_QInputDialog.getText , "Enter new text", "Enter new text")
        __ ok and (len(newtext) !_0
            ui.listWidget.takeItem(ui.listWidget.currentRow())
            ui.listWidget.insertItem(row,QListWidgetItem(newtext))
        
    ___ delitem 
        ui.listWidget.takeItem(ui.listWidget.currentRow())
       
    ___ delallitems 
        ui.listWidget.c..

        
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e
