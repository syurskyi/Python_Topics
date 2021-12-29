'''
Created on Sep 11, 2019

@author: tongq
'''
_______ bisect
class ExamRoom(object):

    ___ __init__(self, N):
        """
        :type N: int
        """
        self.rowNum = N
        self.l    # list

    ___ seat(self):
        """
        :rtype: int
        """
        __ n.. self.l:
            res = 0
        ____:
            d, res = self.l[0], 0
            ___ a, b __ z..(self.l, self.l[1:]):
                __ (b-a)//2 > d:
                    d, res = (b-a)//2, (b+a)//2
            __ self.rowNum - 1 - self.l[-1] > d:
                res = self.rowNum-1
        bisect.insort(self.l, res)
        r.. res

    ___ leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.l.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
