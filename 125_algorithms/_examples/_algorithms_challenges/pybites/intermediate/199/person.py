# see __mro__ output in Bite description

class Person:

    def __init__(self):
        pass

    def __str__(self):
        return "I am a person"


class Father(Person):

    def __init__(self):
        Person.__init__(self)

    def __str__(self):
        return f"{Person.__str__(self)} and cool daddy"


class Mother(Person):

    def __init__(self):
        Person.__init__(self)

    def __str__(self):
        return f"{Person.__str__(self)} and awesome mom"


class Child(Father, Mother):

    def __init__(self):
        pass

    def __str__(self):
        return "I am the coolest kid"


# if __name__ == "__main__":
#     tim = Person()
#     dad = Father()
#     mom = Mother()
#     child = Child()
#     print(child)