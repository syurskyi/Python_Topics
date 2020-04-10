____ one ______ One
____ log_n ______ LogN
____ n ______ N
____ n_square ______ NSquare
____ random

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
