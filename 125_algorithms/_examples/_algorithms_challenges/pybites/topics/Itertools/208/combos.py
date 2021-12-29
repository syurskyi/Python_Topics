from itertools import combinations

""" def find_number_pairs(numbers, N=10):
    temp = []
    for i in range(len(numbers)-1):
        for j in numbers[i+1:]:
            if numbers[i] + j == N:
                temp.append(tuple((numbers[i], j)))
    return temp """

def find_number_pairs(numbers, N=10):
    return[(i,j) for i, j in combinations(numbers,2) if i+j==N]

print(find_number_pairs([9, 1, 3, 8, 7]))