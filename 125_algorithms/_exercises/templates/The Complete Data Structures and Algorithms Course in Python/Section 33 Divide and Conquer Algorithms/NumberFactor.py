#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Number Factor Problem  in Python

___ numberFactor(n
    __ n __ (0,1,2
        r_ 1
    elif n == 3:
        r_ 2
    ____
        subP1 = numberFactor(n-1)
        subP2 = numberFactor(n-3)
        subP3 = numberFactor(n-4)
        r_ subP1+subP2+subP3

print(numberFactor(5))