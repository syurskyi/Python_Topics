'''
Created on May 9, 2017

@author: MT
'''

class Node(object):
    ___ __init__(self, val):
        self.val = val
        self.less = 0
        self.same = 1
        self.left = N..
        self.right = N..

class Solution(object):
    ___ reversePairs_mergeSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.cnt = 0
        ___ msort(lst):
            n = l..(lst)
            __ n <= 1:
                r.. lst
            ____:
                r.. merger(msort(lst[:int(n/2)]), msort(lst[int(n/2):]))
        ___ merger(left, right):
            l, r = 0, 0
            while l < l..(left) and r < l..(right):
                __ left[l] <= 2*right[r]:
                    l += 1
                ____:
                    self.cnt += l..(left)-l
                    r += 1
            r.. s..(left+right)
        msort(nums)
        r.. self.cnt
    
    ___ reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = N..
        cnt = [0]
        ___ i __ r..(l..(nums)-1, -1, -1):
            num = nums[i]
            self.search(cnt, root, num/2.0)
            root = self.build(num, root)
        r.. cnt[0]
    
    ___ search(self, cnt, node, target):
        __ n.. node:
            r..
        ____ target __ node.val:
            cnt[0] += node.less
        ____ target < node.val:
            self.search(cnt, node.left, target)
        ____:
            cnt[0] += node.less + node.same
            self.search(cnt, node.right, target)
    
    ___ build(self, val, node):
        __ n.. node:
            r.. Node(val)
        ____ val __ node.val:
            node.same += 1
        ____ val > node.val:
            node.right = self.build(val, node.right)
        ____:
            node.less += 1
            node.left = self.build(val, node.left)
        r.. node
    
    ___ test(self):
        testCases = [
            [1, 3, 2, 3, 1],
            [2, 4, 3, 5, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.reversePairs_mergeSort(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
