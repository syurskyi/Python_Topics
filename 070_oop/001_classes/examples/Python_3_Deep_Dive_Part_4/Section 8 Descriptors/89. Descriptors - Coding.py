# %%
'''
### Descriptors
'''

# %%
'''
Python **descriptors** are simply objects that implement the **descriptor protocol**.
The protocol is comprised of the following special methods - not all are required.
- `__get__`: used to retrieve the property value
- `__set__`: used to store the property value (we'll see where we can do this in a bit)
- `__del__`: delete a property from the instance
- `__set_name__`: new to Python 3.6, we can use this to capture the property name as it is being defined in the owner 
class (the class where the property is defined).

There are two types of descriptors we need to distingush as I explain in the video lecture:
- non-data descriptors: these are descriptors that only implement `__get__` (and optionally `__set_name__`)
- data descriptors: these implement the `__set__` method, and normally, also the `__get__` method.
'''

# %%
'''
Let's create a simple non-data descriptor:
'''

# %%
from datetime import datetime

class TimeUTC:
    def __get__(self, instance, owner_class):
        return datetime.utcnow().isoformat()

# %%
'''
So `TimeUTC` is a class that implements the `__get__` method only, and is therefore considered a non-data descriptor.
'''

# %%
'''
We can now use it to create properties in other classes:
'''

# %%
class Logger:
    current_time = TimeUTC()

# %%
'''
Note that `current_time` is a class attribute:
'''

# %%
Logger.__dict__

# %%
'''
We can access that attribute from an instance of the `Logger` class:
'''

# %%
l = Logger()

# %%
l.current_time

# %%
'''
We can also access it from the class itself, and for now it behaves the same (we'll come back to that later):
'''

# %%
Logger.current_time

# %%
'''
Let's consider another example.
'''

# %%
'''
Suppose we want to create class that allows us to select a random suit and random card from that suit from a deck 
of cards (with replacement, i.e. the same card can be picked more than once).
'''

# %%
'''
We could approach it this way:
'''

# %%
from random import choice, seed

class Deck:
    @property
    def suit(self):
        return choice(('Spade', 'Heart', 'Diamond', 'Club'))
        
    @property
    def card(self):
        return choice(tuple('23456789JQKA') + ('10',))

# %%
d = Deck()

# %%
seed(0)

for _ in range(10):
    print(d.card, d.suit)

# %%
'''
This was pretty easy, but as you can see both properties essentially did the same thing - they picked a random choice 
from some iterable.
Let's rewrite this using a custom descriptor:
'''

# %%
class Choice:
    def __init__(self, *choices):
        self.choices = choices
        
    def __get__(self, instance, owner_class):
        return choice(self.choices)

# %%
'''
And now we can rewrite our `Deck` class this way:
'''

# %%
class Deck:
    suit = Choice('Spade', 'Heart', 'Diamond', 'Club')
    card = Choice(*'23456789JQKA', '10')

# %%
seed(0)

d = Deck()

for _ in range(10):
    print(d.card, d.suit)

# %%
'''
Of course we are not limited to just cards, we could use it in other classes too:
'''

# %%
class Dice:
    die_1 = Choice(1,2,3,4,5,6)
    die_2 = Choice(1,2,3,4,5,6)
    die_3 = Choice(1,2,3,4,5,6)

# %%
seed(0)

dice = Dice()
for _ in range(10):
    print(dice.die_1, dice.die_2, dice.die_3)

# %%
