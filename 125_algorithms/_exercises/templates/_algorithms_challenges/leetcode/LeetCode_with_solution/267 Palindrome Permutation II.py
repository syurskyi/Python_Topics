"""
Premium Question
https://leetcode.com/problems/palindrome-permutation-ii/
"""
____ collections _______ defaultdict


__author__ = 'Daniel'


class Solution(object):
    ___ generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        m = defaultdict(int)
        ___ c __ s:
            m[c] += 1

        odd = N..
        ___ k, v __ m.items():
            __ v % 2 __ 1:
                __ odd __ n.. N..
                    r.. []
                odd = k

        cur = ""
        __ odd:
            m[odd] -= 1
            cur = odd

        ret    # list
        # actually only need to build half
        self.grow(s, m, N.., cur, ret)
        r.. ret

    ___ grow(self, s, count_map, pi, cur, ret):
        __ l..(cur) __ l..(s):
            ret.a..(cur)
            r..

        ___ k __ count_map.keys():
            __ k != pi and count_map[k] > 0:
                ___ i __ xrange(1, count_map[k]/2+1):  # jump the parent
                    count_map[k] -= i*2
                    self.grow(s, count_map, k, k*i+cur+k*i, ret)
                    count_map[k] += i*2


__ __name__ __ "__main__":
    ... Solution().generatePalindromes("aabb") __ ['baab', 'abba']