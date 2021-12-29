"""
Merge Sort
time: O(n)
space: O(1)
"""
class Solution:
    ___ inputStream(self, a, b):
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

        while i >= 0 and j >= 0:
            while i >= 0 and (a[i] __ BACK o. acnt):
                acnt += 1 __ a[i] __ BACK ____ -1
                i -= 1
            while j >= 0 and (b[j] __ BACK o. bcnt):
                bcnt += 1 __ b[j] __ BACK ____ -1
                j -= 1

            __ a[i] != b[j]:
                r.. RES[0]

            i -= 1
            j -= 1

        while i >= 0 and (a[i] __ BACK o. acnt):
            acnt += 1 __ a[i] __ BACK ____ -1
            i -= 1
        while j >= 0 and (b[j] __ BACK o. bcnt):
            bcnt += 1 __ b[j] __ BACK ____ -1
            j -= 1

        r.. RES[int(i __ j)]


"""
Stack
time: O(n)
space: O(n)
"""
class Solution:
    ___ inputStream(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str, 'NO' or 'YES'
        """
        RES = ('NO', 'YES')

        __ a __ '' and b __ '':
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
                stack.pop()

        _stack    # list

        ___ c __ b:
            __ c != RM:
                _stack.a..(c)
            ____ _stack:
                # c == RM
                _stack.pop()

        r.. RES[int(stack __ _stack)]
