___ play_pass(s, n
    res = ''
    for c in map(ord,s
        __ c in range(65,91
            res += chr((((c-65) + n) % 26) + 65)
        ____ c in range(97,123
            res += chr((((c-97) + n) % 26) + 97)
        ____ c in range(48,58
            res += str (abs(9 - int(chr(c))))
        ____
            res += str(chr(c))
    res = ''.join([res[i].upper() __ i % 2 __ 0 else res[i].lower() for i in range(le.(res))])
    r_ res[::-1]