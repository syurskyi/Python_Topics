"""
Premium Question
https://leetcode.com/problems/palindrome-permutation-ii/
"""
from collections ______ defaultdict


__author__ = 'Daniel'


class Solution(object
    ___ generatePalindromes(self, s
        """
        :type s: str
        :rtype: List[str]
        """
        m = defaultdict(int)
        for c in s:
            m[c] += 1

        odd = None
        for k, v in m.items(
            __ v % 2 __ 1:
                __ odd is not None:
                    r_ []
                odd = k

        cur = ""
        __ odd:
            m[odd] -= 1
            cur = odd

        ret = []
        # actually only need to build half
        self.grow(s, m, None, cur, ret)
        r_ ret

    ___ grow(self, s, count_map, pi, cur, ret
        __ le.(cur) __ le.(s
            ret.append(cur)
            r_

        for k in count_map.keys(
            __ k != pi and count_map[k] > 0:
                for i in xrange(1, count_map[k]/2+1  # jump the parent
                    count_map[k] -= i*2
                    self.grow(s, count_map, k, k*i+cur+k*i, ret)
                    count_map[k] += i*2


__ __name__ __ "__main__":
    assert Solution().generatePalindromes("aabb") __ ['baab', 'abba']