______ unittest
______ math

c_ TestMathMerhods(unittest.TestCase):
    
    ___ test_pow
        assertEqual(math.pow(5,2), 25)

    ___ test_square_root
        assertTrue(math.sqrt(4) == 2)
    
    ___ test_absolute_value
        assertFalse(math.fabs(-4) == -4)

    ___ test_zero_division
        assertRaises(ZeroDivisionError)

    #Podemos usar o skip para passar teste que sabemos que
    #vão falhar com algum motivo
    @unittest.skip("Exemplo de pular")
    ___ test_fsum_method
        assertEqual(math.sum([1.1, 2.2],4.4))

if __name__ == '__main__':
    unittest.main()

