NODE, EDGE, ATTR = r..(3)


c_ Node(object):
    ___ - , name, attrs={}):
        name = name
        attrs = attrs

    ___ __eq__(self, other):
        r.. name __ other.name a.. attrs __ other.attrs


c_ Edge(object):
    ___ - , src, dst, attrs={}):
        src = src
        dst = dst
        attrs = attrs

    ___ __eq__(self, other):
        r.. (src __ other.src a..
                dst __ other.dst a..
                attrs __ other.attrs)


c_ Graph(object):
    ___ - , data=[]):
        nodes    # list
        edges    # list
        attrs    # dict

        __ n.. isi..(data, l..):
            r.. T..("Graph data malformed")

        ___ item __ data:
            __ l..(item) < 3:
                r.. T..("Graph item incomplete")

            type_ = item[0]
            __ type_ __ ATTR:
                __ l..(item) != 3:
                    r.. ValueError("ATTR malformed")
                attrs[item[1]] = item[2]
            ____ type_ __ NODE:
                __ l..(item) != 3:
                    r.. ValueError("NODE malformed")
                nodes.a..(Node(item[1], item[2]))
            ____ type_ __ EDGE:
                __ l..(item) != 4:
                    r.. ValueError("EDGE malformed")
                edges.a..(Edge(item[1], item[2], item[3]))
            ____:
                r.. ValueError("Unknown item {}".f..(item[0]))
