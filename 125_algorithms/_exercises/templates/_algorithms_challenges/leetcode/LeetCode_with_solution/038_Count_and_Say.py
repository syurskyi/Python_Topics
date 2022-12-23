c_ Solution:
    ___ countAndSay  n
        """
        :type n: int
        :rtype: str
        """
        __ n __ 1:
            r_ '1'
        x = '1'
        w.. n > 1:
            # each round, read itself
            x = count(x)
            n -= 1
        r_ x

    ___ count  x
        m = list(x)
        res =    # list
        m.a.. N..)
        i , j = 0 , 0
        w.. i < l.. m) - 1:
            j += 1
            __ m[j] != m[i]:
                # note j - i is the count of m[i]
                res += [j - i, m[i]]
                i = j
        r_ ''.join(s..(s) ___ s __ res)