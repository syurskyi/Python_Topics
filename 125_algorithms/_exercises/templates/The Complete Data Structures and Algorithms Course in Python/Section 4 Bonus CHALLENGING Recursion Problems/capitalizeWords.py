#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# capitalizeWords Solution

___ capitalizeWords(arr
    result = []
    __ len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])



words = ['i', 'am', 'learning', 'recursion']
print(capitalizeWords(words)) # ['I', 'AM', 'LEARNING', 'RECURSION']