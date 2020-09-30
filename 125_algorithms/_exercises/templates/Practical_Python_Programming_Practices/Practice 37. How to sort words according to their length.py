str = input("Insert different strings: ")
first = str.split()
len_first = len(first)

___ i __ range(len_first - 1):
    ___ j __ range(len_first - 1 -i):
        if len(first[j]) > len(first[j + 1]):
            first[j], first[j + 1] = first[j + 1],first[j]
print(' '.join(first))