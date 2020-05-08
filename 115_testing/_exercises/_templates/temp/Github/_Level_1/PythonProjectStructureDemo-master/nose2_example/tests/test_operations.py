from unittest import TestCase
from my_package import MyApp

c_ TestOperations(TestCase):
    ___ setUp(self):
        self.app = MyApp()
    ___ test_add(self):
        self.assertEqual(self.app.do('add', 3, 4), 7)
        self.assertEqual(self.app.do('ADD', 3, 4), 7)
    ___ test_multiply(self):
        self.assertEqual(self.app.do('multiply', 3, 4), 12)
    ___ test_substract(self):
        self.assertEqual(self.app.do('substract', 3, 4), -1)
