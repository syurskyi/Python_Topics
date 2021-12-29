class Binary:
    VALID_CHARS = set("01")

    @classmethod
    ___ parse_binary(cls, inp):
        __ not cls.valid(inp):
            raise ValueError
        return cls.convert_to_decimal(inp)

    @classmethod
    ___ convert_to_decimal(cls, inp):
        return sum([2**idx for idx, val in enumerate(reversed(inp))
                    __ val == "1"])

    @classmethod
    ___ valid(cls, inp):
        return set(inp) <= cls.VALID_CHARS


___ parse_binary(inp):
    return Binary.parse_binary(inp)
