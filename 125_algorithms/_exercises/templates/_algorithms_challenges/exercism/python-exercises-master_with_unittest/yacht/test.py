_______ unittest

_______ yacht
____ yacht _______ score


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

c_ YachtTest(unittest.TestCase
    ___ test_yacht
        assertEqual(score([5, 5, 5, 5, 5], yacht.YACHT), 50)

    ___ test_not_yacht
        assertEqual(score([1, 3, 3, 2, 5], yacht.YACHT), 0)

    ___ test_ones
        assertEqual(score([1, 1, 1, 3, 5], yacht.ONES), 3)

    ___ test_ones_out_of_order
        assertEqual(score([3, 1, 1, 5, 1], yacht.ONES), 3)

    ___ test_no_ones
        assertEqual(score([4, 3, 6, 5, 5], yacht.ONES), 0)

    ___ test_twos
        assertEqual(score([2, 3, 4, 5, 6], yacht.TWOS), 2)

    ___ test_fours
        assertEqual(score([1, 4, 1, 4, 1], yacht.FOURS), 8)

    ___ test_yacht_counted_as_threes
        assertEqual(score([3, 3, 3, 3, 3], yacht.THREES), 15)

    ___ test_yacht_of_threes_counted_as_fives
        assertEqual(score([3, 3, 3, 3, 3], yacht.FIVES), 0)

    ___ test_sixes
        assertEqual(score([2, 3, 4, 5, 6], yacht.SIXES), 6)

    ___ test_full_house_two_small_three_big
        assertEqual(score([2, 2, 4, 4, 4], yacht.FULL_HOUSE), 16)

    ___ test_full_house_three_small_two_big
        assertEqual(score([5, 3, 3, 5, 3], yacht.FULL_HOUSE), 19)

    ___ test_two_pair_is_not_a_full_house
        assertEqual(score([2, 2, 4, 4, 5], yacht.FULL_HOUSE), 0)

    ___ test_four_of_a_kind_is_not_a_full_house
        assertEqual(score([1, 4, 4, 4, 4], yacht.FULL_HOUSE), 0)

    ___ test_yacht_is_not_a_full_house
        assertEqual(score([2, 2, 2, 2, 2], yacht.FULL_HOUSE), 0)

    ___ test_four_of_a_kind
        assertEqual(score([6, 6, 4, 6, 6], yacht.FOUR_OF_A_KIND), 24)

    ___ test_yacht_can_be_scored_as_four_of_a_kind
        assertEqual(score([3, 3, 3, 3, 3], yacht.FOUR_OF_A_KIND), 12)

    ___ test_full_house_is_not_four_of_a_kind
        assertEqual(score([3, 5, 4, 1, 2], yacht.FOUR_OF_A_KIND), 0)

    ___ test_little_straight
        assertEqual(score([3, 5, 4, 1, 2], yacht.LITTLE_STRAIGHT), 30)

    ___ test_little_straight_as_big_straight
        assertEqual(score([1, 2, 3, 4, 5], yacht.BIG_STRAIGHT), 0)

    ___ test_four_in_order_but_not_a_little_straight
        assertEqual(score([1, 1, 2, 3, 4], yacht.LITTLE_STRAIGHT), 0)

    ___ test_no_pairs_but_not_a_little_straight
        assertEqual(score([1, 2, 3, 4, 6], yacht.LITTLE_STRAIGHT), 0)

    ___ test_min_1_max_5_but_not_a_little_straight
        assertEqual(score([1, 1, 3, 4, 5], yacht.LITTLE_STRAIGHT), 0)

    ___ test_big_straight
        assertEqual(score([4, 6, 2, 5, 3], yacht.BIG_STRAIGHT), 30)

    ___ test_big_straight_as_little_straight
        assertEqual(score([6, 5, 4, 3, 2], yacht.LITTLE_STRAIGHT), 0)

    ___ test_choice
        assertEqual(score([3, 3, 5, 6, 6], yacht.CHOICE), 23)

    ___ test_yacht_as_choice
        assertEqual(score([2, 2, 2, 2, 2], yacht.CHOICE), 10)


__ _____ __ _____
    unittest.main()
