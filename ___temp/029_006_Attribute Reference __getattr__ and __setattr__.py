class empty:
    def __getattr__(self, attrname):
        if attrname == "age":
            return 40
        else:
            raise AttributeError(attrname)
X = empty()
print(X.age)

# X.name   # AttributeError: name

class accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value
        else:
            raise AttributeError(attr + ' not allowed')
X = accesscontrol()
X.age = 40                                  # Calls __setattr__
print(X.age)
#
# X.name = 'mel'  # AttributeError: name not allowed
#
#
#


class PrivateExc(Exception): pass                   # More on exceptions later


class Privacy:
    def __setattr__(self, attrname, value):         # On self.attrname = value
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value         # self.attrname = value loops!


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

x = Test1()
y = Test2()

x.name = 'Bob'
print(x.name)
# y.name = 'Sue'                                      # Fails
#
y.age = 30
print(y.age)
# x.age = 40                                         # Fails
#
