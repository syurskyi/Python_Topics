#!usr/bin/python
import ctypes
import unittest

class test_c_lib(unittest.TestCase):
        
        @classmethod
        def setUpClass(self):
            '''This method gets called at the start of all test in this class'''
	    self.cobj = ctypes.CDLL("libMath.so") # create an instance of shared library

        def setUp(self):
             '''This method gets called before each individual test'''
	     self.num1, self.num2 = 90, 9  # define variables

        def tearDown(self):
            '''This method gets called after execution of each test'''
            del self.num1, self.num2
			
        @classmethod
	def tearDownClass(self):
            '''This method gets called at the end of all test in this class'''
	    del self.cobj
        
        def test_add(self):
            result =  self.cobj.add(self.num1, self.num2)
            print("Result of addition is ", result)
            self.assertEqual(99, result)
            
        def test_subtraction(self):
            result =  self.cobj.subtraction(self.num1, self.num2)
            print("Result of subtraction is ", result)
            self.assertEqual(81, result)
			
        def test_multiplication(self):
            result =  self.cobj.multiplication(self.num1, self.num2)
            print("Result of mul is ", result)
            self.assertEqual(810, result)

        def test_divide(self):
            result =  self.cobj.divide(self.num1, self.num2)
            print("Result of divide is ", result)
            self.assertEqual(10.0, result)
			
if __name__ == '__main__':
    unittest.main(verbosity=2)

    
			
		
