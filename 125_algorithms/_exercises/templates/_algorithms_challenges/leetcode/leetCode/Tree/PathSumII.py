"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

PathSum 的进阶版，输出所有符合条件的路径。所以这里直接用遍历，有负数加上不是二叉搜索树应该没太多需要优化的地方。

测试用例：
https://leetcode.com/problems/path-sum-ii/description/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ pathSum  root, s..
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        __ n.. root:
            r_ []
        
        result   # list
        
        ___ helper(prev, root, s.., path
            __ prev + root.val __ s..:
                __ n.. root.left a.. n.. root.right:
                    result.a.. list(map(int, path.split(' ')[1:]))+[root.val])
                    r_ True
                
            __ root.left:
                helper(prev + root.val, root.left, s.., path=path+" "+str(root.val))
                    # return True
            
            __ root.right:
                helper(prev + root.val, root.right, s.., path=path+" "+str(root.val))
            
            r_ F..
        
        helper(0, root, s.., "")  
        
        r_ result
