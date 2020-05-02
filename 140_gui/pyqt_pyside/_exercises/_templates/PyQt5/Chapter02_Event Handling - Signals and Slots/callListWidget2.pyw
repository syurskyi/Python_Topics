_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoListWidget2 _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.listWidgetDiagnosis.itemSelectionChanged.c..(dispSelectedTest)
        s..

    ___ dispSelectedTest 
        ui.listWidgetSelectedTests.clear()
        items = ui.listWidgetDiagnosis.selectedItems()
        x=[]
        for i in list(items
            ui.listWidgetSelectedTests.addItem(i.text())
            x.append(st.(i.text()))
        
__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
