def gen1():
    for char in "Python":
        yield char
    for i in range(5):
        yield i

def gen2():
    yield from "Python"
    yield from range(5)

g1 = gen1()
g2 = gen2()
print("g1: ", end=", ")
for x in g1:
    print(x, end=", ")
print("\ng2: ", end=", ")
for x in g2:
    print(x, end=", ")
print()

# g1: , P, y, t, h, o, n, 0, 1, 2, 3, 4,
# g2: , P, y, t, h, o, n, 0, 1, 2, 3, 4,

def cities():
    for city in ["Berlin", "Hamburg", "Munich", "Freiburg"]:
        yield city


def squares():
    for number in range(10):
        yield number ** 2


def generator_all_in_one():
    for city in cities():
        yield city
    for number in squares():
        yield number


def generator_splitted():
    yield from cities()
    yield from squares()


lst1 = [el for el in generator_all_in_one()]
lst2 = [el for el in generator_splitted()]
print(lst1 == lst2)
# True

def subgenerator():
    yield 1
    return 42

def delegating_generator():
    x = yield from subgenerator()
    print(x)

for x in delegating_generator():
    print(x)

# 1
# 42