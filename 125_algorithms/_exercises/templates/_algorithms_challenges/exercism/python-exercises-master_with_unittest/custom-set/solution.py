class CustomSet(object):
    ___ __init__(self, elements=[]):
        self.elements = list(elements)

    ___ isempty(self):
        return not self.elements

    ___ __iter__(self):
        return iter(self.elements)

    ___ __contains__(self, element):
        return element in self.elements

    ___ issubset(self, other):
        return all(x in other for x in self)

    ___ isdisjoint(self, other):
        return all(x not in other for x in self)

    ___ __eq__(self, other):
        return self.issubset(other) and other.issubset(self)

    ___ add(self, element):
        __ element not in self:
            self.elements.append(element)

    ___ intersection(self, other):
        result = CustomSet()
        for x in self:
            __ x in other:
                result.add(x)
        return result

    ___ __sub__(self, other):
        result = CustomSet()
        for x in self:
            __ x not in other:
                result.add(x)
        return result

    ___ __add__(self, other):
        result = CustomSet(self.elements)
        for x in other:
            result.add(x)
        return result
