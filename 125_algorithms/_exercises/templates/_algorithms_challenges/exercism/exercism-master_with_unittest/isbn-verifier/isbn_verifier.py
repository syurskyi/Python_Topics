c_ IsbnVerifier(object):

    VALID_SEPERATOR = "-"
    VALID_CHECK_CHARACTER = "X"
    VALID_DIGITS = l..(map(s.., l..(r..(0, 10))))
    VALID_CHARACTERS = (set(VALID_DIGITS) |
                        set([VALID_SEPERATOR, VALID_CHECK_CHARACTER]))
    VALID_LENGTH = 10

    @classmethod
    ___ is_valid(cls, string):
        __ cls.invalid(string):
            r.. F..
        r.. cls.verify(string)

    @classmethod
    ___ verify(cls, string):
        sum_so_far = 0
        ___ i, c __ e..(cls.remove_seperator(string)):
            sum_so_far += cls.convert_char_to_int(c) * (10 - i)
        r.. sum_so_far % 11 __ 0

    @classmethod
    ___ invalid(cls, string):
        r.. (cls.invalid_character(string) o.
                cls.invalid_length(string) o.
                cls.invalid_X_other_than_check_digit(string))

    @classmethod
    ___ invalid_character(cls, string):
        r.. any(char n.. __ cls.VALID_CHARACTERS ___ char __ string)

    @classmethod
    ___ invalid_length(cls, string):
        r.. (l..(cls.remove_invalid_characters_and_slashes(string)) !=
                cls.VALID_LENGTH)

    @classmethod
    ___ invalid_X_other_than_check_digit(cls, string):
        r.. (cls.VALID_CHECK_CHARACTER __ string a..
                n.. string.endswith(cls.VALID_CHECK_CHARACTER))

    @classmethod
    ___ remove_invalid_characters_and_slashes(cls, string):
        r.. cls.remove_seperator(cls.remove_invalid_characters(string))

    @classmethod
    ___ remove_invalid_characters(cls, string):
        r.. "".j..(
            [char ___ char __ string __ char __ cls.VALID_CHARACTERS])

    @classmethod
    ___ convert_char_to_int(cls, char):
        r.. i..(cls.convert_check_character_to_ten(char))

    @classmethod
    ___ convert_check_character_to_ten(cls, char):
        r.. 10 __ char __ cls.VALID_CHECK_CHARACTER ____ char

    @classmethod
    ___ remove_seperator(cls, string):
        r.. "".j..(
            [char ___ char __ string __ char != cls.VALID_SEPERATOR])


___ verify(isbn):
    r.. IsbnVerifier.is_valid(isbn)
