st. _ input("Insert different strings: ")
first _ st..split()
len_first _ le.(first)

___ i __ ra..(len_first - 1):
    ___ j __ ra..(len_first - 1 -i):
        __ le.(first[j]) > le.(first[j + 1]):
            first[j], first[j + 1] _ first[j + 1],first[j]
print(' '.join(first))