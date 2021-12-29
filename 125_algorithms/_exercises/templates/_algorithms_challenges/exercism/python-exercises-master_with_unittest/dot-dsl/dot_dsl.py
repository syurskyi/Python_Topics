NODE, EDGE, ATTR = r..(3)


class Node(object):
    ___ __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    ___ __eq__(self, other):
        r.. self.name __ other.name a.. self.attrs __ other.attrs


class Edge(object):
    ___ __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    ___ __eq__(self, other):
        r.. (self.src __ other.src a..
                self.dst __ other.dst a..
                self.attrs __ other.attrs)


class Graph(object):
    ___ __init__(self, data=[]):
        pass
