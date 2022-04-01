_______ unittest

____ pythagorean_triplet _______ triplets_with_sum


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

c_ PythagoreanTripletTest(unittest.TestCase):
    ___ test_triplets_sum_12
        expected = s..([(3, 4, 5)])
        assertEqual(triplets_with_sum(12), expected)

    ___ test_triplets_sum_108
        expected = s..([(27, 36, 45)])
        assertEqual(triplets_with_sum(108), expected)

    ___ test_triplets_sum_1000
        expected = s..([(200, 375, 425)])
        assertEqual(triplets_with_sum(1000), expected)

    ___ test_no_triplet_exists
        expected = s..([])
        assertEqual(triplets_with_sum(1001), expected)

    ___ test_two_matching_triplets
        expected = s..([(9, 40, 41), (15, 36, 39)])
        assertEqual(triplets_with_sum(90), expected)

    ___ test_several_matching_triplets
        expected = s..([(40, 399, 401),
                        (56, 390, 394),
                        (105, 360, 375),
                        (120, 350, 370),
                        (140, 336, 364),
                        (168, 315, 357),
                        (210, 280, 350),
                        (240, 252, 348)])
        assertEqual(triplets_with_sum(840), expected)

    ___ test_triplets_for_large_numbers
        expected = s..([(1200, 14375, 14425),
                        (1875, 14000, 14125),
                        (5000, 12000, 13000),
                        (6000, 11250, 12750),
                        (7500, 10000, 12500)])
        assertEqual(triplets_with_sum(30000), expected)


__ _____ __ _____
    unittest.main()
