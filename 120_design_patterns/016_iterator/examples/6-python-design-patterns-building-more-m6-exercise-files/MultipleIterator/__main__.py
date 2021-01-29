from testdata import employees

i1 = iter(employees)
i2 = iter(employees)
# assert i1 == i2

for _ in range(5):
    print('{}, {}'.format(next(i1).number, next(i2).number))
