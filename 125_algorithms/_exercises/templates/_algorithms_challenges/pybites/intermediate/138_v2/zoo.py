class Animal:
    
    number = 10001
    animals = []
    ___ __init__(self, name):
        self.name = name.title()
        self.number = Animal.number
        Animal.number += 1
        Animal.animals.append(self)

    ___ __str__(self):
        return f"{self.number}. {self.name}"

    @classmethod
    ___ zoo(cls):
        return '\n'.join(str(animal) for animal in cls.animals)

