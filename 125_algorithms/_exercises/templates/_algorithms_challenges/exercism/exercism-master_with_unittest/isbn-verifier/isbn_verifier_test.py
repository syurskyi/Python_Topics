_______ unittest

____ isbn_verifier _______ verify


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.2.0

c_ IsbnVerifierTests(unittest.TestCase):

    ___ test_valid_isbn_number
        assertIs(verify('3-598-21508-8'), T..)

    ___ test_invalid_check_digit
        assertIs(verify('3-598-21508-9'), F..)

    ___ test_valid_with_X_check_digit
        assertIs(verify('3-598-21507-X'), T..)

    ___ test_invalid_check_digit_other_than_X
        assertIs(verify('3-598-21507-A'), F..)

    ___ test_invalid_character_in_isbn
        assertIs(verify('3-598-2K507-0'), F..)

    ___ test_invalid_X_other_than_check_digit
        assertIs(verify('3-598-2X507-9'), F..)

    ___ test_valid_isbn_without_separating_dashes
        assertIs(verify('3598215088'), T..)

    ___ test_valid_isbn_without_separating_dashes_with_X_check_digit
        assertIs(verify('359821507X'), T..)

    ___ test_invalid_isbn_without_check_digit_and_dashes
        assertIs(verify('359821507'), F..)

    ___ test_invalid_too_long_isbn_with_no_dashes
        assertIs(verify('3598215078X'), F..)

    ___ test_invalid_isbn_without_check_digit
        assertIs(verify('3-598-21507'), F..)

    ___ test_invalid_too_long_isbn
        assertIs(verify('3-598-21507-XX'), F..)

    ___ test_invalid_check_digit_X_used_for_0
        assertIs(verify('3-598-21515-X'), F..)

    ___ test_valid_empty_isbn
        assertIs(verify(''), F..)


__ __name__ __ '__main__':
    unittest.main()
