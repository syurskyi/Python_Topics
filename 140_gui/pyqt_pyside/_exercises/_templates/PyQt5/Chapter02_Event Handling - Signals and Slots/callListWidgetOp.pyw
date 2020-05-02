_____ ___

____ ?.?W.. _____ ?D.., ?A.., QInputDialog, QListWidgetItem

____ demoListWidgetOp _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.listWidget.addItem('Ice Cream')
        ui.listWidget.addItem('Soda')
        ui.listWidget.addItem('Coffee')
        ui.listWidget.addItem('Chocolate')
        ui.pushButtonAdd.c___.c..(addlist)
        ui.pushButtonEdit.c___.c..(editlist)
        ui.pushButtonDelete.c___.c..(delitem)
        ui.pushButtonDeleteAll.c___.c..(delallitems)
        s..

    ___ addlist 
        ui.listWidget.addItem(ui.lineEdit.t..())
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
        ui.listWidget.clear()

        
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
