_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoSpinBox _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.spinBoxBookQty.editingFinished.c..(result1)
        ui.doubleSpinBoxSugarWeight.editingFinished.c..(result2)
        s..

    ___ result1
        __ len(ui.lineEditBookPrice.text())!_0:
            bookPrice_int(ui.lineEditBookPrice.text())
        else:
            bookPrice_0
        totalBookAmount_ui.spinBoxBookQty.value() * bookPrice
        ui.lineEditBookAmount.sT..(st.(totalBookAmount))
        
    ___ result2
        __ len(ui.lineEditSugarPrice.text())!_0:
            sugarPrice_float(ui.lineEditSugarPrice.text())
        else:
            sugarPrice_0
        totalSugarAmount_ui.doubleSpinBoxSugarWeight.value() * sugarPrice
        ui.lineEditSugarAmount.sT..(st.(round(totalSugarAmount,2)))
        totalBookAmount_int(ui.lineEditBookAmount.text())
        totalAmount_totalBookAmount+totalSugarAmount
        ui.labelTotalAmount.sT..(st.(round(totalAmount,2)))

__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())
