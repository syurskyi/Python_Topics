____ i.. _______ c..

""" def find_number_pairs(numbers, N=10):
    temp = []
    for i in range(len(numbers)-1):
        for j in numbers[i+1:]:
            if numbers[i] + j == N:
                temp.append(tuple((numbers[i], j)))
    return temp """

___ find_number_pairs(numbers, N=10
    r..[(i,j) ___ i, j __ c..numbers,2) __ i+j__N]

print(find_number_pairs([9, 1, 3, 8, 7]