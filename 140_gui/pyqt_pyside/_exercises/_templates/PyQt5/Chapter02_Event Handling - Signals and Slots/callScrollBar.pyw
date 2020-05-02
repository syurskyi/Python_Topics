_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoScrollBar _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.horizontalScrollBarSugarLevel.valueChanged.c..(scrollhorizontal)
        ui.verticalScrollBarPulseRate.valueChanged.c..(scrollvertical)
        ui.horizontalSliderBloodPressure.valueChanged.c..(sliderhorizontal)
        ui.verticalSliderCholestrolLevel.valueChanged.c..(slidervertical)
        s..

    ___ scrollhorizontal ,value
        ui.lineEditResult.sT..("Sugar Level : "+st.(value))

    ___ scrollvertical , value
        ui.lineEditResult.sT..("Pulse Rate : "+st.(value))

    ___ sliderhorizontal , value
        ui.lineEditResult.sT..("Blood Pressure : "+st.(value))
        
    ___ slidervertical , value
        ui.lineEditResult.sT..("Cholestrol Level : "+st.(value))
      

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
