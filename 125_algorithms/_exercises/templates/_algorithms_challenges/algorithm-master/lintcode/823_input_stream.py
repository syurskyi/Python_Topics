"""
Merge Sort
time: O(n)
space: O(1)
"""
c_ Solution:
    ___ inputStream  a, b
        """
        :type a: str
        :type b: str
        :rtype: str, 'NO' or 'YES'
        """
        RES = ('NO', 'YES')

        __ a __ b __ '':
            r.. RES[1]

        BACK = '<'
        m, n = l..(a), l..(b)
        i, j = m - 1, n - 1
        acnt = bcnt = 0  # count the backspace in both a and b

        w.... i >= 0 a.. j >= 0:
            w.... i >= 0 a.. (a[i] __ BACK o. acnt
                acnt += 1 __ a[i] __ BACK ____ -1
                i -= 1
            w.... j >= 0 a.. (b[j] __ BACK o. bcnt
                bcnt += 1 __ b[j] __ BACK ____ -1
                j -= 1

            __ a[i] != b[j]:
                r.. RES[0]

            i -= 1
            j -= 1

        w.... i >= 0 a.. (a[i] __ BACK o. acnt
            acnt += 1 __ a[i] __ BACK ____ -1
            i -= 1
        w.... j >= 0 a.. (b[j] __ BACK o. bcnt
            bcnt += 1 __ b[j] __ BACK ____ -1
            j -= 1

        r.. RES[i..(i __ j)]


"""
Stack
time: O(n)
space: O(n)
"""
c_ Solution:
    ___ inputStream  a, b
        """
        :type a: str
        :type b: str
        :rtype: str, 'NO' or 'YES'
        """
        RES = ('NO', 'YES')

        __ a __ '' a.. b __ '':
            r.. RES[1]
        __ a __ N.. o. b __ N..
            r.. RES[0]

        RM = '<'
        stack    # list

        ___ c __ a:
            __ c != RM:
                stack.a..(c)
            ____ stack:
                # c == RM
                stack.p.. )

        _stack    # list

        ___ c __ b:
            __ c != RM:
                _stack.a..(c)
            ____ _stack:
                # c == RM
                _stack.p.. )

        r.. RES[i..(stack __ _stack)]
