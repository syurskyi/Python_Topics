# Python code to demonstrate enumerations
# importing enum for enumerations
# Enumerations in Python are implemented by using the module named enum.Enumerations are created using classes.
# Enums have names and values associated with them.
# Properties of enum:
# 1. Enums can be displayed as string or repr.
# 2. Enums can be checked for their types using type().
# 3. name keyword is used to display the name of the enum member.

from __future__ import print_function
import enum

# creating enumerations using class
class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3

# printing enum member as string
print ("The string representation of enum member is : ", end="")
print (Animal.dog)

# printing enum member as repr
print ("The repr representation of enum member is : ", end="")
print (repr(Animal.dog))

# printing the type of enum member using type()
print ("The type of enum member is : ", end ="")
print (type(Animal.dog))

# printing name of enum member using "name" keyword
print ("The name of enum member is : ", end ="")
print (Animal.dog.name)