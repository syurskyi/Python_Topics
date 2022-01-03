c_ CustomSet(object):
    ___ - , elements=[]):
        elements = l..(elements)

    ___ isempty
        r.. n.. elements

    ___ __iter__
        r.. iter(elements)

    ___ __contains__(self, element):
        r.. element __ elements

    ___ issubset(self, other):
        r.. a..(x __ other ___ x __ self)

    ___ isdisjoint(self, other):
        r.. a..(x n.. __ other ___ x __ self)

    ___ __eq__(self, other):
        r.. issubset(other) a.. other.issubset(self)

    ___ add(self, element):
        __ element n.. __ self:
            elements.a..(element)

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
        result = CustomSet(elements)
        ___ x __ other:
            result.add(x)
        r.. result
