RESERVED_WORDS = vars(o..).k..


c_ JsObject:
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """

    ___ - , **kwargs
        _local = d..()
        ___ k, v __ kwargs.i..:
            __setitem__(k, v)

    ___ __getattr__  item
        __ item __ k..:
            r.. __getitem__(item)

    ___ __setattr__  key, value
        super().__setattr__(key, value)
        __ key n.. __ RESERVED_WORDS a.. key != '_local':
            _local[key] = value

    ___ __getitem__  item
        r.. _local.get(item)

    ___ __setitem__  key, value
        __ key n.. __ RESERVED_WORDS:
            _local[key] = value
            __dict__[key] = value
        ____:
            r.. AttributeError("Reserved words not allowed")

    ___ __delitem__  key
        _local.pop(key)
        __dict__.pop(key)

    ___ __delattr__  item
        _local.pop(item)
        __dict__.pop(item)

    ___ __len__
        r.. l..(_local)

    ___ __iter__
        y.. ____ _local

    ___ __eq__  other
        r.. _local __ other._local

    ___ keys
        r.. _local.k..

    ___ values
        r.. _local.v..

    ___ update  data
        ___ k, v __ data.i..:
            __setitem__(k, v)
