print('#' * 22 + ' Simple string outside class')
name = 'Bob Smith'             # Simple string, outside class
print(name.split())            # Extract last name

print(name.split()[-1])        # Or [1], if always just two parts

pay = 100000            # Simple variable, outside class
pay *= 1.10             # Give a 10% raise
print(pay)              # Or: pay = pay * 1.10, if you like to type
                        # Or: pay = pay + (pay * .10), if you _really_ do!


# Process embedded built-in types: strings, mutability

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print('#' * 22 + ' Extract objects last name')
    print(bob.name.split()[-1])            # Extract object's last name
    print('#' * 22 + ' Give this object a raise')
    sue.pay *= 1.10                        # Give this object a raise
    print(sue.pay)

# Add methods to encapsulate operations for maintainability
print('#' * 22)
print('#' * 22 + ' Add methods to encapsulate operations for maintainability')
print('#' * 22)


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):                               # Behavior methods
        return self.name.split()[-1]                  # self is implied subject

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))      # Must change here only

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print('#' * 22 + ' Use the new methods')
    print(bob.lastName(), sue.lastName())             # Use the new methods
    print('#' * 22 + ' instead of hardcoding')
    sue.giveRaise(.10)                                # instead of hardcoding
    print(sue.pay)

