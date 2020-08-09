from itertools ______ chain

class CustomSet(object
    ___ __init__(self, elements=[]
        self._store = dict()
        for e in elements:
            self.add(e)

    ___ isempty(self
        r_ le.(self._store) <= 0

    ___ __contains__(self, element
        r_ element in self._store

    ___ issubset(self, other
        r_ all(e in other for e in self._store.values())

    ___ isdisjoint(self, other
        r_ not any(e in other for e in self._store.values())

    ___ __eq__(self, other
        r_ self.issubset(other) and other.issubset(self)

    ___ add(self, element
        self._store[element] = element

    ___ intersection(self, other
        intersection = CustomSet()
        for e in self._store.values(
            __ e in other:
                intersection.add(e)
        r_ intersection

    ___ __sub__(self, other
        difference = CustomSet() 
        for e in self._store.values(
            __ e not in other:
                difference.add(e)
        r_ difference

    ___ __add__(self, other
        intersection = CustomSet()
        for e in chain(self._store.values(), other._store.values()):
            intersection.add(e)
        r_ intersection
