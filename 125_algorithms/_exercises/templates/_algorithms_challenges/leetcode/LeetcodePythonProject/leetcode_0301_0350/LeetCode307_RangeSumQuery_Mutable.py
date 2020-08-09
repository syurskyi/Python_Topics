'''
Created on May 9, 2018

@author: tongq
'''
class TreeNode(object
    ___ __init__(self, start, end, sumVal=0
        self.sumVal = sumVal
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class NumArray(object

    ___ __init__(self, nums
        """
        :type nums: List[int]
        """
        __ not nums:
            self.root = None
        ____
            self.root = self.buildTree(nums, 0, le.(nums)-1)
    
    ___ buildTree(self, nums, i, j
        __ not nums or i > j:
            r_ None
        __ i __ j:
            r_ TreeNode(i, j, nums[i])
        root = TreeNode(i, j, -1)
        mid = (i+j)//2
        root.left = self.buildTree(nums, i, mid)
        root.right = self.buildTree(nums, mid+1, j)
        root.sumVal = root.left.sumVal+root.right.sumVal
        r_ root

    ___ update(self, i, val
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.updateHelper(self.root, i, val)
    
    ___ updateHelper(self, root, i, val
        __ not root: r_
        __ i __ root.start and i __ root.end:
            root.sumVal = val
            r_
        mid = (root.start+root.end)//2
        __ i <= mid:
            self.updateHelper(root.left, i, val)
        ____
            self.updateHelper(root.right, i, val)
        root.sumVal = root.left.sumVal+root.right.sumVal
    
    ___ sumRange(self, i, j
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        r_ self.sumRangeHelper(self.root, i, j)
    
    ___ sumRangeHelper(self, root, i, j
        __ not root or i > j or j < root.start or i > root.end:
            r_ 0
        __ i __ root.start and j __ root.end:
            r_ root.sumVal
        mid = (root.start+root.end)//2
        res = self.sumRangeHelper(root.left, i, min(j, mid))+\
            self.sumRangeHelper(root.right, max(i, mid+1), j)
        r_ res
