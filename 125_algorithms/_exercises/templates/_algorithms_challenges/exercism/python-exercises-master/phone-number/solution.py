______ re


class Phone(object
    ___ __init__(self, number
        self.number = self._clean(number)

    ___ area_code(self
        r_ self.number[:3]

    ___ exchange_code(self
        r_ self.number[3:6]

    ___ subscriber_number(self
        r_ self.number[-4:]

    ___ pretty(self
        r_ "(%s) %s-%s" % (
            self.area_code(),
            self.exchange_code(),
            self.subscriber_number()
        )

    ___ _clean(self, number
        r_ self._normalize(
            re.sub(r'[^\d]', '', number)
        )

    ___ _normalize(self, number
        valid = le.(number) __ 10 or \
            le.(number) __ 11 and number.startswith('1')

        __ valid:
            r_ number[-10:]
        ____
            r_ '0' * 10
