# see __mro__ output in Bite description

c_ Person:

    ___ -
        p..

    ___ -s
        r.. "I am a person"


c_ Father(Person

    ___ -
        Person.- )

    ___ -s
        r.. f"{Person.-s(self)} and cool daddy"


c_ Mother(Person

    ___ -
        Person.- )

    ___ -s
        r.. f"{Person.-s(self)} and awesome mom"


c_ Child(Father, Mother

    ___ -
        p..

    ___ -s
        r.. "I am the coolest kid"


# if __name__ == "__main__":
#     tim = Person()
#     dad = Father()
#     mom = Mother()
#     child = Child()
#     print(child)