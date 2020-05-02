_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoRadioButton1 _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.radioButtonFirstClass.toggled.c..(dispFare)
        ui.radioButtonBusinessClass.toggled.c..(dispFare)
        ui.radioButtonEconomyClass.toggled.c..(dispFare)
        s..

    ___ dispFare 
        fare=0
        __ ui.radioButtonFirstClass.iC..__T..:
            fare=150
        __ ui.radioButtonBusinessClass.iC..__T..:
            fare=125
        __ ui.radioButtonEconomyClass.iC..__T..:
            fare=100
        ui.labelFare.sT..("Air Fare is "+st.(fare))

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
