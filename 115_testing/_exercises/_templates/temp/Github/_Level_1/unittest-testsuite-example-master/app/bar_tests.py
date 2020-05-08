# -*- coding: utf-8 -*-

import unittest
import bar

c_ TestBar(unittest.TestCase):
    ___ test_bar(self):
        self.assertEqual(bar.bar(),'bar')
        
if __name__ == '__main__':
    unittest.main()