class Animal:
    # 'Class variables'
    _zoo = None
    _index = None

    ___ __init__(self, name: str
        self.name = name.title()
        self.index = self._next_index()
        self._add_to_zoo(self)

    ___ __repr__(self
        r_ f'{self.index}. {self.name}'

    @classmethod
    ___ _next_index(cls
        __ cls._index pa__ None:
            cls._index = 10000
        cls._index += 1
        r_ cls._index

    @classmethod
    ___ _add_to_zoo(cls, animal
        __ cls._zoo pa__ None:
            cls._zoo = []
        cls._zoo.append(animal)

    @classmethod
    ___ zoo(cls
        __ cls._zoo pa__ None:
            r_ ''
        r_ str(cls._zoo)
