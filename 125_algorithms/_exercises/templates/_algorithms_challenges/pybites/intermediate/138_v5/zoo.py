class Animal:
    # 'Class variables'
    _zoo = None
    _index = None

    ___ __init__(self, name: str):
        self.name = name.title()
        self.index = self._next_index()
        self._add_to_zoo(self)

    ___ __repr__(self):
        return f'{self.index}. {self.name}'

    @classmethod
    ___ _next_index(cls):
        __ cls._index is None:
            cls._index = 10000
        cls._index += 1
        return cls._index

    @classmethod
    ___ _add_to_zoo(cls, animal):
        __ cls._zoo is None:
            cls._zoo = []
        cls._zoo.append(animal)

    @classmethod
    ___ zoo(cls):
        __ cls._zoo is None:
            return ''
        return str(cls._zoo)
