# Accessing Modes : Enum members can be accessed by two ways
# 1. By value :- In this method, the value of enum member is passed.
# 2. By name :- In this method, the name of enum member is passed.
# Seperate value or name can also be accessed using name or value keyword.
# Comparison : Enumerations supports two types of comparisons
# 1. Identity :- These are checked using keywords is and is not.
# 2. Equality :- Equality comparisons of == and != types are also supported.


# Python code to demonstrate enumerations
# Access and comparison

# importing enum for enumerations
from __future__ import print_function
import enum


# creating enumerations using class
class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3


# Accessing enum member using value
print ("The enum member associated with value 2 is : ", end="")
print (Animal(2))

# Accessing enum member using name
print ("The enum member associated with name lion is : ", end="")
print (Animal['lion'])

# Assigning enum member
mem = Animal.dog

# Displaying value
print ("The value associated with dog is : ", end="")
print (mem.value)

# Displaying name
print ("The name associated with dog is : ", end="")
print (mem.name)

# Comparison using "is"
if Animal.dog is Animal.cat:
    print ("Dog and cat are same animals")
else:
    print ("Dog and cat are different animals")

# Comparison using "!="
if Animal.lion != Animal.cat:
    print ("Lions and cat are different")
else:
    print ("Lions and cat are same")