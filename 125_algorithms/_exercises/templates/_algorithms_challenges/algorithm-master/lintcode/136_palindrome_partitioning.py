c_ Solution:
    ans    # list
    n 0
    is_palindrome N..

    """
    @param: s: A string
    @return: A list of lists of string
    """
    ___ partition  s
        __ n.. s:
            r.. ans

        n l..(s)
        check_palindrome(s)
        dfs(s, 0, [])

        r.. ans

    ___ check_palindrome  s
        """
        assuming string = 'aabb'
        s: start_index, e: end_index

        `is_palindrome[s][e] == T` means
        the substring(string[s:e+1]) is a palindrome

        the benefit to have the `is_palindrome` in advance is
        we won't need to traverse the whole string again
        when every time we need

            e 0  1  2  3
        s     a  a  b  b
        0 a [[T, T, F, F],
        1 a  [F, T, F, F],
        2 b  [F, F, T, T],
        3 b  [F, F, F, T]]

        and the traversal order to init this matrix is below:
        x: means `start > end`, its impossible

        [[r1, r2, r4, r4],
         [ x, r1, r2, r3],
         [ x,  x, r1, r2],
         [ x,  x,  x, r1]]
        """
        is_palindrome [[F..] * n ___ _ __ r..(n)]
        start end 0

        # check the diagonal line `r1` and `r2`
        # the traversal order is top-left -> bottom-right, see graph above
        # since the status of `r3`, `r4`, ... depends on that
        ___ end __ r..(n
            is_palindrome[end][end] T..

            __ end > 0
                start end - 1
                is_palindrome[start][end] (s[start] __ s[end])

        # check the remaining triangle and traverse by line: `r3`, `r4`, ...
        # the traversal order is bottom -> top, see graph above
        # n - 3 = (n - 1) - 2
        # start + 2
        ___ start __ r..(n - 3, -1, -1
            ___ end __ r..(start + 2, n
                is_palindrome[start][end] (
                    is_palindrome[start + 1][end - 1]
                    a.. s[start] __ s[end]
                )

    # traverse all of the possible substring from start
    # if is a palindrome, continue to traverse
    # otherwise will be ignored
    # and catch all result at the end
    ___ dfs  s, start, palindromes
        __ start >_ n:
            ans.a..(palindromes)
        next_start 0
        ___ end __ r..(start, n
            __ is_palindrome[start][end]:
                # `palindromes + [s[start:next_start]]`
                # will create and return new list
                next_start end + 1
                dfs(s, next_start, palindromes + [s[start:next_start]])
