# see __mro__ output in Bite description

c_ Person(object):
    ___ __repr__
        r.. 'I am a person'


c_ Father(Person):
    ___ __repr__
        r.. f'{super().__repr__()} and cool daddy'


c_ Mother(Person):
    ___ __repr__
        r.. f'{super().__repr__()} and awesome mom'


c_ Child(Father, Mother, Person):
    ___ __repr__
        r.. 'I am the coolest kid'
