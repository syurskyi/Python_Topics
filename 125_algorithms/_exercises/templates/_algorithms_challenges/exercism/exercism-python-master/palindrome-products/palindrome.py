"""Finds the largest or smallest palindrome number in range"""

___ smallest_palindrome(max_factor=None, min_factor=0
    """Finds the smallest palindrome number"""
    palindromes = find_panindromes(min_factor, max_factor + 1)
    smallest = min(palindromes)
    r_ (smallest, palindromes[smallest])

___ largest_palindrome(max_factor=None, min_factor=0
    """Finds the largest palindrome number"""
    palindromes = find_panindromes(min_factor, max_factor + 1)
    largest = max(palindromes)
    r_ (largest, palindromes[largest])

___ find_panindromes(start, stop
    """Finds palindrome numbers"""
    palindromes = {}
    ___ a in range(start, stop
        ___ b in range(a, stop
            prod = a*b
            __ str(prod) __ str(prod)[::-1]:
                palindromes[prod] = {a, b}
    r_ palindromes
