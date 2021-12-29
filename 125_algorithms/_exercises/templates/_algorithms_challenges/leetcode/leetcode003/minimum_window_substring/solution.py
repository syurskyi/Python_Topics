class Solution:
    # @return a string
    ___ minWindow(self, S, T):
        s = S
        t = T
        d = {}
        td = {}
        for c in t:
            td[c] = td.get(c, 0) + 1
        left = 0
        right = 0
        lefts = []
        rights = []
        for i, c in enumerate(s):
            __ c in td:
                d[c] = d.get(c, 0) + 1
                __ self.contains(d, td):  # Contains all characters
                    right = i
                    # Move left pointers
                    cc = s[left]
                    while left <= right and (cc not in d or d[cc] > td[cc]):
                        __ cc in d:
                            d[cc] -= 1
                        left += 1
                        cc = s[left]
                    lefts.append(left)
                    rights.append(right)
        __ not lefts:
            return ''
        res_left = lefts[0]
        res_right = rights[0]
        n = len(lefts)
        for i in range(1, n):
            __ rights[i] - lefts[i] < res_right - res_left:
                res_left = lefts[i]
                res_right = rights[i]
        return s[res_left:res_right + 1]

    ___ contains(self, d, td):
        for k in td:
            __ k not in d or d[k] < td[k]:
                return False
        return True
