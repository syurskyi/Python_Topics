# -*- coding: utf-8 -*-

import unittest
import foo

class TestFoo(unittest.TestCase):
    def setUp(self):
        self.FOO = foo.Foo()
    
    def test_foo(self):
        self.assertEqual(self.FOO.foo(),'foo')
        
if __name__ == '__main__':
    unittest.main()