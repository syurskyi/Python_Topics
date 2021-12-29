str  input("Insert different strings: ")
first  str.s.. 
len_first  l..(first)

___ i __ r..(len_first - 1):
    ___ j __ r..(len_first - 1 -i):
        __ l..(first[j]) > l..(first[j + 1]):
            first[j], first[j + 1]  first[j + 1],first[j]
print(' '.join(first))