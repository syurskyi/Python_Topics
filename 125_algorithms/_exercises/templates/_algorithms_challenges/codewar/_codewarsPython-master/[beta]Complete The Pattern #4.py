___ pattern(n):
    string = [s..(i) ___ i __ r..(1,n+1)]
    r.. '\n'.join([''.join(lst) ___ lst __ [string[i:] ___ i __ r..(n)]])

___ i __ (0,1,2,3,4,5):
    print(pattern(i))    