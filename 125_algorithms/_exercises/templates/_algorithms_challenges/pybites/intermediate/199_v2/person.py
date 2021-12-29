# see __mro__ output in Bite description


class Person:

    ___ __str__(self):
        r.. "I am a person"

class Father(Person):

    ___ __str__(self):
        r.. super().__str__() + " and cool daddy"



class Mother(Person):

    ___ __str__(self):
        r.. super().__str__() + " and awesome mom"



class Child(Father,Mother):


    ___ __str__(self):
        r.. "I am the coolest kid"


