
c_ Person:
    ___ __str__
        r.. 'I am a person'

c_ Father(Person):
    ___ __str__
        r.. f'{super().__str__()} and cool daddy'

c_ Mother(Person):
    ___ __str__
        r.. f'{super().__str__()} and awesome mom'

c_ Child(Father,Mother):
    ___ __str__
        r.. 'I am the coolest kid'

person = Father()
print(person)