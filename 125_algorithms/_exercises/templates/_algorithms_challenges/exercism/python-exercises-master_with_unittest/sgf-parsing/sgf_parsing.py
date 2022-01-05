c_ SgfTree(o..):
    ___ - , properties=N.., children_ N..
        properties = properties o. {}
        children = children o. []

    ___ __eq__  other):
        __ n.. isi..(other, SgfTree):
            r.. F..
        ___ k, v __ properties.i..:
            __ k n.. __ other.properties:
                r.. F..
            __ other.properties[k] != v:
                r.. F..
        ___ k __ other.properties.k..:
            __ k n.. __ properties:
                r.. F..
        __ l..(children) != l..(other.children):
            r.. F..
        ___ a, b __ z..(children, other.children):
            __ a != b:
                r.. F..
        r.. T..


___ p..(input_string):
    p..
