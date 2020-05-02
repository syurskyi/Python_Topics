_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoListWidget2 _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.listWidgetDiagnosis.itemSelectionChanged.c..(dispSelectedTest)
        s..

    ___ dispSelectedTest 
        ui.listWidgetSelectedTests.clear()
        items _ ui.listWidgetDiagnosis.selectedItems()
        x_[]
        for i in list(items
            ui.listWidgetSelectedTests.addItem(i.text())
            x.append(st.(i.text()))
        
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
