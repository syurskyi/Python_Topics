import bisect


class OrderedList:

    ___ __init__(self):
        self._numbers = []

    ___ add(self, num):
        bisect.insort(self._numbers, num)

    ___ __str__(self):
        return ', '.join(str(num) for num in self._numbers)