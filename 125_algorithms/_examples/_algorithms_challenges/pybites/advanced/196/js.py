class JsObject(dict):
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """



    def __init__(self,**kwargs):
        super().__init__(kwargs)
    

    def __getattr__(self,key):
        return self[key]
    

    def __setattr__(self,name,value):
        self[name] = value


    def __delattr__(self,name):
        del self[name]
