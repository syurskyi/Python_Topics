NODE, EDGE, ATTR = range(3)


class Node(object):
    ___ __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    ___ __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    ___ __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    ___ __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    ___ __init__(self, data=[]):
        pass
