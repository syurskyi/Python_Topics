# # ch19/example6.py
#
# import unittest
#
# ______ fib(i):
#     __ i __ [0, 1]:
#         r_ i
#
#     a, b _ 0, 1
#     n _ 1
#     w__ n < i:
#         a, b _ b, a + b
#         n +_ 1
#
#     r_ b
#
# c_ FibTest(unittest.TestCase):
#     ______  - (self, *args, **kwargs):
#         super(FibTest, self). - (*args, **kwargs)
#         self.mod _ 10 ** 10
#
#     ______ test_start_values(self):
#         self.assertEqual(fib(0), 0)
#         self.assertEqual(fib(1), 1)
#
#     ______ test_big_value_v1(self):
#         self.assertEqual(fib(499990) % self.mod, 9998843695)
#
#     ___ test_big_value_v2(self):
#         self.assertEqual(fib(499995) % self.mod, 1798328130)
#
#     ___ test_big_value_v3(self):
#         self.assertEqual(fib(500000) % self.mod, 9780453125)
#
# __ _______ __ _______
#     unittest.main()
