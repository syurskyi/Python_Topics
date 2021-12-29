
class Person:
    def __str__(self):
        return 'I am a person'

class Father(Person):
    def __str__(self):
        return f'{super().__str__()} and cool daddy'

class Mother(Person):
    def __str__(self):
        return f'{super().__str__()} and awesome mom'

class Child(Father,Mother):
    def __str__(self):
        return 'I am the coolest kid'

person = Father()
print(person)