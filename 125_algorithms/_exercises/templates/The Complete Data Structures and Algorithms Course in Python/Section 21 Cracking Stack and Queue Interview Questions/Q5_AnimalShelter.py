#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Implement a cat and dog queue for an animal shelter.

class AnimalShelter(
  ___ __init__(self
    self.cats = []
    self.dogs = []
  
  ___ enqueue(self, animal, type
    __ type == 'Cat':
      self.cats.append(animal)
    ____
      self.dogs.append(animal)
    
  ___ dequeueCat(self
    __ len(self.cats) == 0:
      return None
    ____
      cat = self.cats.pop(0)
      return cat
  
  ___ dequeueDog(self
    __ len(self.dogs) == 0:
      return None
    ____
      dog = self.dogs.pop(0)
      return dog
  
  ___ dequeueAny(self
    __ len(self.cats) == 0:
      result = self.dogs.pop(0)
    ____
      result = self.cats.pop(0)
    return result

customQueue = AnimalShelter()
customQueue.enqueue('Cat1', 'Cat')
customQueue.enqueue('Cat2', 'Cat')
customQueue.enqueue('Dog1', 'Dog')
customQueue.enqueue('Cat3', 'Cat')
customQueue.enqueue('Dog2', 'Dog')
print(customQueue.dequeueAny())
