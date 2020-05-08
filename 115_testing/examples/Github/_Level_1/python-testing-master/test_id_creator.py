import unittest
from unittest import TestCase

from id_creator import IdCreator


class TestIdCreator(TestCase):
    """
    Tests for the IdCreator.
    See id_creator.py
    """
    id_creator = IdCreator()

    def test_valid_value_one(self):
        self.assertEqual(1, self.id_creator.faculty_id(1))

    def test_valid_value_zero(self):
        self.assertEqual(1, self.id_creator.faculty_id(0))

    def test_valid_value_three(self):
        self.assertEqual(6, self.id_creator.faculty_id(3))

    def test_invalid_value_error(self):
        with self.assertRaises(TypeError):
            self.id_creator.faculty_id('a')

    def test_invalid_type_error(self):
        with self.assertRaises(ValueError):
            self.id_creator.faculty_id(-1)


if __name__ == '__main__':
    unittest.main()
