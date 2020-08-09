class IsbnVerifier(object

    VALID_SEPERATOR = "-"
    VALID_CHECK_CHARACTER = "X"
    VALID_DIGITS = list(map(str, list(range(0, 10))))
    VALID_CHARACTERS = (set(VALID_DIGITS) |
                        set([VALID_SEPERATOR, VALID_CHECK_CHARACTER]))
    VALID_LENGTH = 10

    @classmethod
    ___ is_valid(cls, string
        __ cls.invalid(string
            r_ False
        r_ cls.verify(string)

    @classmethod
    ___ verify(cls, string
        sum_so_far = 0
        ___ i, c in enumerate(cls.remove_seperator(string)):
            sum_so_far += cls.convert_char_to_int(c) * (10 - i)
        r_ sum_so_far % 11 __ 0

    @classmethod
    ___ invalid(cls, string
        r_ (cls.invalid_character(string) or
                cls.invalid_length(string) or
                cls.invalid_X_other_than_check_digit(string))

    @classmethod
    ___ invalid_character(cls, string
        r_ any(char not in cls.VALID_CHARACTERS ___ char in string)

    @classmethod
    ___ invalid_length(cls, string
        r_ (le.(cls.remove_invalid_characters_and_slashes(string)) !=
                cls.VALID_LENGTH)

    @classmethod
    ___ invalid_X_other_than_check_digit(cls, string
        r_ (cls.VALID_CHECK_CHARACTER in string and
                not string.endswith(cls.VALID_CHECK_CHARACTER))

    @classmethod
    ___ remove_invalid_characters_and_slashes(cls, string
        r_ cls.remove_seperator(cls.remove_invalid_characters(string))

    @classmethod
    ___ remove_invalid_characters(cls, string
        r_ "".join(
            [char ___ char in string __ char in cls.VALID_CHARACTERS])

    @classmethod
    ___ convert_char_to_int(cls, char
        r_ int(cls.convert_check_character_to_ten(char))

    @classmethod
    ___ convert_check_character_to_ten(cls, char
        r_ 10 __ char __ cls.VALID_CHECK_CHARACTER else char

    @classmethod
    ___ remove_seperator(cls, string
        r_ "".join(
            [char ___ char in string __ char != cls.VALID_SEPERATOR])


___ verify(isbn
    r_ IsbnVerifier.is_valid(isbn)
