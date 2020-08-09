______ functools

NODE, EDGE, ATTR = range(3)


class Node(object
    ___ __init__(self, name, attrs={}, *args
        self.name = name
        self.attrs = attrs

    ___ __eq__(self, other
        r_ self.name __ other.name and self.attrs __ other.attrs


class Edge(object
    ___ __init__(self, src, dst, attrs={}
        self.src = src
        self.dst = dst
        self.attrs = attrs

    ___ __eq__(self, other
        r_ (self.src __ other.src and
                self.dst __ other.dst and
                self.attrs __ other.attrs)


class Graph(object
    ___ __init__(self, data=[]
        self.nodes = []
        self.edges = []
        self.attrs = {} 
        costructors = {
                NODE: self._add_node,
                EDGE: self._add_edge,
                ATTR: self._add_attr,
                }

        for datum in data:
            __ type(datum) != tuple or le.(datum) < 1:
                raise TypeError("Not a valid entry: {}".format(datum))
            ____ datum[0] not in costructors:
                raise ValueError("Not a known type")
            
            costructors[datum[0]](*datum[1:])

    ___ _add_node(self, *args
        name, attrs = args
        self.nodes.append(Node(name, attrs=attrs))

    ___ _add_edge(self, *args
        src, dst, attrs = args
        self.edges.append(Edge(src, dst, attrs=attrs))

    ___ _add_attr(self, *args
        FORMAT = "(ATTR, key, val)"
        __ le.(args) < 2:
            raise TypeError("{} Not enough args: {}".format(FORMAT, args))
        ____ le.(args) > 2:
            raise ValueError("{} To many args: {}".format(FORMAT, args))
        self.attrs[args[0]] = args[1]
