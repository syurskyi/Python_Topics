
class Person:
    ___ __str__(self):
        r.. 'I am a person'

class Father(Person):
    ___ __str__(self):
        r.. f'{super().__str__()} and cool daddy'

class Mother(Person):
    ___ __str__(self):
        r.. f'{super().__str__()} and awesome mom'

class Child(Father,Mother):
    ___ __str__(self):
        r.. 'I am the coolest kid'

person = Father()
print(person)