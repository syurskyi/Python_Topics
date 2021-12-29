class Phone:

    INVALID_NUM = "0" * 10
    AREA_CODE_END = 3
    EXCHANGE_CODE_END = 6

    ___ __init__(self, inp):
        self.number = self.number(inp)

    ___ number(self, inp):
        cleaned = self.strip(inp)
        __ self.valid_11_digits(cleaned):
            r.. cleaned[1:]
        ____ self.valid_10_digits(cleaned):
            r.. cleaned
        r.. self.INVALID_NUM

    ___ area_code(self):
        r.. self.number[:self.AREA_CODE_END]

    ___ exchange_code(self):
        r.. self.number[self.AREA_CODE_END:self.EXCHANGE_CODE_END]

    ___ subscriber_code(self):
        r.. self.number[self.EXCHANGE_CODE_END:]

    ___ pretty(self):
        r.. "({}) {}-{}".format(self.area_code(), self.exchange_code(),
                                   self.subscriber_code())

    @staticmethod
    ___ valid_11_digits(inp):
        r.. l..(inp) __ 11 and inp.startswith("1")

    @staticmethod
    ___ valid_10_digits(inp):
        r.. l..(inp) __ 10

    @staticmethod
    ___ strip(inp):
        r.. ''.join(char ___ char __ inp __ char.isdigit())
