"""
Given a string containing only digits, restore it by returning all possible
valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution:
    # @param {string} s
    # @return {string[]}
    ___ restoreIpAddresses(self, s
        res = []
        cand = []
        self.restore_ip(s, cand, res)
        r_ res

    ___ restore_ip(self, s, cand, res
        # If more than 4 parts, or 4 parts already but with remaining
        # unprocessed sub-string
        __ le.(cand) > 4 or le.(cand) __ 4 and s:
            r_
        ____ not s and le.(cand) __ 4:
                res.append('.'.join(cand))
        ____
            k = min(3, le.(s))  # Ensures s[:j + 1] won't be duplicate
            for j in range(k
                b = s[:j + 1]
                __ self.is_valid_byte(b
                    cand.append(b)
                    self.restore_ip(s[j + 1:], cand, res)
                    cand.pop()

    ___ is_valid_byte(self, b
        __ b __ '0':
            r_ True
        ____ b.startswith('0'
            r_ False
        ____
            r_ int(b) < 256

a = "25525511135"
b = "010010"
s = Solution()
print(s.restoreIpAddresses(a))
print(s.restoreIpAddresses(b))
