___ pattern(n):
    __ n <= 0:
        r.. ''
    __ n __ 1:
        r.. '1'
    res    # list
    pattern = [' '] * ( 2 * n -1)
    ___ i __ r..(1,n):
        temp = pattern[:]
        temp[i-1] = temp[-i] = str(i%10)
        res.a..(''.join(temp))
    pattern[n-1] = str(n%10)
    res.a..(''.join(pattern))
    res += res[n-2::-1]    
    r.. '\n'.join(res)

print(pattern(1))