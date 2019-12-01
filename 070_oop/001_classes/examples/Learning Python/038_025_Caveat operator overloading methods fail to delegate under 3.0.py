# C:\misc> c:\python26\python
from access import Private
@Private('age')
class Person:
    def __init__(self):
        self.age = 42
    def __str__(self):
        return 'Person: ' + str(self.age)
    def __add__(self, yrs):
         self.age += yrs

X = Person()
X.age                                   # Name validations fail correctly
# TypeError: private attribute fetch: age
print(X)                                # __getattr__ => runs Person.__str__
# Person: 42
X + 10                                  # __getattr__ => runs Person.__add__
print(X)                                # __getattr__ => runs Person.__str__
# Person: 52

# C:\misc> c:\python30\python
from access import Private
@Private('age')
class Person:
    def __init__(self):
        self.age = 42
    def __str__(self):
        return 'Person: ' + str(self.age)
    def __add__(self, yrs):
        self.age += yrs

X = Person()                            # Name validations still work
X.age                                   # But 3.0 fails to delegate built-ins!
# TypeError: private attribute fetch: age
print(X)
# <access.onInstance object at 0x025E0790>
X + 10
# TypeError: unsupported operand type(s) for +: 'onInstance' and 'int'
print(X)
# <access.onInstance object at 0x025E0790>

