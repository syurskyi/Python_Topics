# see __mro__ output in Bite description


class Person:

    ___ __str__(self):
        return "I am a person"

class Father(Person):

    ___ __str__(self):
        return super().__str__() + " and cool daddy"



class Mother(Person):

    ___ __str__(self):
        return super().__str__() + " and awesome mom"



class Child(Father,Mother):


    ___ __str__(self):
        return "I am the coolest kid"


