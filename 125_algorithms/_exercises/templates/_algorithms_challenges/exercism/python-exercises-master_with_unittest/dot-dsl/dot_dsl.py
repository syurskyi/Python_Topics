NODE, EDGE, ATTR r..(3)


c_ Node(o..
    ___ - , name, attrs={}
        ? ?
        attrs attrs

    ___ -e  other
        r.. name __ other.name a.. attrs __ other.attrs


c_ Edge(o..
    ___ - , src, dst, attrs={}
        src src
        dst dst
        attrs attrs

    ___ -e  other
        r.. (src __ other.src a..
                dst __ other.dst a..
                attrs __ other.attrs)


c_ Graph(o..
    ___ - , data=[]
        p..
