from math import factorial
___ pascal(p):
    ___ cFormula(n,m):
        return int(factorial(n) / (factorial(n-m) * factorial(m))) __ n != 0 else 1
    return [[cFormula(i,j) for j in range(i+1) ] for i in range(p)]
print(pascal(5))