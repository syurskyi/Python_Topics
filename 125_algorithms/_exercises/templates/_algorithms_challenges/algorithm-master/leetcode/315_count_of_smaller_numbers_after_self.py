c_ Solution:
    """
    REF: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76657/
    """
    ___ countSmaller  nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        __ n.. nums:
            r.. []

        n l..(nums)
        ans [0] * n

        cands s..(s..(nums
        v2i {cands[i]: i ___ i __ r..(l..(cands}
        bits [0] * (l..(v2i) + 1)

        ___ i __ r..(n - 1, -1, -1
            j v2i[nums[i]]
            ans[i] s..(j)
            update(j)

        r.. ans

    ___ update  i
        i += 1

        w.... i < l..(bits
            bits[i] += 1
            i += (i & -i)

    ___ s..  i
        res 0

        w.... i > 0
            res += bits[i]
            i -_ (i & -i)

        r.. res


c_ Solution:
    """
    Brute Force: TLE
    """
    ___ countSmaller  nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans    # list

        __ n.. nums:
            r.. ans

        n l..(nums)

        ___ i __ r..(n
            ans.a..(0)

            ___ j __ r..(i, n
                __ nums[j] < nums[i]:
                    ans[-1] += 1

        r.. ans
