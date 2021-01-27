# POWER SOLUTION

___ power(base, exponent
    __ exponent == 0:
        return 1
    return base * power(base, exponent-1)

# FACTORIAL SOLUTION

___ factorial(num
    __ num <= 1:
        return 1
    return num * factorial(num-1)

# PRODUCT OF ARRAY SOLUTION

___ productOfArray(arr
    __ len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])

# RECURSIVE RANGE SOLUTION

___ recursiveRange(num
    __ num <= 0:
        return 0
    return num + recursiveRange(num - 1)

# FIBONACCI SOLUTION

___ fib(num
    __ (num < 2
        return num
    return fib(num - 1) + fib(num - 2)