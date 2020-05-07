import sys
import unittest
from io import StringIO
from challenge import Printer


class TestPrintedOutPut(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.printer = Printer()

    def test_value_name(self):
        self.printer.set_value('Muhammad Ali')
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Muhammad Ali')

    def test_value_job(self):
        self.printer.set_value('Boxer')
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Boxer')

    def tearDown(self):
        self.printer = None


if __name__ == '__main__':
    unittest.main()