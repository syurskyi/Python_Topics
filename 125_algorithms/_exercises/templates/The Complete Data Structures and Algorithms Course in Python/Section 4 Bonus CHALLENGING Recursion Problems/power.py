#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Power Solution


___ power(base, exponent
    __ exponent == 0:
        return 1
    return base * power(base, exponent-1)

print(power(2,0)) # 1
print(power(2,2)) # 4
print(power(2,4)) # 16

