class Solution:
    # @param s, a string
    # @return a list of lists of string
    ___ partition(self, s
        res = []
        cand = []
        self.partition_aux(s, cand, res)
        r_ res

    ___ partition_aux(self, s, cand, res
        __ not s:
            res.append(cand[:])
        ____
            for i, e in enumerate(s
                __ self.is_palindrome(s[:i + 1]
                    cand.append(s[:i + 1])
                    self.partition_aux(s[i + 1:], cand, res)
                    cand.pop()

    ___ is_palindrome(self, s
        left = 0
        right = le.(s) - 1
        w___ left < right:
            __ s[left] != s[right]:
                r_ False
            left += 1
            right -= 1
        r_ True
