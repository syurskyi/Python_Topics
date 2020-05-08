from unittest import TestCase
from my_package.subpackage.utils import somefunction

c_ TestUtils(TestCase):
    ___ test_somefunction(self):
        self.assertEqual(somefunction('add', 5, 6), 11)

