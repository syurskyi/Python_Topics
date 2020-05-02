_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoCalculator _____ *

c_ MyForm(?D..
    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonPlus.clicked.c..(addtwonum)
        ui.pushButtonSubtract.clicked.c..(subtracttwonum)
        ui.pushButtonMultiply.clicked.c..(multiplytwonum)
        ui.pushButtonDivide.clicked.c..(dividetwonum)
        s..

    ___ addtwonum
        __ len(ui.lineEditFirstNumber.text())!=0:
            a=int(ui.lineEditFirstNumber.text())
        else:
            a=0
        __ len(ui.lineEditSecondNumber.text())!=0:
            b=int(ui.lineEditSecondNumber.text())
        else:
            b=0
        sum=a+b
        ui.labelResult.sT..("Addition: " +st.(sum))

    ___ subtracttwonum
        __ len(ui.lineEditFirstNumber.text())!=0:
            a=int(ui.lineEditFirstNumber.text())
        else:
            a=0
        __ len(ui.lineEditSecondNumber.text())!=0:
            b=int(ui.lineEditSecondNumber.text())
        else:
            b=0
        diff=a-b
        ui.labelResult.sT..("Substraction: " +st.(diff))
        
    ___ multiplytwonum
        __ len(ui.lineEditFirstNumber.text())!=0:
            a=int(ui.lineEditFirstNumber.text())
        else:
            a=0
        __ len(ui.lineEditSecondNumber.text())!=0:
            b=int(ui.lineEditSecondNumber.text())
        else:
            b=0
        mult=a*b
        ui.labelResult.sT..("Multiplication: " +st.(mult))
        
    ___ dividetwonum
        __ len(ui.lineEditFirstNumber.text())!=0:
            a=int(ui.lineEditFirstNumber.text())
        else:
            a=0
        __ len(ui.lineEditSecondNumber.text())!=0:
            b=int(ui.lineEditSecondNumber.text())
        else:
            b=0
        division=a/b
        ui.labelResult.sT..("Division: " +st.(round(division,2)))

__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())
