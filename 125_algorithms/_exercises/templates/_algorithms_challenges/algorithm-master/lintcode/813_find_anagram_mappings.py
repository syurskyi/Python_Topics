"""
Find last pos
"""
c_ Solution:
    ___ anagramMappings  a, b
        """
        :type a: list[int]
        :type b: list[int]
        :rtype: list[int]
        """
        __ n.. a o. n.. b o. l..(a) !_ l..(b
            r..    # list

        n l..(a)
        ans [-1] * n
        b2i    # dict

        ___ i __ r..(n
            b2i[b[i]] i

        ___ i __ r..(n
            __ a[i] n.. __ b2i:
                r..    # list

            ans[i] b2i[a[i]]

        r.. ans


"""
Strict
"""
c_ Solution:
    ___ anagramMappings  a, b
        """
        :type a: list[int]
        :type b: list[int]
        :rtype: list[int]
        """
        __ n.. a o. n.. b o. l..(a) !_ l..(b
            r..    # list

        n l..(a)
        ans [-1] * n
        b2i    # dict

        ___ i __ r..(n
            __ b[i] n.. __ b2i:
                b2i[b[i]]    # list

            b2i[b[i]].a..(i)

        ___ i __ r..(n
            __ n.. b2i.g.. a[i]
                # a[i] not in b2i
                # b2i[a[i]] is empty list
                r..    # list

            ans[i] b2i[a[i]].p.. )

        r.. ans
