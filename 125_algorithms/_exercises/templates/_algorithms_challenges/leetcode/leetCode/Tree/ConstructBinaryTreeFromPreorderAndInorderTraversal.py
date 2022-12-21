"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


给定中序和前序遍历返回完整的二叉树。

就思路上来说比较容易理解：
1. 前序是 根 左 右。
2. 中序是 左 根 右。

也就是在 前序中找到根，然后在中序中找到根的左右两颗子树。不断的重复左右两颗子树这样的过程。

下面是一个递归实现，效率并不是非常高：
beat 40% ~ 50%.

测试地址：
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/


"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ buildTree  preorder, inorder
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        ___ make(preorder, inorder
            __ n.. preorder:
                r_ None
            
            root = TreeNode(preorder[0])
            
            left_in = inorder[:inorder.index(root.val)]
            left_pre = preorder[1:l..(left_in)+1]
            right_in = inorder[l..(left_in)+1:]
            right_pre = preorder[l..(left_in)+1:]

            root.left = make(left_pre, left_in)
            root.right = make(right_pre, right_in)
            
            r_ root
            
        r_ make(preorder, inorder)
            
