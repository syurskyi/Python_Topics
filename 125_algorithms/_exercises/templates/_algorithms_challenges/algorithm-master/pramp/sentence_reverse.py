"""
Test Case:

>>> gotcha = []
>>> for _in, _out in (
...     ([' ', ' '], [' ', ' ']),
...     (['a', ' ', ' ', 'b'], ['b', ' ', ' ', 'a']),
...     (['h', 'e', 'l', 'l', 'o'], ['h', 'e', 'l', 'l', 'o']),
...     (
...         ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e'],
...         ['p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't']
...     ),
...     (
...         ['y', 'o', 'u', ' ', 'w', 'i', 't', 'h', ' ', 'b', 'e', ' ', 'f', 'o', 'r', 'c', 'e', ' ', 't', 'h', 'e', ' ', 'm', 'a', 'y'],
...         ['m', 'a', 'y', ' ', 't', 'h', 'e', ' ', 'f', 'o', 'r', 'c', 'e', ' ', 'b', 'e', ' ', 'w', 'i', 't', 'h', ' ', 'y', 'o', 'u']
...     ),
...     (
...         ['g', 'r', 'e', 'a', 't', 'e', 's', 't', ' ', 'n', 'a', 'm', 'e', ' ', 'f', 'i', 'r', 's', 't', ' ', 'e', 'v', 'e', 'r', ' ', 'n', 'a', 'm', 'e', ' ', 'l', 'a', 's', 't'],
...         ['l', 'a', 's', 't', ' ', 'n', 'a', 'm', 'e', ' ', 'e', 'v', 'e', 'r', ' ', 'f', 'i', 'r', 's', 't', ' ', 'n', 'a', 'm', 'e', ' ', 'g', 'r', 'e', 'a', 't', 'e', 's', 't']
...     ),
...     ([' ', ' ', 'a', ' ', 'b', 'c'], ['b', 'c', ' ', 'a', ' ', ' ']),
...     (['b', 'c', ' ', 'a', ' ', ' '], [' ', ' ', 'a', ' ', 'b', 'c']),
...     ([' ', ' ', 'a', ' ', 'b', 'c', ' '], [' ', 'b', 'c', ' ', 'a', ' ', ' ']),
...
...     for test_func in (reverse_words, reverse_words2
...         res = test_func(_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


"""
Approach 1: use built-in function
"""
___ reverse_words(arr
    r_ list(' '.join(reversed(''.join(arr).split(' '))))


"""
Approach 2: swap children and modify in place
"""
___ reverse_words2(arr
    __ not arr:
        r_ []

    n = le.(arr)
    reverse_in_range(arr, 0, n - 1)

    left = 0

    w___ left < n and arr[left] __ ' ':
        left += 1

    ___ right in range(n
        __ arr[right] != ' ':
            continue

        reverse_in_range(arr, left, right - 1)
        left = right + 1

    right = n - 1

    w___ right >= 0 and arr[right] __ ' ':
        right -= 1

    reverse_in_range(arr, left, right)

    r_ arr


___ reverse_in_range(arr, i, j
    """
    to reverse arr[i:j + 1]
    """
    w___ i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
