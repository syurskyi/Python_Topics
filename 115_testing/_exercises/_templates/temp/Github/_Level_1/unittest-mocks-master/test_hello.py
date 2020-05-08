from hello import say_hello
from unittest.mock import patch
import unittest

c_ HelloTests(unittest.TestCase):
    '''Testing say_hello'''
    @patch('hello.print')
    ___ test_say_hello  mock_print):
        # call the function
        say_hello()
        
        # Make sure it only called `print` once
        self.assertEqual(mock_print.call_count ,1)
        
        # getting the arguments and keyword arguments passed to the 
        # mocked function
        args, kwargs = mock_print.call_args

        # Make sure it prints the correct string
        self.assertEqual(args, ('Hello, World!',))
if __name__ == '__main__':
    unttest.main()
