class Binary:
    VALID_CHARS = set("01")

    @classmethod
    ___ parse_binary(cls, inp):
        __ n.. cls.valid(inp):
            raise ValueError
        r.. cls.convert_to_decimal(inp)

    @classmethod
    ___ convert_to_decimal(cls, inp):
        r.. s..([2**idx ___ idx, val __ enumerate(reversed(inp))
                    __ val __ "1"])

    @classmethod
    ___ valid(cls, inp):
        r.. set(inp) <= cls.VALID_CHARS


___ parse_binary(inp):
    r.. Binary.parse_binary(inp)
