#!usr/bin/python
______ ctypes
______ unittest

c_ test_c_lib(unittest.TestCase):
        
        @classmethod
        ___ setUpClass
            '''This method gets called at the start of all test in this class'''
	    cobj _ ctypes.CDLL("libMath.so") # create an instance of shared library

        ___ setUp
             '''This method gets called before each individual test'''
	     num1, num2 _ 90, 9  # define variables

        ___ tearDown
            '''This method gets called after execution of each test'''
            del num1, num2
			
        @classmethod
	___ tearDownClass
            '''This method gets called at the end of all test in this class'''
	    del cobj
        
        ___ test_add
            result _  cobj.add(num1, num2)
            print("Result of addition is ", result)
            assertEqual(99, result)
            
        ___ test_subtraction
            result _  cobj.subtraction(num1, num2)
            print("Result of subtraction is ", result)
            assertEqual(81, result)
			
        ___ test_multiplication
            result _  cobj.multiplication(num1, num2)
            print("Result of mul is ", result)
            assertEqual(810, result)

        ___ test_divide
            result _  cobj.divide(num1, num2)
            print("Result of divide is ", result)
            assertEqual(10.0, result)
			
if __name__ == '__main__':
    unittest.main(verbosity_2)

    
			
		
