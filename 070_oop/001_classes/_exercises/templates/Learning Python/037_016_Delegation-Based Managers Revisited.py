# NOTE: this is person.py, despite the getattr.py filename in
# its first command line (a minor typo in the first printing)


### file: person.py

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
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)  # Manager.__init__
    print(tom.lastName())  # Manager.__getattr__ -> Person.lastName
    tom.giveRaise(.10)  # Manager.giveRaise -> Person.giveRaise
    print(tom)  # Manager.__str__ -> Person.__str__


# Delete the Manager __str__ method

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)  # Embed a Person object

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)  # Intercept and delegate

    def __getattr__(self, attr):
        return getattr(self.person, attr)  # Delegate all other attrs


# Replace __getattr_ with __getattribute__

class Manager:                                           # Use (object) in 2.6
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)           # Embed a Person object

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)           # Intercept and delegate

    def __getattribute__(self, attr):
        print('**', attr)
        if attr in ['person', 'giveRaise']:
            return object.__getattribute__(self, attr)   # Fetch my attrs
        else:
            return getattr(self.person, attr)            # Delegate all others


# Code __getattribute__ differently to minimize extra calls

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def __getattribute__(self, attr):
        print('**', attr)
        person = object.__getattribute__(self, 'person')
        if attr == 'giveRaise':
            return lambda percent: person.giveRaise(percent+.10)
        else:
            return getattr(person, attr)

    def __str__(self):
        person = object.__getattribute__(self, 'person')
        return str(person)
