# Example
# Create a class that will inherit all the methods and properties from another class:

class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()

# Definition and Usage
# The super() function is used to give access to methods and properties of a parent or sibling class.
#
# The super() function returns an object that represents the parent class.

