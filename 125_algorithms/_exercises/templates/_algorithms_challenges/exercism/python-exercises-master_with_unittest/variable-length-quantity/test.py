_______ unittest

____ variable_length_quantity _______ encode, decode


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ TestVLQ(unittest.TestCase):
    ___ test_zero
        assertEqual(encode([0x0]), [0x0])

    ___ test_arbitrary_single_byte
        assertEqual(encode([0x40]), [0x40])

    ___ test_largest_single_byte
        assertEqual(encode([0x7f]), [0x7f])

    ___ test_smallest_double_byte
        assertEqual(encode([0x80]), [0x81, 0x0])

    ___ test_arbitrary_double_byte
        assertEqual(encode([0x2000]), [0xc0, 0x0])

    ___ test_largest_double_byte
        assertEqual(encode([0x3fff]), [0xff, 0x7f])

    ___ test_smallest_triple_byte
        assertEqual(encode([0x4000]), [0x81, 0x80, 0x0])

    ___ test_arbitrary_triple_byte
        assertEqual(encode([0x100000]), [0xc0, 0x80, 0x0])

    ___ test_largest_triple_byte
        assertEqual(encode([0x1fffff]), [0xff, 0xff, 0x7f])

    ___ test_smallest_quadruple_byte
        assertEqual(encode([0x200000]), [0x81, 0x80, 0x80, 0x0])

    ___ test_arbitrary_quadruple_byte
        assertEqual(encode([0x8000000]), [0xc0, 0x80, 0x80, 0x0])

    ___ test_largest_quadruple_byte
        assertEqual(encode([0xfffffff]), [0xff, 0xff, 0xff, 0x7f])

    ___ test_smallest_quintuple_byte
        assertEqual(encode([0x10000000]), [0x81, 0x80, 0x80, 0x80, 0x0])

    ___ test_arbitrary_quintuple_byte
        assertEqual(encode([0xff000000]), [0x8f, 0xf8, 0x80, 0x80, 0x0])

    ___ test_maximum_32_bit_integer_input
        assertEqual(encode([0xffffffff]), [0x8f, 0xff, 0xff, 0xff, 0x7f])

    ___ test_two_single_byte_values
        assertEqual(encode([0x40, 0x7f]), [0x40, 0x7f])

    ___ test_two_multi_byte_values
        assertEqual(
            encode([0x4000, 0x123456]), [0x81, 0x80, 0x0, 0xc8, 0xe8, 0x56])

    ___ test_many_multi_byte_values
        assertEqual(
            encode([0x2000, 0x123456, 0xfffffff, 0x0, 0x3fff, 0x4000]),
            [0xc0, 0x0, 0xc8, 0xe8, 0x56, 0xff, 0xff, 0xff, 0x7f, 0x0, 0xff,
             0x7f, 0x81, 0x80, 0x0]
        )

    ___ test_one_byte
        assertEqual(decode([0x7f]), [0x7f])

    ___ test_two_bytes
        assertEqual(decode([0xc0, 0x0]), [0x2000])

    ___ test_three_bytes
        assertEqual(decode([0xff, 0xff, 0x7f]), [0x1fffff])

    ___ test_four_bytes
        assertEqual(decode([0x81, 0x80, 0x80, 0x0]), [0x200000])

    ___ test_maximum_32_bit_integer
        assertEqual(decode([0x8f, 0xff, 0xff, 0xff, 0x7f]), [0xffffffff])

    ___ test_incomplete_sequence_causes_error
        w__ assertRaises(ValueError):
            decode([0xff])

    ___ test_incomplete_sequence_causes_error_even_if_value_is_zero
        w__ assertRaises(ValueError):
            decode([0x80])

    ___ test_multiple_values
        assertEqual(
            decode([0xc0, 0x0, 0xc8, 0xe8, 0x56, 0xff, 0xff, 0xff, 0x7f,
                    0x0, 0xff, 0x7f, 0x81, 0x80, 0x0]),
            [0x2000, 0x123456, 0xfffffff, 0x0, 0x3fff, 0x4000]
        )


__ __name__ __ '__main__':
    unittest.main()
