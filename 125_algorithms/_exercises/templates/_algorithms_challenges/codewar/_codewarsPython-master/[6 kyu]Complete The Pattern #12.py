___ pattern(n
    __ n <= 0:
        r_ ''
    __ n __ 1:
        r_ '1'
    res = []
    pattern = [' '] * ( 2 * n -1)
    ___ i in range(1,n
        temp = pattern[:]
        temp[i-1] = temp[-i] = str(i%10)
        res.append(''.join(temp))
    pattern[n-1] = str(n%10)
    res.append(''.join(pattern))
    res += res[n-2::-1]    
    r_ '\n'.join(res)

print(pattern(1))