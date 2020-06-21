import unittest
import math

class TestMathMerhods(unittest.TestCase):
    
    def test_pow(self):
        self.assertEqual(math.pow(5,2), 25)

    def test_square_root(self):
        self.assertTrue(math.sqrt(4) == 2)
    
    def test_absolute_value(self):
        self.assertFalse(math.fabs(-4) == -4)

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError)

    #Podemos usar o skip para passar teste que sabemos que
    #vão falhar com algum motivo
    @unittest.skip("Exemplo de pular")
    def test_fsum_method(self):
        self.assertEqual(math.sum([1.1, 2.2],4.4))

if __name__ == '__main__':
    unittest.main()

