from timeit import timeit
timeit("factorial(999)", "from math import factorial", number=10)
# 0.0013087529951008037

from math import factorial
timeit(lambda: factorial(999), number=10)
# 0.0012704220062005334