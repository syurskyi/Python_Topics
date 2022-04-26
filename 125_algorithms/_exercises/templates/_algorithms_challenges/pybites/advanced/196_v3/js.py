RESERVED_WORDS vars(o..).k..


c_ JsObject:
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """

    ___ - ,  $$
        _local d..()
        ___ k, v __ kwargs.i..
            -s(k, v)

    ___ __getattr__  item
        __ item __ k..:
            r.. -g(item)

    ___ __setattr__  key, value
        ____.__setattr__(key, value)
        __ key n.. __ RESERVED_WORDS a.. key !_ '_local':
            _local[key] value

    ___ -g  item
        r.. _local.g.. item)

    ___ -s  key, value
        __ key n.. __ RESERVED_WORDS:
            _local[key] value
            __dict__[key] value
        ____
            r.. AttributeError("Reserved words not allowed")

    ___ __delitem__  key
        _local.p.. key)
        __dict__.p.. key)

    ___ __delattr__  item
        _local.p.. item)
        __dict__.p.. item)

    ___ -l
        r.. l..(_local)

    ___ -i
        y.. ____ _local

    ___ -e  other
        r.. _local __ other._local

    ___ keys
        r.. _local.k..

    ___ values
        r.. _local.v..

    ___ update  data
        ___ k, v __ data.i..
            -s(k, v)
