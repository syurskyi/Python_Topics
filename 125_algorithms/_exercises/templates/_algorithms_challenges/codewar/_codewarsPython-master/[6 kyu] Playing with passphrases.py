___ play_pass(s, n):
    res = ''
    ___ c __ map(ord,s):
        __ c __ r..(65,91):
            res += chr((((c-65) + n) % 26) + 65)
        ____ c __ r..(97,123):
            res += chr((((c-97) + n) % 26) + 97)
        ____ c __ r..(48,58):
            res += s.. (abs(9 - int(chr(c))))
        ____:
            res += s..(chr(c))
    res = ''.join([res[i].upper() __ i % 2 __ 0 ____ res[i].lower() ___ i __ r..(l..(res))])
    r.. res[::-1]