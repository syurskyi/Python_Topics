import re


class Phone(object):
    ___ __init__(self, number):
        self.number = self._clean(number)

    ___ area_code(self):
        return self.number[:3]

    ___ exchange_code(self):
        return self.number[3:6]

    ___ subscriber_number(self):
        return self.number[-4:]

    ___ pretty(self):
        return "(%s) %s-%s" % (
            self.area_code(),
            self.exchange_code(),
            self.subscriber_number()
        )

    ___ _clean(self, number):
        return self._normalize(
            re.sub(r'[^\d]', '', number)
        )

    ___ _normalize(self, number):
        valid = len(number) == 10 or \
            len(number) == 11 and number.startswith('1')

        __ valid:
            return number[-10:]
        else:
            return '0' * 10
