___ pattern(n
    __ n <= 0:
        r.. ''
    __ n __ 1:
        r.. '1'
    res    # list
    pattern =  ' '  * ( 2 * n -1)
    ___ i __ r..(1,n
        temp = pattern |
        temp[i-1] = temp[-i] = s..(i%10)
        res.a..(''.j..(temp))
    pattern[n-1] = s..(n%10)
    res.a..(''.j..(pattern))
    res += res[n-2::-1]    
    r.. '\n'.j..(res)

print(pattern(1))