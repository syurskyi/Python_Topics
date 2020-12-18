class FirstClass:               # Define a class object
    def setdata(self, value):   # Define class methods
        self.data = value       # self is the instance

    def display(self):
        print(self.data)        # self.data: per instance


class SecondClass(FirstClass):                   # Inherits setdata
    def display(self):                           # Changes display
        print('Current value = "%s"' % self.data)


class ThirdClass(SecondClass):                     # Inherit from SecondClass
    def __init__(self, value):                     # On "ThirdClass(value)"
        self.data = value

    def __add__(self, other):                      # On "self + other"
        return ThirdClass(self.data + other)

    def __str__(self):                             # On "print(self)", "str()"
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):                          # In-place change: named
        self.data *= other


a = ThirdClass('abc')           # __init__ called
print('#' * 52 + ' Inherited method called')
a.display()                     # Inherited method called

print('#' * 52 + ' __str__: returns display string')
print(a)                        # __str__: returns display string

print('#' * 52 + ' __add__: makes a new instance')
print('#' * 52 + ' b has all ThirdClass methods')
b = a + 'xyz'                   # __add__: makes a new instance
b.display()                     # b has all ThirdClass methods
print('#' * 52 + ' __str__: returns display string')
print(b)                        # __str__: returns display string

print('#' * 52 + ' mul: changes instance in-place')
a.mul(3)                        # mul: changes instance in-place
print(a)

