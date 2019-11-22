# Nested Comprehensions
# Just as with list comprehensions, we can nest generator expressions too:
# A multiplication table:
# Using a list comprehension approach first:
# The equivalent generator expression would be:
# We can iterate through mult_list:
# But you'll notice that our rows are themselves generators!
# o fully materialize the table we need to iterate through the row generators too:

start = 1
stop = 10

mult_list = [ [i * j
               for j in range(start, stop+1)]
             for i in range(start, stop+1)]

mult_list

start = 1
stop = 10

mult_list = ( (i * j
               for j in range(start, stop+1))
             for i in range(start, stop+1))

mult_list

table = list(mult_list)
table

table_rows = [list(gen) for gen in table]
table_rows

# Nested Comprehensions
# Of course, we can mix list comprehensions and generators.
# In this modification, we'll make the rows list comprehensions, and retain the generator expression in the outer
# comprehension:
# Notice what is happening here, the table itself is lazy evaluated, i.e. the rows are not yielded until they
# are requested - but once a row is requested, the list comprehension that defines the row will be entirely
# evaluated at that point:

start = 1
stop = 10

mult_list = ( [i * j
               for j in range(start, stop+1)]
             for i in range(start, stop+1))

for item in mult_list:
    print(item)

# Let's try Pascal's triangle again:
# Here's how we did it using a list comprehension:

from math import factorial

def combo(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

size = 10  # global variable
pascal = [ [combo(n, k) for k in range(n+1)] for n in range(size+1) ]

# Let's try Pascal's triangle again:
#
# If we want to materialize the triangle into a list we'll need to do so ourselves:

size = 10  # global variable
pascal = ( (combo(n, k) for k in range(n+1)) for n in range(size+1) )

[list(row) for row in pascal]
