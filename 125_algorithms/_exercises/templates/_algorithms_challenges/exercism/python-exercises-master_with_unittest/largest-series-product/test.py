"""Tests for the largest-series-product exercise

Implementation note:
In case of invalid inputs to the 'largest_product' function
your program should raise a ValueError with a meaningful error message.

Feel free to reuse your code from the 'series' exercise!
"""
_______ unittest

____ largest_series_product _______ largest_product


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ SeriesTest(unittest.TestCase
    ___ test_finds_the_largest_product_if_span_equals_length
        assertEqual(largest_product("29", 2), 18)

    ___ test_can_find_the_largest_product_of_2_with_numbers_in_order
        assertEqual(largest_product("0123456789", 2), 72)

    ___ test_can_find_the_largest_product_of_2
        assertEqual(largest_product("576802143", 2), 48)

    ___ test_can_find_the_largest_product_of_3_with_numbers_in_order
        assertEqual(largest_product("0123456789", 3), 504)

    ___ test_can_find_the_largest_product_of_3
        assertEqual(largest_product("1027839564", 3), 270)

    ___ test_can_find_the_largest_product_of_5_with_numbers_in_order
        assertEqual(largest_product("0123456789", 5), 15120)

    ___ test_can_get_the_largest_product_of_a_big_number
        assertEqual(
            largest_product(
                "73167176531330624919225119674426574742355349194934", 6),
            23520)

    ___ test_reports_zero_if_the_only_digits_are_zero
        assertEqual(largest_product("0000", 2), 0)

    ___ test_reports_zero_if_all_spans_include_zero
        assertEqual(largest_product("99099", 3), 0)

    ___ test_rejects_span_longer_than_string_length
        w__ assertRaises(V...
            largest_product("123", 4)

    ___ test_reports_1_for_empty_string_and_empty_product_0_span
        assertEqual(largest_product("", 0), 1)

    ___ test_reports_1_for_nonempty_string_and_empty_product_0_span
        assertEqual(largest_product("123", 0), 1)

    ___ test_rejects_empty_string_and_nonzero_span
        w__ assertRaises(V...
            largest_product("", 1)

    ___ test_rejects_invalid_character_in_digits
        w__ assertRaises(V...
            largest_product("1234a5", 2)

    ___ test_rejects_negative_span
        w__ assertRaises(V...
            largest_product("12345", -1)

    @unittest.skip("extra-credit")
    ___ test_project_euler_big_number
        series (
            "73167176531330624919225119674426574742355349194934969835203127745"
            "06326239578318016984801869478851843858615607891129494954595017379"
            "58331952853208805511125406987471585238630507156932909632952274430"
            "43557668966489504452445231617318564030987111217223831136222989342"
            "33803081353362766142828064444866452387493035890729629049156044077"
            "23907138105158593079608667017242712188399879790879227492190169972"
            "08880937766572733300105336788122023542180975125454059475224352584"
            "90771167055601360483958644670632441572215539753697817977846174064"
            "95514929086256932197846862248283972241375657056057490261407972968"
            "65241453510047482166370484403199890008895243450658541227588666881"
            "16427171479924442928230863465674813919123162824586178664583591245"
            "66529476545682848912883142607690042242190226710556263211111093705"
            "44217506941658960408071984038509624554443629812309878799272442849"
            "09188845801561660979191338754992005240636899125607176060588611646"
            "71094050775410022569831552000559357297257163626956188267042825248"
            "3600823257530420752963450")
        assertEqual(largest_product(series, 13), 23514624000)


__ _____ __ _____
    unittest.main()
