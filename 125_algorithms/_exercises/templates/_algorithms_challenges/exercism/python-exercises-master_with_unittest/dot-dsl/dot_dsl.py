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
        pass
