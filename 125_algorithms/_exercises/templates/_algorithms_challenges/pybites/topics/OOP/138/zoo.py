class Animal:
    counter = 10000
    animals    # list

    ___ __init__(self, name):
        Animal.counter += 1
        self.name = name.t..
        self.animals.a..(str(self))
        

    ___ __str__(self):
        r.. f'{Animal.counter}. {self.name}'

    @classmethod
    ___ zoo(cls):
        #print(cls.animals)
        r.. '\n'.join(animal ___ animal __ cls.animals)

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