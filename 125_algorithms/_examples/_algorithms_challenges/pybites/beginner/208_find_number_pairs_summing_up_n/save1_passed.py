import itertools


def find_number_pairs(numbers, N=10):
    lis = []
    for i in numbers:
        for comb in itertools.combinations(numbers, 2):
            if sum(comb) == N and comb not in lis:
                lis.append(comb)
    return lis