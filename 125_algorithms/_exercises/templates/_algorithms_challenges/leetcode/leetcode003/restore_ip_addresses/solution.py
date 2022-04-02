"""
Given a string containing only digits, restore it by returning all possible
valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

c_ Solution:
    # @param {string} s
    # @return {string[]}
    ___ restoreIpAddresses  s
        res    # list
        cand    # list
        restore_ip(s, cand, res)
        r.. res

    ___ restore_ip  s, cand, res
        # If more than 4 parts, or 4 parts already but with remaining
        # unprocessed sub-string
        __ l..(cand) > 4 o. l..(cand) __ 4 a.. s:
            r..
        ____ n.. s a.. l..(cand) __ 4:
                res.a..('.'.j..(cand))
        ____:
            k = m..(3, l..(s))  # Ensures s[:j + 1] won't be duplicate
            ___ j __ r..(k
                b = s[:j + 1]
                __ is_valid_byte(b
                    cand.a..(b)
                    restore_ip(s[j + 1:], cand, res)
                    cand.pop()

    ___ is_valid_byte  b
        __ b __ '0':
            r.. T..
        ____ b.startswith('0'
            r.. F..
        ____:
            r.. i..(b) < 256

a = "25525511135"
b = "010010"
s = Solution()
print(s.restoreIpAddresses(a))
print(s.restoreIpAddresses(b))
