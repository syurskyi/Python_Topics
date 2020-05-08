# -*- coding: utf-8 -*-

import unittest
import foo

c_ TestFoo(unittest.TestCase):
    ___ setUp(self):
        self.FOO = foo.Foo()
    
    ___ test_foo(self):
        self.assertEqual(self.FOO.foo(),'foo')
        
if __name__ == '__main__':
    unittest.main()