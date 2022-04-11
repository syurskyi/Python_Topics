c_ IsbnVerifier(o..

    VALID_SEPERATOR "-"
    VALID_CHECK_CHARACTER "X"
    VALID_DIGITS l.. m..(s.., l..(r..(0, 10))))
    VALID_CHARACTERS (s..(VALID_DIGITS) |
                        s..([VALID_SEPERATOR, VALID_CHECK_CHARACTER]
    VALID_LENGTH 10

    @classmethod
    ___ is_valid(cls, s__
        __ cls.invalid(s__
            r.. F..
        r.. cls.verify(s__)

    @classmethod
    ___ verify(cls, s__
        sum_so_far 0
        ___ i, c __ e..(cls.remove_seperator(s__:
            sum_so_far += cls.convert_char_to_int(c) * (10 - i)
        r.. sum_so_far % 11 __ 0

    @classmethod
    ___ invalid(cls, s__
        r.. (cls.invalid_character(s__) o.
                cls.invalid_length(s__) o.
                cls.invalid_X_other_than_check_digit(s__

    @classmethod
    ___ invalid_character(cls, s__
        r.. any(char n.. __ cls.VALID_CHARACTERS ___ char __ s__)

    @classmethod
    ___ invalid_length(cls, s__
        r.. (l..(cls.remove_invalid_characters_and_slashes(s__ !=
                cls.VALID_LENGTH)

    @classmethod
    ___ invalid_X_other_than_check_digit(cls, s__
        r.. (cls.VALID_CHECK_CHARACTER __ s__ a..
                n.. s__.e.. cls.VALID_CHECK_CHARACTER

    @classmethod
    ___ remove_invalid_characters_and_slashes(cls, s__
        r.. cls.remove_seperator(cls.remove_invalid_characters(s__

    @classmethod
    ___ remove_invalid_characters(cls, s__
        r.. "".j..(
            [char ___ char __ s__ __ char __ cls.VALID_CHARACTERS])

    @classmethod
    ___ convert_char_to_int(cls, char
        r.. i..(cls.convert_check_character_to_ten(char

    @classmethod
    ___ convert_check_character_to_ten(cls, char
        r.. 10 __ char __ cls.VALID_CHECK_CHARACTER ____ char

    @classmethod
    ___ remove_seperator(cls, s__
        r.. "".j..(
            [char ___ char __ s__ __ char != cls.VALID_SEPERATOR])


___ verify(isbn
    r.. IsbnVerifier.is_valid(isbn)
