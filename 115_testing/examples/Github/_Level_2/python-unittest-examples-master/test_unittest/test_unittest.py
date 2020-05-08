# -*- coding: utf-8 -*-

import unittest
from sets import Set


class Widget(object):

    """For running tests"""

    def __init__(self, widget_name):
        self._size = (50, 50)
        self.widget_name = widget_name

    def resize(self, x_value, y_value):
        self._size = (x_value, y_value)

    def dispose(self):
        print 'dispose'

    def size(self):
        return self._size

    def raise_exception(self):
        raise Exception()


@unittest.skipIf(3 < 2, 'This class will be executed because 3 is greater than 2, which makes the condition false.')
class TestUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'setUpClass'

    @classmethod
    def tearDownClass(cls):
        print 'tearDownClass'

    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def test_default_size(self):
        self.assertEqual(self.widget.size(), (50, 50),
                         'incorrect default size')

    def test_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150),
                         'wrong size after resize')

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(1 < 2, 'because 1 < 2, this test case will not be executed')
    def test_always_be_tested(self):
        pass

    @unittest.skipUnless(1 > 2, 'This test case will be skipped. Unless the condition is true')
    def test_skipunless_decorator(self):
        pass

    @unittest.expectedFailure
    def test_fail(self):
        self.assertTrue(false)

    def test_basic_usage(self):
        self.assertEqual(1, 1)
        self.assertNotEqual(1, 2)
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertIs(self.widget, self.widget)
        self.assertIsNot(self.widget, Widget('new widget'))
        self.assertIsNone(None)
        self.assertIsNotNone('A value')
        self.assertIn(1, (1, 2, 3))
        self.assertNotIn(1, (2, 3, 4))
        self.assertIsInstance(self.widget, Widget)
        self.assertNotIsInstance(1, Widget)
        self.assertAlmostEqual(2.12345678, 2.12345679)
        self.assertAlmostEqual(2.1, 2.2, delta=0.2)
        self.assertNotAlmostEqual(2.1, 2, 2)
        self.assertGreater(3, 2)
        self.assertGreaterEqual(2, 2)
        self.assertLess(1, 2)
        self.assertLessEqual(1, 1)
        self.assertRegexpMatches('a string', 'string')
        self.assertNotRegexpMatches('a string', 'the')
        # assertItemsEqual: sorted(a) == sorted(b)
        self.assertItemsEqual([1, 2, 3], [1, 3, 2])
        # assertDictContainsSubset: Deprecated since version 3.2.
        self.assertDictContainsSubset(expected={
                                      'key1': 1}, actual={'key1': 1, 'key2': 2})

        self.assertMultiLineEqual('test', 'test')
        """
        assertSequenceEqual: This method is not called directly by assertEqual(), but it’s used to
        implement assertListEqual() and assertTupleEqual().
        """
        self.assertSequenceEqual((1, 2), (1, 2))
        self.assertListEqual([1, 2], [1, 2])
        self.assertTupleEqual((1, 2), (1, 2))
        self.assertSetEqual(Set(['a', 'b', 'c']), Set(['b', 'a', 'c']))
        self.assertDictEqual({'key1': 1, 'key2': 2}, {'key1': 1, 'key2': 2})

    def test_raise_exception(self):
        with self.assertRaises(Exception):
            self.widget.raise_exception()

if __name__ == '__main__':
    unittest.main()
# Do not use the following way to trigger unit testing if you wanna use
# nosetests as the test runner.

# suite = unittest.TestLoader().loadTestsFromTestCase(TestUnittest)
# unittest.TextTestRunner(verbosity=2).run(suite)
