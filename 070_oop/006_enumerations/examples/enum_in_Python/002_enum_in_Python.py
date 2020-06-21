# Python code to demonstrate enumerations
# iterations and hashing
# importing enum for enumerations
# 4. Enumerations are iterable. They can be iterated using loops
# 5. Enumerations support hashing. Enums can be used in dictionaries or sets.



import enum

# creating enumerations using class
class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3


# printing all enum members using loop
print ("All the enum values are : ")
for Anim in (Animal):
    print(Anim)

# Hashing enum member as dictionary
di = {}
di[Animal.dog] = 'bark'
di[Animal.lion] = 'roar'

# checking if enum values are hashed successfully
if di == {Animal.dog: 'bark', Animal.lion: 'roar'}:
    print ("Enum is hashed")
else:
    print ("Enum is not hashed")