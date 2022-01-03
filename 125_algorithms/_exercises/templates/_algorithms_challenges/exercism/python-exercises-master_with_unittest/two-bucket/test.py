_______ unittest

____ two_bucket _______ measure


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.4.0

c_ TwoBucketTest(unittest.TestCase):
    ___ test_bucket_one_size_3_bucket_two_size_5_start_with_bucket_one
        assertEqual(measure(3, 5, 1, "one"), (4, "one", 5))

    ___ test_bucket_one_size_3_bucket_two_size_5_start_with_bucket_two
        assertEqual(measure(3, 5, 1, "two"), (8, "two", 3))

    ___ test_bucket_one_size_7_bucket_two_size_11_start_with_bucket_one
        assertEqual(measure(7, 11, 2, "one"), (14, "one", 11))

    ___ test_bucket_one_size_7_bucket_two_size_11_start_with_bucket_two
        assertEqual(measure(7, 11, 2, "two"), (18, "two", 7))

    ___ test_bucket_one_size_1_bucket_two_size_3_start_with_bucket_two
        assertEqual(measure(1, 3, 3, "two"), (1, "two", 0))

    ___ test_bucket_one_size_2_bucket_two_size_3_start_with_bucket_one
        assertEqual(measure(2, 3, 3, "one"), (2, "two", 2))


__ __name__ __ '__main__':
    unittest.main()
