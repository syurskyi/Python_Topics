_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoSpinBox _____ _

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.spinBoxBookQty.editingFinished.c..(result1)
        ui.doubleSpinBoxSugarWeight.editingFinished.c..(result2)
        s..

    ___ result1
        __ len(ui.lineEditBookPrice.t..())!_0:
            bookPrice_int(ui.lineEditBookPrice.t..())
        ____
            bookPrice_0
        totalBookAmount_ui.spinBoxBookQty.value() * bookPrice
        ui.lineEditBookAmount.sT..(st.(totalBookAmount))
        
    ___ result2
        __ len(ui.lineEditSugarPrice.t..())!_0:
            sugarPrice_float(ui.lineEditSugarPrice.t..())
        ____
            sugarPrice_0
        totalSugarAmount_ui.doubleSpinBoxSugarWeight.value() * sugarPrice
        ui.lineEditSugarAmount.sT..(st.(round(totalSugarAmount,2)))
        totalBookAmount_int(ui.lineEditBookAmount.t..())
        totalAmount_totalBookAmount+totalSugarAmount
        ui.labelTotalAmount.sT..(st.(round(totalAmount,2)))

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e
