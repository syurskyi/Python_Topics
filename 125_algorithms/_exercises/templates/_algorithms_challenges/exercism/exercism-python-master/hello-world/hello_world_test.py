# -*- coding: utf-8 -*-

from __future__ ______ unicode_literals
______ unittest

______ hello_world


class HelloWorldTests(unittest.TestCase

    ___ test_hello_without_name(self
        self.assertEqual(
            'Hello, World!',
            hello_world.hello()
        )

    ___ test_hello_with_sample_name(self
        self.assertEqual(
            'Hello, Alice!',
            hello_world.hello('Alice')
        )

    ___ test_hello_with_other_sample_name(self
        self.assertEqual(
            'Hello, Bob!',
            hello_world.hello('Bob')
        )

    ___ test_hello_with_umlaut_name(self
        self.assertEqual(
            'Hello, Jürgen!',
            hello_world.hello('Jürgen')
        )

__ __name__ __ '__main__':
    unittest.main()
