NODE, EDGE, ATTR = r..(3)


class Node(object):
    ___ __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    ___ __eq__(self, other):
        r.. self.name __ other.name and self.attrs __ other.attrs


class Edge(object):
    ___ __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    ___ __eq__(self, other):
        r.. (self.src __ other.src and
                self.dst __ other.dst and
                self.attrs __ other.attrs)


class Graph(object):
    ___ __init__(self, data=[]):
        self.nodes    # list
        self.edges    # list
        self.attrs = {}

        __ n.. isi..(data, l..):
            raise TypeError("Graph data malformed")

        ___ item __ data:
            __ l..(item) < 3:
                raise TypeError("Graph item incomplete")

            type_ = item[0]
            __ type_ __ ATTR:
                __ l..(item) != 3:
                    raise ValueError("ATTR malformed")
                self.attrs[item[1]] = item[2]
            ____ type_ __ NODE:
                __ l..(item) != 3:
                    raise ValueError("NODE malformed")
                self.nodes.a..(Node(item[1], item[2]))
            ____ type_ __ EDGE:
                __ l..(item) != 4:
                    raise ValueError("EDGE malformed")
                self.edges.a..(Edge(item[1], item[2], item[3]))
            ____:
                raise ValueError("Unknown item {}".format(item[0]))
