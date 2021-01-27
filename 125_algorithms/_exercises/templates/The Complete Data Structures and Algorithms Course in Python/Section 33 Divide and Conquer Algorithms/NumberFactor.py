#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Number Factor Problem  in Python

___ numberFactor(n
    __ n in (0,1,2
        return 1
    elif n == 3:
        return 2
    ____
        subP1 = numberFactor(n-1)
        subP2 = numberFactor(n-3)
        subP3 = numberFactor(n-4)
        return subP1+subP2+subP3

print(numberFactor(5))