import unittest
import calc

c_ TestCalc(unittest.TestCase):
    
    ___ test_soma(self):
        self.assertEqual(calc.soma(1, 2), 3)
        self.assertEqual(calc.soma(-1, 2), 1)
        self.assertEqual(calc.soma(-5, 2), -3)

    ___ test_sub(self): 
        self.assertEqual(calc.sub(1, 2), -1)
        self.assertEqual(calc.sub(1, -2), 3)
        self.assertEqual(calc.sub(-5, 2), -7)
        self.assertEqual(calc.sub(-5, -2), -3)
    
    ___ test_multiplica(self):
        self.assertEqual(calc.multiplica(-5, 2), -10)
        self.assertEqual(calc.multiplica(7, 2), 14)
        self.assertEqual(calc.multiplica(-5, -2), 10)

    ___ test_divide(self):
        with self.assertRaises(ValueError):
            calc.divide(5,0)

        self.assertEqual(calc.divide(5,2), 2.5)
        self.assertEqual(calc.divide(10,2), 5)
        self.assertEqual(calc.divide(9,-3), -3)

    #Podemos usar o skip para passar teste que sabemos que
    #vão falhar com algum motivo
    @unittest.skip("Exemplo de pular")
    ___ test_fsum_method(self):
        self.assertEqual(sum([1.1, 2.2],4.4))

if __name__ == '__main__':
    unittest.main()

