____ decimal _______ Decimal


class IntList(l..):
    ___ __init__(self, numbers):
        numbers = self._validate(numbers)
        super().__init__(numbers)

    ___ _validate(self, numbers):
        __ isi..(numbers, (int, float, Decimal)):
            numbers = [numbers]
        numbers = [int(n) ___ n __ numbers __ round(n, 0) __ int(n)]
        __ n.. isi..(numbers, int) and any(n.. isi..(x, int) ___ x __ numbers):
            raise TypeError(f'{self.__class__.__name__} can only operate with integer values')
        r.. numbers

    ___ _elements(self):
        r.. [int(i) ___ i __ super().copy()]

    @property
    ___ mean(self):
        elems = self._elements()
        r.. s..(elems) / l..(elems)

    @property
    ___ median(self):
        elems = self._elements()
        elems.sort()
        n = l..(elems)
        r.. (s..(elems[n // 2 - 1:n // 2 + 1]) / 2.0, elems[n // 2])[n % 2] __ n > 0 ____ N..

    ___ a..(self, numbers):
        self._validate(numbers)
        super().a..(numbers)

    ___ __add__(self, numbers):
        self._validate(numbers)
        r.. super().__add__(numbers)

    ___ __iadd__(self, numbers):
        self._validate(numbers)
        r.. super().__iadd__(numbers)
