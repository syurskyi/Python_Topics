RESERVED_WORDS = vars(object).keys()


class JsObject:
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """

    ___ __init__(self, **kwargs
        self._local = dict()
        ___ k, v in kwargs.items(
            self.__setitem__(k, v)

    ___ __getattr__(self, item
        __ item in self.keys(
            r_ self.__getitem__(item)

    ___ __setattr__(self, key, value
        super().__setattr__(key, value)
        __ key not in RESERVED_WORDS and key != '_local':
            self._local[key] = value

    ___ __getitem__(self, item
        r_ self._local.get(item)

    ___ __setitem__(self, key, value
        __ key not in RESERVED_WORDS:
            self._local[key] = value
            self.__dict__[key] = value
        ____
            raise AttributeError("Reserved words not allowed")

    ___ __delitem__(self, key
        self._local.pop(key)
        self.__dict__.pop(key)

    ___ __delattr__(self, item
        self._local.pop(item)
        self.__dict__.pop(item)

    ___ __len__(self
        r_ le.(self._local)

    ___ __iter__(self
        yield from self._local

    ___ __eq__(self, other
        r_ self._local __ other._local

    ___ keys(self
        r_ self._local.keys()

    ___ values(self
        r_ self._local.values()

    ___ update(self, data
        ___ k, v in data.items(
            self.__setitem__(k, v)
