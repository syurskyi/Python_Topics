class Wrapper:
    def __init__(self, object):
        self.wrapped = object                    # Save object
    def __getattr__(self, attrname):
        print('Trace:', attrname)                # Trace fetch
        return getattr(self.wrapped, attrname)   # Delegate fetch

x = Wrapper([1,2,3])                         # Wrap a list
x.append(4)                                  # Delegate to list method
# Trace: append
x.wrapped                                    # Print my member
# [1, 2, 3, 4]

x = Wrapper({"a": 1, "b": 2})                # Wrap a dictionary
list(x.keys())                               # Delegate to dictionary method
# Trace: keys                                      # Use list() in 3.0
# ['a', 'b']


def Tracer(aClass):                                   # On @decorator
    class Wrapper:
        def __init__(self, *args, **kargs):           # On instance creation
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)     # Use enclosing scope name
        def __getattr__(self, attrname):
            print('Trace: ' + attrname)               # Catches all but own attrs
            self.fetches += 1
            return getattr(self.wrapped, attrname)    # Delegate to wrapped obj
    return Wrapper

@Tracer
class Spam:                                    # Spam = Tracer(Spam)
    def display(self):                         # Spam is rebound to Wrapper
        print('Spam!' * 8)

@Tracer
class Person:                                  # Person = Tracer(Person)
    def __init__(self, name, hours, rate):     # Wrapper remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):                             # Accesses outside class traced
        return self.hours * self.rate          # In-method accesses not traced

food = Spam()                                  # Triggers Wrapper()
food.display()                                 # Triggers __getattr__
print([food.fetches])

bob = Person('Bob', 40, 50)                    # bob is really a Wrapper
print(bob.name)                                # Wrapper embeds a Person
print(bob.pay())

print('')
sue = Person('Sue', rate=100, hours=60)        # sue is a different Wrapper
print(sue.name)                                # with a different Person
print(sue.pay())

print(bob.name)                                # bob has different state
print(bob.pay())
print([bob.fetches, sue.fetches])              # Wrapper attrs not traced


from tracer import Tracer     # Decorator moved to a module file

@Tracer
class MyList(list): pass      # MyList = Tracer(MyList)


x = MyList([1, 2, 3])         # Triggers Wrapper()
x.append(4)                   # Triggers __getattr__, append
# Trace: append
x.wrapped
# [1, 2, 3, 4]

WrapList = Tracer(list)       # Or perform decoration manually
x = WrapList([4, 5, 6])       # Else subclass statement required
x.append(7)
# Trace: append
x.wrapped
# [4, 5, 6, 7]


@Tracer                                          # Decorator approach
class Person: ...
bob = Person('Bob', 40, 50)
sue = Person('Sue', rate=100, hours=60)


class Person: ...                                # Non-decorator approach
bob = Wrapper(Person('Bob', 40, 50))
sue = Wrapper(Person('Sue', rate=100, hours=60))
