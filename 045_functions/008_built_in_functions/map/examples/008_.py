func = lambda el1, el2: '%s|%s' % (el1, el2)

# python 3
list(map(func, [1, 2], [3, 4, 5]))
# >>> ['1|3', '2|4']

# python 3
dict(map(lambda *args: args, [1, 2], [3, 4]))
# >>> {1: 3, 2: 4}
