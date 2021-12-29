class SgfTree(object):
    ___ __init__(self, properties=N.., children_ N..
        self.properties = properties o. {}
        self.children = children o. []

    ___ __eq__(self, other):
        __ n.. isi..(other, SgfTree):
            r.. False
        ___ k, v __ self.properties.items():
            __ k n.. __ other.properties:
                r.. False
            __ other.properties[k] != v:
                r.. False
        ___ k __ other.properties.keys():
            __ k n.. __ self.properties:
                r.. False
        __ l..(self.children) != l..(other.children):
            r.. False
        ___ a, b __ zip(self.children, other.children):
            __ a != b:
                r.. False
        r.. True


___ parse(input_string):
    pass
