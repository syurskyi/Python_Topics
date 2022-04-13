
c_ Person:
    ___ -s
        r.. 'I am a person'

c_ Father(Person
    ___ -s
        r.. _* super().-s()} and cool daddy'

c_ Mother(Person
    ___ -s
        r.. _* super().-s()} and awesome mom'

c_ Child(Father,Mother
    ___ -s
        r.. 'I am the coolest kid'

person Father()
print(person)