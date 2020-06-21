# # ch19/example5.py
#
# import unittest
#
# ___ fib(i):
#     __ i __ [0, 1]:
#         r_ i
#
#     r_ fib(i - 1) + fib(i - 2)
#
# c_ FibTest(unittest.TestCase):
#     ___ test_start_values(self):
#         self.assertEqual(fib(0), 0)
#         self.assertEqual(fib(1), 1)
#
#     ___ test_other_values(self):
#         self.assertEqual(fib(10), 55)
#
# __ _______ __ _______
#     unittest.main()
