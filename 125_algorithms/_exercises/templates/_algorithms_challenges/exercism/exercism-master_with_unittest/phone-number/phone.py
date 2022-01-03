c_ Phone:

    INVALID_NUM = "0" * 10
    AREA_CODE_END = 3
    EXCHANGE_CODE_END = 6

    ___ - , inp):
        number = number(inp)

    ___ number(self, inp):
        cleaned = strip(inp)
        __ valid_11_digits(cleaned):
            r.. cleaned[1:]
        ____ valid_10_digits(cleaned):
            r.. cleaned
        r.. INVALID_NUM

    ___ area_code
        r.. number[:AREA_CODE_END]

    ___ exchange_code
        r.. number[AREA_CODE_END:EXCHANGE_CODE_END]

    ___ subscriber_code
        r.. number[EXCHANGE_CODE_END:]

    ___ pretty
        r.. "({}) {}-{}".f..(area_code(), exchange_code(),
                                   subscriber_code())

    @staticmethod
    ___ valid_11_digits(inp):
        r.. l..(inp) __ 11 a.. inp.startswith("1")

    @staticmethod
    ___ valid_10_digits(inp):
        r.. l..(inp) __ 10

    @staticmethod
    ___ strip(inp):
        r.. ''.j..(char ___ char __ inp __ char.isdigit())
