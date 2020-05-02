_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoSpinBox _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.spinBoxBookQty.editingFinished.c..(result1)
        ui.doubleSpinBoxSugarWeight.editingFinished.c..(result2)
        s..

    ___ result1
        __ len(ui.lineEditBookPrice.text())!=0:
            bookPrice=int(ui.lineEditBookPrice.text())
        else:
            bookPrice=0
        totalBookAmount=ui.spinBoxBookQty.value() * bookPrice
        ui.lineEditBookAmount.sT..(st.(totalBookAmount))
        
    ___ result2
        __ len(ui.lineEditSugarPrice.text())!=0:
            sugarPrice=float(ui.lineEditSugarPrice.text())
        else:
            sugarPrice=0
        totalSugarAmount=ui.doubleSpinBoxSugarWeight.value() * sugarPrice
        ui.lineEditSugarAmount.sT..(st.(round(totalSugarAmount,2)))
        totalBookAmount=int(ui.lineEditBookAmount.text())
        totalAmount=totalBookAmount+totalSugarAmount
        ui.labelTotalAmount.sT..(st.(round(totalAmount,2)))

__ __name____"__main__":
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
