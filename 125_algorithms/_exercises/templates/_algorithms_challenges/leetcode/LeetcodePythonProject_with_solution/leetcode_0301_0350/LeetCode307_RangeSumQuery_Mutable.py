'''
Created on May 9, 2018

@author: tongq
'''
class TreeNode(object):
    ___ __init__(self, start, end, sumVal=0):
        self.sumVal = sumVal
        self.start = start
        self.end = end
        self.left = N..
        self.right = N..

class NumArray(object):

    ___ __init__(self, nums):
        """
        :type nums: List[int]
        """
        __ n.. nums:
            self.root = N..
        ____:
            self.root = self.buildTree(nums, 0, l..(nums)-1)
    
    ___ buildTree(self, nums, i, j):
        __ n.. nums o. i > j:
            r.. N..
        __ i __ j:
            r.. TreeNode(i, j, nums[i])
        root = TreeNode(i, j, -1)
        mid = (i+j)//2
        root.left = self.buildTree(nums, i, mid)
        root.right = self.buildTree(nums, mid+1, j)
        root.sumVal = root.left.sumVal+root.right.sumVal
        r.. root

    ___ update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.updateHelper(self.root, i, val)
    
    ___ updateHelper(self, root, i, val):
        __ n.. root: r..
        __ i __ root.start a.. i __ root.end:
            root.sumVal = val
            r..
        mid = (root.start+root.end)//2
        __ i <= mid:
            self.updateHelper(root.left, i, val)
        ____:
            self.updateHelper(root.right, i, val)
        root.sumVal = root.left.sumVal+root.right.sumVal
    
    ___ sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        r.. self.sumRangeHelper(self.root, i, j)
    
    ___ sumRangeHelper(self, root, i, j):
        __ n.. root o. i > j o. j < root.start o. i > root.end:
            r.. 0
        __ i __ root.start a.. j __ root.end:
            r.. root.sumVal
        mid = (root.start+root.end)//2
        res = self.sumRangeHelper(root.left, i, m..(j, mid))+\
            self.sumRangeHelper(root.right, max(i, mid+1), j)
        r.. res
