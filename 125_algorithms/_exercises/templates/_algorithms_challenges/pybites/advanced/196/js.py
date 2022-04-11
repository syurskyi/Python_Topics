c_ JsObject(d..
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """



    ___ - , $$
        super().__init__(kwargs)
    

    ___ __getattr__ key
        r.. self[key]
    

    ___ __setattr__ name,value
        self[name] value


    ___ __delattr__ name
        del self[name]
