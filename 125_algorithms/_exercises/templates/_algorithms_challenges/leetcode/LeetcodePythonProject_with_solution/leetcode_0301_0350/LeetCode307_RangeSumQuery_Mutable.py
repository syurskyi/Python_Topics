'''
Created on May 9, 2018

@author: tongq
'''
class TreeNode(object):
    ___ __init__(self, start, end, sumVal=0):
        self.sumVal = sumVal
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class NumArray(object):

    ___ __init__(self, nums):
        """
        :type nums: List[int]
        """
        __ not nums:
            self.root = None
        else:
            self.root = self.buildTree(nums, 0, len(nums)-1)
    
    ___ buildTree(self, nums, i, j):
        __ not nums or i > j:
            return None
        __ i == j:
            return TreeNode(i, j, nums[i])
        root = TreeNode(i, j, -1)
        mid = (i+j)//2
        root.left = self.buildTree(nums, i, mid)
        root.right = self.buildTree(nums, mid+1, j)
        root.sumVal = root.left.sumVal+root.right.sumVal
        return root

    ___ update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.updateHelper(self.root, i, val)
    
    ___ updateHelper(self, root, i, val):
        __ not root: return
        __ i == root.start and i == root.end:
            root.sumVal = val
            return
        mid = (root.start+root.end)//2
        __ i <= mid:
            self.updateHelper(root.left, i, val)
        else:
            self.updateHelper(root.right, i, val)
        root.sumVal = root.left.sumVal+root.right.sumVal
    
    ___ sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumRangeHelper(self.root, i, j)
    
    ___ sumRangeHelper(self, root, i, j):
        __ not root or i > j or j < root.start or i > root.end:
            return 0
        __ i == root.start and j == root.end:
            return root.sumVal
        mid = (root.start+root.end)//2
        res = self.sumRangeHelper(root.left, i, min(j, mid))+\
            self.sumRangeHelper(root.right, max(i, mid+1), j)
        return res
