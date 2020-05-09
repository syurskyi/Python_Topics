______ u__
______ calc

c_ TestCalc?.?
    
    ___ test_soma
        aE..(calc.soma(1, 2), 3)
        aE..(calc.soma(-1, 2), 1)
        aE..(calc.soma(-5, 2), -3)

    ___ test_sub 
        aE..(calc.sub(1, 2), -1)
        aE..(calc.sub(1, -2), 3)
        aE..(calc.sub(-5, 2), -7)
        aE..(calc.sub(-5, -2), -3)
    
    ___ test_multiplica
        aE..(calc.multiplica(-5, 2), -10)
        aE..(calc.multiplica(7, 2), 14)
        aE..(calc.multiplica(-5, -2), 10)

    ___ test_divide
        w__ aR..(V..
            calc.divide(5,0)

        aE..(calc.divide(5,2), 2.5)
        aE..(calc.divide(10,2), 5)
        aE..(calc.divide(9,-3), -3)

    #Podemos usar o skip para passar teste que sabemos que
    #vão falhar com algum motivo
    @u__.skip("Exemplo de pular")
    ___ test_fsum_method
        aE..(sum([1.1, 2.2],4.4))

__ _____ __ _____
    ?.?

