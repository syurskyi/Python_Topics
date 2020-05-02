_____ ___

____ ?.?W.. _____ ?D.., ?A.., QInputDialog, QListWidgetItem

____ demoListWidgetOp _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.listWidget.addItem('Ice Cream')
        ui.listWidget.addItem('Soda')
        ui.listWidget.addItem('Coffee')
        ui.listWidget.addItem('Chocolate')
        ui.pushButtonAdd.clicked.c..(addlist)
        ui.pushButtonEdit.clicked.c..(editlist)
        ui.pushButtonDelete.clicked.c..(delitem)
        ui.pushButtonDeleteAll.clicked.c..(delallitems)
        s..

    ___ addlist 
        ui.listWidget.addItem(ui.lineEdit.text())
        ui.lineEdit.sT..('')
        ui.lineEdit.setFocus()
        
    ___ editlist 
        row=ui.listWidget.currentRow()
        newtext, ok=QInputDialog.getText , "Enter new text", "Enter new text")
        __ ok and (len(newtext) !=0
            ui.listWidget.takeItem(ui.listWidget.currentRow())
            ui.listWidget.insertItem(row,QListWidgetItem(newtext))
        
    ___ delitem 
        ui.listWidget.takeItem(ui.listWidget.currentRow())
       
    ___ delallitems 
        ui.listWidget.clear()

        
__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
