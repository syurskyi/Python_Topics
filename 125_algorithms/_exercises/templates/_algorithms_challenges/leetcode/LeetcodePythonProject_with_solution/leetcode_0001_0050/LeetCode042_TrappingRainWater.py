'''
Created on Jun 5, 2018

@author: tongq
'''
c_ Solution(o..
    ___ trap  height
        """
        :type height: List[int]
        :rtype: int
        """
        __ n.. height: r.. 0
        n l..(height)
        left [0]*n
        left[0] height[0]
        ___ i __ r..(1, n
            left[i] m..(height[i], left[i-1])
        right [0]*n
        right[-1] height[-1]
        ___ i __ r..(n-2, -1, -1
            right[i] m..(height[i], right[i+1])
        res 0
        ___ i __ r..(n
            res += m..(left[i], right[i])-height[i]
        r.. res
