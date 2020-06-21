# NOTE: this chapter repeatedly modifies the same file, person.py;
# changed lines are highlighted in the text; here, all of this file's
# extensions are colected

# File person.py (start)


class Person:
    pass

# Add record field initialization


class Person:
    def __init__(self, name, job, pay):      # Constructor takes 3 arguments
        self.name = name                     # Fill out fields when created
        self.job = job                      # self is the new instance object
        self.pay = pay


# Add defaults for constructor arguments


class Person:
    def __init__(self, name, job=None, pay=0):         # Normal function args
        self.name = name
        self.job = job
        self.pay = pay


# Add incremental self-test code


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

print('#' * 22 + ' Add incremental self-test code')
print('#' * 22 + ' Test the class')
print('#' * 22 + ' Runs __init__ automatically')
print('#' * 22 + ' Fetch attached attributes')
print('#' * 22 + ' sues and bobs attrs differ')

bob = Person('Bob Smith')                         # Test the class
sue = Person('Sue Jones', job='dev', pay=100000)  # Runs __init__ automatically
print(bob.name, bob.pay)                          # Fetch attached attributes
print(sue.name, sue.pay)                          # sues and bobs attrs differ

# Allow this file to be imported as well as run/tested


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

print('#' * 22 + ' Allow this file to be imported as well as run/tested')
print('#' * 22 + ' When run for testing only')

if __name__ == '__main__':                  # When run for testing only
    # self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)

print('#' * 22 + ' New format method')
print('{0} {1}'.format(bob.name, bob.pay))    # New format method

print('#' * 22 + ' Format expression')
print('%s %s' % (bob.name, bob.pay))          # Format expression
