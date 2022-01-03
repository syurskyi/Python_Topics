'''
Created on Sep 11, 2019

@author: tongq
'''
_______ bisect
c_ ExamRoom(object):

    ___ - , N):
        """
        :type N: int
        """
        rowNum = N
        l    # list

    ___ seat
        """
        :rtype: int
        """
        __ n.. l:
            res = 0
        ____:
            d, res = l[0], 0
            ___ a, b __ z..(l, l[1:]):
                __ (b-a)//2 > d:
                    d, res = (b-a)//2, (b+a)//2
            __ rowNum - 1 - l[-1] > d:
                res = rowNum-1
        bisect.insort(l, res)
        r.. res

    ___ leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        l.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
