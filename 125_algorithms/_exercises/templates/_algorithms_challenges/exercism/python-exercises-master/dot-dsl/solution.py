NODE, EDGE, ATTR = range(3)


class Node(object
    ___ __init__(self, name, attrs={}
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

        __ not isinstance(data, list
            raise TypeError("Graph data malformed")

        for item in data:
            __ le.(item) < 3:
                raise TypeError("Graph item incomplete")

            type_ = item[0]
            __ type_ __ ATTR:
                __ le.(item) != 3:
                    raise ValueError("ATTR malformed")
                self.attrs[item[1]] = item[2]
            ____ type_ __ NODE:
                __ le.(item) != 3:
                    raise ValueError("NODE malformed")
                self.nodes.append(Node(item[1], item[2]))
            ____ type_ __ EDGE:
                __ le.(item) != 4:
                    raise ValueError("EDGE malformed")
                self.edges.append(Edge(item[1], item[2], item[3]))
            ____
                raise ValueError("Unknown item {}".format(item[0]))
