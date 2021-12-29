'''
Created on Oct 5, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        __ n.. nums: r.. N..
        maxVal = max(nums)
        ind = nums.index(maxVal)
        root = TreeNode(maxVal)
        root.left = self.constructMaximumBinaryTree(nums[:ind])
        root.right = self.constructMaximumBinaryTree(nums[ind+1:])
        r.. root
    
    ___ test(self):
        testCases = [
            [3, 2, 1, 6, 0, 5]
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            newNode = self.constructMaximumBinaryTree(nums)
            __ newNode:
                print(newNode.val)
            ____:
                print(N..)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
