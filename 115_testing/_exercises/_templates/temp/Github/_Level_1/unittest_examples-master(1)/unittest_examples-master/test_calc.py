______ unittest
______ calc

c_ TestCalc(unittest.TestCase):
    
    ___ test_soma
        assertEqual(calc.soma(1, 2), 3)
        assertEqual(calc.soma(-1, 2), 1)
        assertEqual(calc.soma(-5, 2), -3)

    ___ test_sub 
        assertEqual(calc.sub(1, 2), -1)
        assertEqual(calc.sub(1, -2), 3)
        assertEqual(calc.sub(-5, 2), -7)
        assertEqual(calc.sub(-5, -2), -3)
    
    ___ test_multiplica
        assertEqual(calc.multiplica(-5, 2), -10)
        assertEqual(calc.multiplica(7, 2), 14)
        assertEqual(calc.multiplica(-5, -2), 10)

    ___ test_divide
        with assertRaises(ValueError):
            calc.divide(5,0)

        assertEqual(calc.divide(5,2), 2.5)
        assertEqual(calc.divide(10,2), 5)
        assertEqual(calc.divide(9,-3), -3)

    #Podemos usar o skip para passar teste que sabemos que
    #vão falhar com algum motivo
    @unittest.skip("Exemplo de pular")
    ___ test_fsum_method
        assertEqual(sum([1.1, 2.2],4.4))

if __name__ == '__main__':
    unittest.main()

