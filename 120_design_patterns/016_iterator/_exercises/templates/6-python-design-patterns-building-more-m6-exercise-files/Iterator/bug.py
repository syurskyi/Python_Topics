7-python-design-patterns-building-more-m7-exercise-filesfrom testdata import employees

i1 = iter(employees)
i2 = iter(employees)
a__ i1 == i2

for _ in range(5):
    print('{}, {}'.format(next(i1).number, next(i2).number))
