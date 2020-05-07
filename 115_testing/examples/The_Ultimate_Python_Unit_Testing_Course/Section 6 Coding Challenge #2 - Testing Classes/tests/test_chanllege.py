import unittest
from challenge import Car


class EasyTestCase(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_easy_input(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.assertEqual(self.car.current_speed(), 20)

    def test_easy_input_two(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.stop()
        self.assertEqual(self.car.current_speed(), 0)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


class MediumTestCase(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_medium_input(self):
        with self.assertRaises(Exception):
            self.car.start_car()

    def test_medium_input_two(self):
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.assertEqual(self.car.current_speed(), 0)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


class HardTestCase(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_hard_input(self):
        with self.assertRaises(Exception):
            self.car.add_speed()
            self.car.add_speed()
            self.car.add_speed()
            self.car.add_speed()
            self.car.turn_off_car()

    def test_hard_input_two(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.stop()
        self.assertEqual(self.car.current_speed(), 0)

        self.car.stop()
        self.car.stop()
        self.assertEqual(self.car.current_speed(), 0)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


if __name__ == '__main__':
    unittest.main()