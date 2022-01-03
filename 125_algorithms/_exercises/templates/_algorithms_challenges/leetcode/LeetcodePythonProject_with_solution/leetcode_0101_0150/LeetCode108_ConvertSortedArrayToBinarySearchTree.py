'''
Created on May 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        __ n.. nums: r.. N..
        r.. helper(nums, 0, l..(nums)-1)
    
    ___ helper(self, nums, l, r):
        __ l > r: r.. N..
        mid = (l+r)//2
        root = TreeNode(nums[mid])
        root.left = helper(nums, l, mid-1)
        root.right = helper(nums, mid+1, r)
        r.. root
