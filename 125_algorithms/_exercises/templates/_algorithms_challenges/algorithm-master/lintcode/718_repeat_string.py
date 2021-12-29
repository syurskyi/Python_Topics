class Solution:
    ___ repeatedString(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        __ len(b) <= len(a) and b in a:
            return 1
        __ not a or not b:
            return -1

        ans = b.count(a)
        c = b.split(a)

        __ c[0] and a.endswith(c[0]):
            ans += 1

        __ c[-1] and a.startswith(c[-1]):
            ans += 1

        return ans __ a.startswith(c[-1]) and a.endswith(c[0]) else -1
