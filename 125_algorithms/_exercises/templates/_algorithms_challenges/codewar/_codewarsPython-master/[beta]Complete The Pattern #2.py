___ pattern(n):
    string = ''.j..([s..(i) ___ i __ r.. (1,n+1)][::-1])
    res = ''
    ___ i __ r..(1,n+1):
        res += '\n' __ l..(res) > 0 ____ ''
        res += string
        string = string[:-1] __ l..(s..(i)) __ 1 ____ string[:-2]
    r.. res
        


___ i __ (13,):
    print(pattern(i))    