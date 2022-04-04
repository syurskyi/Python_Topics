c_ Solution:
    ___ intersect  a, b
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        ans    # list

        __ n.. a o. n.. b:
            r.. ans

        freq    # dict

        ___ x __ a:
            freq[x] = freq.g.. x, 0) + 1

        ___ x __ b:
            __ n.. freq.g.. x
                _____

            freq[x] -= 1
            ans.a..(x)

        r.. ans


c_ Solution:
    ___ intersect  a, b
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

        m, n = l..(a), l..(b)
        i = j = 0

        w.... i < m a.. j < n:
            __ a[i] __ b[j]:
                ans.a..(a[i])
                i += 1
                j += 1
            ____ a[i] < b[j]:
                i += 1
            ____
                j += 1

        r.. ans
