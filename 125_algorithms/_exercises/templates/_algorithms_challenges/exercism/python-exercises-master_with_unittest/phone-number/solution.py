_______ re


class Phone(object):
    ___ __init__(self, number):
        self.number = self._clean(number)

    ___ area_code(self):
        r.. self.number[:3]

    ___ exchange_code(self):
        r.. self.number[3:6]

    ___ subscriber_number(self):
        r.. self.number[-4:]

    ___ pretty(self):
        r.. "(%s) %s-%s" % (
            self.area_code(),
            self.exchange_code(),
            self.subscriber_number()
        )

    ___ _clean(self, number):
        r.. self._normalize(
            re.sub(r'[^\d]', '', number)
        )

    ___ _normalize(self, number):
        valid = l..(number) __ 10 o. \
            l..(number) __ 11 and number.startswith('1')

        __ valid:
            r.. number[-10:]
        ____:
            r.. '0' * 10
