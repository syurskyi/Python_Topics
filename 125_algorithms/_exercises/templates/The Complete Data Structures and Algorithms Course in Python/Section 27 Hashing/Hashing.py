#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

___ mod(number, cellNumber
    r_ number % cellNumber


# print(mod(400, 24))


___ modASCII(s__, cellNumber
    total  0
    ___ i __ s__:
        total + ord(i)
    r_ total % cellNumber

print(modASCII("ABC", 24))
