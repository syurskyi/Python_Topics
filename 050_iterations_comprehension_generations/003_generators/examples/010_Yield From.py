# Yield From
# Suppose we want an iterator to iterate over all the values of the matrix, element by element.
# All we have done here is create a generator (iterator) that can be used to iterate of the elements
# of a nested iterator.

def matrix_iterator(n):
    for row in matrix(n):
        for item in row:
            yield item

for i in matrix_iterator(3):
    print(i)

# Yield From
# But we can avoid using that nested for loop by using a special form of yield: yield from

def matrix_iterator(n):
    for row in matrix(n):
        yield from row

for i in matrix_iterator(3):
    print(i)

# Yield From
#
# we need to read car brands from multiple files to get it as a single collection.

def brands(*files):
    for f_name in files:
        with open(f_name) as f:
            yield from f

files = 'car-brands-1.txt', 'car-brands-2.txt', 'car-brands-3.txt'

for brand in brands(*files):
    print(brand, end=', ')

# Yield From
#
# we are going to create generators that can read each line of the file, and yield a clean result,
# and we'll yield from that generator:
# As you can see, this generator function will clean each line of the file before yielding it.
# Let's try it with a single file and make sure it works:
# So now, we can proceed with our overarching generator function as before, except we'll yield from our generators,
# instead of directly from the file iterator:
# I want to point out that in this particular instance, we are using yield from as a simple replacement for a for loop

def gen_clean_read(file):
    with open(file) as f:
        for line in f:
            yield line.strip('\n')

f1 = gen_clean_read('car-brands-1.txt')
for line in f1:
    print(line, end=', ')

files = 'car-brands-1.txt', 'car-brands-2.txt', 'car-brands-3.txt'

def brands(*files):
    for file in files:
        yield from gen_clean_read(file)

for brand in brands(*files):
    print(brand, end=', ')
