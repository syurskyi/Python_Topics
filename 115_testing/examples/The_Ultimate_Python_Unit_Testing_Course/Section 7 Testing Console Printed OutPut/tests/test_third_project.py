import sys
import unittest
from io import StringIO
from third_project import Profile


class TestPrintedOutPut(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.profile = Profile('Mohammad Mahjoub', 21, 'student')

    def test_name(self):
        self.profile.print_name()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Mohammad Mahjoub')

    def test_age(self):
        self.profile.print_age()
        self.assertEqual(sys.stdout.getvalue().strip(), '21')

    def test_job(self):
        self.profile.print_job()
        self.assertEqual(sys.stdout.getvalue().strip(), 'student')

    def tearDown(self):
        self.profile = None


if __name__ == '__main__':
    unittest.main()