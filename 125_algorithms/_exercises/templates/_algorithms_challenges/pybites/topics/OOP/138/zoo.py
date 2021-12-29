class Animal:
    counter = 10000
    animals = []

    ___ __init__(self, name):
        Animal.counter += 1
        self.name = name.title()
        self.animals.append(str(self))
        

    ___ __str__(self):
        return f'{Animal.counter}. {self.name}'

    @classmethod
    ___ zoo(cls):
        #print(cls.animals)
        return '\n'.join(animal for animal in cls.animals)

"""
dog = Animal('dog')
cat = Animal('cat')
fish = Animal('fish')
lion = Animal('lion')
mouse = Animal('mouse')
print(Animal.zoo())
horse = Animal('horse')
print(Animal.zoo())
print(str(horse))
"""