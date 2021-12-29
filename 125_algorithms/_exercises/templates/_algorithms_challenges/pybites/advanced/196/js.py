class JsObject(d..):
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """



    ___ __init__(self,**kwargs):
        super().__init__(kwargs)
    

    ___ __getattr__(self,key):
        r.. self[key]
    

    ___ __setattr__(self,name,value):
        self[name] = value


    ___ __delattr__(self,name):
        del self[name]
