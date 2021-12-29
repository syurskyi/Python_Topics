'''
Created on Oct 5, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        __ not nums: return None
        maxVal = max(nums)
        ind = nums.index(maxVal)
        root = TreeNode(maxVal)
        root.left = self.constructMaximumBinaryTree(nums[:ind])
        root.right = self.constructMaximumBinaryTree(nums[ind+1:])
        return root
    
    ___ test(self):
        testCases = [
            [3, 2, 1, 6, 0, 5]
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            newNode = self.constructMaximumBinaryTree(nums)
            __ newNode:
                print(newNode.val)
            else:
                print(None)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
