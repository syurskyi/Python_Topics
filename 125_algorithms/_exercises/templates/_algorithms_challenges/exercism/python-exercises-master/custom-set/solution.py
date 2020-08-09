class CustomSet(object
    ___ __init__(self, elements=[]
        self.elements = list(elements)

    ___ isempty(self
        r_ not self.elements

    ___ __iter__(self
        r_ iter(self.elements)

    ___ __contains__(self, element
        r_ element in self.elements

    ___ issubset(self, other
        r_ all(x in other for x in self)

    ___ isdisjoint(self, other
        r_ all(x not in other for x in self)

    ___ __eq__(self, other
        r_ self.issubset(other) and other.issubset(self)

    ___ add(self, element
        __ element not in self:
            self.elements.append(element)

    ___ intersection(self, other
        result = CustomSet()
        for x in self:
            __ x in other:
                result.add(x)
        r_ result

    ___ __sub__(self, other
        result = CustomSet()
        for x in self:
            __ x not in other:
                result.add(x)
        r_ result

    ___ __add__(self, other
        result = CustomSet(self.elements)
        for x in other:
            result.add(x)
        r_ result
