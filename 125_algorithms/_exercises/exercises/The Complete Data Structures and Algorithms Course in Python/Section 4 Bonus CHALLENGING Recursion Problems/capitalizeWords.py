#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# capitalizeWords Solution

___ capitalizeWords(arr
    result = []
    __ le_(arr) __ 0:
        r_ result
    result.ap..(arr[0].upper())
    r_ result + capitalizeWords(arr[1:])



words = ['i', 'am', 'learning', 'recursion']
print(capitalizeWords(words)) # ['I', 'AM', 'LEARNING', 'RECURSION']