class Name:                             # Use (object) in 2.6
    "name descriptor docs"
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name
    def __set__(self, instance, value):
        print('change...')
        instance._name = value
    def __delete__(self, instance):
        print('remove...')
        del instance._name

class Person:                           # Use (object) in 2.6
    def __init__(self, name):
        self._name = name
    name = Name()                       # Assign descriptor to attr

bob = Person('Bob Smith')               # bob has a managed attribute
print(bob.name)                         # Runs Name.__get__
bob.name = 'Robert Smith'               # Runs Name.__set__
print(bob.name)
del bob.name                            # Runs Name.__delete__

print('-'*20)
sue = Person('Sue Jones')               # sue inherits descriptor too
print(sue.name)
print(Name.__doc__)                     # Or help(Name)

class Super:
    def __init__(self, name):
        self._name = name
    name = Name()

class Person(Super):                            # Descriptors are inherited
   pass


class Person:
    def __init__(self, name):
        self._name = name

    class Name:                                 # Using a nested class
        "name descriptor docs"
        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name
        def __set__(self, instance, value):
            print('change...')
            instance._name = value
        def __delete__(self, instance):
            print('remove...')
            del instance._name
    name = Name()


print(Person.Name.__doc__)     # Differs: not Name.__doc__ outside class

