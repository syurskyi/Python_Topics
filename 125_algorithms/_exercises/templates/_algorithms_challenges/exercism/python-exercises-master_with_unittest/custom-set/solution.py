c_ CustomSet(o..
    ___ - , elements=   # list
        elements l..(elements)

    ___ isempty
        r.. n.. elements

    ___ -i
        r.. i..(elements)

    ___  -c  element
        r.. element __ elements

    ___ issubset  other
        r.. a..(x __ other ___ x __ self)

    ___ isdisjoint  other
        r.. a..(x n.. __ other ___ x __ self)

    ___ -e  other
        r.. issubset(other) a.. other.issubset ____

    ___ add  element
        __ element n.. __ self:
            elements.a..(element)

    ___ intersection  other
        result CustomSet()
        ___ x __ self:
            __ x __ other:
                result.add(x)
        r.. ?

    ___ -s  other
        result CustomSet()
        ___ x __ self:
            __ x n.. __ other:
                result.add(x)
        r.. ?

    ___ -a  other
        result CustomSet(elements)
        ___ x __ other:
            result.add(x)
        r.. ?
