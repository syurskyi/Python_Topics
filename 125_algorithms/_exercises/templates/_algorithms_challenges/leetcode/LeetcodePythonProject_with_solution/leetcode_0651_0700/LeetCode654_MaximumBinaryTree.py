'''
Created on Oct 5, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        __ n.. nums: r.. N..
        maxVal = max(nums)
        ind = nums.index(maxVal)
        root = TreeNode(maxVal)
        root.left = constructMaximumBinaryTree(nums[:ind])
        root.right = constructMaximumBinaryTree(nums[ind+1:])
        r.. root
    
    ___ test
        testCases = [
            [3, 2, 1, 6, 0, 5]
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            newNode = constructMaximumBinaryTree(nums)
            __ newNode:
                print(newNode.val)
            ____:
                print(N..)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
