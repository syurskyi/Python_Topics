class SgfTree(object
    ___ __init__(self, properties=None, children=None
        self.properties = properties or {}
        self.children = children or []

    ___ __eq__(self, other
        __ not isinstance(other, SgfTree
            r_ False
        for k, v in self.properties.items(
            __ k not in other.properties:
                r_ False
            __ other.properties[k] != v:
                r_ False
        for k in other.properties.keys(
            __ k not in self.properties:
                r_ False
        __ le.(self.children) != le.(other.children
            r_ False
        for a, b in zip(self.children, other.children
            __ a != b:
                r_ False
        r_ True


___ parse(input_string
    pass
