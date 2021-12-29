class SgfTree(object):
    ___ __init__(self, properties=None, children_ N..
        self.properties = properties or {}
        self.children = children or []

    ___ __eq__(self, other):
        __ not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            __ k not in other.properties:
                return False
            __ other.properties[k] != v:
                return False
        for k in other.properties.keys():
            __ k not in self.properties:
                return False
        __ len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            __ a != b:
                return False
        return True


___ parse(input_string):
    pass
