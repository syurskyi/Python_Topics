class CustomSet(object):
    ___ __init__(self, elements=[]):
        self.elements = l..(elements)

    ___ isempty(self):
        r.. n.. self.elements

    ___ __iter__(self):
        r.. iter(self.elements)

    ___ __contains__(self, element):
        r.. element __ self.elements

    ___ issubset(self, other):
        r.. a..(x __ other ___ x __ self)

    ___ isdisjoint(self, other):
        r.. a..(x n.. __ other ___ x __ self)

    ___ __eq__(self, other):
        r.. self.issubset(other) and other.issubset(self)

    ___ add(self, element):
        __ element n.. __ self:
            self.elements.a..(element)

    ___ intersection(self, other):
        result = CustomSet()
        ___ x __ self:
            __ x __ other:
                result.add(x)
        r.. result

    ___ __sub__(self, other):
        result = CustomSet()
        ___ x __ self:
            __ x n.. __ other:
                result.add(x)
        r.. result

    ___ __add__(self, other):
        result = CustomSet(self.elements)
        ___ x __ other:
            result.add(x)
        r.. result
