from ma__ ______ factorial
___ pascal(p
    ___ cFormula(n,m
        r_ int(factorial(n) / (factorial(n-m) * factorial(m))) __ n != 0 else 1
    r_ [[cFormula(i,j) ___ j in range(i+1) ] ___ i in range(p)]
print(pascal(5))