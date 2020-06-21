class SharedData:
    spam = 42          # Generates a class data attribute

x = SharedData()       # Make two instances
y = SharedData()
print('#' * 23 + ' They inherit and share spam')
print(x.spam, y.spam)         # They inherit and share 'spam'

SharedData.spam = 99
print(x.spam, y.spam, SharedData.spam)

x.spam = 88
print(x.spam, y.spam, SharedData.spam)


class MixedNames:                            # Define class
    data = 'spam'                            # Assign class attr

    def __init__(self, value):               # Assign method name
        self.data = value                    # Assign instance attr

    def display(self):
        # print('#' * 23 + '  Instance attr, class attr')
        print(self.data, MixedNames.data)    # Instance attr, class attr

x = MixedNames(1)          # Make two instance objects
y = MixedNames(2)          # Each has its own data
print('#' * 23 + '  self.data differs, MixedNames.data is the same')
x.display(); y.display()   # self.data differs, MixedNames.data is the same


