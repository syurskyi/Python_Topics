class FirstClass:               # Define a class object
    def setdata(self, value):   # Define class methods
        self.data = value       # self is the instance

    def display(self):
        print(self.data)        # self.data: per instance


x = FirstClass()
x.data = "New value"


class SecondClass(FirstClass):                   # Inherits setdata
    def display(self):                           # Changes display
        print('Current value = "%s"' % self.data)


z = SecondClass()
z.setdata(42)           # Finds setdata in FirstClass
print('#' * 52 + ' Finds overridden method in SecondClass')
z.display()             # Finds overridden method in SecondClass

print('#' * 52 + '  x is still a FirstClass instance (old message)')
x.display()             # x is still a FirstClass instance (old message)
