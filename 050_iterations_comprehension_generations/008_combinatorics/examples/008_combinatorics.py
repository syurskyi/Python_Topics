# Combinatorics
# Cartesian Product
# The cartesian product is actually a lot more useful than it might appear at first.
# Consider this example, where we want to create a multiplication table as we have seen before:
# We can look at a few elements using islice:
# So, the Cartesian product of two iterables in general can be generated using a nested loop:
# We can achieve the same result with the product function in itertools. As usual, it is lazy as well.

def matrix(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            yield f'{i} x {j} = {i*j}'

list(itertools.islice(matrix(10), 10, 20))

l1 = ['x1', 'x2', 'x3', 'x4']
l2 = ['y1', 'y2', 'y3']
for x in l1:
    for y in l2:
        print((x, y), end=' ')
    print('')

l1 = ['x1', 'x2', 'x3', 'x4']
l2 = ['y1', 'y2', 'y3']
list(itertools.product(l1, l2))

# Combinatorics
# Cartesian Product
# As a simple example, let's go back to the multiplication table we created using a generator function.
# And of course this is now simple enough to even use just a generator expression:

def matrix(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            yield (i, j, i*j)

list(matrix(4))

def matrix(n):
    for i, j in itertools.product(range(1, n+1), range(1, n+1)):
        yield (i, j, i*j)

list(matrix(4))

def matrix(n):
    return ((i, j, i*j)
            for i, j in itertools.product(range(1, n+1), range(1, n+1)))

list(matrix(4))


# Combinatorics
# Cartesian Product
#
# You'll notice how we repeated the range(1, n+1) twice?
#
# This is a great example of where tee can be useful:

from itertools import tee

def matrix(n):
    return ((i, j, i*j)
            for i, j in itertools.product(*itertools.tee(range(1, n+1), 2)))

list(matrix(4))

# A common usage of Cartesian products might be to generate a grid of coordinates.
# For a 2D space for example, we might want to generate a grid of points ranging from -5 to 5 in both the x and y axes,
# with a step of 0.5.
# We can't use a range since ranges need integral numbers,
# but we have the count function in itertools we have seen before:
# And of course we can now do it in 3D as well:

def grid(min_val, max_val, step, *, num_dimensions=2):
    axis = itertools.takewhile(lambda x: x <= max_val,
                               itertools.count(min_val, step))

    # to handle multiple dimensions, we just need to repeat the axis that
    # many times - tee is perfect for that
    axes = itertools.tee(axis, num_dimensions)

    # and now we just need the product of all these iterables
    return itertools.product(*axes)


list(grid(-1, 1, 0.5))

list(grid(-1, 1, 0.5, num_dimensions=3))

# Another simple application of this might be to determine the odds of rolling an 8 with a pair of dice
# (with values 1 - 6).
# We can brute force this by generating all the possible results (the sample space),
# and counting how may items add up to 8.
# Now we want to filter out the tuples whose elements add up to 8:
# And we can calculate the odds by dividing the number acceptable outcomes by the size of the sample space.
# I'll actually use a Fraction so we retain our result as a rational number:

sample_space = list(itertools.product(range(1, 7), range(1, 7)))
print(sample_space)

outcomes = list(filter(lambda x: x[0] + x[1] == 8, sample_space))
print(outcomes)

from fractions import Fraction
odds = Fraction(len(outcomes), len(sample_space))
print(odds)
