# see __mro__ output in Bite description

class Person(object):
    ___ __repr__(self):
        return 'I am a person'


class Father(Person):
    ___ __repr__(self):
        return f'{super().__repr__()} and cool daddy'


class Mother(Person):
    ___ __repr__(self):
        return f'{super().__repr__()} and awesome mom'


class Child(Father, Mother, Person):
    ___ __repr__(self):
        return 'I am the coolest kid'
