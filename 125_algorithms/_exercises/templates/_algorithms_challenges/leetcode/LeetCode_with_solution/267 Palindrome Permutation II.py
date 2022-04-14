"""
Premium Question
https://leetcode.com/problems/palindrome-permutation-ii/
"""
____ c.. _______ d..


__author__ 'Daniel'


c_ Solution(o..
    ___ generatePalindromes  s
        """
        :type s: str
        :rtype: List[str]
        """
        m d..(i..)
        ___ c __ s:
            m[c] += 1

        odd N..
        ___ k, v __ m.i..
            __ v % 2 __ 1:
                __ odd __ n.. N..
                    r.. []
                odd k

        cur ""
        __ odd:
            m[odd] -_ 1
            cur odd

        ret    # list
        # actually only need to build half
        grow(s, m, N.., cur, ret)
        r.. ret

    ___ grow  s, count_map, pi, cur, ret
        __ l..(cur) __ l..(s
            ret.a..(cur)
            r..

        ___ k __ count_map.k..:
            __ k !_ pi a.. count_map[k] > 0
                ___ i __ x..(1, count_map[k]/2+1  # jump the parent
                    count_map[k] -_ i*2
                    grow(s, count_map, k, k*i+cur+k*i, ret)
                    count_map[k] += i*2


__ _______ __ _______
    ... Solution().generatePalindromes("aabb") __  'baab', 'abba'