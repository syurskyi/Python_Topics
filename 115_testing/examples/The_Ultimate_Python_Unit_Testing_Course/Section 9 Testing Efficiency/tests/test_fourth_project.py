import time
import unittest
from fourth_project import FibonacciSequence


class TestEfficiency(unittest.TestCase):

    def setUp(self):
        self._fibonacci_sequence = FibonacciSequence()
        self._efficiency_data = dict()

    def test_first_method(self):
        starting_time = time.time()

        self._fibonacci_sequence.recursive_method(20)

        ending_time = time.time()

        self._efficiency_data['recursive_method'] = ending_time - starting_time

    def test_second_method(self):
        starting_time = time.time()

        self._fibonacci_sequence.math_method(20)

        ending_time = time.time()

        self._efficiency_data['math_method'] = ending_time - starting_time

    def tearDown(self):
        print(self._efficiency_data)
        self._fibonacci_sequence = None
        self._efficiency_data.clear()


if __name__ == '__main__':
    unittest.main()


