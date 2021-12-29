#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Implement a cat and dog queue for an animal shelter.

c_ AnimalShelter(
  ___  - (self
    cats  []
    dogs  []
  
  ___ enqueue  animal, ty..
    __ ty.. __ 'Cat':
      cats.ap..(animal)
    ____
      dogs.ap..(animal)
    
  ___ dequeueCat(self
    __ le_(cats) __ 0:
      r_ N..
    ____
      cat  cats.pop(0)
      r_ cat
  
  ___ dequeueDog(self
    __ le_(dogs) __ 0:
      r_ N..
    ____
      dog  dogs.pop(0)
      r_ dog
  
  ___ dequeueAny(self
    __ le_(cats) __ 0:
      result  dogs.pop(0)
    ____
      result  cats.pop(0)
    r_ result

customQueue  AnimalShelter()
customQueue.enqueue('Cat1', 'Cat')
customQueue.enqueue('Cat2', 'Cat')
customQueue.enqueue('Dog1', 'Dog')
customQueue.enqueue('Cat3', 'Cat')
customQueue.enqueue('Dog2', 'Dog')
print(customQueue.dequeueAny())
