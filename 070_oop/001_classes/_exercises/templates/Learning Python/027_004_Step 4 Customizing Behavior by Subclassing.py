class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):                                         # Added method
        return '[Person: %s, %s]' % (self.name, self.pay)      # String to print


class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        self.pay = int(self.pay * (1 + percent + bonus))  # Bad: cut-and-paste


class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)  # Good: augment original


# Add customization of one behavior in a subclass

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def giveRaise(self, percent, bonus=.10):  # Redefine at this level
        Person.giveRaise(self, percent + bonus)  # Call Person's version


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    print('#' * 52 + ' Make a Manager: __init__')
    tom = Manager('Tom Jones', 'mgr', 50000)  # Make a Manager: __init__
    tom.giveRaise(.10)  # Runs custom version
    print('#' * 52 + ' Runs inherited method')
    print(tom.lastName())  # Runs inherited method
    print('#' * 52 + ' Runs inherited __str__')
    print(tom)  # Runs inherited __str__

print('#' * 22)
print('#' * 22)
print('#' * 22)
print('#' * 23 + ' Process objects generically')
print('#' * 23 + ' Run this objects giveRaise')
print('#' * 23 + ' Run the common __str__')
if __name__ == '__main__':
    print('--All three--')
    for object in (bob, sue, tom):  # Process objects generically
        object.giveRaise(.10)  # Run this objects giveRaise
        print(object)  # Run the common __str__

'''
class Person:
    def lastName(self):
        pass

    def giveRaise(self):
        pass

    def __str__(self): pass


class Manager(Person):  # Inherit
    def giveRaise(self, ...): pass  # Customize

    def someThingElse(self, ...): pass  # Extend
'''
"""
tom = Manager()
tom.lastName()  # Inherited verbatim
tom.giveRaise()  # Customized version
tom.someThingElse()  # Extension here
print(tom)  # Inherited overload method
"""
