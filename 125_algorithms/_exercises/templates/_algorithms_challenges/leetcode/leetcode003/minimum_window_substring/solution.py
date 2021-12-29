class Solution:
    # @return a string
    ___ minWindow(self, S, T):
        s = S
        t = T
        d = {}
        td = {}
        ___ c __ t:
            td[c] = td.get(c, 0) + 1
        left = 0
        right = 0
        lefts    # list
        rights    # list
        ___ i, c __ e..(s):
            __ c __ td:
                d[c] = d.get(c, 0) + 1
                __ self.contains(d, td):  # Contains all characters
                    right = i
                    # Move left pointers
                    cc = s[left]
                    w.... left <= right a.. (cc n.. __ d o. d[cc] > td[cc]):
                        __ cc __ d:
                            d[cc] -= 1
                        left += 1
                        cc = s[left]
                    lefts.a..(left)
                    rights.a..(right)
        __ n.. lefts:
            r.. ''
        res_left = lefts[0]
        res_right = rights[0]
        n = l..(lefts)
        ___ i __ r..(1, n):
            __ rights[i] - lefts[i] < res_right - res_left:
                res_left = lefts[i]
                res_right = rights[i]
        r.. s[res_left:res_right + 1]

    ___ contains(self, d, td):
        ___ k __ td:
            __ k n.. __ d o. d[k] < td[k]:
                r.. False
        r.. True
