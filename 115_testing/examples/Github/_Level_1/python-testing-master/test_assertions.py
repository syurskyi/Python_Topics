from unittest import TestCase


class TestAssertions(TestCase):
    """
    Showcase for different assertions provided by the unittest library.
    These are just a few examples and do not cover every assertion method provided.
    For the full documentation see the python docs: https://docs.python.org/3/library/unittest.html
    """

    def test_equality(self):
        x = 42
        y = 42

        self.assertEqual(x, y)
        self.assertNotEqual(42, 1337)

    def test_none_values(self):
        x = 42
        y = None

        self.assertIsNone(None)
        self.assertIsNone(y)
        self.assertIsNotNone(x)

    def test_bool(self):
        self.assertTrue(1 == 1)
        self.assertFalse(1 == 0)

    def test_comparison(self):
        self.assertGreater(1337, 42)
        self.assertGreaterEqual(13, 13)
        self.assertLess(42, 1337)
        self.assertLessEqual(13, 13)
        self.assertAlmostEqual(2.012, 2.013, 2)
        self.assertNotAlmostEqual(2.012, 2.013, 3)

    def test_exceptions(self):
        with self.assertRaises(ZeroDivisionError):
            x = 42 / 0

    def test_list_comparison(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        list3 = [3, 2, 1]
        self.assertListEqual(list1, list2)
        self.assertCountEqual(list1, list3)
        # same methods exist for strings, sequences, tuples, sets and dictionaries
