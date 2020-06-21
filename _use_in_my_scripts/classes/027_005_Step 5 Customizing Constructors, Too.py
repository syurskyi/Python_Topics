# Add customization of constructor in a subclass


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
    def __init__(self, name, pay):  # Redefine constructor
        Person.__init__(self, name, 'mgr', pay)  # Run original with 'mgr'

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print('#' * 22)
    print('#' * 23 + ' Add customization of constructor in a subclass')
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)  # Job name not needed:
    tom.giveRaise(.10)  # Implied/set by class
    print(tom.lastName())
    print(tom)


# Embedding-based Manager alternative

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


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)  # Embed a Person object

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)  # Intercept and delegate

    def __getattr__(self, attr):
        return getattr(self.person, attr)  # Delegate all other attrs

    def __str__(self):
        return str(self.person)  # Must overload again (in 3.0)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print('#' * 22)
    print('#' * 23 + ' Embedding-based Manager alternative')
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', pay=100000)  # Job name not needed:
    tom.giveRaise(.10)  # Implied/set by class
    print(tom.lastName())
    print(tom)
# Aggregate embedded objects into a composite


bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


development = Department(bob, sue)  # Embed objects in a composite
development.addMember(tom)
development.giveRaises(.10)  # Runs embedded objects' giveRaise
development.showAll()  # Runs embedded objects' __str__s

