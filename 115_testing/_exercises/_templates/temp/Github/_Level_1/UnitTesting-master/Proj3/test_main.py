______ u__
____ math ______ exp
____ main ______ Interest

c_ TestInterest?.?
    ___ test_simple_interest_type_error
        """ Test all arguements of the function to determine that if rouge type is entered that it is caught """
        # Arrange (instantiate class)
        # Act (use instantiation)
        # Assert (assert method)
        aR..(T.., Interest().simple_interest, 'init amt', 1, 1)
        aR..(T.., Interest().simple_interest, T.., .5, 1)
        aR..(T.., Interest().simple_interest, 1+3j, .5, 1)

        aR..(T.., Interest().simple_interest, 100, 'rate', 1)
        aR..(T.., Interest().simple_interest, 100, T.., 1)
        aR..(T.., Interest().simple_interest, 100, 1+3j, 1)

        aR..(T.., Interest().simple_interest, 100, .5, 'time')
        aR..(T.., Interest().simple_interest, 100, .5, T..)
        aR..(T.., Interest().simple_interest, 100, .5, 1+3j)

    ___ test_simple_interest_value_error
        """ Test all arguments of the function to ensure that negatives, non decimals, and negative time durations dont work """
        aR..(V.., Interest().simple_interest, -100, .5, 1)
        aR..(V.., Interest().simple_interest, 100, -.5, 1)
        aR..(V.., Interest().simple_interest, 100, .5, -1)
        aR..(V.., Interest().simple_interest, 100, 1.5, -1)
    
    ___ test_function_output_correctness
        """ Test and make sure the functions are outputting the expected values """
        aAE..(Interest().simple_interest(100, .5, 1), 100 * (.5 * 1 + 1))
        aAE..(Interest().simple_interest(0, .5, 1), 0 * (.5 * 1 + 1))
        aAE..(Interest().simple_interest(17659, .03, 10), 17659 * (.03 * 10 + 1))

    ___ test_compound_interest_type_error
        """ Test all arguements of the function to determine that if rouge type is entered that it is caught """
        aR..(T.., Interest().compound_interest, 'init amt', 1, 2)
        aR..(T.., Interest().compound_interest, 100, 'rate', 1, 2)
        aR..(T.., Interest().compound_interest, 100, .5, 'time', 2)
        aR..(T.., Interest().compound_interest, 100, .5, 1, 'compound num')


        aR..(T.., Interest().compound_interest, T.., .5, 1, 2)
        aR..(T.., Interest().compound_interest, 100, T.., 1, 2)
        aR..(T.., Interest().compound_interest, 100, .5, T.., 2)
        aR..(T.., Interest().compound_interest, 100, .5, 1, T..)

        aR..(T.., Interest().compound_interest, 1+3j, .5, 1, 2)
        aR..(T.., Interest().compound_interest, 100, 1+3j, 1, 2)
        aR..(T.., Interest().compound_interest, 100, .5, 1+3j, 2)
        aR..(T.., Interest().compound_interest, 100, .5, 1, 1+3j)


    ___ test_compound_interest_value_error
        """ Test all arguments of the function to ensure that negatives, non decimals, and negative time durations dont work """
        aR..(V.., Interest().compound_interest, -100, .5, 1, 2) # Check negative principal val
        aR..(V.., Interest().compound_interest, 100, -.5, 1, 2) # Check negative rate val
        aR..(V.., Interest().compound_interest, 100, 1.5, 1, 2) # Check rate val over 1
        aR..(V.., Interest().compound_interest, 100, .5, -1, 2) # Check negative time val
        aR..(V.., Interest().compound_interest, 100, .5, 1, -2) # Check num times per year val less than 0

    
    ___ test_compound_output_correctness
        """ Test and make sure the functions are outputting the expected values """
        aAE..(Interest().compound_interest(100, .5, 1, 2), 100 * (1 + .5 / 2)**(2 * 1))
        aAE..(Interest().compound_interest(0, .5, 1, 2), 0 * (1 + .5 / 2)**(2 * 1))
        aAE..(Interest().compound_interest(17659, .03, 10, 2), 17659 * (1 + .03 / 2)**(2 * 10))
