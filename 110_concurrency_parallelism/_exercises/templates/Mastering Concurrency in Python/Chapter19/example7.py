# # ch19/example7.py
#
# import unittest
# ____ concurrencytest ______ ConcurrentTestSuite, fork_for_tests
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
#     ______ -(, *args, **kwargs):
#         super(FibTest, ?). - (*args, **kwargs)
#         .mod _ 10 ** 10
#
#     ______ test_start_values():
#         .assertEqual(fib(0), 0)
#         .assertEqual(fib(1), 1)
#
#     ______ test_big_value_v1():
#         .assertEqual(fib(499990) % .mod, 9998843695)
#
#     ______ test_big_value_v2():
#         .assertEqual(fib(499995) % .mod, 1798328130)
#
#     ______ test_big_value_v3():
#         .assertEqual(fib(500000) % .mod, 9780453125)
#
# __ _______ __ _______
#     runner _ unittest.TextTestRunner()
#
#     # multiprocessing testing
#     suite _ unittest.TestLoader().loadTestsFromTestCase(FibTest)
#     concurrent_suite _ ConcurrentTestSuite(suite, fork_for_tests(4))
#     runner.run(concurrent_suite)
