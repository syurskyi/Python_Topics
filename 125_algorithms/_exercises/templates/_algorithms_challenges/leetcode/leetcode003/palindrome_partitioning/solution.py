class Solution:
    # @param s, a string
    # @return a list of lists of string
    ___ partition(self, s):
        res    # list
        cand    # list
        self.partition_aux(s, cand, res)
        r.. res

    ___ partition_aux(self, s, cand, res):
        __ n.. s:
            res.a..(cand[:])
        ____:
            ___ i, e __ e..(s):
                __ self.is_palindrome(s[:i + 1]):
                    cand.a..(s[:i + 1])
                    self.partition_aux(s[i + 1:], cand, res)
                    cand.pop()

    ___ is_palindrome(self, s):
        left = 0
        right = l..(s) - 1
        w.... left < right:
            __ s[left] != s[right]:
                r.. False
            left += 1
            right -= 1
        r.. True
