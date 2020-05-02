_____ ___

____ ?.?W.. _____ ?D.., ?A..

____ demoCalculator _____ _

c_ MyForm ?D..
    ___  -
        s__. -
        ui _ ?
        ui.sU..
        ui.pushButtonPlus.c___.c..(addtwonum)
        ui.pushButtonSubtract.c___.c..(subtracttwonum)
        ui.pushButtonMultiply.c___.c..(multiplytwonum)
        ui.pushButtonDivide.c___.c..(dividetwonum)
        s..

    ___ addtwonum
        __ le.(ui.lineEditFirstNumber.t..())!_0:
            a_int(ui.lineEditFirstNumber.t..())
        ____
            a_0
        __ le.(ui.lineEditSecondNumber.t..())!_0:
            b_int(ui.lineEditSecondNumber.t..())
        ____
            b_0
        sum_a+b
        ui.labelResult.sT..("Addition: " +st.(sum))

    ___ subtracttwonum
        __ le.(ui.lineEditFirstNumber.t..())!_0:
            a_int(ui.lineEditFirstNumber.t..())
        ____
            a_0
        __ le.(ui.lineEditSecondNumber.t..())!_0:
            b_int(ui.lineEditSecondNumber.t..())
        ____
            b_0
        diff_a-b
        ui.labelResult.sT..("Substraction: " +st.(diff))
        
    ___ multiplytwonum
        __ le.(ui.lineEditFirstNumber.t..())!_0:
            a_int(ui.lineEditFirstNumber.t..())
        ____
            a_0
        __ le.(ui.lineEditSecondNumber.t..())!_0:
            b_int(ui.lineEditSecondNumber.t..())
        ____
            b_0
        mult_a*b
        ui.labelResult.sT..("Multiplication: " +st.(mult))
        
    ___ dividetwonum
        __ le.(ui.lineEditFirstNumber.t..())!_0:
            a_int(ui.lineEditFirstNumber.t..())
        ____
            a_0
        __ le.(ui.lineEditSecondNumber.t..())!_0:
            b_int(ui.lineEditSecondNumber.t..())
        ____
            b_0
        division_a/b
        ui.labelResult.sT..("Division: " +st.(ro..(division,2)))

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e..(app.e
