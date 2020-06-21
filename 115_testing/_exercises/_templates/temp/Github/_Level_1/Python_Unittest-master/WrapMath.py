#!usr/bin/python
______ ctypes
______ u__

c_ test_c_lib?.?
        
        ??
        ___ setUpClass
            '''This method gets called at the start of all test in this class'''
	    cobj _ ctypes.CDLL("libMath.so") # create an instance of shared library

        ___ setUp
             '''This method gets called before each individual test'''
	     num1, num2 _ 90, 9  # define variables

        ___ tearDown
            '''This method gets called after execution of each test'''
            del num1, num2
			
        ??
	___ tearDownClass
            '''This method gets called at the end of all test in this class'''
	    del cobj
        
        ___ test_add
            result _  cobj.add(num1, num2)
            print("Result of addition is ", result)
            aE..(99, result)
            
        ___ test_subtraction
            result _  cobj.subtraction(num1, num2)
            print("Result of subtraction is ", result)
            aE..(81, result)
			
        ___ test_multiplication
            result _  cobj.multiplication(num1, num2)
            print("Result of mul is ", result)
            aE..(810, result)

        ___ test_divide
            result _  cobj.divide(num1, num2)
            print("Result of divide is ", result)
            aE..(10.0, result)
			
__ _____ __ _____
    u__.main(verbosity_2)

    
			
		
