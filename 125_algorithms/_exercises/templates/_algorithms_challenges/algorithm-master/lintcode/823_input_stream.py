"""
Merge Sort
time: O(n)
space: O(1)
"""
class Solution:
    ___ inputStream(self, a, b
        """
        :type a: str
        :type b: str
        :rtype: str, 'NO' or 'YES'
        """
        RES = ('NO', 'YES')

        __ a __ b __ '':
            r_ RES[1]

        BACK = '<'
        m, n = le.(a), le.(b)
        i, j = m - 1, n - 1
        acnt = bcnt = 0  # count the backspace in both a and b

        w___ i >= 0 and j >= 0:
            w___ i >= 0 and (a[i] __ BACK or acnt
                acnt += 1 __ a[i] __ BACK else -1
                i -= 1
            w___ j >= 0 and (b[j] __ BACK or bcnt
                bcnt += 1 __ b[j] __ BACK else -1
                j -= 1

            __ a[i] != b[j]:
                r_ RES[0]

            i -= 1
            j -= 1

        w___ i >= 0 and (a[i] __ BACK or acnt
            acnt += 1 __ a[i] __ BACK else -1
            i -= 1
        w___ j >= 0 and (b[j] __ BACK or bcnt
            bcnt += 1 __ b[j] __ BACK else -1
            j -= 1

        r_ RES[int(i __ j)]


"""
Stack
time: O(n)
space: O(n)
"""
class Solution:
    ___ inputStream(self, a, b
        """
        :type a: str
        :type b: str
        :rtype: str, 'NO' or 'YES'
        """
        RES = ('NO', 'YES')

        __ a __ '' and b __ '':
            r_ RES[1]
        __ a is None or b is None:
            r_ RES[0]

        RM = '<'
        stack = []

        ___ c in a:
            __ c != RM:
                stack.append(c)
            ____ stack:
                # c == RM
                stack.pop()

        _stack = []

        ___ c in b:
            __ c != RM:
                _stack.append(c)
            ____ _stack:
                # c == RM
                _stack.pop()

        r_ RES[int(stack __ _stack)]
