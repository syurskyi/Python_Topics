
___ fibonacci_recursion(n

    __ n __ 0:
        r_ 1

    __ n __ 1:
        r_ 1

    r_ fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


# top-down approach
___ fibonacci_memoization(n, table

    __ n not __ table:
        table[n] = fibonacci_memoization(n-1, table) + fibonacci_memoization(n-2, table)

    # O(1) running time
    r_ table[n]


# bottom-up approach
___ fibonacci_tabulation(n, table

    ___ i __ ra__(2, n+1
        table[i] = table[i-1] + table[i-2]

    r_ table[n]


t = {0: 1, 1: 1}
# exponential running time
print(fibonacci_recursion(1))
# these are the O(N) linear running time approaches
print(fibonacci_tabulation(50, t))
print(fibonacci_memoization(40, t))

