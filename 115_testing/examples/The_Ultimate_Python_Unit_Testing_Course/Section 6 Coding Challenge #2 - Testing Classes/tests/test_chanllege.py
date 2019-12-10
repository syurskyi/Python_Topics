import sys
import unittest
from io import StringIO
from challenge import Printer


class TestPrintedOutPut(unittest.TestCase):

    def setUp(self):
        # Todo: setup the system to record console printed output.
        # Todo: create an object from the Printer class named printer.
        pass

    def test_value_name(self):
        # Todo: use the object printer to add the name 'Muhammad Ali' to the set_value method.
        # Todo: use the object printer to call the method print_value.
        # Todo: use assertEqual to check if the printed string is 'Muhammad Ali'
        pass

    def test_value_job(self):
        # Todo: use the object printer to add the job 'Boxer' to the set_value method.
        # Todo: use the object printer to call the method print_value.
        # Todo: use assertEqual to check if the printed string is 'Boxer'
        pass

    def tearDown(self):
        # Todo: set the printer object to None.
        pass


if __name__ == '__main__':
    unittest.main()
