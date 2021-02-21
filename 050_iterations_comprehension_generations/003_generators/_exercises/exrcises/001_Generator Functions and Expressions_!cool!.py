def gensquares(N):
    for i in range(N):
        yield  i ** 2  # Resume here later

for i in gensquares(5):  # Resume the function
    print(i, end=' : ')  # # Print last yield value

print()
x = gensquares(4)
print(x)

print(next(x))  # Same as x.__next__() i_ 3.0
#
# print n___ x  # Use x.n___() or n___() i_ 2.6
# print n___ x
# print n___ x
#
# # Generator Functions and Expressions
# #  Returns a generator which is its own iterator
def gensquares(N):
    for i in range(N):
        yield i ** 2


y = gensquares(5)  # Returns a generator which is its own iterator

print(iter(y) is y)  # iter() is not required a no-op here

print(next(y))  # Can run n___()immediately
#
# # Generator Functions and Expressions
# ___ buildsquares(n)

def buildsquares(n):
    res = []    #list
    for i in range(n):
        res.append(i ** 2)
    return res


for x in buildsquares(5):
    print(x, end='  ')
print()

for x in [n ** 2 for n in range(5)]:
    print(x, end='  ')    # list

print()

for x in map((lambda n: n ** 2), range(5)):
    print(x, end=" : ")

# Generator Functions and Expressions
# def  ups()
def ups(line):
    for sub in line.split(','):  # Substring generator
        yield sub.upper()


print(tuple(ups('aaa,bbb,ccc')))  # All iteration contexts)

print({i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))})   # dict   be careful here
