c_ CustomSet(o..):
    ___ - , elements=[]):
        elements = l..(elements)

    ___ isempty
        r.. n.. elements

    ___ __iter__
        r.. i..(elements)

    ___ __contains__  element):
        r.. element __ elements

    ___ issubset  other):
        r.. a..(x __ other ___ x __ self)

    ___ isdisjoint  other):
        r.. a..(x n.. __ other ___ x __ self)

    ___ __eq__  other):
        r.. issubset(other) a.. other.issubset(self)

    ___ add  element):
        __ element n.. __ self:
            elements.a..(element)

    ___ intersection  other):
        result = CustomSet()
        ___ x __ self:
            __ x __ other:
                result.add(x)
        r.. result

    ___ __sub__  other):
        result = CustomSet()
        ___ x __ self:
            __ x n.. __ other:
                result.add(x)
        r.. result

    ___ __add__  other):
        result = CustomSet(elements)
        ___ x __ other:
            result.add(x)
        r.. result
