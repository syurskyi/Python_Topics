import unittest
from second_project import Counter


class EasyTestCase(unittest.TestCase):

    def setUp(self):
        self.counter = Counter()

    def test_easy_input(self):
        self.assertEqual(self.counter.get_value(), 0)

    def test_easy_input_two(self):
        self.counter.clear()
        self.assertEqual(self.counter.get_value(), 0)

    def tearDown(self):
        self.counter = None


class MediumTestCase(unittest.TestCase):

    def setUp(self):
        self.counter = Counter()

    def test_medium_input(self):
        self.counter.add()
        self.counter.add()
        self.counter.add()
        self.assertEqual(self.counter.get_value(), 3)

    def test_medium_input_two(self):
        self.counter.add()
        self.counter.add()
        self.counter.add()
        self.counter.remove()
        self.counter.remove()
        self.assertEqual(self.counter.get_value(), 1)

    def tearDown(self):
        self.counter = None


class HardTestCase(unittest.TestCase):

    def setUp(self):
        self.counter = Counter()

    def test_hard_input(self):
        self.counter.remove()
        self.counter.remove()
        self.counter.remove()
        self.counter.remove()
        self.assertEqual(self.counter.get_value(), 0)

    def test_hard_input_two(self):
        for _ in range(0, 1000):
            self.counter.add()
        self.assertEqual(self.counter.get_value(), 1000)

    def tearDown(self):
        self.counter = None


if __name__ == '__main__':
    unittest.main()
