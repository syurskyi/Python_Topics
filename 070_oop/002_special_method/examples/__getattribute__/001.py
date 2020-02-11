class Foo(object):

    def __getattribute__(self, name):
        print "getting attribute %s" % name
        return object.__getattribute__(self, name)

    def __setattr__(self, name, val):
        print "setting attribute %s to %r" % (name, val)
        return object.__setattr__(self, name, val)



foo = Foo()
foo.var = 100
# setting attribute var to 100
foo.name = 'stuart'
# setting attribute name to 'stuart'
bar = foo.var
# getting attribute var
foo.var = foo.name
# getting attribute name
# setting attribute var to 'stuart'
