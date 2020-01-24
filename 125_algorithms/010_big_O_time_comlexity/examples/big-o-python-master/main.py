from one import One
from log_n import LogN
from n import N
from n_square import NSquare
import random

algorithms = [ One(), LogN(), N(), NSquare() ]
elements = [10, 100, 250, 500, 1000, 2000, 2500, 3000]

print("-" * 50)
print("Running algorithms...")
print("-" * 50)

for e in elements:
    print("Elements: %d" % e)
    for alg in algorithms:
        alg.run(e)
        alg.print_results()
    print()

print("-" * 50)
print("-" * 50)
