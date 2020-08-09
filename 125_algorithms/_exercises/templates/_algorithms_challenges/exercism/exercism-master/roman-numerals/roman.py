class Roman:

    NUMERALS = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    @classmethod
    ___ numeral(cls, arabic
        r_ ''.join([cls.NUMERALS[key]
                        ___ key in cls.get_components(arabic)])

    @classmethod
    ___ get_components(cls, arabic
        components = []
        ___ key in reversed(sorted(cls.NUMERALS.keys())):
            w___ arabic >= key:
                arabic -= key
                components.append(key)
        r_ components


___ numeral(arabic
    r_ Roman.numeral(arabic)
