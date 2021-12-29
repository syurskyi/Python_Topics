class Animal:
    # 'Class variables'
    _zoo = N..
    _index = N..

    ___ __init__(self, name: str):
        self.name = name.t..
        self.index = self._next_index()
        self._add_to_zoo(self)

    ___ __repr__(self):
        r.. f'{self.index}. {self.name}'

    @classmethod
    ___ _next_index(cls):
        __ cls._index __ N..
            cls._index = 10000
        cls._index += 1
        r.. cls._index

    @classmethod
    ___ _add_to_zoo(cls, animal):
        __ cls._zoo __ N..
            cls._zoo    # list
        cls._zoo.a..(animal)

    @classmethod
    ___ zoo(cls):
        __ cls._zoo __ N..
            r.. ''
        r.. str(cls._zoo)
