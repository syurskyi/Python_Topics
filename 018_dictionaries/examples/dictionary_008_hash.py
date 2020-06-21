# Dictionary keys must be hashable objects. Associated values on the other hand can be any object
# So tuples of hashable objects are themselves hashable, but lists are not, even if they only contain hashable elements.
# Tuples of non-hashable elements are also not hashable.
#
hash((1, 2, 3))
hash([1, 2, 3])
hash(([1, 2], [3, 4]))

# Interestingly, functions are hashable:
def my_func(a, b, c):
    print(a, b, c)

# Which means we can use functions as keys in dictionaries:
d = {my_func: [10, 20, 30]}

