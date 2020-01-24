# Chicken Coop Exercise Solution:
#
# Here's my implementation of the Chicken class.  Notice the total_eggs class attribute.


class Chicken:
    total_eggs = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs
