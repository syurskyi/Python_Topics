instances = {}


def getInstance(aClass, *args):                 # Manage global table
    if aClass not in instances:                 # Add **kargs for keywords
        instances[aClass] = aClass(*args)       # One dict entry per class
    return instances[aClass]


def singleton(aClass):                          # On @ decoration
    def onCall(*args):                          # On instance creation
        return getInstance(aClass, *args)
    return onCall


@singleton                                      # Person = singleton(Person)
class Person:                                   # Rebinds Person to onCall
     def __init__(self, name, hours, rate):     # onCall remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate
     def pay(self):
        return self.hours * self.rate


@singleton                                      # Spam = singleton(Spam)
class Spam:                                     # Rebinds Spam to onCall
    def __init__(self, val):                    # onCall remembers Spam
        self.attr = val


bob = Person('Bob', 40, 10)                     # Really calls onCall
print(bob.name, bob.pay())

sue = Person('Sue', 50, 20)                     # Same, single object
print(sue.name, sue.pay())

X = Spam(42)                                    # One Person, one Spam
Y = Spam(99)
print(X.attr, Y.attr)


def singleton(aClass):                          # On @ decoration
    instance = None

    def onCall(*args):                          # On instance creation
        nonlocal instance                       # 3.0 and later nonlocal
        if instance == None:
            instance = aClass(*args)            # One scope per class
        return instance
    return onCall


class singleton:
    def __init__(self, aClass):                 # On @ decoration
        self.aClass = aClass
        self.instance = None

    def __call__(self, *args):                  # On instance creation
        if self.instance == None:
            self.instance = self.aClass(*args)  # One instance per class
        return self.instance

