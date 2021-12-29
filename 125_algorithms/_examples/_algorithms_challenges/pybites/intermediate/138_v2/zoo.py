class Animal:
    
    number = 10001
    animals = []
    def __init__(self, name):
        self.name = name.title()
        self.number = Animal.number
        Animal.number += 1
        Animal.animals.append(self)

    def __str__(self):
        return f"{self.number}. {self.name}"

    @classmethod
    def zoo(cls):
        return '\n'.join(str(animal) for animal in cls.animals)

