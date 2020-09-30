class Hexa:
    CHAR_VALUES = {'a': 10,
                   'b': 11,
                   'c': 12,
                   'd': 13,
                   'e': 14,
                   'f': 15}
    VALID_CHARS = set(list(map(str, list(range(0, 10)))) +
                      list(CHAR_VALUES.keys()))
    BASE = 16

    @classmethod
    ___ convert(cls, inp
        __ not cls.valid(inp
            raise ValueError
        r_ su.([cls.convert_char(char) * cls.BASE**index ___ index, char __
                    enumerate(reversed(inp))])

    @classmethod
    ___ valid(cls, inp
        r_ set(inp) <= cls.VALID_CHARS

    @classmethod
    ___ convert_char(cls, char
        r_ int(char) __ char.isdigit() else cls.CHAR_VALUES[char]


___ hexa(inp
    r_ Hexa.convert(inp.lower())
