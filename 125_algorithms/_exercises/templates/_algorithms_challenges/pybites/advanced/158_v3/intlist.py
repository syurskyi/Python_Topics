____ decimal _______ Decimal


c_ IntList(l..):
    ___ - , numbers):
        numbers = _validate(numbers)
        super().__init__(numbers)

    ___ _validate(self, numbers):
        __ isi..(numbers, (int, float, Decimal)):
            numbers = [numbers]
        numbers = [int(n) ___ n __ numbers __ round(n, 0) __ int(n)]
        __ n.. isi..(numbers, int) a.. any(n.. isi..(x, int) ___ x __ numbers):
            raise TypeError(f'{__class__.__name__} can only operate with integer values')
        r.. numbers

    ___ _elements
        r.. [int(i) ___ i __ super().c..]

    $
    ___ mean
        elems = _elements()
        r.. s..(elems) / l..(elems)

    $
    ___ median
        elems = _elements()
        elems.s..()
        n = l..(elems)
        r.. (s..(elems[n // 2 - 1:n // 2 + 1]) / 2.0, elems[n // 2])[n % 2] __ n > 0 ____ N..

    ___ a..(self, numbers):
        _validate(numbers)
        super().a..(numbers)

    ___ __add__(self, numbers):
        _validate(numbers)
        r.. super().__add__(numbers)

    ___ __iadd__(self, numbers):
        _validate(numbers)
        r.. super().__iadd__(numbers)
