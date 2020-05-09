# -*- coding: utf-8 -*-

______ unittest
______ foo

c_ TestFoo(unittest.TestCase):
    ___ setUp
        FOO _ foo.Foo()
    
    ___ test_foo
        assertEqual(FOO.foo(),'foo')
        
if __name__ == '__main__':
    unittest.main()