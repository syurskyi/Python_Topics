# from person_composite import Person
from person_department import Person
bob = Person('Bob Smith')

# print('#' * 22)
print('#' * 23 + ' Show bob __str__')
print(bob)  # Show bob's __str__

print('#' * 23 + ' Show bobs class and its name')
print(bob.__class__)  # Show bob's class and its name
print(bob.__class__.__name__)

print('#' * 23 + ' Attributes are really dict keys')
print('#' * 23 + ' Use list() to force list in 3.0')
print(list(bob.__dict__.keys()))  # Attributes are really dict keys
# ['pay', 'job', 'name']     # Use list() to force list in 3.0

print('#' * 23 + ' Index manually')
for key in bob.__dict__:
    print(key, '=>', bob.__dict__[key])  # Index manually

print('#' * 23 + ' obj.attr, but attr is a var')
for key in bob.__dict__:
    print(key, '=>', getattr(bob, key))  # obj.attr, but attr is a var

# ## File: classtools.py (new)

"Assorted class utilities and tools"


class AttrDisplay:
    """
    Provides an inheritable print overload method that displays
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())


if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2


    class SubTest(TopTest):
        pass


    X, Y = TopTest(), SubTest()
    print('#' * 22)
    print('#' * 22)
    print('#' * 23 + ' Show all instance attrs')
    print(X)  # Show all instance attrs
    print('#' * 23 + ' Show lowest class name')
    print(Y)  # Show lowest class name



# from person import Person
# from person_composite import Person
from person_department import Person
bob = Person('Bob Smith')

# In Python 2.6:
print('#' * 23 + ' Instance attrs only')
print(bob.__dict__.keys())  # Instance attrs only

print('#' * 23 + ' inherited attrs in classes')
print(dir(bob))  # + inherited attrs in classes

# In Python 3.0:
print('#' * 23 + ' 3.0 keys() is a view, not a list')
print(list(bob.__dict__.keys()))  # 3.0 keys() is a view, not a list

print('#' * 23 + ' 3.0 includes class type methods')
print(dir(bob))  # 3.0 includes class type methods


class TopTest(AttrDisplay):

    def gatherAttrs(self):  # Replaces method in AttrDisplay!
        return 'Spam'


# File person.py (final)

from classtools import AttrDisplay  # Use generic display tool


class Person(AttrDisplay):
    """
    Create and process person records
    """

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):  # Assumes last is last
        return self.name.split()[-1]

    def giveRaise(self, percent):  # Percent must be 0..1
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    """
    A customized Person with special requirements
    """

    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print('#' * 102)
    print('#' * 23 + ' 3.0 includes class type methods # File person.py (final)')
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
