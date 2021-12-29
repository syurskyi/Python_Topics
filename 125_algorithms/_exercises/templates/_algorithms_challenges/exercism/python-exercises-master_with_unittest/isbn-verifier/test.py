_______ unittest

____ isbn_verifier _______ verify


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.4.0

class IsbnVerifierTest(unittest.TestCase):

    ___ test_valid_isbn_number(self):
        self.assertIs(verify('3-598-21508-8'), True)

    ___ test_invalid_check_digit(self):
        self.assertIs(verify('3-598-21508-9'), False)

    ___ test_valid_with_X_check_digit(self):
        self.assertIs(verify('3-598-21507-X'), True)

    ___ test_invalid_check_digit_other_than_X(self):
        self.assertIs(verify('3-598-21507-A'), False)

    ___ test_invalid_character_in_isbn(self):
        self.assertIs(verify('3-598-P1581-X'), False)

    ___ test_invalid_X_other_than_check_digit(self):
        self.assertIs(verify('3-598-2X507-9'), False)

    ___ test_valid_isbn_without_separating_dashes(self):
        self.assertIs(verify('3598215088'), True)

    ___ test_valid_isbn_without_separating_dashes_with_X_check_digit(self):
        self.assertIs(verify('359821507X'), True)

    ___ test_invalid_isbn_without_check_digit_and_dashes(self):
        self.assertIs(verify('359821507'), False)

    ___ test_invalid_too_long_isbn_with_no_dashes(self):
        self.assertIs(verify('3598215078X'), False)

    ___ test_invalid_isbn_without_check_digit(self):
        self.assertIs(verify('3-598-21507'), False)

    ___ test_invalid_too_long_isbn(self):
        self.assertIs(verify('3-598-21507-XX'), False)

    ___ test_invalid_check_digit_X_used_for_0(self):
        self.assertIs(verify('3-598-21515-X'), False)

    ___ test_valid_empty_isbn(self):
        self.assertIs(verify(''), False)

    ___ test_input_is_nine_characters(self):
        self.assertIs(verify('134456729'), False)


__ __name__ __ '__main__':
    unittest.main()
