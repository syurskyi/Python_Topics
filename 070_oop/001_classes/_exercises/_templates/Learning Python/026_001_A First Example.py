class FirstClass:               # Define a class object
    def setdata(self, value):   # Define class methods
        self.data = value       # self is the instance

    def display(self):
        print(self.data)        # self.data: per instance


x = FirstClass()                # Make two instances
y = FirstClass()                # Each is a new namespace

x.setdata("King Arthur")        # Call methods: self is x
y.setdata(3.14159)              # Runs: FirstClass.setdata(y, 3.14159)

print('#' * 52 + ' self.data differs in each instance')
x.display()                   # self.data differs in each instance
y.display()

print('#' * 52 + ' Can get/set attributes')
print('#' * 52 + ' Outside the class too')
x.data = "New value"            # Can get/set attributes
x.display()                    # Outside the class too

x.anothername = "spam"          # Can set new attributes here too!

