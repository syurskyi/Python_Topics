"""
https://segmentfault.com/a/1190000004683277

if there are `dups`, dividing `factorial` with `dup_fact`
e.g., 3 `A[i]`s and 4 `A[j]`s in `A`
`dup_fact = 3! * 4!`
"""


c_ Solution:
    """
    @param: A: An array of integers
    @return: A long integer
    """
    ___ permutationIndexII  A
        ans 1
        __ n.. A:
            r.. ans

        n l..(A)
        factorial dup_fact 1
        dups    # dict

        ___ i __ r..(n - 1, -1, -1
            dups[A[i]] dups.g.. A[i], 0) + 1
            dup_fact *= dups[A[i]]

            cnt 0
            ___ j __ r..(i + 1, n
                __ A[i] > A[j]:
                    cnt += 1

            ans += cnt * factorial // dup_fact
            factorial *= n - i

        r.. ans
