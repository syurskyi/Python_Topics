"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]


无难度..做了1的话直接把返回结果倒置即可。

beat 94%
28ms 

测试地址：
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

c.. Solution o..
    ___ levelOrderBottom  root
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        __ n.. root:
            r_ []
        
        result   # list
        
        temp = deque([root])
        next_temp = deque()
        _result   # list
        _____ 1:
            __ temp:
                node = temp.popleft()
                _result.a.. node.val)
                __ node.left:
                    next_temp.a.. node.left)
                    
                __ node.right:
                    next_temp.a.. node.right)
            ____
                result.a.. _result)
                _result   # list
                temp = next_temp
                next_temp = deque()
            
            __ n.. temp a.. n.. next_temp:
                __ _result:
                    result.a.. _result)
                r_ result[::-1]
