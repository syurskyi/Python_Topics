_______ unittest

_______ hello_world


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class HelloWorldTests(unittest.TestCase):
    ___ test_hello(self):
        self.assertEqual(hello_world.hello(), 'Hello, World!')


__ __name__ __ '__main__':
    unittest.main()
