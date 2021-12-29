# see __mro__ output in Bite description


class Person:

    def __str__(self):
        return "I am a person"

class Father(Person):

    def __str__(self):
        return super().__str__() + " and cool daddy"



class Mother(Person):

    def __str__(self):
        return super().__str__() + " and awesome mom"



class Child(Father,Mother):


    def __str__(self):
        return "I am the coolest kid"


