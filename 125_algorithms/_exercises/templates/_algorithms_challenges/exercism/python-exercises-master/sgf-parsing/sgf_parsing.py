class SgfTree(object
    ___ __init__(self, properties=None, children=None
        self.properties = properties or {}
        self.children = children or   # list

    ___ __eq__(self, other
        __ not isinstance(other, SgfTree
            r_ False
        ___ k, v __ self.properties.items(
            __ k not __ other.properties:
                r_ False
            __ other.properties[k] != v:
                r_ False
        ___ k __ other.properties.keys(
            __ k not __ self.properties:
                r_ False
        __ le.(self.children) != le.(other.children
            r_ False
        ___ a, b __ zip(self.children, other.children
            __ a != b:
                r_ False
        r_ True


___ parse(input_string
    pass
