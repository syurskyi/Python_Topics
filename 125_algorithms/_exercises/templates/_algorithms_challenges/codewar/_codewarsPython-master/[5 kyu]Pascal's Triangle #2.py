____ math _______ factorial
___ pascal(p
    ___ cFormula(n,m
        r.. i..(factorial(n) / (factorial(n-m) * factorial(m))) __ n != 0 ____ 1
    r.. [[cFormula(i,j) ___ j __ r..(i+1) ] ___ i __ r..(p)]
print(pascal(5))