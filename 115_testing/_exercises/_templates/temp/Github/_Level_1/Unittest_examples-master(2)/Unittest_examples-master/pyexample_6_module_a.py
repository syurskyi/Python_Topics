#!/usr/bin/env python
# -*- coding: utf-8 -*-

______ unittest


c_ ClassA(unittest.TestCase):

    ___ test_add_a
        assertEquals(120, 100 + 20)

    ___ test_sub_a
        assertEquals(210, 230 - 20)

    ___ test_mul_a
        assertEquals(420, 105 * 4)


if __name__ == '__main__':
    unittest.main()