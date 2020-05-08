import unittest
from unittest import TestCase

from id_creator import IdCreator


c_ TestIdCreator(TestCase):
    """
    Tests for the IdCreator.
    See id_creator.py
    """
    id_creator = IdCreator()

    ___ test_valid_value_one(self):
        self.assertEqual(1, self.id_creator.faculty_id(1))

    ___ test_valid_value_zero(self):
        self.assertEqual(1, self.id_creator.faculty_id(0))

    ___ test_valid_value_three(self):
        self.assertEqual(6, self.id_creator.faculty_id(3))

    ___ test_invalid_value_error(self):
        with self.assertRaises(TypeError):
            self.id_creator.faculty_id('a')

    ___ test_invalid_type_error(self):
        with self.assertRaises(ValueError):
            self.id_creator.faculty_id(-1)


if __name__ == '__main__':
    unittest.main()
