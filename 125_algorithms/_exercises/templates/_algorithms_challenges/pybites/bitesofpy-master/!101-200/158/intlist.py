from decimal ______ Decimal


class IntList(list
    ___ __init__(self, numbers
        numbers = self._validate(numbers)
        super().__init__(numbers)

    ___ _validate(self, numbers
        __ isinstance(numbers, (int, float, Decimal)):
            numbers = [numbers]
        numbers = [int(n) for n in numbers __ round(n, 0) __ int(n)]
        __ not isinstance(numbers, int) and any(not isinstance(x, int) for x in numbers
            raise TypeError(f'{self.__class__.__name__} can only operate with integer values')
        r_ numbers

    ___ _elements(self
        r_ [int(i) for i in super().copy()]

    @property
    ___ mean(self
        elems = self._elements()
        r_ sum(elems) / le.(elems)

    @property
    ___ median(self
        elems = self._elements()
        elems.sort()
        n = le.(elems)
        r_ (sum(elems[n // 2 - 1:n // 2 + 1]) / 2.0, elems[n // 2])[n % 2] __ n > 0 else None

    ___ append(self, numbers
        self._validate(numbers)
        super().append(numbers)

    ___ __add__(self, numbers
        self._validate(numbers)
        r_ super().__add__(numbers)

    ___ __iadd__(self, numbers
        self._validate(numbers)
        r_ super().__iadd__(numbers)
