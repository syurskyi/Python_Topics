c_ Roman:

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
        r.. ''.j..([cls.NUMERALS[key]
                        ___ key __ cls.get_components(arabic)])

    @classmethod
    ___ get_components(cls, arabic
        components    # list
        ___ key __ r..(s..(cls.NUMERALS.keys())):
            w.... arabic >_ key:
                arabic -= key
                components.a..(key)
        r.. components


___ numeral(arabic
    r.. Roman.numeral(arabic)
