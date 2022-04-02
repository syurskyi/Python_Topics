c_ Solution:
    # @param s, a string
    # @return a list of lists of string
    ___ partition  s
        res    # list
        cand    # list
        partition_aux(s, cand, res)
        r.. res

    ___ partition_aux  s, cand, res
        __ n.. s:
            res.a..(cand | )
        ____:
            ___ i, e __ e..(s
                __ is_palindrome(s[:i + 1]
                    cand.a..(s[:i + 1])
                    partition_aux(s[i + 1:], cand, res)
                    cand.pop()

    ___ is_palindrome  s
        left = 0
        right = l..(s) - 1
        w.... left < right:
            __ s[left] != s[right]:
                r.. F..
            left += 1
            right -= 1
        r.. T..
