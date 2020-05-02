_____ ___

____ ?.?W.. _____ ?D..
____ ?.?W.. _____ ?A.., ?W.., ?PB..
____ ?.?C.. _____ py_S..
____ demoCheckBox2 _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.checkBoxChoclateAlmond.sC__.c..(dispAmount)
        ui.checkBoxChoclateChips.sC__.c..(dispAmount)
        ui.checkBoxCookieDough.sC__.c..(dispAmount)
        ui.checkBoxRockyRoad.sC__.c..(dispAmount)
        ui.checkBoxCoffee.sC__.c..(dispAmount)
        ui.checkBoxSoda.sC__.c..(dispAmount)
        ui.checkBoxTea.sC__.c..(dispAmount)

        s..

    @py_S..()
    ___ dispAmount 
        amount=0
        __ ui.checkBoxChoclateAlmond.iC..__T..:
            amount=amount+3
        __ ui.checkBoxChoclateChips.iC..__T..:
            amount=amount+4
        __ ui.checkBoxCookieDough.iC..__T..:
            amount=amount+2
        __ ui.checkBoxRockyRoad.iC..__T..:
            amount=amount+5
        __ ui.checkBoxCoffee.iC..__T..:
            amount=amount+2
        __ ui.checkBoxSoda.iC..__T..:
            amount=amount+3
        __ ui.checkBoxTea.iC..__T..:
            amount=amount+1
        ui.labelAmount.sT..("Total amount is $"+st.(amount))

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
