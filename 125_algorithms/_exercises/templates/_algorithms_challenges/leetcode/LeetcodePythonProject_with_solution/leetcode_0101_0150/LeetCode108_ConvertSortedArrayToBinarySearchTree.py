'''
Created on May 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        __ n.. nums: r.. N..
        r.. self.helper(nums, 0, l..(nums)-1)
    
    ___ helper(self, nums, l, r):
        __ l > r: r.. N..
        mid = (l+r)//2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, l, mid-1)
        root.right = self.helper(nums, mid+1, r)
        r.. root
