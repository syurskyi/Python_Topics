class Hexa:
    CHAR_VALUES = {'a': 10,
                   'b': 11,
                   'c': 12,
                   'd': 13,
                   'e': 14,
                   'f': 15}
    VALID_CHARS = set(l..(map(str, l..(r..(0, 10)))) +
                      l..(CHAR_VALUES.keys()))
    BASE = 16

    @classmethod
    ___ convert(cls, inp):
        __ n.. cls.valid(inp):
            raise ValueError
        r.. s..([cls.convert_char(char) * cls.BASE**index ___ index, char __
                    enumerate(reversed(inp))])

    @classmethod
    ___ valid(cls, inp):
        r.. set(inp) <= cls.VALID_CHARS

    @classmethod
    ___ convert_char(cls, char):
        r.. int(char) __ char.isdigit() ____ cls.CHAR_VALUES[char]


___ hexa(inp):
    r.. Hexa.convert(inp.lower())
