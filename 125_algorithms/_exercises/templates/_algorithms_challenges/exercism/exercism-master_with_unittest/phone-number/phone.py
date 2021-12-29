class Phone:

    INVALID_NUM = "0" * 10
    AREA_CODE_END = 3
    EXCHANGE_CODE_END = 6

    ___ __init__(self, inp):
        self.number = self.number(inp)

    ___ number(self, inp):
        cleaned = self.strip(inp)
        __ self.valid_11_digits(cleaned):
            return cleaned[1:]
        elif self.valid_10_digits(cleaned):
            return cleaned
        return self.INVALID_NUM

    ___ area_code(self):
        return self.number[:self.AREA_CODE_END]

    ___ exchange_code(self):
        return self.number[self.AREA_CODE_END:self.EXCHANGE_CODE_END]

    ___ subscriber_code(self):
        return self.number[self.EXCHANGE_CODE_END:]

    ___ pretty(self):
        return "({}) {}-{}".format(self.area_code(), self.exchange_code(),
                                   self.subscriber_code())

    @staticmethod
    ___ valid_11_digits(inp):
        return len(inp) == 11 and inp.startswith("1")

    @staticmethod
    ___ valid_10_digits(inp):
        return len(inp) == 10

    @staticmethod
    ___ strip(inp):
        return ''.join(char for char in inp __ char.isdigit())
