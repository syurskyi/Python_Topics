____ hello ______ say_hello
____ u__.m.. ______ patch
______ u__

c_ HelloTests?.?
    '''Testing say_hello'''
    ?p..('hello.print')
    ___ test_say_hello  mock_print
        # call the function
        say_hello()
        
        # Make sure it only called `print` once
        aE..(mock_print.call_count ,1)
        
        # getting the arguments and keyword arguments passed to the 
        # mocked function
        args, kwargs _ mock_print.call_args

        # Make sure it prints the correct string
        aE..(args, ('Hello, World!',))
__ _____ __ _____
    unttest.main()
