"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.


判断左子树是否与右子树互为镜像。

思路：
遍历左子树，把结果放入队列中。
按照相反的左右遍历右子树，同时让压出队列顶的一项作对比。
不匹配或队列中没有足够的数据都可判为False.

效率 O(n)
beat 100%.

测试地址：
https://leetcode.com/problems/symmetric-tree/description/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ isSymmetric  root
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root:
            r_ True
        
        left = root.left
        right = root.right
        
        left_node = [left]
        right_node = [right]
        
        left_node_value   # list
        
        _____ left_node:
            # if left_node:
            _left = left_node.pop()
            __ _left:
                left_node_value.a.. _left.val)        
            ____
                left_node_value.a.. None)

            __ _left:
                left_node.a.. _left.right)
                left_node.a.. _left.left)
        
        left_node_value.r..
        
        _____ right_node:
            _right = right_node.pop()
            
            __ left_node_value:
                left_value = left_node_value.pop()
            ____
                r_ False
            
            __ _right:
                __ left_value != _right.val:
                    r_ False
            ____
                __ left_value != None:
                    r_ False

            __ _right:
                right_node.a.. _right.left)
                right_node.a.. _right.right)
        r_ True
