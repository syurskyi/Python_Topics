c_ Solution:
    ___ intersection  a, b
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        ans    # list

        __ n.. a o. n.. b:
            r.. ans

        s s..(a)
        t s..(b)

        ___ x __ s:
            __ x __ t:
                ans.a..(x)

        r.. ans


c_ Solution:
    ___ intersection  a, b
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        ans    # list

        __ n.. a o. n.. b:
            r.. ans

        a.s..()
        b.s..()

        m, n l..(a), l..(b)
        i j 0

        w.... i < m a.. j < n:
            __ a[i] __ b[j]:
                __ n.. ans o. a[i] !_ ans[-1]:
                    ans.a..(a[i])
                i += 1
                j += 1
            ____ a[i] < b[j]:
                i += 1
            ____
                j += 1

        r.. ans
