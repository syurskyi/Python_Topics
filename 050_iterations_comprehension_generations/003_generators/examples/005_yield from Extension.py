# The Python 3.3 yield from Extension
# def both(N)

def both(N):
    for i in range(N): yield i
    for i in (x ** 2 for x in range(N)): yield i


print(both(5))
print(list(both(5)))


def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))


print(list(both(5)))

print(' : '.join(str(i) for i in both(5)))
