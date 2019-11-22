# Rolling our own Next method
# implement a __len__ method to support the len() function

class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0

    def next_(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

    def __len__(self):
        return self.length

sq = Squares(3)
len(sq)
sq.next_()
sq.next_()
sq.next_()
#
# So now, we can essentially loop over the collection in a very similar way to how we did it with sequences and the __getitem__ method:
#
sq = Squares(5)
while True:
    try:
        print(sq.next_())
    except StopIteration:
        # reached end of iteration
        # stop looping
        break

# Iterating Collections
# class RandomNumbers:

import random

class RandomNumbers:
    def __init__(self, length, *, range_min=0, range_max=10):
        self.length = length
        self.range_min = range_min
        self.range_max = range_max
        self.num_requested = 0

    def __len__(self):
        return self.length

    def __next__(self):
        if self.num_requested >= self.length:
            raise StopIteration
        else:
            self.num_requested += 1
            return random.randint(self.range_min, self.range_max)


numbers = RandomNumbers(10)
len(numbers)

while True:
    try:
        print(next(numbers))
    except StopIteration:
        break

# We still cannot use a for loop, and if we want to 'restart' the iteration, we have to create a new object every time.
#
numbers = RandomNumbers(10)

for item in numbers:
    print(item) #error


# Iterators and Iterables
# build class Cities

class Cities:
    def __init__(self):
        self._cities = ['New York', 'Newark', 'New Delhi', 'Newcastle']
    def __len__(self):
        return len(self._cities)
    def __getitem__(self, s):
        print('getting item...')
        return self._cities[s]
    def __iter__(self):
        print('Calling Cities instance __iter__')
        return self.CityIterator(self)
    class CityIterator:
        def __init__(self, city_obj):
            # cities is an instance of Cities
            print('Calling CityIterator __init__')
            self._city_obj = city_obj
            self._index = 0
        def __iter__(self):
            print('Calling CitiyIterator instance __iter__')
            return self
        def __next__(self):
            print('Calling __next__')
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item
# cities = Cities()
# cities[0]
# next(iter(cities))
# cities = Cities()
# for city in cities:
