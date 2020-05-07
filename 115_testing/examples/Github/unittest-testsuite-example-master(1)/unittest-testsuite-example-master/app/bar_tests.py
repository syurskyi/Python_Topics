# -*- coding: utf-8 -*-

import unittest
import bar

class TestBar(unittest.TestCase):
    def test_bar(self):
        self.assertEqual(bar.bar(),'bar')
        
if __name__ == '__main__':
    unittest.main()