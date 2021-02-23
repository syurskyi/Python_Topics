# Yielding and Generators
# create def squares (sentinel) :
# without error

def squares(sentinel):
    i = 0
    while True:
        if i < sentinel:
            yield  i**2
            i += 1 # note how we can incremenet **after** the yield
        else:
            return 'all done!'

# num
for num in squares(5):
    print(num)
#
# # Yielding and Generators
# #
# # So now let's see how we could re-write our initial factorial example:

import math
# i
def factorials(n):
    for i in range(n):
        yield  math.factorial(i)

# num
for num in factorials(5):
    print(num)

print()
facts = factorials(5)
list(facts)
list(facts)
# ne.. f...  # error
#
# # Making an Iterable from a Generator
# # As we now know, generators are iterators.
# # This means that they become exhausted - so sometimes we want to create an iterable instead.
# # But, sq was an iterator - so now it's been exhausted:
# # To restart the iteration we have to create a new instance of the generator  iterator :

# i
def squares_gen(n):
    for i in range(n):
        yield i** 2

sq = squares_gen(5)
print()
# num
for num in sq:
    print(num)
print()
# next(sq)

sq = squares_gen(5)
[num for num in sq]

# # Generators used with other Generators
# # Now enumerate is lazy, so sq had not, at this point, been consumed:
# # Since we have consumed two elements from sq, when we now use enumerate it will have two less elements from sq:

# i
def squares(n):
    for i in range(n):
        yield i ** 2

sq = squares(5)
enum_sq = enumerate(sq)

print()
print(next(sq))
print(next(sq))

print(next(enum_sq))

# # Generator Expressions
# # Recall how li.. comprehensions worked:
# # We can easily create a generator by using    parentheses instead of the [] brackets:
# # Note that g is a generator, and is also lazily evaluated:

# i
l = [i ** 2 for i in range(5)] # list comprehension
print(l)
# The expression inside the [] brackets is called a comprehension expression.

g = (i ** 2 for i in range(5))

print(type(g))

# item
for item in g:
    print(item)
#
# # Generator Expressions
# #
# # We can iterate over the same li.. comprehension multiple times, since it is an iterable.
# # However, we can only iterate over a comprehension expression once, since it is an iterator.
#
# # i
l = [i * 2 for i in range(5)]
print(type(l))

g = (i ** 2 for i in range(5))
print(type(g))