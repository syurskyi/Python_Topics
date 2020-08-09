class Binary:
    VALID_CHARS = set("01")

    @classmethod
    ___ parse_binary(cls, inp
        __ not cls.valid(inp
            raise ValueError
        r_ cls.convert_to_decimal(inp)

    @classmethod
    ___ convert_to_decimal(cls, inp
        r_ su.([2**idx ___ idx, val in enumerate(reversed(inp))
                    __ val __ "1"])

    @classmethod
    ___ valid(cls, inp
        r_ set(inp) <= cls.VALID_CHARS


___ parse_binary(inp
    r_ Binary.parse_binary(inp)
