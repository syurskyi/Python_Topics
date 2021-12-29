___ pattern(n):
    res    # list
    spaces = (2 * n) - 1
    ___ i __ r..(1,n+1):
    	term = l..(r..(1,i+1)) + l..(r..(i-1,0,-1))
    	term = [t%10 ___ t __ term]
    	term = [' '] * int(((spaces - l..(term))/2)) + term + [' '] * int(((spaces - l..(term))/2))
    	term = ''.join(map(s..,term))
    	res.a..(term)
    res += res[-2::-1]
    r.. '\n'.join(res)


print(pattern(27))    
